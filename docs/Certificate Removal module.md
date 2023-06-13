**Certificate Removal module**
=================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will let you remove certificates from VXM trust store according to fingerprint.
  
Supported Endpoints
--------

* DELETE /trust-store/certificates/{fingerprint}

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
                <b>fingerprint</b>
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
                                        <div>Provide a fingerprint for delete target certificate from VXM trust store</div>
                                                    </td>
        </tr>

</table>

Notes
-----
- This module calls DELETE /trust-store/certificates/{fingerprint} api, make sure your VxRail environment support this api. 
- Can check Log file /tmp/vxrail_ansible_removecertificate.log for more details about execution result.


Examples
--------

``` yaml+jinja
    - name: Remove the certificate according to the fingerprint
      dellemc_vxrail_certificates_removecertificate:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        fingerprint: "{{ fingerprint }}"
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
                <b>fingerprint</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                                      </div>
                                </td>
            <td>When the target certificate has been existed in VXM trust store.</td>
            <td>
                                        <div>Remove certificate from VXM trust store</div>
                                    <br/>
                                </td>
        </tr>

</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;
