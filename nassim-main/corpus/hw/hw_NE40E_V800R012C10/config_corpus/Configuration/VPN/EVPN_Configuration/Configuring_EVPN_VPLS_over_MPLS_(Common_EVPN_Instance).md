Configuring EVPN VPLS over MPLS (Common EVPN Instance)
======================================================

Configuring EVPN VPLS over MPLS (common EVPN instance) includes configuring EVPN instances, EVPN source addresses, bindings between EVPN instances and interfaces, ESIs, and BGP EVPN peer relationships.

#### Usage Scenario

EVPN is used for Layer 2 internetworking.

On the network shown in [Figure 1](#EN-US_CONCEPT_0172370428__fig_dc_vrp_evpn_cfg_000301), to allow Layer 2 networks at different sites to communicate, configure EVPN. Specifically:

* Configure an EVPN instance on each PE and bind the EVPN instance on each PE to the interface that connects the PE to a site.
* Configure EVPN source addresses to identify PEs in the EVPN networking.
* Configure ESIs for PE interfaces connecting to CEs. PE interfaces connecting to the same CE have the same ESI.
* Configure BGP EVPN peer relationships between PEs on the backbone network to allow MAC addresses within each site to be advertised over routes.
* Configure RRs to decrease the number of BGP EVPN peer relationships required.

**Figure 1** EVPN networking  
![](images/fig_dc_vrp_evpn_cfg_000301.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS over MPLS (common EVPN instance), complete the following tasks:

* Configure an IGP on the backbone network to ensure IP connectivity.
* Configure MPLS LDP or TE tunnels on the backbone network.
* Configure Layer 2 connections between CEs and PEs.


[Configuring an EVPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0004.html)

You can configure EVPN instances on PEs to manage EVPN routes.

[Configuring EVPN Source Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0012.html)

An EVPN source address uniquely identifies a PE in EVPN networking.

[Binding an Interface to an EVPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0005.html)

After an interface is bound to an EVPN instance, the interface becomes a part of the EVPN. Packets entering the interface will then be forwarded based on forwarding entries in the EVPN instance.

[Configuring an ESI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0013.html)

An ESI must be configured on a PE interface connecting to a CE. The PE interfaces connecting to the same CE must have the same ESI configured.

[Configuring BGP EVPN Peer Relationships](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0006.html)

After a BGP EVPN peer relationship is established between PEs, the PEs can exchange EVPN routes when MPLS or SR-MPLS tunnels are deployed on the backbone network.

[(Optional) Configuring the Global Redundancy Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0014.html)

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

[(Optional) Configuring a BGP EVPN RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0007.html)

Configuring a BGP EVPN RR helps reduce the number of required BGP EVPN peer relationships, and therefore saves network resources.

[(Optional) Setting a Redundancy Mode and DF Priority per ESI Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0110.html)

In a scenario where multiple CEs are dual-homed to PEs, if you want to use different transmission modes (load balancing and non-load balancing) to send unicast traffic to different CEs or if you want to specify DFs for traffic forwarding by setting priority values, you can set a redundancy mode and DF priority values based on ESIs.

[(Optional) Associating DFs with BFD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0076.html)

If a CE is dual-homed to PEs, you can associate the DF with BFD. If an access link fails, this configuration accelerates primary/backup DF switching.

[(Optional) Improving the Switching Performance of BUM Traffic When the Active Interface Board Fails](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_evpn_cfg_0005.html)

Enabling a device to deliver standby leaf node information to the standby interface board helps improve the switching performance of BUM traffic when the active interface board of the device fails.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0008.html)

After configuring EVPN functions, check the operating status of and information about these functions.