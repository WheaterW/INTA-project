Overview of VRRP
================

The Virtual Router Redundancy Protocol (VRRP) is a fault-tolerant protocol running on routers. VRRP implements egress gateway backup and ensures communication continuity and reliability.

#### Definition

The Virtual Router Redundancy Protocol (VRRP) is a standard-defined fault-tolerant protocol that groups several physical routing devices into a virtual one. If a physical routing device (master) that serves as the next hop of hosts fails, the virtual device switches traffic to a different physical routing device (backup), thereby ensuring service continuity and reliability.

VRRP allows logical and physical devices to work separately and implements route selection among multiple egress gateways.

On the network shown in [Figure 1](#EN-US_CONCEPT_0172361732__en-us_concept_0172351596_fig_dc_vrp_vrrp_cfg_010202), a VRRP group is configured on two Routers, one of which serves as the master, and the other as the backup. The two devices form a virtual Router that is assigned a virtual IP address and a virtual MAC address. Hosts are only aware of this virtual Router, as opposed to the master and backup Routers, and they use it to communicate with devices on different network segments.

A virtual Router consists of a master Router and one or more backup Routers. Only the master Router forwards packets. If the master Router fails, a backup Router is elected as the new master Router through VRRP negotiation and takes over traffic.

**Figure 1** Network diagram of a VRRP group  
![](images/fig_dc_vrp_vrrp_cfg_010202.png)  

On a multicast or broadcast LAN such as an Ethernet network, a logical VRRP gateway ensures reliability for key links. VRRP is highly reliable and prevents service interruption if a physical VRRP-enabled gateway fails. VRRP configuration is simple and takes effect without modifying configurations such as routing protocols.


#### Purpose

As networks rapidly develop and applications diversify, various value-added services (VASs), such as Internet Protocol television (IPTV) and video conferencing, are being widely deployed. As a result, network reliability is required to ensure uninterrupted service transmission for users.

Hosts are usually connected to an external network through a default gateway. If the default gateway fails, communication between the hosts and external network is interrupted. System reliability can be improved using dynamic routing protocols (such as RIP and OSPF) or ICMP Router Discovery Protocol (IRDP). However, this method requires complex configurations and each host must support dynamic routing protocols.

VRRP provides a better option, which involves grouping multiple routing devices into a virtual router without changing existing networking. The IP address of the virtual router is configured as the default gateway address. If a gateway fails, VRRP selects a different gateway to forward traffic, thereby ensuring reliable communication.

Hosts on a local area network (LAN) are usually connected to an external network through a default gateway. When the hosts send packets destined for addresses not within the local network segment, these packets follow a default route to an egress gateway (PE in [Figure 2](#EN-US_CONCEPT_0172361732__en-us_concept_0172351596_fig_dc_vrp_vrrp_cfg_010201)). Subsequently, PE forwards packets to the external network to enable the hosts to communicate with the external network.

**Figure 2** Network diagram of a default gateway on a LAN  
![](images/fig_dc_vrp_vrrp_cfg_010201.png)  

If PE fails, the hosts connected to it will not be able to communicate with the external network, causing service interruptions. This communication failure persists even if an additional Router is added to the LAN. The reasons for this are that only one default gateway can be configured for most hosts on a LAN and hosts send packets destined for addresses beyond the local network segment only through the default gateway even if they are connected to multiple Router.

One common method of improving system reliability is by configuring multiple egress gateways. However, this works only if hosts support route selection among multiple egress gateways. Another method involves deploying a dynamic routing protocol, such as Routing Information Protocol (RIP), or Open Shortest Path First (OSPF), as well as Internet Control Message Protocol (ICMP). However, it is difficult to run a dynamic routing protocol on every host due to possible management or security issues, as well as the fact that a host's operating system may not support the dynamic routing protocol.

VRRP resolves this issue. VRRP is configured only on involved Routers to implement gateway backup, without any networking changes or burden on hosts.


#### Benefits

Benefits to carriers:

* Simplified network management: On a multicast or broadcast LAN such as an Ethernet network, VRRP provides a highly reliable default link that is applicable even if a device fails. Furthermore, it prevents network interruptions caused by single link faults without changing configurations, such as those of dynamic routing and route discovery protocols.
* Strong adaptability: VRRP Advertisement packets are encapsulated into IP packets, supporting various upper-layer protocols.
* Small network overheads: VRRP defines only VRRP Advertisement packets.

Benefits to users:

* Simple configuration: Users only need to specify a gateway address, without the need to configure complex routing protocols on their hosts.
* Improved user experience: Users are unaware of single point of failures on gateways, and their hosts can uninterruptedly communicate with external networks.

#### Implementation Differences Between VRRP and VRRP6

VRRP supports both IPv4 and IPv6, but some features are different, as shown in the following table.

| Feature | Supported by IPv4 | Supported by IPv6 | Implementation Difference |
| --- | --- | --- | --- |
| [Association between VRRP and an interface monitoring group](feature_0029070718.html) | Yes | No | - |
| [Association between VRRP and EFM](feature_0003993407.html) | Yes | No | - |
| [Association between VRRP and NQA](feature_0003997816.html) | Yes | No | - |
| [Association between VRRP and route status](feature_0003993733.html) | Yes | No | - |
| [Unicast VRRP](feature_0029070719.html) | Yes | No | - |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this document, if a VRRP function supports both IPv4 and IPv6, the implementation of this VRRP function is the same for IPv4 and IPv6 unless otherwise specified.