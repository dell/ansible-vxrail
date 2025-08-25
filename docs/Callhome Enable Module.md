**Callhome Enable Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will enable call home functionality by enabling remote connectivity service.

Supported Endpoints
--------
* Post /callhome/enable

Parameters
----------
<details>
   <summary>/v1/callhome/enable</summary>
<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="3">
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
                                                            <td colspan="3">
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
                                                            <td colspan="3">
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
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>serial_number</b>
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
                                        <div>The node serial number for ESE enablement</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>connection_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>DIRECT</li>
<li>GATEWAY</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The connection type of callhome, allowed values are DIRECT and GATEWAY</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>pin</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The PIN code</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>access_key</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The access key</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SYSTEM</li>
<li>USER</li>
<li>NA</li>
                                                                                </ul>                                                                                                                    </td>
                                                            <td>
                                        <div></div>
                                        <div>The type of proxy, allowed values are USER,SYSTEM and NA</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_protocol</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SOCK5</li>
<li>HTTP</li>
<li>HTTPS</li>
                                                                                </ul>  
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The protocol of proxy, allowed values are SOCK5, HTTP and HTTPS</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_address</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The address of proxy</div>
                                                    </td>
        </tr>
        <tr>
 <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>proxy_port</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                    <span style="color: red">required=false</span>
                                      </div>
            <td></td>
            <td><div>The port of proxy</div></td>
        </tr>
        <tr>
            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>proxy_user</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                    <span style="color: red">required=false</span>
                                      </div>
            </td>
            <td></td>
            <td><div>The user account of the proxy</div></td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The password for the user account provided in proxy</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>gateways_host</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The host ip of gateways</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>gateways_port</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The port of gateways</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_contact_order</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The contact order of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_first_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The first name of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_last_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The last name of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_email_address</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The email address of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_phone_number</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The phone_number of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_pref_language</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The preferred language of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=false</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>300s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for enabling call home, the default value is 300 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=false</span>
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
</details>
<details>
   <summary>/v2/callhome/enable</summary>
<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="3">
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
                                                            <td colspan="3">
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
                                                            <td colspan="3">
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
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>serial_number</b>
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
                                        <div>The node serial number for ESE enablement</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>connection_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>DIRECT</li>
<li>GATEWAY</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The connection type of callhome, allowed values are DIRECT and GATEWAY</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>pin</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The PIN code</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>access_key</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The access key</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SYSTEM</li>
<li>USER</li>
<li>NA</li>
                                                                                </ul>                                                                                                                    </td>
                                                            <td>
                                        <div></div>
                                        <div>The type of proxy, allowed values are USER,SYSTEM and NA</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_protocol</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SOCK5</li>
<li>HTTP</li>
<li>HTTPS</li>
                                                                                </ul>  
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The protocol of proxy, allowed values are SOCK5, HTTP and HTTPS</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_address</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The address of proxy</div>
                                                    </td>
        </tr>
        <tr>
 <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>proxy_port</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                    <span style="color: red">required=false</span>
                                      </div>
            <td></td>
            <td><div>The port of proxy</div></td>
        </tr>
        <tr>
            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>proxy_user</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                    <span style="color: red">required=false</span>
                                      </div>
            </td>
            <td></td>
            <td><div>The user account of the proxy</div></td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The password for the user account provided in proxy</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>gateways_host</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The host ip of gateways</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>gateways_port</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The port of gateways</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_contact_order</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The contact order of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_first_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The first name of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_last_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The last name of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_email_address</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The email address of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_phone_number</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The phone_number of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_pref_language</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The preferred language of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=false</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>300s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for enabling call home, the default value is 300 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=false</span>
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
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>ip_version</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>IPV4</li>
<li>IPV6</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The ip version of callhome, allowed values are IPV4 and IPV6</div>
                                                    </td>
        </tr>
                    </table>
</details>
<details>
   <summary>/v3/callhome/enable</summary>
<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="3">
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
                                                            <td colspan="3">
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
                                                            <td colspan="3">
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
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>appliance_id</b>
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
                                        <div>The node appliance id for ESE enablement</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>connection_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>DIRECT</li>
<li>GATEWAY</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The connection type of callhome, allowed values are DIRECT and GATEWAY</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>pin</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The PIN code</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>access_key</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The access key</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SYSTEM</li>
<li>USER</li>
<li>NA</li>
                                                                                </ul>                                                                                                                    </td>
                                                            <td>
                                        <div></div>
                                        <div>The type of proxy, allowed values are USER,SYSTEM and NA</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_protocol</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SOCK5</li>
<li>HTTP</li>
<li>HTTPS</li>
                                                                                </ul>  
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The protocol of proxy, allowed values are SOCK5, HTTP and HTTPS</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_address</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=str</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The address of proxy</div>
                                                    </td>
        </tr>
        <tr>
 <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>proxy_port</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                    <span style="color: red">required=false</span>
                                      </div>
            <td></td>
            <td><div>The port of proxy</div></td>
        </tr>
        <tr>
            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>proxy_user</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                    <span style="color: red">required=false</span>
                                      </div>
            </td>
            <td></td>
            <td><div>The user account of the proxy</div></td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>proxy_passwd</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The password for the user account provided in proxy</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>gateways_host</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The host ip of gateways</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>gateways_port</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The port of gateways</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_contact_order</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The contact order of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_first_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The first name of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_last_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The last name of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_email_address</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The email address of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_phone_number</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The phone_number of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>customer_pref_language</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=false</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The preferred language of customer</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=false</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>300s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for enabling call home, the default value is 300 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>api_version_number</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=false</span>
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
<tr>
                                                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>ip_version</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td><ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>IPV4</li>
<li>IPV6</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The ip version of callhome, allowed values are IPV4 and IPV6</div>
                                                    </td>
        </tr>
                    </table>
</details>

Notes
-----
- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_callhome_enable.py calls any existing version of Post /callhome/enable API
- Details on execution of module dellemc_vxrail_callhome_enable.py can be checked in the logs /tmp/vxrail_ansible_callhome_enable.log


Examples
--------

``` yaml+jinja
  - name: Enable call home functionality, version specified by api_version_number
      dellemc_vxrail_callhome_enable:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        appliance_id: "{{ appliance_id }}"
        connection_type: "{{ connection_type }}"
        pin: "{{ pin }}"
        access_key: "{{ access_key }}"
        proxy_type: "{{ proxy_type }}"
        proxy_protocol: "{{ proxy_protocol }}"
        proxy_address: "{{ proxy_address }}"
        proxy_port: "{{ proxy_port }}"
        proxy_user: "{{ proxy_user }}"
        proxy_passwd: "{{ proxy_passwd }}"
        gateways_host: "{{ gateways_host }}"
        gateways_port: "{{ gateways_port }}"
        customer_contact_order: "{{ customer_contact_order }}"
        customer_first_name: "{{ customer_first_name }}"
        customer_last_name: "{{ customer_last_name }}"
        customer_phone_number: "{{ customer_phone_number }}"
        customer_email_address: "{{ customer_email_address  }}"
        customer_pref_language: "{{ customer_pref_language }}"
        timeout: "{{ timeout }}"
        ip_verion: "{{ ip_version }}"
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
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>failed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the API call has failed or not</div>
                                    <br/>
                                </td>
        </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
