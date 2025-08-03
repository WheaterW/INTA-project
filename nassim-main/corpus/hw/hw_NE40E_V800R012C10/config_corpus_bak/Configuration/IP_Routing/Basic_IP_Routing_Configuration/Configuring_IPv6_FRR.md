Configuring IPv6 FRR
====================

IPv6 FRR is applicable to services that are sensitive to the delay and packet loss on an IPv6 network.

#### Usage Scenario

Public network IPv6 FRR is applicable to services that are sensitive to the delay and packet loss on an IP public network.

After IPv6 FRR is configured, if a fault is detected at the lower layer, the fault is reported to the upper-layer routing system. Then, packets are forwarded through a backup link, which minimizes the impact of link faults on ongoing services.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

IPv6 FRR enables routes of different protocols to back up each other, which may result in loops.



#### Pre-configuration Tasks

Before configuring IPv6 FRR, complete the following tasks:

* Configure parameters of the link layer protocol and IPv6 addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.
* Configure routes of different routing protocols but destined for the same destination address.


[Enabling IPv6 FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0073.html)

Before configuring IPv6 FRR, you need to enable IPv6 FRR globally.

[(Optional) Enabling IPv6 FRR Poison Reverse](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0074.html)

To configure IPv6 FRR on an IP ring network, you need to enable IPv6 FRR poison reverse to prevent instantaneous traffic storms during route convergence.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ip-route_cfg_0075.html)

After configuring IPv6 FRR, you can view information about the backup outbound interfaces and backup next hops in the routing table.