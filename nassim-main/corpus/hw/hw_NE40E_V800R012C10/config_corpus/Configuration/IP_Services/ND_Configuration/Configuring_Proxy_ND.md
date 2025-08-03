Configuring Proxy ND
====================

A device can function as the proxy of a target host in NS messages to respond to unreachable NS messages in special cases.

#### Usage Scenario

ND applies only to the communication of hosts on the same network segment and physical network. When a Router receives an NS packet from a host, the Router checks whether the destination IPv6 address in the NS packet is the local IPv6 address. This helps to determine whether the NS packet requests for the local MAC address. If yes, an NA packet is sent as a reply. If not, the NS packet is discarded.

For the hosts on the same network segment but different physical networks or the hosts that are on the same network segment and physical network but fail in Layer 2 interworking, proxy ND can be deployed on the Router between the hosts to allow such hosts to communicate with each other. After proxy ND is deployed and the Router receives an NS packet, the Router finds that the destination address in the NS packet is not its own IPv6 address and then replies the source host with an NA packet carrying its own MAC address and the IPv6 address of the destination host. Specifically, the Router takes the place of the destination host to reply with an NA packet.

[Table 1](#EN-US_TASK_0161511713__en-us_concept_0161511699_tab_dc_vrp_nd_feature_002901) describes the usage scenarios for different types of proxy ND.

**Table 1** Usage scenarios of proxy ND
| Proxy ND Mode | Usage Scenario |
| --- | --- |
| Routed proxy ND | Hosts that need to communicate reside on the same network segment but different physical networks, and the gateways connecting to the two hosts are configured with different IP addresses. |
| Any proxy ND | VMs that need to communicate reside on the same network segment but different physical networks, and the gateways connected to the VMs have the same IP address. |
| Intra-VLAN proxy ND | Hosts that need to communicate reside on the same network segment and belong to the same VLAN, but user isolation is configured in the VLAN. |
| Inter-VLAN proxy ND | Hosts that need to communicate reside on the same network segment but belong to different VLANs. |
| Local proxy ND | Hosts that need to communicate reside on the same network segment and BD, but user isolation is configured in the BD. |



![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Proxy ND cannot be enabled on an interface configured with a CGA address. Otherwise, the NA messages â carrying the CGA/RSA option â returned by the proxy device may be directly discarded.
* You can configure multiple types of proxy ND in the interface view. The configuration takes effect in descending order of priority: proxy ND anyway > intra-VLAN proxy ND/inter-VLAN proxy ND/local proxy ND > routed proxy ND.
* Proxy ND is not supported for the following types of messages:
  + NS messages with a link-local address as the target address
  + DAD NS messages with the source address of all 0s
  + NS messages with a local address as the target address.


#### Pre-configuration Tasks

Before configuring proxy ND, complete the following tasks:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.
* Configure the link layer protocol parameters for interfaces.
* Enable IPv6 in the interface view.
* Configure IPv6 addresses for interfaces.


[Configuring Routed Proxy ND](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0004.html)

Routed proxy ND can be deployed if hosts are on the same network segment but different physical networks and the gateways connected to the hosts have different addresses.

[Configuring Proxy ND Anyway](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0005.html)

Proxy ND anyway can be deployed if VMs are on the same network segment but different physical networks and the gateways connected to the VMs have the same address.

[Configuring Intra-VLAN Proxy ND](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0006.html)

Intra-VLAN proxy ND can be deployed if hosts are on the same VLAN but the VLAN is configured with Layer 2 port isolation.

[Configuring Inter-VLAN Proxy ND](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0007.html)

Inter-VLAN proxy ND can be deployed if hosts that are on the same network segment and physical network but belong to different VLANs need to communicate with each other at Layer 3.

[Configuring Local Proxy ND](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nd_cfg_0008.html)

Local proxy ND can be deployed if hosts on the same network segment and in the same BD want to communicate with each other but the BD is configured with split horizon.