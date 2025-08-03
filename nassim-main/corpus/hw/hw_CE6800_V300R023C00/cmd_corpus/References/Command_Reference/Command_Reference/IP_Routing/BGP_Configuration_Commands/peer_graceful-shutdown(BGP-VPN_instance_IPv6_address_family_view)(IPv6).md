peer graceful-shutdown(BGP-VPN instance IPv6 address family view)(IPv6)
=======================================================================

peer graceful-shutdown(BGP-VPN instance IPv6 address family view)(IPv6)

Function
--------



The **peer graceful-shutdown** command enables the g-shut function for a single peer (without activating the function) and specifies the attributes to be modified during the g-shut period.

The **undo peer graceful-shutdown** command disables the g-shut function of a single peer.



By default, the g-shut function is disabled on a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **graceful-shutdown** [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ]

**peer** *peerIpv6Addr* **graceful-shutdown** **disable**

**undo peer** *peerIpv6Addr* **graceful-shutdown** [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ]

**undo peer** *peerIpv6Addr* **graceful-shutdown** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **local-preference** *local-preference-value* | Indicates the local-preference value of the routes to be advertised to the peer. Setting the value to 0 is recommended. If there are alternative routes, you can reduce the local preference of the routes advertised to IBGP peers to affect route selection. | The value is an integer that ranges from 0 to 4294967295. |
| **as-prepend** *as-prepend-value* | Specifies the number of ASs to be added to the AS\_Path of the routes to be advertised to the peer. If alternative routes exist, the length of the AS\_Path is increased to affect the route selection. | The value is an integer ranging from 1 to 6. |
| **disable** | Disables the g-shut feature of a peer. The difference between this parameter and the undo command is that this parameter disables the peer from inheriting the g-shut feature from a peer group. | - |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to enable the g-shut feature for a single peer and specify multiple attribute values.


Example
-------

# Enable the g-shut feature of the peer and set the value of the local-preference parameter to 1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 graceful-shutdown local-preference 1

```