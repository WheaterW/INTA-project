supernet unicast advertise (BGP-VPN instance IPv6 address family view)
======================================================================

supernet unicast advertise (BGP-VPN instance IPv6 address family view)

Function
--------



The **supernet unicast advertise enable** command enables a device to advertise BGP supernet unicast routes to BGP peers.

The **supernet unicast advertise disable** command restores the default configuration.

The **undo supernet unicast advertise enable** command restores the default configuration.



By default, BGP supernet unicast routes are considered invalid and cannot be advertised to BGP peers or delivered to the IP routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**supernet unicast advertise enable**

**supernet unicast advertise disable**

**undo supernet unicast advertise enable**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A BGP supernet route has the same destination address and next hop address or has a more detailed destination address than the next hop address. Any route that meets one of the following conditions is a BGP supernet route.

* If you perform bitwise AND operations on the destination address mask with the destination address and next hop address, respectively, the calculated network addresses are the same, and the destination address mask is greater than or equal to the next hop address mask.
* If you perform bitwise AND operations on the destination address mask with the destination address and next hop address, respectively, the calculated network addresses are different. However, if you perform bitwise AND operations on the next hop address mask with the destination address and next hop address, respectively, the calculated network addresses are the same.BGP supernet routes include BGP supernet labeled routes and BGP supernet unicast routes. To allow a Huawei device to advertise BGP supernet unicast routes that it receives from a connected non-Huawei device to its BGP peers, run the **supernet unicast advertise enable** command on the Huawei device.

**Precautions**

If the next hop to which a supernet route is recursed is also a BGP route, this command does not take effect.


Example
-------

# Configure a BGP device to advertise BGP supernet unicast routes to its peers.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] supernet unicast advertise enable

```