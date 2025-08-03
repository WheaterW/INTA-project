peer graceful-shutdown(BGP-VPN instance IPv4 address family view)(IPv4)
=======================================================================

peer graceful-shutdown(BGP-VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer graceful-shutdown** command enables the g-shut function for a single peer (without activating the function) and specifies the attributes to be modified during the g-shut period.

The **undo peer graceful-shutdown** command disables the g-shut function of a single peer.



By default, the g-shut function is disabled on a peer.


Format
------

**peer** *peerIpv4Addr* **graceful-shutdown** [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ]

**peer** *peerIpv4Addr* **graceful-shutdown** **disable**

**undo peer** *peerIpv4Addr* **graceful-shutdown** [ **local-preference** *local-preference-value* | **as-prepend** *as-prepend-value* ]

**undo peer** *peerIpv4Addr* **graceful-shutdown** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **local-preference** *local-preference-value* | Indicates the local-preference value of the routes to be advertised to the peer. Setting the value to 0 is recommended. If there are alternative routes, you can reduce the local preference of the routes advertised to IBGP peers to affect route selection. | The value is an integer that ranges from 0 to 4294967295. |
| **as-prepend** *as-prepend-value* | Specifies the number of ASs to be added to the AS\_Path of the routes to be advertised to the peer. If alternative routes exist, the length of the AS\_Path is increased to affect the route selection. | The value is an integer ranging from 1 to 6. |
| **disable** | Disables the g-shut feature of a peer. The difference between this parameter and the undo command is that this parameter disables the peer from inheriting the g-shut feature from a peer group. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to enable the g-shut feature for a single peer and specify multiple attribute values.




Example
-------

# Enable the g-shut feature of the peer and set the value of the local-preference parameter to 1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 graceful-shutdown local-preference 1

```