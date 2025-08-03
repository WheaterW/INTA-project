Configuring an MCE
==================

Multi-VPN-instance can be configured for routing protocols on a CE to isolate different types of services on a LAN.

#### Usage Scenario

VPN services are becoming increasingly refined and the demand for VPN service security is growing. Carriers must isolate different types of VPN services on networks to meet this demand. The traditional BGP/MPLS VPN technology isolates VPN services by deploying one CE for each VPN, which is expensive and complicates network deployment. If multiple VPNs use the same CE to access upper-layer devices, these VPNs share the same routing and forwarding table, and data security for these VPNs cannot be ensured. The MCE technology addresses the conflict between network costs and data security problems caused by multiple VPNs sharing the same CE.

On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_0069.html#EN-US_TASK_0172369390__fig_dc_vrp_mpls-l3vpn-v4_cfg_006901), the R&D and sales departments of Company X share the same LAN in City A. The two departments use the same CE to access the VPN backbone network. You can configure OSPF multi-VPN-instance on the CE in City A and the PE to which the CE is connected to achieve the following objectives:

* The sales departments in cities A and B can communicate with each other.
* The R&D departments in cities A and C can communicate with each other.
* The R&D departments are isolated from the sales departments.

Similar to OSPF multi-vpn-instance on a PE, each OSPF instance on the CE in City A serves as a virtual CE for each type of service. This CE is called an MCE. The MCE can isolate different types of services at low costs, ensuring service security.
**Figure 1** MCE networking  
![](figure/en-us_image_0278570307.png)
#### Pre-configuration Tasks

Before configuring an MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and the PE to which the MCE is connected (for details, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0155.html))
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interfaces connecting to the MCE to VPN instances (for details, see [Binding Interfaces to a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html)), and configure IP addresses for these interfaces.


[Configuring a Routing Protocol on an MCE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0070.html)

To enable an MCE to communicate with PEs and VPNs, configure a routing protocol for each type of service on the MCE.

[Configuring a Routing Protocol on the PE Connected to an MCE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0071.html)

To enable a PE to communicate with an MCE, configure routing protocol multi-instance on the PE.

[Verifying the MCE Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0072.html)

After configuring the MCE, check the routes to the LAN and remote sites for each type of service in the VRF table of the MCE.