**Dell Identity Service Start Device Auth Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will initiate a new device code flow. This API returns the verification URL and the user code. Go to the verification URL to authenticate a given support account with the DI token and activate access.
  
Supported Endpoints
--------

* GET /device-auth/start
  

Parameters
----------

<table border="0" cellpadding="0" class="documentation-table">
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
        <td></td>
        <td>
            <div></div>
            <div>The password for the administrator account provided in vcadmin</div>
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
            <ul style="margin: 0; padding: 0">
                <b>Default:</b>
                <li>1800 seconds(30 minutes)</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>Time out value for cvs compliance report, the default value is
                1800 seconds(30 minutes).</div>
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
        <td></td>
        <td>
            <div></div>
            <div>The version of API to call. If omitted, will use highest version on the system.</div>
        </td>
    </tr>
</table>

Notes
-----

- Make sure your VxRail environment supports the API that you use
* Module dellemc_vxrail_dell_identity_service_start_device_auth.py calls any existing version of POST /device-auth/start API
* Details on execution of module dellemc_vxrail_dell_identity_service_start_device_auth.py can be checked in the logs /tmp/vxrail_ansible_dell_identity_service_start_device_auth.log


Examples
--------

``` yaml+jinja
 - name: Start device authentication via Dell Identity Service, version specified by api_version_number
    dellemc_vxrail_dell_identity_service_start_device_auth:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
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
            <div class="ansibleOptionAnchor" id="return-user_code"></div>
            <b>user_code</b>
            <a class="ansibleOptionLink" href="#return-user_code" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>user code. This is the code the user needs to enter after authentication.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <div class="ansibleOptionAnchor" id="return-verification_uri"></div>
            <b>verification_uri</b>
            <a class="ansibleOptionLink" href="#return-verification_uri" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>verification_uri. URI for user authentication.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <div class="ansibleOptionAnchor" id="return-verification_uri_complete"></div>
            <b>verification_uri_complete</b>
            <a class="ansibleOptionLink" href="#return-verification_uri_complete" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>verification_uri_complete_value. This URL is the combination of verification URI and user code.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <div class="ansibleOptionAnchor" id="return-expires_in"></div>
            <b>expires_in</b>
            <a class="ansibleOptionLink" href="#return-expires_in" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=integer</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>When the return verification URL and user code expire, the value is provided in seconds.</div>
            <br/>
        </td>
    </tr>
</table>

Authors
-------

- VxRail Development Team &lt;<ansible.team@dell.com>&gt;
