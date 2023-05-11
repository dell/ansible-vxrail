**Certificate Get Automated Renewal Status Module for Dell EMC VxRail**
=========================================
### Product Guide 2.0.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module is to get automated renewal status of the VxRail Manager TLS certificate.

Supported Endpoints
--------
* GET /cluster/certificates/scep/status

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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vcadmin</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vcpasswd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
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
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
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
- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_certificates_get_scep_status.py can call any existing version of /cluster/certificates/scep/status
- Details on execution of module dellemc_vxrail_certificates_get_scep_status.py can be checked in the logs /tmp/vxrail_ansible_certificates_get_scep_status.log

Examples
--------

``` yaml+jinja
  - name: Get automated renewal status
    dellemc_vxrail_certificates_get_scep_status:
      vxmip: "{{ vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
      api_version_number: "{{ api_version_number }}"
```

Return Values
-------------

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
                <b>vxm_cert_expire_time</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Expiration time of the VxRail Manager TLS Certificate</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>last_failure_time</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Last failure time of the automated renewal</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>last_error_msg</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>The error message of last failure of the automated renewal</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>last_result</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>The status of last automated renewal</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>last_run_time</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Last run time of the automated renewal</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>last_success_time</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Last success time of the automated renewal</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>scep_enabled</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=boolean</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>The automated renewal is enabled or not</div>
            <br/>
        </td>
    </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
