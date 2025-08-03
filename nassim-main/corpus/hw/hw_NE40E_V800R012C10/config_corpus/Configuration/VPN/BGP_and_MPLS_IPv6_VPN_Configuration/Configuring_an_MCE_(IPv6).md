Configuring an MCE (IPv6)
=========================

Multi-VPN-instance can be configured for routing protocols on a customer edge (CE) to isolate different types of services on a local area network (LAN).

#### Usage Scenario

Virtual private network (VPN) services are becoming increasingly refined and the demand for VPN service security is growing. Operators must isolate different types of VPN services on networks to meet this demand. The traditional Border Gateway Protocol (BGP)/Multiprotocol Label Switching (MPLS) VPN IPv6 technology isolates VPN services by deploying one CE for each VPN, which is expensive and complicates network deployment. If multiple VPNs use the same CE to access upper-layer devices, these VPNs share the same routing and forwarding table, and data security for these VPNs cannot be ensured. The multi-VPN-instance CE (MCE) technology addresses the conflict between network costs and data security problems caused by multiple VPNs sharing the same CE.

On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v6_cfg_2070.html#EN-US_TASK_0172369663__fig_dc_vrp_mpls-l3vpn-v6_cfg_207001), the R&D and sales departments of company X share the same LAN in city A. Moreover, the two departments use the same CE to access the VPN backbone network. OSPF multi-instance can be configured on the CE in city A and the PE to which the CE is connected to achieve the following objectives:

* The sales departments in cities A and B can communicate with each other.
* The R&D departments in cities A and C can communicate with each other.
* The R&D departments are isolated from the sales departments.

Similar to OSPF multi-instance on a PE, each OSPF instance on the CE in city A serves as a virtual CE for each type of service. Such a CE is called an MCE. These MCEs can isolate different types of services at low costs, ensuring service security.

**Figure 1** MCE networking  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_207001.png)

#### Pre-configuration Tasks

Before configuring an MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and the PE to which the MCE is connected (for details, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html)).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interfaces connected to the MCE to VPN instances (for details, see [Binding Interfaces to a VPN Instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html)), and configure IPv6 addresses for these interfaces.


[Configuring a Routing Protocol on an MCE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2071.html)

To enable a multi-VPN-instance customer edge (MCE) to communicate with provider edge (PE) and virtual private network (VPN) devices, configure a routing protocol for each type of service on the MCE.

[Configuring a Routing Protocol on the PE Connected to the MCE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2072.html)

To enable a provider edge (PE) to communicate with a multi-VPN-instance customer edge (MCE), configure routing protocol multi-VPN-instance on the MCE.

[Verifying the MCE (IPv6) Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2073.html)

After the multi-VPN-instance CE (MCE) is configured, the VPN routing and forwarding (VRF) table of the MCE contains the routes to the local area network (LAN) and remote sites for each type of service.