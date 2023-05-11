**iDRAC Update Network Settings Module for Dell EMC VxRail**
=========================================
### Product Guide 2.0.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will update the iDRAC network settings on the specified host.

Supported Endpoints
--------

* PATCH /v1/hosts/{sn}/idrac/network
* PATCH /v2/hosts/{sn}/idrac/network
* GET /v1/requests/{id}

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
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>sn</b>
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
                                        <div>The serial number of the host to be queried.</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>ip_address</b>
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
                                        <div>The MAC address of the iDRAC.</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>netmask</b>
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
                                        <div>The netmask of the iDRAC.</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>gateway</b>
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
                                        <div>The gateway address of the iDRAC.</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>dhcp_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                    <br>                    </div>
                                                    </td>
                            <td>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Whether DHCP service enabled or not.</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>vlan_id</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The VLAN ID setting of the iDRAC. Set 0 to disable.</div>
                                        <div></div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>vlan_priority</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>                   </div>
                                                    </td>
                            <td>
                            <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>0</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The VLAN priority setting of the iDRAC. The default value is 0.</div>
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
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>300s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for updating iDRAC network settings, the default value is 300 seconds</div>
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
- Module dellemc_vxrail_idrac_updatenetwork.py calls any existing version of PATCH /hosts/{sn}/idrac/network API
- Details on execution of module dellemc_vxrail_idrac_updatenetwork.py can be checked in the logs /tmp/vxrail_ansible_idrac_updatenetwork.log


Examples
--------

``` yaml+jinja
 - name: Update iDRAC network settings, version specified by api_version_number
    dellemc_vxrail_idrac_updatenetwork:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        sn: "{{ sn }}"
        ip_address: "{{ ip_address }}"
        netmask: "{{ netmask }}"
        gateway: "{{ gateway }}"
        vlan_id: "{{ vlan_id }}"
        dhcp_enabled: "{{ dhcp_enabled }}"
        vlan_priority: "{{ vlan_priority }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"

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
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>all</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>Update_iDRAC_Network_Settings</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When request has been created to update iDRAC network settings</td>
            <td>all</td>
            <td>
                                        <div>The infomation of request sent to the system to update iDRAC network settings</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>Request_ID</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The Request ID created by API to update the iDRAC network settings</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>Request_Status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>When the request to update the iDRAC network settings has completed</td>
            <td>v1</td>
            <td>
                                        <div>The status of request to update an iDRAC network settings</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
