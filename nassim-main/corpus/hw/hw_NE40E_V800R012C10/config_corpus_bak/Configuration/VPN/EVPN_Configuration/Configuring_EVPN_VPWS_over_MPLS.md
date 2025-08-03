Configuring EVPN VPWS over MPLS
===============================

EVPN VPWS over MPLS allows you to establish P2P MPLS tunnels between PEs and implement the P2P L2VPN function.

#### Usage Scenario

EVPN VPWS provides a P2P L2VPN service solution based on the EVPN service architecture. Regarding this solution, a P2P MPLS tunnel is established between PEs and traverses the backbone network. By binding the AC interface on the user side to the P2P MPLS tunnel on the network side, traffic can be transmitted between the AC interface and the P2P MPLS tunnel. As a result, traffic that enters the AC interface is forwarded directly to the peer PE through the P2P MPLS tunnel. This solution provides a simple Layer 2 packet forwarding mode for the connection between AC interfaces at both ends, avoiding the need to search MAC address entries. This service solution is named Ethernet Line (E-Line).

As shown in [Figure 1](#EN-US_TASK_0172370462__fig_dc_vrp_evpn_cfg_110001), the basic EVPN VPWS architecture has the following components:

* AC: An AC is an independent physical or virtual circuit connecting a CE and a PE. An AC interface can be a physical interface or a logical interface. AC attributes include the encapsulation type, maximum transmission unit (MTU), and interface parameters of a specified link type.
* EVPN VPWS instance: An EVPN VPWS instance is deployed on an edge PE and contains services that have the same access-side or network-side attributes. Routes are transmitted based on the RD and RT configured in each EVPN VPWS instance in a BGP EVPN address family.
* EVPL instance: An EVPL instance corresponds to an AC. Each EVPL instance has a service ID. An EVPL instance on the local PE corresponds to an EVPL instance on the remote PE. PEs exchange EVPN routes carrying a service ID to construct forwarding entries that are used to forward or receive service traffic from different ESs, achieving P2P interworking.
* Tunnel: network-side MPLS tunnel.

**Figure 1** Configuring EVPN VPWS over MPLS  
![](images/fig_dc_vrp_evpn_cfg_110001.png)
#### Pre-configuration Tasks

Before configuring EVPN VPWS over MPLS, complete the following tasks:

Configure Layer 3 route reachability on the IPv4 network.



[Configuring EVPN Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0027.html)

EVPN VPWS is established based on the EVPN service architecture. Before configuring EVPN VPWS over MPLS, you need to configure EVPN functions.

[(Optional) Configuring the Global Redundancy Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0014-VPWS-NEW.html)

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

[Configuring an EVPL Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0021.html)

Before binding an AC interface on the user side to an MPLS tunnel interface on the network side, you must create an EVPL instance.

[Configuring an AC Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0022.html)

In MPLS E-Line scenarios, a Layer 2 sub-interface can function as an AC interface, and traffic encapsulation can be configured on the AC interface to transmit different types of data packets.

[Configuring an ESI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0263.html)

An ESI must be configured on a PE interface connecting to a CE. The PE interfaces connecting to the same CE must have the same ESI configured.

[Configuring an MPLS LDP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0023.html)

The EVPN E-Line model allows you to configure packets to traverse the backbone network through P2P MPLS LDP, TE, SR, or other tunnels.

[(Optional) Configuring a DF Election Mode for EVPN VPWS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0024.html)

In an EVPN VPWS over MPLS scenario where a CE is multi-homed to PEs in single-active mode and no E-Trunk is configured, DF election needs to be performed between the PEs to determine the active/standby status of the PEs.

[(Optional) Setting a Redundancy Mode and DF Priority per ESI Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0024-esi.html)

In a scenario where multiple CEs are dual-homed to PEs, if you want to use different transmission modes (load balancing and non-load balancing) to send unicast traffic to different CEs or if you want to specify DFs for traffic forwarding by setting priority values, you can set a redundancy mode and DF priority values based on ESIs.

[(Optional) Configuring FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0025.html)

In EVPN VPWS over MPLS multi-homing single-active scenarios, FRR needs to be configured to prevent traffic loss if the primary PE fails.

[(Optional) Configuring Flow Label-based Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0223.html)

After flow label-based load balancing is configured, EVPN VPWS services can select forwarding paths based on flow labels, improving forwarding efficiency.

[(Optional) Configuring Port-Level Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0225.html)

In an EVPN VPWS dual-homing single-active scenario, after port-level load balancing is configured, EVPN VPWS services can use LACP signaling to notify CEs of DF election results for port-level load balancing.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0026.html)

After configuring EVPN VPWS over MPLS, verify EVPL instance information.