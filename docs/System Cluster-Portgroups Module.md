System Cluster-Portgroups Module for Dell EMC VxRail
=================
### Product Guide 2.0.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will return the cluster's portgroup information used by a given node.
  
Supported Endpoints
--------

* GET /system/cluster-portgroups/
  

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
                <b>node_fqdn</b>
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
                                        <div>The Fully Qualified Domain Name of the node to query</div>
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
                                        <div>Time out value for getting system infomation, the default value is 60 seconds</div>
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
- This module calls any existing version of the /system/cluster-portgroups API, please ensure your VxRail cluster supports this API.
- Can check Log file /tmp/vxrail_ansible_system_cluster_portgroups.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrieves VxRail Cluster Portgroup Information. Version specified by api_version_number
    dellemc_vxrail_system_cluster_portgroups:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        node_fqdn: "{{ node_fqdn }}"
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
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>all</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>Cluster_Portgroups</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When cluster exists and node FQDN is resolvable.</td>
            <td>v1</td>
            <td>
                                        <div>The collection of queried portgroups from the given node.</div>
                                    <br/>
                                </td>
        </tr>

<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The name of the portgroup</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The type of the portgroup</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>portgroup_key</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The key of the portgroup</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>portgroup_vlan</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The VLAN ID of the portgroup</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>vds_moid</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The Managed Object ID (MOID) of the VMware Distributed Switch (VDS)</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>vds_name</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The name of the VDS</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>vds_uuid</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>v1</td>
            <td>
                                        <div>The UUID of the VDS</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;