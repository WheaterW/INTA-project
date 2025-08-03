advertise (BGP-VPN instance IPv6 address family view)
=====================================================

advertise (BGP-VPN instance IPv6 address family view)

Function
--------



The **advertise valid-routes** command configures a device to send only valid routes in a BGP VPN routing table to a BGP VPNv4/VPNv6 routing table.

The **undo advertise valid-routes** command restores the default configuration.



By default, a device sends all routes in a BGP VPN routing table to a BGP VPNv4/VPNv6 routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**advertise valid-routes**

**undo advertise valid-routes**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, the device advertises all routes in the BGP VPN routing table to the BGP VPNv4/VPNv6 routing table. For example, the supernet unicast routes are invalid, but VPNv4 and VPNv6 routing tables have such routes. In addition, forwarding entries are generated for such routes, and the routes are advertised to peers. You can run the **advertise valid-routes** command to configure a device to send only valid routes in a BGP VPN routing table to a BGP VPNv4/VPNv6 routing table.


Example
-------

# Configure a device to send only valid routes in a BGP VPN routing table to a BGP VPNv4 routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] advertise valid-routes

```