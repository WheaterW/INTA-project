Configuring PIM-SM Inter-domain Multicast
=========================================

When a multicast network is divided into multiple PIM-SM domains, MSDP is required to connect Rendezvous Points (RPs) in different domains and enable RPs to share multicast source information. As a result, hosts in the local PIM-SM domain can receive multicast data sent by multicast sources in other domains.

#### Usage Scenario

On a multicast network that has multiple PIM-SM domains, to enable hosts in a local PIM-SM domain to receive multicast data from multicast sources in other domains, configure MSDP to connect RPs in different domains and enable RPs to share multicast source information.

To prevent Source Active (SA) messages from being blocked by Reverse Path Forwarding (RPF) rules and to reduce redundant traffic, performing the following operations is recommended:

* Add all MSDP peers in the same autonomous system (AS) to the same mesh group.
* Perform one of the following operations on the inter-AS MSDP peers:
  
  + Configure BGP to advertise routes, specify MSDP peers as routes' next hops, and configure advertised BGP routes to be preferentially selected by multicast devices.
  + Specify the RPs as static RPF peers of each other.
  + Add all inter-AS MSDP peers to the same mesh group. (This operation is recommended.)

#### Pre-configuration Tasks

Before configuring PIM-SM inter-domain multicast, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Enable multicast routing on all Routers and PIM-SM on all Router interfaces.
* Divide the network into multiple PIM-SM domains and configure RPs.


[Configuring Intra-AS MSDP Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0046.html)

If multiple PIM-SM domains exist in an AS or multiple Rendezvous Points (RPs) serving different multicast groups exist in a PIM-SM domain, configure MSDP peer relationships between RPs (including static RPs and Candidate-Rendezvous Points (C-RPs)) and add all MSDP peers to the same mesh group.

[Configuring Inter-AS MSDP Peers for BGP Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0047.html)

To enable PIM-SM domains in different ASs to share multicast source information, configure an MSDP peer relationship between Rendezvous Points (RPs) in different ASs in which a BGP peer relationship is set up.

[Configuring Inter-AS Static RPF Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0048.html)

To enable PIM-SM domains in different ASs to share multicast source information, configure a static Reverse Path Forwarding (RPF) peer relationship between Rendezvous Points (RPs) in different ASs.

[Adding Inter-AS MSDP Peers to the Same Mesh Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2266.html)

To prevent SA messages exchanged between inter-AS MSDP peers from being discarded due to RPF check failures, add inter-AS MSDP peers to the same mesh group after they are configured.

[Verifying the Configuration of PIM-SM Inter-domain Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0049.html)

After configuring PIM-SM inter-domain multicast, verify information about MSDP peers.