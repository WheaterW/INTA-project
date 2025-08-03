Configuring IPv4 FRR
====================

IPv4 FRR is applicable to IPv4 services that are sensitive to the packet loss and delay.

#### Usage Scenario

Public network IPv4 FRR is applicable to services that are sensitive to packet loss or delay on the IPv4 public network.

After FRR is configured, if a fault is detected at the lower layer, the fault is reported to the upper-layer routing system. Then, packets are forwarded through a backup link, which minimizes the impact of link faults on ongoing services.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

IPv4 FRR enables routes of different protocols to back up each other, which may result in loops.

With IP FRR, traffic is switched to a backup link if the primary link fails and switched back when the primary link recovers. If the inbound and outbound interfaces reside on different boards, packet loss may occur during the switchback. The packet loss duration varies with the service volume and CPU usage. To prevent the packet loss, perform any of the following operations:

* For IS-IS routes, run the [**timer spf**](cmdqueryname=timer+spf) command in the IS-IS view.
* For OSPF routes, run the [**spf-schedule-interval**](cmdqueryname=spf-schedule-interval) command in the OSPF view.
* For BGP routes, run the [**route-select delay**](cmdqueryname=route-select+delay) command in the BGP view.



#### Pre-configuration Tasks

Before configuring IPv4 FRR, complete the following task:

* Configure parameters of the link layer protocol and IPv4 addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.
* Configure routes of different routing protocols but destined for the same destination address.


[Enabling IPv4 FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0070.html)

Before configuring IPv4 FRR, you need to enable IPv4 FRR globally.

[(Optional) Enabling IPv4 FRR Poison Reverse](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0071.html)

To configure IPv4 FRR on an IP ring network, you need to enable IPv4 FRR poison reverse to prevent instantaneous traffic storms during route convergence.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0072.html)

After configuring IPv4 FRR, you can view information about the backup outbound interfaces and backup next hops in the routing table.