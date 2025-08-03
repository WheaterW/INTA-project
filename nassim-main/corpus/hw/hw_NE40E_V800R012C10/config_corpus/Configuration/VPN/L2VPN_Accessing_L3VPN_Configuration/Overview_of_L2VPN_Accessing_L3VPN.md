Overview of L2VPN Accessing L3VPN
=================================

Overview of L2VPN Accessing L3VPN

#### Definition

Multiprotocol Label Switching (MPLS) is widely applied in Metropolitan Area Networks (MANs) because it features high reliability, high security, and sound IP-based operation and maintenance capabilities, and supports quality of service (QoS). A Layer 2 virtual private network (L2VPN) provides MPLS-based L2VPN services to transparently transmits Layer 2 user data over tunnels on an MPLS network. This reduces the number of label switched paths (LSPs) maintained by transit nodes.

**Figure 1** Traditional L2VPN accessing L3VPN  
![](images/fig_feature_image_0003994359.png)  

On a traditional network, a provider edge aggregation (PE-AGG) and a network provider edge (NPE) are required to connect the access network to the bearer network. Then, the L2VPN can access the public network or Layer 3 virtual private network (L3VPN).

On the network shown in [Figure 1](#EN-US_CONCEPT_0172370309__en-us_concept_0172356411_fig_dc_vrp_l2-l3_feature_500101), the user provider edges (UPEs) are responsible for providing access services for user sites by creating an L2VPN tunnel between the access network and PE-AGG. The PE-AGG terminates the L2VPN and connects to the NPE. An L3VPN is set up between the NPE and other common PEs on the bearer network of the carrier. As a CE of the L2VPN, the NPE connects to the PE-AGG. For the L3VPN on the bearer network, CE1 accesses the L3VPN over the leased line emulated by the L2VPN.

**Figure 2** L2VPN accessing L3VPN supported by the NE40E  
![](images/fig_feature_image_0003992754.png)  

If an NPE can provide the functions of a PE-AGG and an NPE, it helps lower the networking costs and simplify the networking. As shown in [Figure 2](#EN-US_CONCEPT_0172370309__en-us_concept_0172356411_fig_dc_vrp_l2-l3_feature_500102), the NPE terminates an L2VPN and accesses an L3VPN over a virtual Ethernet (VE) group. The NPE provides the functions of the PE-AGG and NPE in the traditional networking.

In a VE group, the VE interface used to terminate an L2VPN is called a Layer 2 Virtual Ethernet (L2VE) interface, and the VE interface used to access an L3VPN is called a Layer 3 Virtual Ethernet (L3VE) interface.

An NPE supports the division of multiple VSs. To implement L2VPN and L3VPN service interworking between different VSs, you can allocate the L2VE and L3VE interfaces in the same VE group to different VSs.