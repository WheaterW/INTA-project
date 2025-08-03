peer graceful-shutdown manual-activate(BGP view)
================================================

peer graceful-shutdown manual-activate(BGP view)

Function
--------



The **peer graceful-shutdown manual-activate** command activates the g-shut function for a specified peer.

The **undo peer graceful-shutdown manual-activate** command restores the default configuration.



By default, the g-shut function of a peer is not activated.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **graceful-shutdown** **manual-activate**

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **graceful-shutdown** **manual-activate** **disable**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **graceful-shutdown** **manual-activate**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **graceful-shutdown** **manual-activate** **disable**

For CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate**

**peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate** **disable**

**undo peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate**

**undo peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **disable** | Deactivates the g-shut feature of a peer. The difference between this parameter and the undo command is that this parameter enables the device not to inherit the g-shut activation status of a peer group. | - |



Views
-----

BGP view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 graceful-shutdown manual-activate

```