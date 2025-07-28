**System Primary Storage Provision Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will provision and finalize a dynamic node cluster.

Supported Endpoints
--------

* POST /system/primary-storage

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vxm-ip"></div>
                <b>vxmip</b>
                <a class="ansibleOptionLink" href="#parameter-vxm-ip" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The IP address of the VxRail Manager System</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vcadmin"></div>
                <b>vcadmin</b>
                <a class="ansibleOptionLink" href="#parameter-vcadmin" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Administrative account of the vCenter Server the VxRail Manager is registered to</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vcpasswd"></div>
                <b>vcpasswd</b>
                <a class="ansibleOptionLink" href="#parameter-vcpasswd" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The password for the administrator account provided in vcadmin</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-primary_storage_name"></div>
                <b>primary_storage_name</b>
                <a class="ansibleOptionLink" href="#parameter-primary_storage_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The datastore name used for provisioning</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-primary_storage_type"></div>
                <b>primary_storage_type</b>
                <a class="ansibleOptionLink" href="#parameter-primary_storage_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The type of datastore used for provisioning</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-storage_policy_profile_name"></div>
                <b>storage_policy_profile_name</b>
                <a class="ansibleOptionLink" href="#parameter-storage_policy_profile_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The storage policy for the datastore used for provisioning</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>60s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for getting system infomation, the default value is 60 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-api_version_number"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-api_version_number" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The version of API to call. If omitted, will use highest version on the system.</div>
                                        <div></div>
                                                    </td>
        </tr>
                    </table>

Notes
-----
- This module calls any existing version of the /system/primary-storage api, please ensure your VxRail cluster supports this API.
- Can check Log file /tmp/vxrail_ansible_primary_storage_provision.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: VxRail Primary Storage Provision. Version specified by api_version_number
    dellemc_vxrail_system_primary_storage_provision:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        primary_storage_name: "{{ primary_storage_name }}"
        primary_storage_type: "{{ primary_storage_type }}"
        storage_policy_profile_name: "{{ storage_policy_profile_name }}"
        api_version_number "{{ api_version_number }}"
        timeout: "{{ timeout }}"
```

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th>Minimum API Version</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-request_id"></div>
                <b>request_id</b>
                <a class="ansibleOptionLink" href="#return-request_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>all</td>
            <td>
                                        <div>Request ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <!-- <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-datastore_name"></div>
                <b>datastore_name</b>
                <a class="ansibleOptionLink" href="#return-datastore_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>all</td>
            <td>
                                        <div>Datastore name</div>
                                    <br/>
                                </td>
        </tr> -->
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
