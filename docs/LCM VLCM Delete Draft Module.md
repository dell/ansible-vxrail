**LCM VLCM Information Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
> EMC, and other trademarks are trademarks of Dell Inc. or its
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will delete vLCM draft.

Supported Endpoints
--------

* DELETE /v1/lcm/vlcm/enablement/draft

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
               id="parameter-host_name"/>
            <b>vc_root_account</b>
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
            <div>Root account of the vCenter Server the VxRail Manager is registered to</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vc_root_passwd</b>
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
            <div>The password for the root account provided in vcadmin</div>
         </td>
      </tr>
   </table>


Notes
-----
- Make sure your VxRail environment supports the API that you use.
- Details on execution of module dellemc_vxrail_lcm_vlcm_delete_draft.py can be checked in the logs /tmp/vxrail_ansible_lcm_vlcm_delete_draft.log



Examples
--------

``` yaml+jinja
    - name: Start to delete vLCM draft
      dellemc_vxrail_lcm_vlcm_delete_draft:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
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
         <b>VLCM_DELETE_DRAFT_API</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">complex</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>The delete vLCM draft info from the cluster</div>
         <br/>
      </td>
   </tr>
   <tr>
      <td class="elbow-placeholder">&nbsp;</td>
      <td colspan="1">
         <div class="ansibleOptionAnchor"></div>
         <b>result</b>
         <a class="ansibleOptionLink" ></a>
         <div style="font-size: small">
            <span style="color: purple">type=string</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>The result of deleting vlcm draft</div>
   </tr>
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
         <div>End of deleting vLCM draft. Please see the /tmp/vxrail_ansible_lcm_vlcm_delete_draft.log for more details</div>
         <br/>
      </td>
   </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
