advertise (BGP-VPN instance IPv4 address family view)
=====================================================

advertise (BGP-VPN instance IPv4 address family view)

Function
--------



The **advertise valid-routes** command configures a device to send only valid routes in a BGP VPN routing table to a BGP VPNv4/VPNv6 routing table.

The **undo advertise valid-routes** command restores the default configuration.



By default, a device sends all routes in a BGP VPN routing table to a BGP VPNv4 routing table.


Format
------

**advertise valid-routes**

**undo advertise valid-routes**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv4 address family view


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
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 both
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] advertise valid-routes

```