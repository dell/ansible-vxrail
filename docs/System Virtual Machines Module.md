System Virtual Machines Module for Dell EMC VxRail
=================
### Product Guide 1.4.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will retrieve name, status and host information for system virtual machines in the VxRail cluster.

Supported Endpoints
--------

* GET /cluster/system-virtual-machines

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
                <b>timeout</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
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
                                        <div>Time out value for getting iDRAC Network Settings infomation, the default value is 60 seconds</div>
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
                                                                                                                        <ul style="margin: 0; padding: 0"><b></b>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The version of API to call. If omitted, will use highest version on the system</div>
                                        <div></div>
                                                    </td>
        </tr>
                    </table>

Notes
-----
- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_cluster_getvm.py can call any existing version of /cluster/system-virtual-machines API
- Details on execution of module dellemc_vxrail_cluster_getvm.py can be checked in the logs /tmp/vxrail_ansible_cluster_getvm.log


Examples
--------

``` yaml+jinja
  - name: Retrieves name, status and host information for system  virtual machines in the VxRail cluster. Version specified by 'api_version_number'.
    dellemc_vxrail_cluster_getvm:
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
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th>Minimum API Version</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>When VM information exists</td>
            <td>v1</td>
            <td>
                                        <div>Name of the Virtual Machine.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>host</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>When VM information exists</td>
            <td>v1</td>
            <td>
                                        <div>Host FQDN system for the virtual machine</div>
                                    <br/>
                                </td>
        </tr> 
        <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>When VM information exists</td>
            <td>v1</td>
            <td>
                                        <div>Status of Virtual Machine</div>
                                    <br/>
                                </td>
        </tr>   
                    </table>


Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;