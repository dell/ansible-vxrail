**Day1 Initialization Module for Dell EMC VxRail**
=========================================
### Product Guide 1.4.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will configure and deploy a new VxRail cluster
  based on the provided day1 json file.

Supported Endpoints
--------

* POST /system/initialize
* GET /system/initialize/status


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
- Make sure your cluster with Day0 build only, prepare day1 json file for FirstRun
- Module dellemc_vxrail_day1.py can call any existing version of /system/initialize and /system/initialize/status API
- Details on execution of module dellemc_vxrail_day1.py  can be checked in the logs /tmp/vxrail_ansible_day1.log


Examples
--------

``` yaml+jinja
  - name: Configure and deploy a new VxRail cluster
    dellemc_vxrail_day1:
        vxmip: "{{ vxmip }}"
        day1json_file: "{{ day1json_file }}"
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
		<th>Minimum API Version</th>
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
			<td>all</td>
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
			<td>v1</td>
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
			<td> </td>
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
			<td>v1</td>
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
			<td>v1</td>			
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
			<td> </td>		
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
			<td>v1</td>
            <td>
                                        <div>The current state of the execution</div>

</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;