peer high-priority (BGP-EVPN address family view)
=================================================

peer high-priority (BGP-EVPN address family view)

Function
--------



The **peer high-priority** command enables a device to preferentially select routes based on their priorities in the EVPN address family.

The **undo peer high-priority** command disables a device from preferentially selecting routes based on their priorities in the EVPN address family.



By default, routes are preferentially selected based on BGP route selection rules in the EVPN address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **high-priority** [ **disable** ]

**undo peer** *peerIpv4Addr* **high-priority** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 address for a BGP EVPN peer. | The value is in dotted decimal notation. |
| **disable** | Disables a device from preferentially selecting routes based on their high priority in the EVPN address family. | - |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The EVPN address family supports the coexistence of IPv4 and IPv6 peers. A device may learn routes with the same prefix from IPv4 and IPv6 peers. To control the route priority, run the route-priority command. This function takes effect only locally and is not transmitted through packets.


Example
-------

# Enable a device to preferentially select a route with an IPv4 next hop based on a high priority in the EVPN address family.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 high-priority

```