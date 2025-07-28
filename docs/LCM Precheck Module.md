**LCM Precheck Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will Perform a separate health pre-check for the VxRail system.
  
Supported Endpoints
--------

* POST /lcm/precheck
* GET /requests/{id}
  

Parameters
----------

<details>
    <summary>/v1/lcm/precheck</summary>
    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
        <th width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vxmip</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vcadmin</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vcpasswd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vc_root_account</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Root account of the vCenter Server the VxRail Manager is registered to</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vc_root_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>The password for the root account provided in vcadmin</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vxm_root_account</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Root account of  VxRail Manager </div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vxm_root_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>The password for the root account provided in vxm root account</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>bundle_file_locator</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>the path of lcm bundle on vxm, which is recommended under /data/store2</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>health_precheck_type</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0"><b>Default:</b>
                    <li>LCM_PRECHECK</li>
                </ul>
            </td>
            <td>
                <div></div>
                <div>The type of health pre-check to be run, the default value is LCM_PRECHECK</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0"><b>Default:</b>
                    <li>1800 seconds(30 minutes)</li>
                </ul>
            </td>
            <td>
                <div></div>
                <div>Time out value for LCM, the default value is 1800 seconds(30 minutes).</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>
                </div>
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
</details>
<details>
    <summary>/v2/lcm/precheck</summary>
    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
        <th width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vxmip</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vcadmin</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vcpasswd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vc_root_account</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Root account of the vCenter Server the VxRail Manager is registered to</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vc_root_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>The password for the root account provided in vcadmin</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vxm_root_account</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Root account of  VxRail Manager </div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vxm_root_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>The password for the root account provided in vxm root account</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>bundle_file_locator</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>the path of lcm bundle on vxm, which is recommended under /data/store2</div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>health_precheck_type</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0"><b>Default:</b>
                    <li>LCM_PRECHECK</li>
                </ul>
            </td>
            <td>
                <div></div>
                <div>The type of health pre-check to be run, the default value is LCM_PRECHECK</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0"><b>Default:</b>
                    <li>1800 seconds(30 minutes)</li>
                </ul>
            </td>
            <td>
                <div></div>
                <div>Time out value for LCM, the default value is 1800 seconds(30 minutes).</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>The version of API to call. If omitted, will use highest version on the system.</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>enable_quick_boot_var</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Enable quick boot when set to true.</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>parallel_remediation_enable_var</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Enable parallel remediation when set to true.</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>parallel_remediation_max_var</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>The max number of hosts to be remediated.</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>enforce_quick_patch_var</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Enable quick patch when set to true.</div>
                <div></div>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>retry_as_standard_var</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div></div>
                <div>Enable retry as standard when set to true.</div>
                <div></div>
            </td>
        </tr>
    </table>
</details>

Notes
-----
- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_lcm_precheck.py calls any existing version of Post /lcm/precheck API
- Details on execution of module dellemc_vxrail_lcm_precheck.py can be checked in the logs /tmp/vxrail_ansible_lcm_precheck.log


Examples
--------

``` yaml+jinja
- name: Start to do LCM Precheck, version specified by api_version_number
    dellemc_vxrail_lcm_precheck:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle_file_locator: "{{ bundle_file_locator }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"

- name: Start to do LCM Precheck with v2, version specified by api_version_number
    dellemc_vxrail_lcm_precheck:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle_file_locator: "{{ bundle_file_locator }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        enable_quick_boot_var: "{{ enable_quick_boot_var | default(omit) }}"
        parallel_remediation_enable_var: "{{ parallel_remediation_enable_var | default(omit) }}"
        parallel_remediation_max_var: "{{ parallel_remediation_max_var | default(omit) }}"
        enforce_quick_patch_var: "{{ enforce_quick_patch_var | default(omit) }}"
        retry_as_standard_var: "{{ retry_as_standard_var | default(omit) }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
        
```
Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
    <tr>
        <td colspan="2">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>changed</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=boolean</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Whether or not the resource has changed.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <div class="ansibleOptionAnchor" id="return-host_details"></div>
            <b>LCM_V1_Precheck</b>
            <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=list</span>
            </div>
        </td>
        <td>When LCM Precheck completes</td>
        <td>
            <div>LCM Precheck Status</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td class="elbow-placeholder">&nbsp;</td>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="return-host_details/bw_limit"></div>
            <b>request_id</b>
            <a class="ansibleOptionLink" href="#return-host_details/bw_limit" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>success</td>
        <td>
            <div>LCM Precheck (long-running) request returns a requestId.</div>
        </td>
    </tr>
    <tr>
        <td class="elbow-placeholder">&nbsp;</td>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="return-host_details/bw_limit"></div>
            <b>status</b>
            <a class="ansibleOptionLink" href="#return-host_details/bw_limit" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>success</td>
        <td>
            <div>The current state of the execution</div>
        </td>
    </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
