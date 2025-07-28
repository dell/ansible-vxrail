**Support Logs Get Module for Dell EMC VxRail**
===============================================

### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
> EMC, and other trademarks are trademarks of Dell Inc. or its
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------

This module will retrieve VxRail Support Logs Information by Id.

Supported Endpoints
-------------------

* GET /support/logs/{log_id}

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
                <b>log_id</b>
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
                                        <div>Support log id</div>
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

- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_support_logs_id_get.py calls any existing version of Get /support/logs/{log_id} API
- Details on execution of module dellemc_vxrail_support_logs_id_get.py can be checked in the logs /tmp/vxrail_log_support_logs_id_get.log

Examples
--------

```yaml+jinja
 - name: Retrieves VxRail Support Logs Information, version specified by api_version_number
   dellemc.vxrail.dellemc_vxrail_support_logs_get:
     vxmip: "{{ vxmip }}"
     vcadmin: "{{ vcadmin }}"
     vcpasswd: "{{ vcpasswd }}"
     log_id: "{{ log_id }}"
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
        <th width="100%">Description</th>
    </tr>
        <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>support_logs_information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When the support logs information exists.</td>
            <td>
                                        <div>Information about the support logs</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder"> </td>
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
                                        <div>support log id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder"> </td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>creation_time</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=timestamp</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>support log create time</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder"> </td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>path</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>support log path in the VxRail manager</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder"> </td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=int</span>
                </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>support log size</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

- VxRail Development Team &lt;<ansible.team@dell.com>&gt;
