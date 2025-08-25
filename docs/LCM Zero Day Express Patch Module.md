**LCM downlad bundle from ACG server for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will execute zero day express patch.

Supported Endpoints
--------

  * Get   /lcm/patch/status
  * Post  /lcm/patch/upload
  * Post  /lcm/patch/upgrade
  * Post  /lcm/patch/cancel
  * Post  /lcm/patch/precheck

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
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>vxmip</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>                
            </div>
        </td>
        <td></td>                                                                
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
        <td></td>
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
            <b>witness_user_name</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=false</span>                    
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>Administrative account name of the witness</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>witness_user_password</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=false</span>                    
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>The password for the administrator account provided in witness patching</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>auto_witness_upgrade</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=bool</span>
                <br>
                <span style="color: red">required=false</span>                    
            </div>
        </td>
        <td>
            <ul style="margin: 0; padding: 0"><b>Default:</b>
                <li>False</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>The password for the administrator account provided in witness patching</div>
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
                <li>3600s</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>Time out value for patching task, the default value is 3600 seconds</div>
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

Notes
-----
- Make sure your VxRail environment supports the APIs that you use
- Module dellemc_vxrail_lcm_zero_day_express_patch.py will execute VxRail 0 day express patch 
- Details on execution of module  dellemc_vxrail_lcm_zero_day_express_patch.py can be checked in the logs /tmp/vxrail_ansible_lcm_zero_day_express_patch.log

Examples
--------

``` yaml+jinja
    - name: Execute VxRail Zero Day Express Patch
      dellemc.vxrail.dellemc_vxrail_lcm_zero_day_express_patch:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        component_bundle: "{{ component_bundle }}"
        witness_user_name: "{{ witness_user_name_var | default(omit) }}"
        witness_user_password: "{{ witness_user_password_var | default(omit) }}"
        auto_witness_upgrade: "{{ auto_witness_upgrade_var | default(omit) }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
      register: execute_0day_express_patch

    - name: Display execute the VxRail Zero day express patch result
      debug:
        msg: "{{ execute_0day_express_patch }}"
```

Return Values
-------------
* /lcm/patch/status
The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>step</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
           <div>NONE</div>
           <div>UPLOAD</div>
           <div>DRY_RUN</div>
           <div>UPGRADE</div>
        </td>
        <td>
            <div>Current stage of execution process</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>status</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
          <div>NOT_STARTED</div>
          <div>IN_PROGRESS</div>
          <div>COMPLETED</div>
          <div>COMPLETED_WITH_ERRORS</div>
          <div>FAILED</div>
        </td>
        <td>
            <div>Current stage of execution process</div>
            <br/>
        </td>
    </tr>
    </tr>
        <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>progress_percent</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=int</span>
            </div>
        </td>
        <td>
        </td>
        <td>
            <div>Execution progress value</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>witness_upgrade</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=bool</span>
            </div>
        </td>
        <td>false</td>
        <td>
            <div>Is there any upgrade of witness platform?</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>bundle_name</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>VMware-ESXi-8.0U3e-24674464-depot.zip</td>
        <td>
            <div>patching package name.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>error</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=array</span>
            </div>
        </td>
        <td>["error_message"]</td>
        <td>
            <div>End time of download package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>precheck_state</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
           <div>NOT_STARTED</div>
           <div>IN_PROGRESS</div>
           <div>SUCCESS</div>
           <div>FAILED</div>
        </td>
        <td>
            <div>Status of precheck step</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>last_updated</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>"2025-05-29T12:34:56Z"</td>
        <td>
            <div>Last updated time</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>bundle_version</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td></td>
        <td>
            <div>Version of package package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>bundle_build</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td></td>
        <td>
            <div>Build number of package package.</div>
            <br/>
        </td>
    </tr>
</table>

* /lcm/patch/upload
The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>message</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
            <div>Upload finished</div>
        </td>
        <td>
            <div>Message for uploading</div>
            <br/>
        </td>
    </tr>
</table>

* /lcm/patch/upgrade
The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>message</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
            <div>Upgrade started</div>
        </td>
        <td>
            <div>Message for upgrading</div>
            <br/>
        </td>
    </tr>
</table>

* /lcm/patch/cancel
The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>message</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
            <div>Operation cancelled successfully</div>
        </td>
        <td>
            <div>Message for cancell API</div>
            <br/>
        </td>
    </tr>
</table>

* /lcm/patch/precheck
The following are the fields unique to this module:
<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>message</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>
            <div>Operation cancelled successfully</div>
        </td>
        <td>
            <div>Message for precheck API</div>
            <br/>
        </td>
    </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;