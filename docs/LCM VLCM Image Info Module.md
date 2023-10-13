**LCM VLCM Image Information Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
> EMC, and other trademarks are trademarks of Dell Inc. or its
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will retrieve vLCM image information from the provided LCM bundle.

Supported Endpoints
--------

* Post /v1/lcm/upgrade/vlcm/image

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
            <b>vxm_root_account</b>
            <a class="ansibleOptionLink"
               href="#parameter-state"
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
            <div>The root account of VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>vxm_root_passwd</b>
            <a class="ansibleOptionLink"
               href="#parameter-state"
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
            <div>The password for the root account provided in VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>bundle</b>
            <a class="ansibleOptionLink"
               href="#parameter-state"
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
            <div>The file path for the bundle.</div>
         </td>
      </tr>
   </table>


Notes
-----
- Make sure your VxRail environment supports the API that you use.
- Details on execution of module dellemc_vxrail_lcm_vlcm_image.py can be checked in the logs /tmp/vxrail_ansible_lcm_vlcm_image.log



Examples
--------

``` yaml+jinja
    - name: Start to retrieve vLCM image information from the provided bundle.
      dellemc_vxrail_lcm_vlcm_image:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        bundle: "{{ bundle }}"
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
         <b>VLCM_IMAGE_INFO</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">complex</span>
         </div>
      </td>
      <td></td>
      <td>
         <div>The vLCM image information from the provided LCM bundle</div>
         <br/>
      </td>
   </tr>
   <tr>
      <td class="elbow-placeholder">&nbsp;</td>
      <td colspan="1">
         <div class="ansibleOptionAnchor"></div>
         <b>base_image</b>
         <a class="ansibleOptionLink" ></a>
         <div style="font-size: small">
            <span style="color: purple">type=object</span>
         </div>
      </td>
      <td>success</td>
      <td>
         <div>ersion of the vLCM image.</div>
   <tr>
      <td class="elbow-placeholder">&nbsp;</td>
      <td colspan="1">
         <div class="ansibleOptionAnchor"></div>
         <b>components</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">type=object</span>
         </div>
      </td>
      <td>success</td>
      <td>
         <div>Components of the vLCM image.</div>
    <tr>
      <td class="elbow-placeholder">&nbsp;</td>
      <td colspan="1">
         <div class="ansibleOptionAnchor"></div>
         <b>hardware_support</b>
         <a class="ansibleOptionLink"></a>
         <div style="font-size: small">
            <span style="color: purple">type=object</span>
         </div>
      </td>
      <td>success</td>
      <td>
         <div>Messages about hardware support for the vLCM image.</div>
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
         <div>Retrieve vLCM image informations success. Please see the /tmp/vxrail_ansible_lcm_vlcm_image.log for more details</div>
         <br/>
      </td>
   </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
