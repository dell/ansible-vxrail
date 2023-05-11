**Certificate Import Certs Into Truststore module**
=================
### Product Guide 2.0.0

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will let you to import certificates into the VXM trust store according to parameters list.
  
Supported Endpoints
--------

* POST /trust-store/certificates

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
                                                                                                                                                                                        <li>60 seconds</li>
                                                                                                            </ul>
                                                                                                    </td>
                                                                                        <td>
                                                                    <div></div>
                                                                    <div>Time out value for get cert content, the default value is 60 seconds.</div>
                                                                    <div></div>
                                                                                </td>
</tr>
<tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>certs</b>
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
                                        <div>Provide a certificates or certificates + CRL list to import certificates into the VXM trust store</div>
                                                    </td>
        </tr>

</table>

Notes
-----
- This module calls /trust-store/certificates api, make sure your VxRail environment support this api. 
- Can check Log file /tmp/vxrail_ansible_importcertsintotruststore.log for more details about execution result.


Examples
--------

``` yaml+jinja
    - name: Import certificates into VXM trust store with api
      dellemc_vxrail_certificates_getcontent:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        certs: "{{ certs }}"
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
                <b>certs</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When the parameters is legal certificates.</td>
            <td>
                                        <div>Import the certificates into the VXM trust store</div>
                                    <br/>
                                </td>
        </tr>

</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
