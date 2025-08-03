advertise l2vpn evpn (BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)
==========================================================================================================

advertise l2vpn evpn (BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)

Function
--------



The **advertise l2vpn evpn** command enables a VPN instance to advertise EVPN IP prefix routes.

The **undo advertise l2vpn evpn** command restores the default configuration.



By default, a VPN instance is disabled from advertising EVPN IP prefix routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**advertise l2vpn evpn** { **best-route** | **valid-routes** } [ **import-route-multipath** ] [ **include-local-cross-route** ]

**undo advertise l2vpn evpn** { **best-route** | **valid-routes** } [ **import-route-multipath** ] [ **include-local-cross-route** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **best-route** | Advertises only optimal routes in a VPN instance as EVPN IP prefix routes. | - |
| **valid-routes** | Advertises only valid routes in a VPN instance as EVPN IP prefix routes. | - |
| **import-route-multipath** | Advertises all routes with the same destination address in a VPN instance as EVPN IP prefix routes. | - |
| **include-local-cross-route** | Advertises all locally leaked routes in a VPN instance as EVPN IP prefix routes. | - |



Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If EVPN IP prefix routes are used to advertise IP routes between devices, you need to enable the VPN instance to advertise EVPN IP prefix routes so that the local VPN instance can advertise IP routes to the peer device through BGP EVPN peer relationships.By default, the device advertises external routes in the VPN instance routing table, including invalid routes and non-optimal routes, as EVPN IP prefix routes. To prevent invalid routes from being advertised, you can specify valid-routes. If you want to advertise only the optimal VPN routes as EVPN IP prefix routes, specify best-route.If the **advertise l2vpn evpn** command does not contain the import-route-multipath parameter when it is run, the VPN instance advertises only optimal locally imported routes as EVPN IP prefix routes. In load-balancing scenarios, the import-route-multipath parameter must be specified in the **advertise l2vpn evpn** command, so that the VPN instance advertises all locally imported routes with the same destination address as EVPN IP prefix routes.




Example
-------

# Enable the VPN instance vpna to advertise valid routes as EVPN IP prefix routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] advertise l2vpn evpn valid-routes

```