Overview of VRRP
================

Overview of VRRP

#### Definition

The Virtual Router Redundancy Protocol (VRRP) is a standard-defined fault-tolerant protocol that groups several physical devices into a virtual one. If a physical device (master) that serves as the next hop of hosts fails, the virtual device switches traffic to a different physical device (backup), thereby ensuring service continuity and reliability.

VRRP allows logical and physical devices to work separately and implements route selection among multiple egress gateways. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130784052__fig_dc_vrp_vrrp_cfg_010202), a VRRP group is configured on two devices, one of which serves as the master, and the other as the backup. The two devices form a virtual device that is assigned a virtual IP address and a virtual MAC address. Hosts are only aware of this virtual device, as opposed to the master and backup devices, and they use it to communicate with devices on different network segments.

**Figure 1** VRRP networking  
![](figure/en-us_image_0000001176663839.png)

#### Purpose

As networks rapidly develop and applications diversify, various value-added services (VASs), such as Internet Protocol television (IPTV) and video conferencing, are being widely deployed. As a result, network reliability is required to ensure uninterrupted service transmission for users.

Hosts on a local area network (LAN) are usually connected to an external network through a default gateway. When the hosts send packets destined for addresses not within the local network segment, these packets follow a default route to an egress gateway (Gateway in [Figure 2](#EN-US_CONCEPT_0000001130784052__fig_dc_vrp_vrrp_cfg_010201)). Subsequently, Gateway forwards packets to the external network to enable the hosts to communicate with the external network. If Gateway fails, the hosts connected to it will not be able to communicate with the external network, causing service interruptions. This communication failure persists even if an additional device is added to the LAN. The reasons for this are that only one default gateway can be configured for most hosts on a LAN and hosts send packets destined for addresses beyond the local network segment only through the default gateway even if they are connected to multiple devices.

One common method of improving system reliability is by configuring multiple egress gateways. However, this works only if hosts support route selection among multiple egress gateways. Another method involves deploying a dynamic routing protocol, such as Routing Information Protocol (RIP) or Open Shortest Path First (OSPF). However, it is difficult to run a dynamic routing protocol on every host due to possible management or security issues, as well as the fact that a host's operating system may not support the dynamic routing protocol.

VRRP provides a better option, which involves grouping multiple devices into a virtual device without changing existing networking. The IP address of the virtual device is configured as the default gateway address. If a gateway fails, VRRP selects a different gateway to forward traffic, thereby ensuring reliable communication.

**Figure 2** Network diagram of a default gateway on a LAN  
![](figure/en-us_image_0000001176743745.png)

#### Benefits

* Simplified network management: VRRP provides a highly reliable default link that is applicable even if a device fails. Furthermore, it prevents network interruptions caused by single link faults without changing configurations, such as those of dynamic routing and route discovery protocols.
* Strong adaptability: VRRP Advertisement packets are encapsulated into IP packets, supporting various upper-layer protocols.
* Small network overheads: VRRP defines only VRRP Advertisement packets.

* Simple configuration: Users only need to specify a gateway address, without needing to configure complex routing protocols on their hosts.
* Improved user experience: Users are unaware of single points of failures on gateways, and their hosts can communicate with external networks without interruptions.