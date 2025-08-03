advertise l2vpn evpn
====================

advertise l2vpn evpn

Function
--------



The **advertise l2vpn evpn** command enables a VPN instance to advertise EVPN IP prefix routes.

The **undo advertise l2vpn evpn** command restores the default configuration.



By default, a VPN instance is disabled from advertising EVPN IP prefix routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**advertise l2vpn evpn** [ **import-route-multipath** ] [ **include-local-cross-route** ]

**undo advertise l2vpn evpn** [ **import-route-multipath** ] [ **include-local-cross-route** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
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



If EVPN IP prefix routes are used to advertise IP routes between devices, you need to enable the VPN instance to advertise EVPN IP prefix routes so that the local VPN instance can advertise IP routes to the peer device through BGP EVPN peer relationships.If import-route-multipath is not specified in the **advertise l2vpn evpn** command, the VPN instance advertises only the optimal route among the routes with the same destination address when advertising EVPN IP prefix routes. In load balancing scenarios, the import-route-multipath parameter must be specified in the **advertise l2vpn evpn** command so that all routes with the same destination address are advertised as EVPN IP prefix routes.By default, the locally leaked routes of a VPN instance are not advertised as EVPN IP prefix routes. To solve the problem of mutual access between VPN instances, run the **advertise l2vpn evpn** command with the include-local-cross-route parameter specified, the locally leaked routes collected by the VPN instance can be advertised as EVPN IP prefix routes and then sent to the remote device through BGP EVPN peer relationships.




Example
-------

# Enable the VPN instance vpna to advertise EVPN IP prefix routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] advertise l2vpn evpn

```