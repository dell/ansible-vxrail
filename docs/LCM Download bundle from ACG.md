**LCM downlad bundle from ACG server for Dell EMC VxRail**
=========================================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners. 

Synopsis
--------
This module will downlaod a available online updates into VxM.

Supported Endpoints
--------

* Get  /lcm/available-online-updates
* Post /lcm/available-online-updates/{update_id}/download
* Get  /lcm/download-progress/{request_id}

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
- Make sure your VxRail environment supports the API that you use (DI is enabled)
- Module dellemc_vxrail_lcm_acg_available_online_download.py calls any existing version for download available online updates packages
- Details on execution of module dellemc_vxrail_lcm_acg_available_online_download.py can be checked in the logs /tmp/vxrail_ansible_lcm_acg_available_online_download.log

Examples
--------

``` yaml+jinja
    - name: Get available online updates packages
      dellemc.vxrail.dellemc_vxrail_lcm_acg_available_online_download:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
      register: download_acg_available_packages

    - name: Display download ACG available packages result
      debug:
        msg: "{{ download_acg_available_packages }}"
```

Return Values
-------------
* /lcm/available-online-updates. 
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
            <b>id</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>Example: 1234</td>
        <td>
            <div>Available online updates package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>version</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>7.0.450</td>
        <td>
            <div>Available online updates package version.</div>
            <br/>
        </td>
    </tr>
    </tr>
        <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>file_path</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>STARTED
            IN_PROGRESS
            FAILED
            COMPLETED
        </td>
        <td>
            <div>Available online updates package path.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>title</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>VxRail 7.0.450 GA</td>
        <td>
            <div>Title of vailable online updates package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>description</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>Critical fixes and enhancements</td>
        <td>
            <div>Description of download package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>is_recommend</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>true</td>
        <td>
            <div>End time of download package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>publish_date</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>2025-07-01T07:01:30.872709</td>
        <td>
            <div>Publish date.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>link</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>[]</td>
        <td>
            <div>URL of AR report.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>type</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>FULL_BUNDLE</td>
        <td>
            <div>Type of download package.</div>
            <br/>
        </td>
    </tr>
</table>

* /lcm/available-online-updates/{update_id}/download. 
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
            <b>request_id</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>Example: 5ffe7062-a590-45b8-a172-8d2cf119562e</td>
        <td>
            <div>Download task ID.</div>
            <br/>
        </td>
    </tr>
</table>

* /v1/lcm/download-progress/{request_id}. 
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
            <b>requestID</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>Example: 66366c67-e5ba-42e7-a57d-948ad7827a7</td>
        <td>
            <div>Download task ID.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>updateID</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>Example: 80360175</td>
        <td>
            <div>Available online updates package ID.</div>
            <br/>
        </td>
    </tr>
    </tr>
        <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>status</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>STARTED
            IN_PROGRESS
            FAILED
            COMPLETED
        </td>
        <td>
            <div>Status for download available online updates package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>progress</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>0</td>
        <td>
            <div>Download progress of vailable online updates package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>startTime</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>/data/store2/lcm_download</td>
        <td>
            <div>Start time of download package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>endTime</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>2025-07-01T07:01:30.872709</td>
        <td>
            <div>End time of download package.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>downloadDirectory</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>2025-07-01T07:01:30.872709</td>
        <td>
            <div>Download package will be save in /data/store2/lcm_download.</div>
            <br/>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            <div class="ansibleOptionAnchor" id="return-changed"></div>
            <b>downloadedFiles</b>
            <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
            <div style="font-size: small">
                <span style="color: purple">type=string</span>
            </div>
        </td>
        <td>[]</td>
        <td>
            <div>Nmae of download package.</div>
            <br/>
        </td>
    </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;