#! /bin/bash

# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# This software contains the intellectual property of Dell Inc. or is licensed to Dell Inc. from third parties.
# Use of this software and the intellectual property contained therein is expressly limited to the terms and 
# conditions of the License Agreement under which it is provided by or on behalf of Dell Inc. or its subsidiaries.

set -e

BUILD_OUTPUT_FOLDER="build-output/" 

echo ">>>>>>>>>>>> sanity tests"

mkdir "${BUILD_OUTPUT_FOLDER}"
ansible-galaxy collection build --output-path "${BUILD_OUTPUT_FOLDER}" -f

tar_file=$(find ${BUILD_OUTPUT_FOLDER} -type f -name "*.tar.gz" | head -1)
if [ "$tar_file" == "" ]; then
    echo "Failed to build ansible galaxy collection! Exit!"
    exit 1
fi

ansible-galaxy collection install "$tar_file" -f | tee temp.log
collection_folder=$(< temp.log grep "Installing" | sed "s#.*to ##g;s#'##g" )
if [ "$collection_folder" == "" ]; then
    echo "Failed to install ansible galaxy collection! Exit!"
    exit 1
fi

git config --global http.sslVerify false
git config --global url."https://${GITHUB_USER}:$GITHUB_API_TOKEN@${GITHUB_HOST}".insteadOf "https://${GITHUB_HOST}"
git clone "${UTILITY_REPO_URL}" "${UTILITY_REPO_NAME}"
pushd "${UTILITY_REPO_NAME}"
pip install .
popd

pip install -r sanity-test-requirements.txt

pushd "$collection_folder"
ansible-test sanity plugins/modules/*.py
popd
