**LCM Module for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
> EMC, and other trademarks are trademarks of Dell Inc. or its
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will perform the LCM full upgrade or partial upgrade via v4+ API of all VxRail software and hardware.

Supported Endpoints
--------

* POST /lcm/upgrade


Parameters
----------

<details>
   <summary>/v1/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>psc_root_account</b>
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
         </td>
         <td>
            <div>Root account of the PSC the VxRail Manager is registered to.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>psc_root_passwd</b>
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
         </td>
         <td>
            <div>The password for the root account provided in PSC.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_psc_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source PSC host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_psc_host_user_name</b>
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
         </td>
         <td>
            <div>The username of source PSC host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_psc_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of source PSC host account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
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
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>
<details>
   <summary>/v2/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>psc_root_account</b>
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
         </td>
         <td>
            <div>Root account of the PSC the VxRail Manager is registered to.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>psc_root_passwd</b>
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
         </td>
         <td>
            <div>The password for the root account provided in PSC.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_psc_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source PSC host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_psc_host_user_name</b>
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
         </td>
         <td>
            <div>The username of source PSC host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_psc_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of source PSC host account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
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
               <li>2</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>
<details>
   <summary>/v3/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
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
               <li>3</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>
<details>
   <summary>/v4/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_hosts_name</b>
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
         </td>
         <td>
            <div>The list of the target host name for partial upgrade, the default value is all host.</div>
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
               <li>4</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>
<details>
   <summary>/v5/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_hosts_name</b>
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
         </td>
         <td>
            <div>The list of the target host name for partial upgrade, the default value is all host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>missing_file_check</b>
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
               <li>true</li>
            </ul>
         </td>
         <td>
            <div>Validate if all files in the upgrade bundle are present. The default value is true, set to false when using a customized bundle.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>skip_failed_hosts</b>
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
         </td>
         <td>
            <div>Skip the nodes that the upgrade failed. The default value is false.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_components</b>
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
         </td>
         <td>
            <div>The components of ecosystem pre-check. The default components are RP4VM, WITNESS, and EXTERNAL_VC.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_continue_with_incompatible</b>
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
         </td>
         <td>
            <div>Ignore the ecosystem pre-check when set to true. The default value is false.</div>
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
               <li>5</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>
<details>
   <summary>/v6/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vc_mgmt_account</b>
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
            <div>Management account of the vCenter Server</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vc_mgmt_passwd</b>
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
            <div>The password for the management account of the vCenter Server</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_hosts_name</b>
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
         </td>
         <td>
            <div>The list of the target host name for partial upgrade, the default value is all host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>missing_file_check</b>
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
               <li>true</li>
            </ul>
         </td>
         <td>
            <div>Validate if all files in the upgrade bundle are present. The default value is true, set to false when using a customized bundle.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>skip_failed_hosts</b>
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
         </td>
         <td>
            <div>Skip the nodes that the upgrade failed. The default value is false.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_components</b>
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
         </td>
         <td>
            <div>The components of ecosystem pre-check. The default components are RP4VM, WITNESS, and EXTERNAL_VC.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_continue_with_incompatible</b>
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
         </td>
         <td>
            <div>Ignore the ecosystem pre-check when set to true. The default value is false.</div>
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
               <li>5</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>
<details>
   <summary>/v7/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_hosts_name</b>
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
         </td>
         <td>
            <div>The list of the target host name for partial upgrade, the default value is all host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>missing_file_check</b>
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
               <li>true</li>
            </ul>
         </td>
         <td>
            <div>Validate if all files in the upgrade bundle are present. The default value is true, set to false when using a customized bundle.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>skip_failed_hosts</b>
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
         </td>
         <td>
            <div>Skip the nodes that the upgrade failed. The default value is false.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_components</b>
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
         </td>
         <td>
            <div>The components of ecosystem pre-check. The default components are RP4VM, WITNESS, and EXTERNAL_VC.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_continue_with_incompatible</b>
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
         </td>
         <td>
            <div>Ignore the ecosystem pre-check when set to true. The default value is false.</div>
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
               <li>7</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>

