**Certificate Update Automated Renewal Configurations Module for Dell EMC VxRail**
=========================================
### Product Guide 1.4.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module is to udpate automated renewal configurations of the VxRail Manager TLS certificate through SCEP.

Supported Endpoints
--------
* POST /cluster/certificates/scep/config

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
                <b>caserver_url</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Certificate Authority server URL</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>challenge_password</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Challenge password</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>scep_on</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Enable or disable the automated renewal</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>scep_renewal_interval_in_minutes</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>Choices: 60 - 1440 (minutes)</td>
                                                            <td>
                                        <div></div>
                                        <div>Certificate validation frequency in minutes</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>scep_days_before_expire</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>Choices: 14 - 60 (days)</td>
                                                            <td>
                                        <div></div>
                                        <div>Renew certificate before expiration</div>
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
- Module dellemc_vxrail_certificates_update_scep_config.py can call any existing version of POST /cluster/certificates/scep/config
- Details on execution of module dellemc_vxrail_certificates_update_scep_config.py can be checked in the logs /tmp/vxrail_ansible_certificates_get_scep_config.log

Examples
--------

``` yaml+jinja
  - name: Update automated renewal configurations
    dellemc_vxrail_certificates_update_scep_config:
      vxmip: "{{ vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
      caserver_url: "{{ caserver_url }}"
      challenge_password: "{{ challenge_password }}"
      scep_on: "{{ scep_on }}"
      scep_renewal_interval_in_minutes: "{{ scep_renewal_interval_in_minutes }}"
      scep_days_before_expire: "{{ scep_days_before_expire }}"
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
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>error_code</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=integer</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Error code of the operation</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>error_message</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Error message of the operation</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>caserver_url</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Certificate Authority server URL</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>scep_on</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>The automated renewal is enabled or not</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>scep_renewal_interval_in_minutes</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=integer</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Certificate validation frequency</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>scep_days_before_expire</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                <span style="color: purple">type=integer</span>
            </div>
        </td>
        <td>always</td>
        <td>
            <div>Days to renew the certificate before expiration</div>
            <br/>
        </td>
    </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
