**LCM VLCM Information Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
> EMC, and other trademarks are trademarks of Dell Inc. or its
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will retrieve cluster vLCM information to check if vlcm enable or not.

Supported Endpoints
--------

* Get /v1/lcm/vlcm

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
   </table>


Notes
-----
- Make sure your VxRail environment supports the API that you use.
- Details on execution of module dellemc_vxrail_lcm_vlcm_get.py can be checked in the logs /tmp/vxrail_ansible_lcm_vlcm.log



Examples
--------

``` yaml+jinja
    - name: Start to retrieve cluster vLCM information
      dellemc_vxrail_lcm_vlcm_get:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
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
         <div class="ansibleOptionAnchor"></div>
         <b>VLCM_INFO</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">complex</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>The vLCM info from the cluster</div>
         <br/>
      </td>
   </tr>
   <tr>
      <td class="elbow-placeholder">&nbsp;</td>
      <td colspan="1">
         <div class="ansibleOptionAnchor"></div>
         <b>enable</b>
         <a class="ansibleOptionLink" ></a>
         <div style="font-size: small">
            <span style="color: purple">type=boolean</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>The vlcm enable status in the cluster</div>
   <tr>
      <td class="elbow-placeholder">&nbsp;</td>
      <td colspan="1">
         <div class="ansibleOptionAnchor"></div>
         <b>cluster_name</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">type=string</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>The name of cluster</div>
       <tr>
    <td colspan="2">
         <div class="ansibleOptionAnchor"></div>
         <b>msg</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">type=string</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>Retrieve vLCM informations success. Please see the /tmp/vxrail_ansible_lcm_vlcm.log for more details</div>
         <br/>
      </td>
   </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
