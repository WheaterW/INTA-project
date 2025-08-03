Configuring PBB-EVPN
====================

This section describes how to configure provider backbone
bridge Ethernet VPN (PBB-EVPN).

#### Usage Scenario

PBB-EVPN, which is used for Layer 2 internetworking, involves
the following configurations:

* Configure EVPN instances on each PE.
* Configure B-MAC addresses for EVPN instances.
* Bind an AC interface to each I-EVPN instance.
* Configure PBB-EVPN source addresses to identify PEs in EVPN
  networking.
* Configure an Ethernet segment identifier (ESI) for each PE
  interface connecting to a CE. PE interfaces connecting to the same
  CE have the same ESI.
* Configure EVPN Border Gateway Protocol (BGP) peer relationships
  between PEs on the backbone network to allow MAC addresses to be advertised
  over routes.
* Configure a route reflector (RR) to decrease the number of
  BGP EVPN peer relationships required.

**Figure 1** PBB-EVPN networking
![](images/fig_dc_vrp_pbb-evpn_cfg_000101.png)










To improve PBB-EVPN reliability, perform the following operations:

* [Configure BFD for BGP.](dc_vrp_bgp_cfg_4056.html)
* [Configure LDP Auto
  FRR](dc_vrp_ldp-p2p_cfg_0049.html) if LDP tunnels are used.
* [Configure MPLS TE FRR](dc_vrp_te-p2p_cfg_0048.html) or [MPLS TE Auto FRR](dc_vrp_te-p2p_cfg_0053.html) if TE tunnels are used.


#### Pre-configuration Tasks

Before configuring PBB-EVPN, complete the following
tasks:

* Configure an IGP on the backbone network to ensure IP connectivity.
* Configure MPLS LDP tunnels on the backbone network.
* (Optional) Configure primary and backup MPLS TE tunnels and
  a tunnel policy for tunnel selection if you want to use MPLS TE tunnels.
* Configure Layer 2 connections between CEs and PEs.


[Configuring a PBB-EVPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0002.html)

PEs use provider backbone bridge Ethernet VPN (PBB-EVPN) instances to interconnect private networks with the public network.

[Binding an Interface to an I-EVPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0005.html)

After an interface is bound to an I-EVPN instance, the interface becomes a part of the provider backbone bridge (PBB-EVPN). Packets entering the interface will then be forwarded based on PBB-EVPN instance traffic forwarding entries.

[Configuring PBB-EVPN B-MAC Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0003.html)

Provider backbone bridge (PBB) precedes customer MAC (C-MAC) addresses with backbone MAC (B-MAC) addresses in packets to completely separate the user network from the carrier network.

[Configuring a PBB-EVPN Source Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0004.html)

A provider backbone bridge Ethernet VPN (PBB-EVPN) source address uniquely identifies a provider edge (PE) in PBB-EVPN networking.

[Configuring an ESI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0006.html)

An ESI must be configured on a PE interface connecting to a CE. The PE interfaces connecting to the same CE must have the same ESI configured.

[Configuring a BGP EVPN Peer Relationship](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0007.html)

After two provider edges (PEs) establish a Border Gateway Protocol (BGP) Ethernet VPN (EVPN) peer relationship, they can exchange EVPN routes.

[(Optional) Configuring a PBB-EVPN RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0008.html)

Configuring a provider backbone bridge Ethernet VPN (PBB-EVPN) route reflector (RR) helps reduce the number of required BGP EVPN peer relationships, and therefore conserves network resources.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0010.html)

After configuring PBB-EVPN, check the operating status of and information about PBB-EVPN functions.