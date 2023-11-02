**LCM Retry Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will retry the LCM full upgrade or partial upgrade if started through the LCM API call. 
  
Supported Endpoints
--------

* POST /lcm/upgrade/retry
  

Parameters
----------

   <table border=0
      cellpadding=0
      class="documentation-table">
      <tr>
         <th colspan="1">Parameter</th>
         <th>Choices/<font color="blue">Defaults</font>
         </th>
         <th width="100%">Comments</th>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxmip</b>
            <a class="ansibleOptionLink"
               href="#parameter-host_name"
               title="Permalink to this option"/>
            <div style="font-size: small">
               <span style="color: purple">type=string</span>
               <br>
               <span style="color: red">required=true</span>
            </div>
         </td>
         <td>
         </td>
         <td>
            <div>The IP address of the VxRail Manager System</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vcadmin</b>
            <a class="ansibleOptionLink"
               href="#parameter-host_name"
               title="Permalink to this option"/>
            <div style="font-size: small">
               <span style="color: purple">type=string</span>
               <br>
               <span style="color: red">required=true</span>
            </div>
         </td>
         <td>
         </td>
         <td>
            <div>Administrative account of the vCenter Server the VxRail Manager is registered to</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vcpasswd</b>
            <a class="ansibleOptionLink"
               href="#parameter-host_name"
               title="Permalink to this option"/>
            <div style="font-size: small">
               <span style="color: purple">type=string</span>
               <br>
               <span style="color: red">required=true</span>
            </div>
         </td>
         <td>
         </td>
         <td>
            <div>The password for the administrator account provided in vcadmin</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>api_version_number</b>
            <a class="ansibleOptionLink"
               href="#parameter-state"
               title="Permalink to this option"/>
            <div style="font-size: small">
               <span style="color: purple">type=str</span>
               <br>
               <span style="color: red"/>
            </div>
         </td>
         <td>
            <ul style="margin: 0; padding: 0">
               <b>Default:</b>
               <li>1</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade retry API, the default value is the highest available version in your VxRail system.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>timeout</b>
            <a class="ansibleOptionLink"
               href="#parameter-state"
               title="Permalink to this option"/>
            <div style="font-size: small">
               <span style="color: purple">type=integer</span>
               <br>
               <span style="color: red"/>
            </div>
         </td>
         <td>
            <ul style="margin: 0; padding: 0">
               <b>Default:</b>
               <li>21600s (6 hours)</li>
            </ul>
         </td>
         <td>
            <div>Time out value for LCM retry, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>




Notes
-----
- Make sure your VxRail environment supports the API that you use.
- This module will only retry a failed LCM upgrade. 
- This module can only retry LCM upgrades done through the LCM API call or module. Returns a 400 error when attempting to retry an upgrade started manually.
- Details on execution of module dellemc_vxrail_lcm.py can be checked in the logs /tmp/vxrail_ansible_lcm.log


Examples
--------

``` yaml+jinja
   -  name: Retry Failed LCM Upgrade. Version specified by api_version_number. 
      dellemc_vxrail_lcm_retry:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        api_version_number: "{{ api_version_number }}"
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
         <b>LCM_API_Upgrade</b>
         <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
         <div style="font-size: small">
            <span style="color: purple">type=list</span>
         </div>
      </td>
      <td>When LCM completes</td>
      <td>
         <div>LCM Status</div>
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
         <div>LCM(long-running) request returns a requestId.</div>
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
