display bgp ipv6 routing-table peer statistics
==============================================

display bgp ipv6 routing-table peer statistics

Function
--------



The **display bgp ipv6 routing-table peer statistics** command displays the routing statistics of the specified BGP4+ peer.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } { **advertised-routes** | **received-routes** | **received-routes** **active** } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remoteIpv4Addr* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |
| **advertised-routes** | Routes advertised to the remote peer. | - |
| **received-routes** | Indicates the routes from the peer. | - |
| **active** | Displays the active routes received from the specified peer. | - |
| **statistics** | Displays statistics about routes. | - |
| **peer** *remoteIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp ipv6 routing-table peer statistics** command displays the routing statistics of the specified BGP4+ peer. You can specify different parameters to view the specific routing statistics information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays statistics about IPv6 routes received from the peer.
```
<HUAWEI> display bgp ipv6 routing-table peer 2001:DB8:9:3::1 received-routes statistics

 Received routes total: 2

```

**Table 1** Description of the **display bgp ipv6 routing-table peer statistics** command output
| Item | Description |
| --- | --- |
| Received routes total | Number of BGP routes received from the peer. |