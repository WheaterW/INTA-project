Configuring EVPN VPLS over MPLS (BD EVPN Instance)
==================================================

Configuring BD EVPN involves configuring a BD EVPN instance, creating a BD and binding an EVPN instance to the BD, configuring an L3VPN instance and binding a VBDIF interface to it, and configuring BGP EVPN peer relationships.

#### Usage Scenario

This section describes how to configure BD EVPN functions. A non-BD EVPN can only carry Layer 2 services, whereas a BD EVPN can carry both Layer 2 and Layer 3 services.


#### Pre-configuration Tasks

Before configuring EVPN VPLS over MPLS (BD EVPN instance), complete the following tasks:

* Configure an IGP on the backbone network to ensure IP connectivity.
* Configure MPLS LDP or TE tunnels on the backbone network.
* Configure Layer 2 connections between CEs and PEs.
* (Optional) In a CE dual-homing scenario where Layer 3 traffic is transmitted, configure the [function of sending ARP messages at a constant rate](dc_vrp_arp_cfg_2083.html) to limit the rate at which ARP broadcasts request packets. It is recommended that an ARP request packet be broadcast every 10 ms. This ensures a rapid traffic switchover after a CE fault occurs.


[Configuring an EVPN Instance in BD Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0061.html)

To implement service access based on a BD and manage EVPN routes, configure BD EVPN instances on PEs.

[Configuring EVPN Source Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0012bd.html)

An EVPN source address uniquely identifies a PE in EVPN networking.

[Configuring an ESI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0064.html)

An ESI must be configured for a PE interface connecting to a CE or the BD to which such an interface is bound. The PE interfaces connecting to the same CE or the BDs to which such interfaces are bound must have the same ESI configured.

[Configuring a BD and Binding an EVPN Instance to the BD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0062.html)

An EVPN instance in BD mode is only bound to a BD instead of an interface.

[Configuring BGP EVPN Peer Relationships](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0006bd.html)

After a BGP EVPN peer relationship is established between PEs, the PEs can exchange EVPN routes when MPLS or SR-MPLS tunnels are deployed on the backbone network.

[(Optional) Creating an L3VPN Instance and Binding It to a VBDIF Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0063.html)

To enable an EVPN to transmit Layer 3 services, configure an L3VPN instance and bind it to a VBDIF interface. 

[(Optional) Configuring the Global Redundancy Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0014bd-NEW.html)

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

[(Optional) Setting a Redundancy Mode and DF Priority per ESI Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0110bd.html)

In a scenario where multiple CEs are dual-homed to PEs, if you want to use different transmission modes (load balancing and non-load balancing) to send unicast traffic to different CEs or if you want to specify DFs for traffic forwarding by setting priority values, you can set a redundancy mode and DF priority values based on ESIs.

[(Optional) Configuring a BGP EVPN RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0007bd.html)

Configuring a BGP EVPN RR helps reduce the number of required BGP EVPN peer relationships, and therefore saves network resources.

[(Optional) Configuring Proxy ARP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2096.html)

When users communicate with each other for the first time, they send ARP request packets, which are broadcast on the Layer 2 network. To reduce the number of broadcast ARP packets, configure proxy ARP.

[(Optional) Configuring Flow Label-based Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0018bd.html)

After flow label-based load balancing is configured, EVPN VPLS services can select forwarding paths based on flow labels, improving forwarding efficiency.

[(Optional) Configuring Port-Level Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0019bd.html)

In an EVPN VPLS dual-homing single-active scenario, after port-level load balancing is configured, EVPN VPLS services can use LACP signaling to notify CEs of DF election results for port-level load balancing.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0008bd.html)

After configuring EVPN functions, check the operating status of and information about these functions.