**LCM Upload Customized Component Module for Dell EMC VxRail**
=========================================
### Product Guide 1.6.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will upload a customized Component for legacy LCM mode.

Supported Endpoints
--------

* Post /lcm/upgrade/upload-bundle

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
                <span style="color: red">required=true</span>                
            </div>
        </td>
        <td></td>                                                                
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
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>vcpasswd</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
                <br>
                <span style="color: red">required=true</span>                   
            </div>
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
            <b>customized_component</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
            <span style="color: purple">type=string</span>
            <br>
            <span style="color: red">required=true</span>                    
            </div>
        </td>
        <td>
            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                <li>true</li>
                <li>false</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>Default value is true. Specifies if the uploading file is a customized component. If specifies as false, system will treat this file as a common file, such as lcm bundle.</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>checksum</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
            <span style="color: purple">type=string</span>
            <br>
            <span style="color: red">required=true</span>                    
        </div>
        </td>
        <td>
        </td>
        <td>
            <div></div>
            <div>Specifies the checksum of uploading file encoded in SHA512. Users need to fill in the correct checksum value, which will be verified after uploading.</div>
            </div>How to manually generate SHA512 checksum value:</div>
               <div>1. Linux system: sha512sum <component file></div>
                  <div>ex: sha512sum  NVD-VGPU_460.32.04-1OEM.700.0.0.15525992_17478485.zip</div>
               <div>2. Windows 10 system: certutil -hashfile <component file> sha512</div>
                  <div>ex: certutil -hashfile NVD-VGPU_460.32.04-1OEM.700.0.0.15525992_17478485.zip sha512</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>type</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
            <span style="color: purple">type=string</span>
            <br>
            <span style="color: red">required=true</span>                    
        </div>
        </td>
        <td>
            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                <li>driver</li>
                <li>firmware</li>
                <li>bundle</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>Only support driver/firmware/bundle customized type.</div>
        </td>
    </tr>
    <tr>
        <td colspan="1">
            <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
            <b>component_bundle</b>
            <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
            <div style="font-size: small">
            <span style="color: purple">type=string</span>
            <br>
            <span style="color: red">required=true</span>                    
        </div>
        </td>
        <td>
        </td>
        <td>
            <div></div>
            <div>The path of the file to be uploaded on the local machine. To upload files, the Content-Type must be set to "multipart/form-data".</div>
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
            <span style="color: red"></span>                  
            </div>
        </td>
        <td>
            <ul style="margin: 0; padding: 0"><b>Default:</b>
                <li>3600s</li>
            </ul>
        </td>
        <td>
            <div></div>
            <div>Time out value for uploading customized component, the default value is 3600 seconds</div>
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
            <span style="color: red"></span>                    
            </div>
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
- Module dellemc_vxrail_lcm_customized_component.py calls any existing version of Post /lcm/upgrade/upload-bundle API
- Details on execution of module dellemc_vxrail_lcm_customized_component.py can be checked in the logs /tmp/vxrail_ansible_lcm_customized_component.log

Examples
--------

``` yaml+jinja
    - name: Start to upload customized component
      dellemc_vxrail_lcm_customized_component:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        customized_component: "{{ customized_component }}"
        checksum: "{{ checksum }}"
        type: "{{ type }}"
        component_bundle: "{{ component_bundle }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
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
            <b>file</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>success</td>
        <td>
            <div>Upload customized component is completed and return the upload path.</div>
            <br/>
        </td>
    </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;