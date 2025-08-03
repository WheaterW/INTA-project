Migrating an HVPLS Network to a PBB-EVPN
========================================

During migration from a large-scale hierarchical virtual
private LAN service (HVPLS) network to a provider backbone bridge
Ethernet VPN (PBB-EVPN), HVPLS and PBB-EVPN will coexist for some
time.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172370739__fig_dc_vrp_pbb-evpn_cfg_001301), HVPLS is deployed to reduce the number of required pseudo wires
(PWs) and improve bandwidth usage.

As this network has large
numbers of devices, migration must be performed step by step after
devices have PBB-EVPN enabled, and HVPLS and PBB-EVPN will temporarily
coexist in this process.

**Figure 1** Migrating an HVPLS network to a PBB-EVPN
  
![](images/fig_dc_vrp_pbb-evpn_cfg_001301.png)  



#### Pre-configuration Tasks

Before migrating an HVPLS network to a PBB-EVPN, complete
the following tasks:

* Configure an Interior Gateway Protocol (IGP) on the backbone
  network to ensure IP connectivity.
* Configure Multiprotocol Label Switching (MPLS) Label Distribution
  Protocol (LDP) tunnels on the backbone network.
* (Optional) Configure primary and backup MPLS traffic engineering
  (TE) tunnels and a tunnel policy for tunnel selection if you want
  to use MPLS TE tunnels.


[Configuring a B-EVPN Instance on an SPE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0014.html)

A backbone Ethernet VPN (B-EVPN) instance is essential for a superstratum provider edge (SPE) in connecting to hierarchical virtual private LAN service (HVPLS) and provider backbone bridge Ethernet VPN (PBB-EVPN) networks.

[Configuring an I-VSI on an SPE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0015.html)

This section describes how to change a common virtual switching instance (VSI) on a superstratum provider edge (SPE) to be a multipoint-to-multipoint (MP2MP) I-VSI and bind the I-VSI to a backbone Ethernet VPN (B-EVPN) instance.

[Configuring PBB-EVPN on UPEs on One Side](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0016.html)

Configuring provider backbone bridge Ethernet VPN (PBB-EVPN) on user-end provider edges (UPEs) is the prerequisite for migrating a hierarchical virtual private LAN service (HVPLS) network to a PBB-EVPN.

[Configuring BGP EVPN Peer Relationships Between the SPE and UPEs on One Side](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0017.html)

After a superstratum provider edge (SPE) and a user-end provider edge (UPE) establishes a Border Gateway Protocol (BGP) Ethernet VPN (EVPN) peer relationship, they can exchange EVPN routes.

[Configuring PBB-EVPN on UPEs on the Other Side](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0018.html)

Configuring provider backbone bridge Ethernet VPN (PBB-EVPN) on user-end provider edges (UPEs) is the prerequisite for migrating a hierarchical virtual private LAN service (HVPLS) network to a PBB-EVPN.

[Configuring BGP EVPN Peer Relationships Between the SPE and UPEs on the Other Side](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0019.html)

After a superstratum provider edge (SPE) and a user-end provider edge (UPE) establishes a Border Gateway Protocol (BGP) Ethernet VPN (EVPN) peer relationship, they can exchange EVPN routes.

[Configuring an SPE as an RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0020.html)

Configuring a provider backbone bridge Ethernet VPN (PBB-EVPN) route reflector (RR) helps reduce the number of required BGP EVPN peer relationships, and therefore conserves network resources.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pbb-evpn_cfg_0021.html)

After an HVPLS network evolves to PBB-EVPN, check the operating status of and information about PBB-EVPN functions.