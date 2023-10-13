**System Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will retrieve VxRail System Information.

Supported Endpoints
--------

* GET /system

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
                                        <div>Time out value for getting system infomation, the default value is 60 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
                    </table>

Notes
-----
- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_getsysteminfo.py can call any existing version of /system APIs
- Details on execution of module dellemc_vxrail_getsysteminfo.py can be checked in the logs /tmp/vxrail_ansible_getsysteminfo.log


Examples
--------

``` yaml+jinja
  - name: Retrieve VxRail System Information with GET /system API. Version specified by api_version_number
    dellemc_vxrail_getsysteminfo:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
        api_version_number : "{{ api_version_number }}"

```

Return Values
-------------

Fields are unique to the modules as follows:

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
            <td> v1 </td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>system_information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When cluster exists.</td>
            <td> v1 </td>
            <td>
                                        <div>Details of Vxrail System</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Description of the VxRail system</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>version</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Software version of the VxRail appliance</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>installed_time</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Time that the VxRail appliance software was installed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>health</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Health status of the VxRail system</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/hostGroupId"></div>
                <b>network_connected</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/hostGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the host is connected to the internet</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/maskingview"></div>
                <b>vc_connected</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the vCenter is connected</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_hosts"></div>
                <b>satellite_host_count</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/cluster_host_count" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v4 </td>
            <td>
                                        <div>Number of satellite hosts in the cluster</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>cluster_host_count(number_of_host)</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/cluster_host_count" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v4 </td>
            <td>
                                        <div>Number of hosts in the cluster. The corresponding name in APIs before v4 is number_of_host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>deployment_type(cluster_type)</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Information about the type of cluster deployed. The corresponding name in APIs before v2 is cluster_type</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>is_external_vc</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the vCenter is an external vCenter</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>logical_view_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>                   </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the VxRail Manager logical view is enabled</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>upgrade_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                  </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>The upgrade status of the VxRail appliance software</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>installed_components</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=InstalledComponent</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Software components installed in the VxRail system</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/port_flags_override"></div>
                <b>baseline</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v4 </td>
            <td>
                                        <div>Software version of component at the time the component was initially installed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>baseline_drifted</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the current configuration of the installed software component is different than the initial configuration</div>
                                    <br/>
                                </td>
        </tr>
 <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>component</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td> v4 </td>
            <td>
                                        <div>The type of software component installed</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>current_version</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Installed component version</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Installed component description</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>incompatibilties</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>A list of other software components that the installed component is incompatible with</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>installed_time</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>The time that the software component was initially installed (in milliseconds)</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>multiple_version</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the software component has different versions installed in other nodes in the cluster</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Installed component name</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>supported</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>                   </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                                        <div>Whether the current version of installed software component is supported</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>upgrade_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                </div>
                                </td>
            <td>success</td>
            <td> v4 </td>
            <td>
                                        <div>Description of the upgrade status of the installed software component</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>shared_storage</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=SharedStorage</span>                    </div>
                                </td>
            <td>success</td>
            <td> v3 </td>
            <td>
                                        <div>Information about shared storage in the VxRail cluster</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>datastore_id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                  </div>
                                </td>
            <td>success</td>
            <td> v3 </td>
            <td>
                                        <div>The shared datastore ID</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>is_primary</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>                 </div>
                                </td>
            <td>success</td>
            <td> v3 </td>
            <td>
                                        <div>Whether the datastore is primary datastore where VxRail Manager is deployed on it</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                    </div>
                                </td>
            <td>success</td>
            <td> v3 </td>
            <td>
                                        <div>The shared datastore name</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>protocol</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                 </div>
                                </td>
            <td>success</td>
            <td> v3 </td>
            <td>
                                        <div>The storage protocol used by the host</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                   </div>
                                </td>
            <td>success</td>
            <td> v3 </td>
            <td>
                                        <div>The shared datastore type</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;