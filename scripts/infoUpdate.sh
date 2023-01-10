#! /bin/bash

# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
#
# This software contains the intellectual property of Dell Inc. or is licensed to Dell Inc. from third parties.
# Use of this software and the intellectual property contained therein is expressly limited to the terms and 
# conditions of the License Agreement under which it is provided by or on behalf of Dell Inc. or its subsidiaries.

echo '************************** update readme.md and galaxy.yml **************************'
target_word=$1
tag=$2
target_index=$(grep -Pon '(\| [a-z 0-9\<\>\.\+]+){5} \|' README.md | cut --delimiter=":" --fields=1)
if [[ -z $target_index ]]; then
    echo "Target index not found"
    exit 1
else
    sed -i "${target_index}s/.*/${target_word}/g" README.md
    sed -i "s/version:.*/version: ${tag}/g" galaxy.yml
    cat README.md
fi
