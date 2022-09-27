**Host Folder LCM Module for Dell EMC VxRail**
=========================================
### Product Guide 1.4.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
> EMC, and other trademarks are trademarks of Dell Inc. or its
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------

This module will perform node upgrade for all eligible satellite nodes in the specific host folder
based on the provided upgrade specification and query the status.

Supported Endpoints
--------

* POST /lcm/host-folder/upgrade


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
            <b>action</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>
            </div>
        </td>
        <td>
            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                <li>UPGRADE</li>
                <li>STAGE</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>STAGE will transfer the upgrade bundle to the nodes but will not initiate the upgrade procedure. UPGRADE will initiate the upgrade procedure.</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>api_version_number</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=integer</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>A specific version number to use for the API call. If not included, will use the highest version by default</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>concurrent_size</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=integer</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>Number of nodes that can be upgraded in parallel. This parameter is only valid for UPGRADE requests.</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>failure_rate</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=int</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>The failure rate of LCM batch job. failure_rate = failed nodes count / total nodes count. This parameter is only valid for UPGRADE requests.</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>folder_id</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>The specific folder id</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>target_version</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>The target VxRail system version</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>vcadmin</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>Administrative account of the vCenter Server the VxRail Manager is registered to</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>vcpasswd</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>The password for the administrator account provided in vcadmin</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
            <b>vxmip</b>
            <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>
            </div>
        </td>
        <td></td>
        <td>
            <div></div>
            <div>The IP address of the VxRail Manager System</div>
        </td>
    </tr>
</table>

Notes
-----

- Make sure your VxRail environment supports the API that you use
- Module dellemc_vxrail_host_folder_upgrade.py can call any existing version of /lcm/host-folder/upgrade API
- Can check Log file /tmp/vxrail_ansible_host_folder_upgrade.log for more details about folders upgrade.

Examples
--------

``` yaml+jinja
- name: Start host folder upgrade. Version specified by api_version_number
  dellemc_vxrail_host_folder_upgrade:
      vxmip: "{{ vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
      action: "{{ action }}"
      folder_id: "{{ folder_id }}"
      target_version: "{{ target_version }}"
      failure_rate: "{{ failure_rate }}"
      concurrent_size: "{{ concurrent_size }}"
      api_version_number: "{{ api_version_number }}"
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
            <b>NodeExpansion</b>
            <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=list</span>
            </div>
        </td>
        <td>When Host Folder Upgrade completes</td>
        <td>
            <div>Host Folder Upgrade Status</div>
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
            <div>Host Folder Upgrade (long-running) request returns a requestId.</div>
        </td>
    </tr>
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
        </td>
    </tr>
</table>

Authors
-------

- VxRail Development Team &lt;<ansible.team@dell.com>&gt;
