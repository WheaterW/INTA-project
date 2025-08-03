peer graceful-shutdown manual-activate(BGP-VPN instance IPv6 address family view)(IPv6)
=======================================================================================

peer graceful-shutdown manual-activate(BGP-VPN instance IPv6 address family view)(IPv6)

Function
--------



The **peer graceful-shutdown manual-activate** command activates the g-shut function for a specified peer.

The **undo peer graceful-shutdown manual-activate** command restores the default configuration.



By default, the g-shut function of a peer is not activated.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **graceful-shutdown** **manual-activate**

**peer** *peerIpv6Addr* **graceful-shutdown** **manual-activate** **disable**

**undo peer** *peerIpv6Addr* **graceful-shutdown** **manual-activate**

**undo peer** *peerIpv6Addr* **graceful-shutdown** **manual-activate** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **disable** | Deactivates the g-shut feature of a peer. The difference between this parameter and the undo command is that this parameter enables the device not to inherit the g-shut activation status of a peer group. | - |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to activate the g-shut feature for a single peer.


Example
-------

# Activate the g-shut function for a specified peer.
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
[*HUAWEI-bgp] peer 2001:DB8:1::1 graceful-shutdown manual-activate

```