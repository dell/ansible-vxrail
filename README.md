# Ansible Modules for Dell EMC VxRail

The Ansible Modules for Dell EMC VxRail allow data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC VxRail.

The Ansible Modules for Dell EMC VxRail are used for gathering system information and performing cluster level operations. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## Support
Ansible modules for VxRail are supported by Dell EMC open source community, but not product support agreements, and are provided under the terms of the license attached to the source code. Dell EMC does not provide support for any source code modifications. For any Ansible module issues, questions or feedback, join the [Dell EMC Automation community]( https://www.dell.com/community/Automation/bd-p/Automation ).

## Supported Platforms
  * Dell EMC VxRail

## Prerequisites
This table provides information about the software prerequisites for the Ansible Modules for Dell EMC VxRail.

| **Ansible Modules** | **VxRail version** | **Python version** | **Python library (VxRail Ansible Utility) version** | **Ansible Version** |
|---------------------|----------------|--------------------|----------------------------|-------------|
| v1.3.0 | 7.0.240 | 3.7.x | 1.3.0 | 2.9 and 2.10 |

  * Please follow VxRail Ansible Utility installation instructions on [VxRail Ansible Utility Documentation](https://github.com/dell/ansible-vxrail-utility)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC VxRail
  * Cluster expansion module
  * System module
  * Day1 Initialization module
  * Cluster information module
  * Hosts module
  * Callhome module
  * iDRAC Network Settings module
  * Chassis module
  * Remove Host module
  * System Virtual Machines module
  * Telemetry Tier Info module
  * iDRAC Users module
  * LCM module
  * Support Account module
  * Satellite Node Expansion module
  * Satellite Node Remove module
  * System Cluster Hosts module
  * Cluster Portgroups module
  * Cluster Layer3 Get Segments module
  * Cluster Layer3 Get Segment Health module
  * VC Mode Information module
  * Telemetry Tier Change module
  * Internet Mode Info module
  * Internet Mode Change module
  * Cluster Layer3 Specific Segment module
  * System Available Hosts module
  * System DNS Information module
  * System DNS Change Module
  * LCM Precheck module
  * Cluster Layer3 New Segment module

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
