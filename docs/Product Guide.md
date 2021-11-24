
**Ansible Modules for Dell EMC VxRail**
=========================================
### Product Guide 1.1.0

>� 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 


-   [Cluster Expansion Module](#cluster-expansion-module)
    -   [Synopsis](#synopsis)
    -   [Supported Endpoints](#supported-endpoints)
    -   [Parameters](#parameters)
    -   [Notes](#notes)
    -   [Examples](#examples)
    -   [Return Values](#return-values)
    -   [Authors](#authors)
-   [System Module](#system-module)
    -   [Synopsis](#synopsis-1)
    -   [Supported Endpoints](#supported-endpoints-1)
    -   [Parameters](#parameters-1)
    -   [Notes](#notes-1)
    -   [Examples](#examples-1)
    -   [Return Values](#return-values-1)
    -   [Authors](#authors-1)
-   [Day1 Initialization Module](#day1-initialization-module)
    -   [Synopsis](#synopsis-2)
    -   [Supported Endpoints](#supported-endpoints-2)
    -   [Parameters](#parameters-2)
    -   [Notes](#notes-2)
    -   [Examples](#examples-2)
    -   [Return Values](#return-values-2)
    -   [Authors](#authors-2)
-   [Cluster Information Module](#cluster-information-module)
    -   [Synopsis](#synopsis-3)
    -   [Supported Endpoints](#supported-endpoints-3)
    -   [Parameters](#parameters-3)
    -   [Notes](#notes-3)
    -   [Examples](#examples-3)
    -   [Return Values](#return-values-3)
    -   [Authors](#authors-3)
-   [Hosts Module](#hosts-module)
    -   [Synopsis](#synopsis-4)
    -   [Supported Endpoints](#supported-endpoints-4)
    -   [Parameters](#parameters-4)
    -   [Notes](#notes-4)
    -   [Examples](#examples-4)
    -   [Return Values](#return-values-4)
    -   [Authors](#authors-4)
-   [CallHome Module](#callhome-module)
    -   [Synopsis](#synopsis-5)
    -   [Supported Endpoints](#supported-endpoints-5)
    -   [Parameters](#parameters-5)
    -   [Notes](#notes-5)
    -   [Examples](#examples-5)
    -   [Return Values](#return-values-5)
    -   [Authors](#authors-5)
-   [iDRAC Network Settings Module](#idrac-network-settings-module)
    -   [Synopsis](#synopsis-6)
    -   [Supported Endpoints](#supported-endpoints-6)
    -   [Parameters](#parameters-6)
    -   [Notes](#notes-6)
    -   [Examples](#examples-6)
    -   [Return Values](#return-values-6)
    -   [Authors](#authors-6)
-   [Chassis Module](#chassis-module)
    -   [Synopsis](#synopsis-7)
    -   [Supported Endpoints](#supported-endpoints-7)
    -   [Parameters](#parameters-7)
    -   [Notes](#notes-7)
    -   [Examples](#examples-7)
    -   [Return Values](#return-values-7)
    -   [Authors](#authors-7)
-   [Remove Host Module](#remove-host-module)
    -   [Synopsis](#synopsis-8)
    -   [Supported Endpoints](#supported-endpoints-8)
    -   [Parameters](#parameters-8)
    -   [Notes](#notes-8)
    -   [Examples](#examples-8)
    -   [Return Values](#return-values-8)
    -   [Authors](#authors-8)
-   [System Virtual Machines Module](#system-virtual-machines-module)
    -   [Synopsis](#synopsis-9)
    -   [Supported Endpoints](#supported-endpoints-9)
    -   [Parameters](#parameters-9)
    -   [Notes](#notes-9)
    -   [Examples](#examples-9)
    -   [Return Values](#return-values-9)
    -   [Authors](#authors-9)
-   [Telemetry Tier Module](#telemetry-tier-module)
    -   [Synopsis](#synopsis-10)
    -   [Supported Endpoints](#supported-endpoints-10)
    -   [Parameters](#parameters-10)
    -   [Notes](#notes-10)
    -   [Examples](#examples-10)
    -   [Return Values](#return-values-10)
    -   [Authors](#authors-10)     


Cluster Expansion Module
===========

Synopsis
--------

This module will validate a L2 node expansion, perform a L2 node expansion
based on the provided expansion specification and query the status.

Supported Endpoints
--------

* POST /v1/cluster/expansion/validate
* POST /v1/cluster/expansion
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
                <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
                <b>vxm_version</b>
                <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                      <br>
                    <span style="color: red">required=true</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div></div>
                                        <div>The version of the VxRail Manager System</div>
                                                    </td>
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
                <b>host_psnt</b>
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
                                        <div>The psnt number for the ESX Host</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>hostname</b>
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
                                        <div>The name for the ESX Host.</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>mgt_ip</b>
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
                                        <div>The management IP address for the ESX Host</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vsan_ip</b>
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
                                        <div>The vsan IP address for the ESX Host</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>vmotion_ip</b>
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
                                        <div>The vmotion IP address for the ESX Host</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>mgt_account</b>
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
                                        <div>Management account the VxRail Manager is registered to</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>mgt_passwd</b>
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
                                        <div>The password for the Management account</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>root_passwd</b>
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
                                        <div>The password for the root account</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>rack_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
 <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>default-rack</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The name of the rack that houses the host, default value is default-rack.</div>
                                                    </td>
        </tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>order_number</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                    <br>
                    <span style="color: red"></span>                    </div>
                                                    </td>
                            <td>
 <ul style="margin: 0; padding: 0"><b>Default:</b>
                                                                                                                                                            <li>5</li>
                                                                                </ul>
                                                                                                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>The position of the node in the rack, default value is 5.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_type"></div>
                <b>maintenance_mode</b>
                <a class="ansibleOptionLink" href="#parameter-host_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                    <br>
                    <span style="color: red"></span> 
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>False</li>
                                                                                                                                                                                            <li>True</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>	Whether the hosts remain in maintenance mode after being added to the cluster, default value is false.</div>
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
                                                                                                                                                            <li>1800s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for cluster expansion, the default value is 1800 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
                            </table>

Notes
-----

- Make sure added node can be discovered by LoudMouth.
- Can check Log file /tmp/vxrail_ansible_cluster.log for more details about cluster expansion.

Examples
--------

``` yaml+jinja
 - name: Start a cluster expansion
    dellemc_vxrail_cluster_expansion:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vxm_version: "{{ vxm_version }}"
        host_psnt: "{{ host_psnt }}"
        hostname: "{{ hostname }}"
        mgt_account: "{{ mgt_account }}"
        mgt_passwd: "{{ mgt_passwd }}"
        root_passwd: "{{ root_passwd }}"
        mgt_ip: "{{ mgt_ip }}"
        vsan_ip: "{{ vsan_ip }}"
        vmotion_ip: "{{ vmotion_ip }}"
        rack_name: "{{ rack_name }}"
        order_number: "{{ order_number }}"
        maintenance_mode: "{{ maintenance_mode }}"
        timeout: "{{ timeout }}"
    
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
                <b>NodeCompatiblityValidation</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When Node Validation completes</td>
            <td>
                                        <div>Node Validation Status</div>
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
                                        <div>Node Validation (long-running) request returns a requestId.</div>
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
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details"></div>
                <b>NodeExpansion</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When Node Expansion completes</td>
            <td>
                                        <div>Node Expansion Status</div>
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
                                        <div>Node Expansion (long-running) request returns a requestId.</div>
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

</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

System Module
=================

Synopsis
--------
This module will retrieve VxRail System Information.

Supported Endpoints
--------

* GET /v3/system

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
- This module called v3/system api,make sure your VxRail environment supported this API.
- Can check Log file /tmp/vxrail_ansible_system.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrives VxRail System Information
    dellemc_vxrail_system:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>system_information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When cluster exists.</td>
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
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
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
            <td>
                                        <div>Whether the vCenter is connected</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_hosts"></div>
                <b>number_of_host</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of hosts in the cluster</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>deployment_type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about the type of cluster deployed</div>
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
            <td>
                                        <div>Software components installed in the VxRail system</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/port_flags_override"></div>
                <b>is_external_vc</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the vCenter is an external vCenter</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>logical_view_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the VxRail Manager logical view is enabled</div>
                                    <br/>
                                </td>
        </tr>
 <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>upgrade_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The upgrade status of the VxRail appliance software</div>
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
            <td>
                                        <div>Information about shared storage in the VxRail cluster</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;


Day1 Initialization Module
=================

Synopsis
--------
This module will configure and deploy a new VxRail cluster
  based on the provided day1 json file.
  
Supported Endpoints
--------

* POST /v1/system/initialize
* GET /v1/system/initialize/status
  

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
                <b>day1json_file</b>
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
                                        <div>The path of Day1 Json file.</div>
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
                                                                                                                                                            <li>18000s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for Day1 bring up, the default value is 18000 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
                    </table>

Notes
-----
- Make sure your cluster with Day0 build only, prepare day1 json file for FirstRun
- Can check Log file /tmp/vxrail_ansible_day1.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Configure and deploy a new VxRail cluster
    dellemc_vxrail_day1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        day1json_file: "{{ day1json_file }}"
        timeout : "{{ timeout }}"

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
                <b>Day1DryRun</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When Day1 DryRun Validation completes</td>
            <td>
                                        <div>Day1 DryRun Status</div>
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
                                        <div>Day1 DryRun(long-running) request returns a requestId.</div>
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
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details"></div>
                <b>Day1Initialization</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When Day1 Initialization completes</td>
            <td>
                                        <div>Day1 Initialization Status</div>
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
                                        <div>Day1 Initialization (long-running) request returns a requestId.</div>
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

</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;


Cluster Information Module
=================

Synopsis
--------
This module will retrieve VxRail Cluster Information.

Supported Endpoints
--------

* GET /v1/cluster

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

- Can check Log file /tmp/vxrail_ansible_clusterinfo.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrives VxRail Cluster Information
    dellemc_vxrail_clusterinfo:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>Cluster_Information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When cluster exists</td>
            <td>
                                        <div>Details of Vxrail System</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>chassises</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When chassis exist</td>
            <td>
                                        <div>Description of Chassis in VxRail Cluster</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>generation</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Generation of the chassis</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>health</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of the health of the chassis</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the chassis</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>missing</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the host health status is critical</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>model</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Model of the chassis</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>psnt</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>PSNT of the chassis</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>render_category</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The chassis render category</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>cluster_id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The UUID of the VxRail cluster</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/hostGroupId"></div>
                <b>device_type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/hostGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Device type of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/maskingview"></div>
                <b>health</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of the health of the cluster</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_hosts"></div>
                <b>last_time</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The last time the cluster was updated</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>operational_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Operational status information</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>product_type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>                  </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Product type of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/port_flags_override"></div>
                <b>supressed</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether under suppression mode or not</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>vc_connected</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the vCenter is connected</div>
                                    <br/>
                                </td>
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
                                        <div>Whether or not the resource has changed</div>
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


Hosts Module
=================

Synopsis
--------
This module will retrieve VxRail hosts Information.

Supported Endpoints
--------

* GET /v4/hosts
* GET /v4/hosts/{sn}

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
- This module called v4/hosts api,make sure your VxRail environment supported this API.
- Can check Log file /tmp/vxrail_ansible_hosts.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrives VxRail Hosts Information
    dellemc_vxrail_hosts:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>hosts_information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When hosts exist.</td>
            <td>
                                        <div>Details of Vxrail Hosts</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID number of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>sn</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Serial number of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>slot</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Rack slot position where the VxRail host appliance is installed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>hostname</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hostname of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/hostGroupId"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/hostGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/maskingview"></div>
                <b>manufacturer</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Manufacturer of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_hosts"></div>
                <b>psnt</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Product serial number tag (PSNT) of the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>boot_devices</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=BootDeviceV2</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about each boot device on the VxRail host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>nics</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=Nic</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about each NIC on the VxRail host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/port_flags_override"></div>
                <b>led_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>State of the chassis LED indicator for the host</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>health</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Health status of the VxRail system.</div>
                                    <br/>
                                </td>
        </tr>
 <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>operational_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Operational status of the host</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>missing</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the chassis health status is critical.</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>power_status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Power supply status of the host</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>tpm_present</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether a TPM security device is installed on the VxRail host</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>disks</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=DiskInfoV2</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about each disk installed in the VxRail host.</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>firmwareInfo</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=FirmwareInfoV2</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about the firmware versions installed on the host.</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>geo_location</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=GeoLocation</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about the geographical location of the host</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>drive_configuration</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=DriveConfigurationInfo</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about the drive configuration on the host.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

Callhome Module
=================

Synopsis
--------
This module will retrieve VxRail CallHome Information.

Supported Endpoints
--------

* GET /v2/callhome/info

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
- This module called v2/callhome/info api,make sure your VxRail environment supported this API.
- Can check Log file /tmp/vxrail_ansible_callhome.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrives VxRail Callhome Information
    dellemc_vxrail_callhome:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>callhome_information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When callhome server exists.</td>
            <td>
                                        <div>Information about the call home servers</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of the SRS server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>integrated</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the SRS server is integrated (internal) or external</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>site_id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Site ID for the SRS server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>address_list</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=Address</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>An array of SRS server addresses with associated information</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

iDRAC Network Settings Module
=================

Synopsis
--------
This module will retrieve iDRAC Network Settings Information.

Supported Endpoints
--------

* GET /v1/hosts/{sn}/idrac/network

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
                                        <div>The serial number of the host to be queried</div>
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
                    </table>

Notes
-----
- This module calls /v1/hosts/{sn}/idrac/network api, make sure your VxRail environment supports this API
- For more details about execution result, log file can be found at /tmp/vxrail_ansible_idrac.log


Examples
--------

``` yaml+jinja
  - name: Get iDRAC Network Settings
    DellEMC_VxRail_idrac_GetNetworkSettings_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        sn: "{{ sn }}"
        timeout: "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>iDRAC_Network_Settings</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When iDRAC Network Settings exists</td>
            <td>
                                        <div>Information about the iDRAC Network Settings</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>dhcp_enabled</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether DHCP service is enabled</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>ip</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The iDRAC Network IP Settings</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The VLAN ID settings of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The MAC address of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>netmask</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The netmask of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>gateway</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The gateway address of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>vlan</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The IPv4 address of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>vlan_id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The VLAN ID setting of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>vlan_priority</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The VLAN priority setting of the iDRAC</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

Chassis Module
=================

Synopsis
--------
This module will retrieve VxRail Chassis Information.

Supported Endpoints
--------

* GET /v3/chassis

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
- This module called v3/chassis api,make sure your VxRail environment supported this API.
- Can check Log file /tmp/vxrail_ansible_chassis.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrives VxRail Chassis Information
    dellemc_vxrail_chassis:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>chassis_information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When cluster exists.</td>
            <td>
                                        <div>Details of Vxrail System</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>sn</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis sn</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>part_number</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis part number</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis description</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/hostGroupId"></div>
                <b>service_tag</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/hostGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis service tag</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/maskingview"></div>
                <b>psnt</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis psnt</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_hosts"></div>
                <b>model</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis model</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>render_category</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis render category</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>hosts</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=HostBasicInfoV3</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>host basic infomation</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/port_flags_override"></div>
                <b>generation</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis generation</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>health</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>chassis health status</div>
                                    <br/>
                                </td>
        </tr>
 <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>missing</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The upgrade status of the VxRail appliance software</div>
                                    <br/>
                                </td>
        </tr>
<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>power_supplies</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=PowerSupplyInfo</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about the chassis power supplies</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

Remove Host Module
=================

Synopsis
--------
This module will Remove a host from the cluster.
  
Supported Endpoints
--------

* POST /v1/cluster/remove-host
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
                <b>vc_root_account</b>
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
                    <span style="color: red">required=true</span>                    </div>
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
                <b>host_sn</b>
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
                                        <div>Serial number of the host to be removed</div>
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
                                                                                                                                                            <li>1800s</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div></div>
                                        <div>Time out value for node removal, the default value is 1800 seconds</div>
                                        <div></div>
                                                    </td>
        </tr>
                    </table>

Notes
-----
- Make sure you have done precheck action, e.g, entering maintainance mode and vsan Health checking is pass.
- Can check Log file /tmp/vxrail_ansible_rmnode.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Remove a host
    DellEMC_VxRail_Cluster_RemoveHost_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        host_sn: "{{ host_sn }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        timeout : "{{ timeout }}"

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
                <b>Remove_Node</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When Node Removal completes</td>
            <td>
                                        <div>Node Removal Status</div>
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
                                        <div>Node Removal(long-running) request returns a requestId.</div>
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


</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

System Virtual Machines Module
=================

Synopsis
--------
This module will retrieve name, status and host information for system virtual machines in the VxRail cluster.

Supported Endpoints
--------

* GET /v1/cluster/system-virtual-machines

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
                    </table>

Notes
-----
- This module calls /v1/cluster/system-virtual-machines  api, make sure your VxRail environment supports this API
- For more details about execution result, log file can be found at /tmp/VxRail_Ansible_Cluster_GetSystemVirtualMachines_v1.log


Examples
--------

``` yaml+jinja
  - name: Retrives name, status and host information for system  virtual machines in the VxRail cluster
    DellEMC_VxRail_Cluster_GetSystemVirtualMachines_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>When VM information exists</td>
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
            <td>
                                        <div>Status of Virtual Machine</div>
                                    <br/>
                                </td>
        </tr>   
                    </table>


Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;

Telemetry Tier Module
=================

Synopsis
--------
This module will return the system's telemetry tier.
  
Supported Endpoints
--------

* GET /v1/telemetry/tier
  

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
- Can check Log file /tmp/vxrail_telemetry_info.log for more details about execution result.


Examples
--------

``` yaml+jinja
  - name: Retrives VxRail Telemetry Tier
    DellEMC_VxRail_Telemetry_GetTier_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"

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
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>telemtry_tier</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When cluster exists.</td>
            <td>
                                        <div>The telemetry tier of the cluster.</div>
                                    <br/>
                                </td>
        </tr>

<tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>level</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                 </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The current telemetry tier of the system. Options include: BASIC (default), OFF, LIGHT, ADVANCED</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