<details>
   <summary>/v8/lcm/upgrade</summary>
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
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_account</b>
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
            <div>Root account of  VxRail Manager</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>vxm_root_passwd</b>
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
            <div>The password for the root account provided in vxm root account</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-host_name"/>
            <b>bundle</b>
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
            <div>The path of lcm bundle on vxm, which is recommended under /data/store2</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>source_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The password of account in the source ESXi host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_name</b>
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
         </td>
         <td>
            <div>Hostname of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_name</b>
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
         </td>
         <td>
            <div>The username of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_vcsa_host_user_passwd</b>
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
         </td>
         <td>
            <div>The account password of the target host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_ip</b>
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
         </td>
         <td>
            <div>Temporary IP to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_gateway</b>
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
         </td>
         <td>
            <div>Gateway to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>temporary_netmask</b>
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
         </td>
         <td>
            <div>Netmask to be used during the vCenter upgrade.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_username</b>
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
         </td>
         <td>
            <div>Username of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>witness_password</b>
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
         </td>
         <td>
            <div>Password of the witness account.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>auto_witness_upgrade</b>
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
         </td>
         <td>
            <div>Automatically upgrade the witness node by VxRail.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>preferred_fault_domain_first</b>
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
         </td>
         <td>
            <div>Upgrade preferred fault domain hosts first.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>target_hosts_name</b>
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
         </td>
         <td>
            <div>The list of the target host name for partial upgrade, the default value is all host.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>missing_file_check</b>
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
               <li>true</li>
            </ul>
         </td>
         <td>
            <div>Validate if all files in the upgrade bundle are present. The default value is true, set to false when using a customized bundle.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>skip_failed_hosts</b>
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
         </td>
         <td>
            <div>Skip the nodes that the upgrade failed. The default value is false.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_components</b>
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
         </td>
         <td>
            <div>The components of ecosystem pre-check. The default components are RP4VM, WITNESS, and EXTERNAL_VC.</div>
         </td>
      </tr>
      <tr>
         <td colspan="1">
            <div class="ansibleOptionAnchor"
               id="parameter-state"/>
            <b>ecosystem_check_continue_with_incompatible</b>
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
         </td>
         <td>
            <div>Ignore the ecosystem pre-check when set to true. The default value is false.</div>
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
               <li>7</li>
            </ul>
         </td>
         <td>
            <div>The version of LCM upgrade API, the default value is the highest available version in your VxRail system.</div>
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
            <div>Time out value for LCM, the default value is 21600 seconds(6 hours).</div>
         </td>
      </tr>
   </table>
</details>

Notes
-----
- Make sure your VxRail environment supports the API that you use.
- Make sure you have done precheck action, e.g., upload bundle to vxrail manager..., we suggest upload it under /data/store2 directory.
- Make sure vlcm is enabled if you would like to do th partial upgrade.
- The information for vCenter migration part based upgrade, for major vCenter upgrades (e.g., from v6.7 to v7.0), the following parameters must be provided: source_vcsa_host_name, source_vcsa_host_user_name, source_vcsa_host_user_passwd, source_psc_host_name, source_psc_host_user_name, target_vcsa_host_name target_vcsa_host_user_name, target_vcsa_host_user_passwd, temporary_ip, temporary_gateway, temporary_netmask. For minor vCenter upgrades (for example v7.0 U1 to v7.0 U2), these parameters must be null.
- Details on execution of module dellemc_vxrail_lcm.py can be checked in the logs /tmp/vxrail_ansible_lcm.log


Examples
--------

``` yaml+jinja
   -  name: Start to upgrade with v1
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"

   -  name: Start to upgrade with v2
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        witness_username: "{{ witness_username | default(omit) }}"
        witness_password: "{{ witness_password | default(omit) }}"
        auto_witness_upgrade: "{{ auto_witness_upgrade | default(omit) }}"
        preferred_fault_domain_first: "{{ preferred_fault_domain_first | default(omit) }}"

   -  name: Start to upgrade with v3
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        witness_username: "{{ witness_username | default(omit) }}"
        witness_password: "{{ witness_password | default(omit) }}"
        auto_witness_upgrade: "{{ auto_witness_upgrade | default(omit) }}"
        preferred_fault_domain_first: "{{ preferred_fault_domain_first | default(omit) }}"

   -  name: Start to upgrade with v4
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        target_hosts_name: "{{ target_hosts_name | default(omit) }}"

   -  name: Start to upgrade with v5
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        missing_file_check: "{{ missing_file_check | default(True) }}"
        skip_failed_hosts: "{{ skip_failed_hosts | default(omit) }}"
        ecosystem_check_continue_with_incompatible: "{{ ecosystem_check_continue_with_incompatible | default(omit) }}"
        ecosystem_check_components: "{{ ecosystem_check_components | default(omit) }}"

   -  name: Start to upgrade with v6
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vc_mgmt_account: "{{ vc_mgmt_account_var }}"
        vc_mgmt_passwd: "{{ vc_mgmt_passwd_var }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        missing_file_check: "{{ missing_file_check | default(True) }}"
        skip_failed_hosts: "{{ skip_failed_hosts | default(omit) }}"
        ecosystem_check_continue_with_incompatible: "{{ ecosystem_check_continue_with_incompatible | default(omit) }}"
        ecosystem_check_components: "{{ ecosystem_check_components | default(omit) }}"

   -  name: Start to upgrade with v7
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        missing_file_check: "{{ missing_file_check | default(True) }}"
        skip_failed_hosts: "{{ skip_failed_hosts | default(omit) }}"
        ecosystem_check_continue_with_incompatible: "{{ ecosystem_check_continue_with_incompatible | default(omit) }}"
        ecosystem_check_components: "{{ ecosystem_check_components | default(omit) }}"

   -  name: Start to upgrade with v8
      dellemc_vxrail_lcm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        bundle: "{{ bundle }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        missing_file_check: "{{ missing_file_check | default(True) }}"
        skip_failed_hosts: "{{ skip_failed_hosts | default(omit) }}"
        ecosystem_check_continue_with_incompatible: "{{ ecosystem_check_continue_with_incompatible | default(omit) }}"
        ecosystem_check_components: "{{ ecosystem_check_components | default(omit) }}"
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
