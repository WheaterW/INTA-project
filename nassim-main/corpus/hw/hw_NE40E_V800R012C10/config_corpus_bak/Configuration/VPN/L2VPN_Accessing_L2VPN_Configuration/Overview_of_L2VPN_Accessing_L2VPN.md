Overview of L2VPN Accessing L2VPN
=================================

Overview_of_L2VPN_Accessing_L2VPN

#### Description

Multiprotocol Label Switching (MPLS) is widely applied in Metropolitan Area Networks (MANs) because it features high reliability, high security, and sound IP-based operation and maintenance capabilities, and supports quality of service (QoS). A Layer 2 virtual private network (L2VPN) provides MPLS-based L2VPN services to transparently transmit Layer 2 user data over tunnels on an MPLS network. This reduces the number of label switched paths (LSPs) maintained by transit nodes.

**Figure 1** Networking of traditional L2VPN accessing L2VPN  
![](figure/en-us_image_0000001199479289.png)

In a traditional networking environment, a provider edge aggregation (PE-AGG) and a network provider edge (NPE) are generally used to connect the access network to the bearer network, implementing L2VPN accessing L2VPN.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001153300972__en-us_concept_0000001153036304_fig_dc_vrp_l2-l3_feature_500101), the user provider edge (UPE) provides access services for user sites by creating an L2VPN between the access network and PE-AGG. The PE-AGG terminates the L2VPN and connects to the NPE. An L2VPN is set up between the NPE and other common PEs on the bearer network of the carrier. The NPE connects to the PE-AGG as a CE of the L2VPN. For the L2VPN on the bearer network, CE1 accesses the L2VPN through the private line emulated by another L2VPN.

**Figure 2** Networking of L2VPN accessing L2VPN supported by the NE40E  
![](figure/en-us_image_0000001199195813.png)

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001153300972__en-us_concept_0000001153036304_fig_dc_vrp_l2-l3_feature_500102), if an NPE can implement the functions of a PE-AGG and an NPE, it helps lower the networking cost and simplify the networking. The NPE terminates an L2VPN and accesses another L2VPN over a virtual Ethernet (VE) group. The NPE provides the functions of the PE-AGG and NPE in the traditional networking.

In a VE group, the VE interface used to terminate L2VPN is called a Layer 2 Virtual Ethernet (L2VE) interface, and that used to terminate L2VPN is called a Layer 3 Virtual Ethernet (L3VE) interface.

An NPE can be divided into multiple VSs. To implement L2VPN + L2VPN interworking between different VSs, you can allocate L2VE and L3VE interfaces in the same VE group to different VSs.