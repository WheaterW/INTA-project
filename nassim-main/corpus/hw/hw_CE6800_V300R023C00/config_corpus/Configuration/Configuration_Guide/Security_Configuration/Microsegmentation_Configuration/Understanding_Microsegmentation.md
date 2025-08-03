Understanding Microsegmentation
===============================

Understanding Microsegmentation

#### Basic Concepts of Microsegmentation

Microsegmentation is a security isolation technology that groups data center (DC) services based on certain rules and deploys policies between groups to implement traffic control.

* Microsegmentation enables more fine-grained segmentation, for example, segmentation based on IP addresses, IP network segments, MAC addresses, and VM names.
* It divides a network into several segments based on grouping rules and applies policies to control traffic between these segments. In this way, data packets can only be transmitted between specific nodes.

Microsegmentation groups DC services based on certain rules and implements traffic control through inter-group policies. It implements fine-grained isolation between groups based on the following elements:

* **End Point Group (EPG)**
  
  Servers are allocated to EPGs based on rules.
  
  After servers are allocated to EPGs, the servers that do not belong to any EPG are unknown EPG members and the servers that belong to EPGs are EPG members. Multiple servers can belong to the same EPG. An EPG can contain multiple servers.
* **Group-Based Policy (GBP)**
  
  GBP defines traffic control for members in an EPG or in different EPGs.
  
  You can change the default GBP as needed and specify GBPs for EPGs. The default GBP is as follows:
  + The default access control policy for unknown EPG members is **permit**; that is, unknown EPG members can communicate with each other.
  + The default access control policy for EPG members is **deny**; that is, members cannot communicate with each other regardless of their EPGs.
  + The default access control policy for members in an EPG is **none**; that is, access control is not performed for members in an EPG. In this case, the device performs access control for members in the EPG according to the default access control policy.
    
    When the default access control policy for members in an EPG is not **none**, the configured default access control policy is used for the members.


#### How Does Microsegmentation Work?

Microsegmentation allocates servers to EPGs and defines GBPs between EPGs to implement traffic control between servers.

In [Figure 1](#EN-US_CONCEPT_0000001512675382__fig2436162216131), four servers are deployed on the VXLAN network. The user requirements are as follows: Server1 and Server3 can communicate. Server2 and Server4 can communicate. Server1 and Server3 cannot communicate with Server2 or Server4.**Figure 1** Networking of microsegmentation  
![](figure/en-us_image_0000001513034554.png)

Through microsegmentation, Server1 and Server3 on Leaf1 and Leaf2 are added to EPG1, Server2 and Server4 are added to EPG2, and intra-EPG access and inter-EPG isolation are implemented.


#### Microsegmentation Information in the VXLAN Packet Header

In [Figure 2](#EN-US_CONCEPT_0000001512675382__fig_dc_cfg_micro-segmentation_000303), the source VXLAN Tunnel Endpoint (VTEP) sends microsegmentation information to the destination VTEP using the **G flag bit** and **Group Policy ID** field in the VXLAN packet header.**Figure 2** Microsegmentation information in the VXLAN packet header  
![](figure/en-us_image_0000001563874513.png)

* G flag bit: The default value is 0. When the value is 1, the Group Policy ID field in the VXLAN packet header carries the ID of an EPG that the source server belongs to.
* Group Policy ID field: When the value of the G flag bit is 1, the Group Policy ID field in the VXLAN packet header carries the ID of an EPG that the source server belongs to.