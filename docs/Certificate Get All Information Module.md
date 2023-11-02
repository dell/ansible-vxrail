**Certificate Get All Information module**
=================
### Product Guide

> © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell 
> EMC, and other trademarks are trademarks of Dell Inc. or its 
> subsidiaries. Other trademarks may be trademarks of their respective owners.

Synopsis
--------
This module will return the information of all the certificates in the trust store.
  
Supported Endpoints
--------

* GET /trust-store/certificates

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
</table>

Notes
-----
- This module calls /trust-store/certificates api, make sure your VxRail environment support this api. 
- Can check Log file /tmp/vxrail_ansible_certificates_get_all_info.log for more details about execution result.


Examples
--------

``` yaml+jinja
    - name: Get the information of all the certificates in the trust store with api
      dellemc_vxrail_certificates_get_all_info:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
```

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th>Minimum API Version</th>
        <th width="100%">Description</th>
        </tr>
        <tr>
            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>certificate_Information</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                </div>
            </td>
            <td>When the task of getting the certificate information is completed.</td>
            <td> v1 </td>
            <td>
                <div>Information of all certificates</div>
                <br/>
            </td>
        </tr>
        <tr>
            <td class="elbow-placeholder">&nbsp;</td>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>certificates</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                </div>
            </td>
            <td>When esisted at least one certificate file in VXM trust store</td>
            <td> v1 </td>
            <td>
                <div>List all of certificates that store in VXM trust store</div>
                <br/>
            </td>
        <tr>
            <td class="elbow-placeholder">&nbsp;</td>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
            </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The name of the certificate</div>
                <br/>
                </td>
        </tr>
        <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>
                </div>
                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The status of the certificate</div>
                <br/>
            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>status_message</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The status message of the certificate</div>
                <br/>
            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>issued_by</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
                <td>success</td>
                <td> v1 </td>
                <td>
                    <div>Name of the issuer</div>
                    <br/>
                </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>signature_algorithm</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The signature algorithm</div>
                <br/>
            </td>
        </tr>
                <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>issued_time</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The issued time</div>
                <br/>
            </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>expiration_time</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The expiration time</div>
                <br/>
            </td>
        </tr>
        <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>cert</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>Content of the certificate</div>
                <br/>
            </td>
        </tr>
        <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>filepath</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The file path of the certificate</div>
                <br/>
            </td>
        </tr>
        <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>fingerprint</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                  <br>
                  <span style="color: purple"></span>                    </div>
                                </td>
            <td>success</td>
            <td> v1 </td>
            <td>
                <div>The fingerprint of the certificate</div>
                <br/>
            </td>
        </tr>
        <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td> v1 </td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>failed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td> v1 </td>
            <td>
                                        <div>Whether or not the API call has failed or not</div>
                                    <br/>
                                </td>
        </tr>
</table>

Authors
-------

-   VxRail Development Team &lt;<ansible.team@dell.com>&gt;