# Ansible Modules for Dell EMC VxRail

The Ansible Modules for Dell EMC VxRail allow data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC VxRail.

The capabilities of Ansible modules are gathering system information and performing Lay2 Node Expansion. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## Support
Ansible modules for VxRail are supported by Dell EMC open source community, but not product support agreements, and are provided under the terms of the license attached to the source code. Dell EMC does not provide support for any source code modifications. For any Ansible module issues, questions or feedback, join the [Dell EMC Automation community]( https://www.dell.com/community/Automation/bd-p/Automation ).

## Supported Platforms
  * Dell EMC VxRail

## Prerequisites
This table provides information about the software prerequisites for the Ansible Modules for Dell EMC VxRail.

| **Ansible Modules** | **VxRail version** | **Python version** | **Python library (VxRail Ansible Utility) version** | **Ansible Version** |
|---------------------|----------------|--------------------|----------------------------|-------------|
| v2.9.0 | 8.0.360 | 2.9.0 | 2.9.0 | 2.9 and 2.10 |

  * Please follow VxRail Ansible Utility installation instructions on [VxRail Ansible Utility Documentation](https://github.com/dell/ansible-vxrail-utility)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC VxRail
  * [Auto Discovery hosts module](./docs/Day1%20Auto%20Discovery%20Host%20Module.md)
  * [Callhome Information module](./docs/Callhome%20Information%20Module.md)
  * [Callhome Disable module](./docs/Callhome%20Disable%20Module.md)
  * [Callhome Enable module](./docs/Callhome%20Enable%20Module.md)
  * [Callhome Mode Information module](./docs/Callhome%20Mode%20Information%20Module.md)
  * [Callhome Mode Change module](./docs/Callhome%20Mode%20Change%20Module.md)
  * [Certificate Get Automated Renewal Configurations module](./docs/Certificate%20Get%20Automated%20Renewal%20Configurations%20Module.md)
  * [Certificate Get Automated Renewal Status module](./docs/Certificate%20Get%20Automated%20Renewal%20Status%20Module.md)
  * [Certificate Get Content module](./docs/Certificate%20Get%20Content%20module.md)
  * [Certificate Get Fingerprints module](./docs/Certificate%20Get%20Fingerprints%20module.md)
  * [Certificate Get All Information module](./docs/Certificate%20Get%20All%20Information%20Module.md)
  * [Certificate Import Certs Into Truststore module](./docs/Certificate%20Import%20Certs%20Into%20Truststore%20module.md)
  * [Certificate Removal module](./docs/Certificate%20Removal%20module.md)
  * [Certificate Signing Request Generation module](./docs/Certificate%20CSR%20Module.md)
  * [Certificate Update Automated Renewal Configurations module](./docs/Certificate%20Update%20Automated%20Renewal%20Configurations%20Module.md)
  * [Certificate Update module](./docs/Certificate%20Update%20Module.md)
  * [Certificate Validate module](./docs/Certificate%20Validation%20Module.md)
  * [Chassis module](./docs/Chassis%20Module.md)
  * [Cluster expansion module](./docs/Cluster%20Expansion%20Module.md)
  * [Cluster expansion cancel module](./docs/Cluster%20Expansion%20Cancel%20Module.md)
  * [Cluster information module](./docs/Cluster%20Info%20Module.md)
  * [Cluster Layer3 Get Segment Health module](./docs/Cluster%20Layer3%20Get%20Segment%20Health%20module.md)
  * [Cluster Layer3 Get Segments module](./docs/Cluster%20Layer3%20Get%20Segments%20module.md)
  * [Cluster Layer3 New Segment module](./docs/Cluster%20Layer3%20New%20Segment%20module.md)
  * [Cluster Layer3 Segement change module](./docs/Cluster%20Layer3%20Segment%20change%20module.md)
  * [Cluster Layer3 Segment Label change module](./docs/Cluster%20Layer3%20Segment%20Label%20change%20module.md)
  * [Cluster Layer3 Segment remove module](./docs/Cluster%20Layer3%20Segment%20remove%20module.md)
  * [Cluster Layer3 Specific Segment module](./docs/Cluster%20Layer3%20Specific%20Segment%20module.md)
  * [Cluster Portgroups module](./docs/System%20Cluster-Portgroups%20Module.md)
  * [Cluster Shutdown module](./docs/Cluster%20Shutdown%20Module.md)
  * [Configure Manager Address module](./docs/Configure%20Manager%20Address%20module.md)
  * [Customer Supplied Hosts module](./docs/Customer%20Supplied%20Hosts%20Module.md)
  * [CVS Compliance Report module](./docs/CVS%20Compliance%20Report%20Module.md)
  * [Day1 Initialization module](./docs/Day1%20Initialization%20Module.md)
  * [Dell Identity Service Start Device Auth](./docs/Dell%20Identity%20Service%20Start%20Device%20Auth.md)
  * [Dell Identity Service Logout Device Auth](./docs/Dell%20Identity%20Service%20Logout%20Device%20Auth.md)
  * [Dell Identity Service Query Device Auth](./docs/Dell%20Identity%20Service%20Query%20Device%20Auth.md)
  * [Disks Information module](./docs/Disks%20Information%20Module.md)
  * [Export CVS Compliance Report module](./docs/Export%20CVS%20Compliance%20Report%20Module.md)
  * [Hosts module](./docs/Hosts%20Module.md)
  * [Host Shutdown module](./docs/Host%20Shutdown%20Module.md)
  * [Hosts Update module](./docs/Hosts%20Update%20Module.md)
  * [iDRAC Add User Module](./docs/iDRAC%20Add%20User%20Module.md)
  * [iDRAC Available User Slot ID Module](./docs/iDRAC%20Available%20User%20Slot%20ID%20Module.md)
  * [iDRAC Network Settings module](./docs/iDRAC%20Network%20Settings%20Module.md)
  * [iDRAC Update Network Settings Module](./docs/iDRAC%20Update%20Network%20Settings%20Module.md)
  * [iDRAC Update User Account Information Module](./docs/iDRAC%20Update%20User%20Account.md)
  * [iDRAC Users module](./docs/iDRAC%20Users%20Module.md)
  * [LCM Advisory Meta Bundle module](./docs/LCM%20Advisory%20Meta%20Bundle%20Module.md)
  * [LCM Upload Customized Component](./docs/LCM%20Upload%20Customized%20Component.md)
  * [LCM Advisory Report module](./docs/LCM%20Advisory%20Report%20Module.md)
  * [LCM module](./docs/LCM%20Module.md)
  * [LCM Retry module](./docs/LCM%20Retry%20Module.md)
  * [LCM VLCM Image Info module](./docs/LCM%20VLCM%20Image%20Info%20Module.md)
  * [LCM VLCM Info module](./docs/LCM%20VLCM%20Info%20Module.md)
  * [LCM VLCM Enable module](./docs/LCM%20VLCM%20Enable%20Module.md)
  * [LCM VLCM Generate Draft module](./docs/LCM%20VLCM%20Generate%20Draft%20Module.md)
  * [LCM VLCM Commit Draft module](./docs/LCM%20VLCM%20Commit%20Draft%20Module.md)
  * [LCM VLCM Delete Draft module](./docs/LCM%20VLCM%20Delete%20Draft%20Module.md)
  * [LCM Download Available Bundle module](./docs/LCM%20Download%20bundle%20from%20ACG.md)
  * [Host Folder LCM](./docs/Host%20Folder%20LCM.md)
  * [LCM Precheck module](./docs/LCM%20Precheck%20Module.md)
  * [LCM Zero Day Express Patch Module](./docs/LCM%20Zero%20Day%20Express%20Patch%20Module)
  * [Network throttling Change module](./docs/Bandwidth%20Throttling%20Change%20Module.md)
  * [Network throttling Info module](./docs/Bandwidth%20Throttling%20Information%20Module.md)
  * [Prechecks Report Module](./docs/Prechecks%20Report%20Module.md)
  * [Remove Host module](./docs/Remove%20Host%20Module.md)
  * [Satellite Node Expansion module](./docs/Satellite%20Node%20Expansion%20Module.md)
  * [Satellite Node Remove module](./docs/Satellite%20Node%20Remove%20Module.md)
  * [Sequential Reboot Cancel Module](./docs/Sequential%20Reboot%20Cancel%20Module.md)
  * [Sequential Reboot Module](./docs/Sequential%20Reboot%20Module.md)
  * [Sequential Reboot Retry Module](./docs/Sequential%20Reboot%20Retry%20Module.md)
  * [Stig Information module](./docs/Stig%20Information%20Module.md)
  * [System Available Hosts module](./docs/System%20Available%20Hosts%20Module.md)
  * [System Cluster Hosts module](./docs/System%20Cluster%20Hosts%20Module.md)
  * [System Disable Proxy module](./docs/System%20Disable%20Proxy%20Module.md)
  * [System DNS Change module](./docs/DNS%20Change%20Module.md)
  * [System DNS Information module](./docs/DNS%20Information%20Module.md)
  * [System Get Management Accounts module](./docs/System%20Get%20Management%20Accounts%20Module.md)
  * [System Internet Mode Change module](./docs/System%20Internet%20Mode%20Change%20Module.md)
  * [System Internet Mode Information module](./docs/System%20Internet%20Mode%20Information%20Module.md)
  * [System module](./docs/System%20Module.md)
  * [System NTP Change module](./docs/NTP%20Change%20Module.md)
  * [System NTP Information module](./docs/NTP%20Information%20Module.md)
  * [System Precheck module](./docs/System%20Precheck%20Module.md)
  * [System Prechecks Profiles module](./docs/System%20Prechecks%20Profiles%20Module.md)
  * [System Precheck Version module](./docs/System%20Precheck%20Version%20Module.md)
  * [System Proxy Information module](./docs/System%20Proxy%20Information%20Module.md)
  * [System Set Proxy module](./docs/System%20Set%20Proxy%20Module.md)
  * [System Update Credential module](./docs/System%20Update%20Credential%20Module.md)
  * [System Update Proxy module](./docs/System%20Update%20Proxy%20Module.md)
  * [System Validate Credential module](./docs/System%20Validate%20Credential%20Module.md)
  * [System Virtual Machines module](./docs/System%20Virtual%20Machines%20Module.md)
  * [Telemetry Tier Change module](./docs/Telemetry%20Tier%20Change%20Module.md)
  * [Telemetry Tier Info module](./docs/Telemetry%20Tier%20Information%20Module.md)
  * [VC Mode Change module](./docs/VC%20Mode%20Change%20Module.md)
  * [VC Mode Information module](./docs/VC%20Mode%20Information%20Module.md)


## Installation of SDK

Install the python sdk named ['VxRail Ansible Utility'](https://github.com/dell/ansible-vxrail-utility). It can be installed using pip, based on the appropriate python version.

## Installing Collections

  * Download the tar build and install the collection anywhere in your system, e.g.

        ansible-galaxy collection install dellemc-vxrail-1.1.0.tar.gz -p <install_path>

  * Set the environment variable:

        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections

  * In order to use any Ansible module, ensure that the importation of the proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. For example,
<br>collections:
<br>&nbsp;&nbsp;&nbsp; - dellemc.vxrail
  * To generate Ansible documentation for a specific module, embed the FQCN before the module name. For example,
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *ansible-doc dellemc.vxrail.dellemc_vxrail_cluster*

## Running Ansible Modules

The Ansible server must be configured with Python library for VxRail Ansible Utility to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-vxrail/tree/master/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.
