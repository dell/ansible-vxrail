# Ansible Modules for Dell EMC VxRail

The Ansible Modules for Dell EMC VxRail allow data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC VxRail.

The capabilities of Ansible modules are gathering system information and performing Lay2 Node Expansion. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## Support
Ansible modules for VxRail are supported by Dell EMC and are provided under the terms of the license attached to the source code. Dell EMC does not provide support for any source code modifications. For any Ansible module issues, questions or feedback, join the [Dell EMC Automation community]( https://www.dell.com/community/Automation/bd-p/Automation ).

## Supported Platforms
  * Dell EMC VxRail

## Prerequisites
This table provides information about the software prerequisites for the Ansible Modules for Dell EMC VxRail.

| **Ansible Modules** | **VxRail version** | **Python version** | **Python library (VxRail Ansible Utility) version** | **Ansible Version** |
|---------------------|----------------|--------------------|----------------------------|-------------|
| v1.0.0 | 7.0.240 | <br> 3.6.x <br> 3.7.x | 1.0.0| 2.9 and 2.10 | 

  * Please follow VxRail Ansible Utility installation instructions on [VxRail Ansible Utility Documentation](https://github.com/dell/ansible-vxrail-utility)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC VxRail
  * Cluster module
  * System module

## Installation of SDK
Install the python [sdk](https://github.com/dell/ansible-vxrail-utility) named 'VxRail Ansible Utility'. It can be installed using pip, based on the appropriate python version.

## Installing Collections

  * Download the tar build and run the following command to install the collection anywhere in your system:
        
        ansible-galaxy collection install dellemc-vxrail-1.0.0.tar.gz -p <install_path>
  
  * Set the environment variable:
        
        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections

  * In order to use any Ansible module, ensure that the importation of the proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. For example,
 <br>collections:
 <br>&nbsp;&nbsp;&nbsp; - dellemc.vxrail
  * To generate Ansible documentation for a specific module, embed the FQCN before the module name. For example,
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *ansible-doc dellemc.vxrail.dellemc_vxrail_cluster*

## Running Ansible Modules

The Ansible server must be configured with Python library for VxRail Ansible Utility to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-vxrail/tree/1.0.0/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## Results
Each module returns the updated state and details of the entity, for example, if you are using the Volume module, all calls will return the updated details of the volume. A sample result is shown in each module's documentation.
