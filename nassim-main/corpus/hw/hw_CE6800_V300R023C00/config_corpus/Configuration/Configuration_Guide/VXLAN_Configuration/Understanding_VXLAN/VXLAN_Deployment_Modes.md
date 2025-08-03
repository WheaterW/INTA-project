VXLAN Deployment Modes
======================

Currently, two VXLAN deployment modes are available: **single-node mode** and **controller mode**.

* **Single-node mode**: This traditional network deployment mode requires you to log in to each device in order to perform configurations as planned. If cloud computing data centers are deployed, this mode cannot implement collaboration with cloud platforms for automatic network deployment.
* **Controller mode**: A controller is introduced to facilitate control and deployment on large Layer 2 networks. A controller is a unified network control platform that orchestrates and manages network resources and works with the cloud platform to implement automated service and network provisioning.

#### Controller Mode

* Introduction to the controller mode
  
  In controller mode, iMaster NCE-Fabric dynamically establishes VXLAN tunnels. In this situation, iMaster NCE-Fabric uses NETCONF to control VXLAN tunnel setup between devices.
  
  As shown in [Figure 1](#EN-US_CONCEPT_0000001176743961__fig_03), iMaster NCE-Fabric can directly manage users' virtual networks and obtain related information through Neutron. The controller dynamically computes network configurations based on virtual network information, automatically delivers the configurations to the physical network, and deploys services on the virtual network.
  
  **Figure 1** Controller + VXLAN solution networking  
  ![](figure/en-us_image_0000001176744051.png)
  [Table 1](#EN-US_CONCEPT_0000001176743961__tab_3) describes the layers in the controller + VXLAN solution.
  
  **Table 1** Layers in the controller + VXLAN solution
  | Layer | Description |
  | --- | --- |
  | Cloud platform | Schedules network, compute, and storage resources based on demands, and provides service management and O&M interfaces. Neutron is a component of the cloud platform and is used to provide network services. |
  | Network controller | Implements network modeling and completes network configuration.  iMaster NCE-Fabric uses RESTful interfaces to receive network modeling configurations from the cloud platform and convert them into related commands, and uses NETCONF to establish channels with network devices at the infrastructure layer and deliver commands to these devices. |
  | Infrastructure network | Allows virtual network construction over a physical network. + This layer supports hardware VXLAN gateway deployment mode to improve service performance. + This layer enables compatibility with traditional VLANs. |
* Channel establishment and maintenance between the controller and network devices
  
  The controller can detect the tenant status in real time and obtain the virtual network information from the cloud platform. As shown in [Figure 2](#EN-US_CONCEPT_0000001176743961__fig_04), after tenants go online, the controller obtains virtual network information from the cloud platform, and dynamically computes network configurations based on this information. The controller then automatically delivers the configurations to the physical network and deploys services on the virtual network.
  
  **Figure 2** Channel establishment and maintenance between the controller and network devices  
  ![](figure/en-us_image_0000001176664137.png)
  
  Administrators are required to complete the NETCONF and mandatory VXLAN configurations (for example, creating NVE interfaces and configuring VTEP IP addresses, as shown in [Figure 2](#EN-US_CONCEPT_0000001176743961__fig_04)) on the devices using CLI or Zero Touch Provisioning (ZTP). After these configurations are complete, iMaster NCE-Fabric can automatically manage the devices using NETCONF.

![](../public_sys-resources/note_3.0-en-us.png) 

VXLAN can be configured using CLI or iMaster NCE-Fabric. This document describes only CLI-based configuration. For details about iMaster NCE-Fabric-based configuration, see the related deployment guide for the CloudFabric solution.