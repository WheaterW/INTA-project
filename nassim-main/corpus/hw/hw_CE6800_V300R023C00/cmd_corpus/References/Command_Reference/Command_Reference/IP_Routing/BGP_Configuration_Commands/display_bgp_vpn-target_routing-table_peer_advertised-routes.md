display bgp vpn-target routing-table peer advertised-routes
===========================================================

display bgp vpn-target routing-table peer advertised-routes

Function
--------



The **display bgp vpn-target routing-table peer advertised-routes** command displays information about routes in the BGP-VPN-Target address family.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp vpn-target routing-table peer** { *ipv4-address* | *ipv6-address* } **advertised-routes**

For CE6885-LL (low latency mode):

**display bgp vpn-target routing-table peer** *ipv4-address* **advertised-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **advertised-routes** | Displays information about routes advertised to a specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display bgp vpn-target routing-table peer advertised-routes command displays information about routes in the BGP-VPN-Target address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about routes advertised to the peer with IP address 1.1.1.1 in the BGP-VPN-Target address family.
```
<HUAWEI> display bgp vpn-target routing-table peer 1.1.1.1 advertised-routes
 Advertised routes total: 3

 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete


 Origin AS: 100


        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
 *>i    RT<1:1>            2.2.2.2        0          100        0        ?
 *>i    RT<4:5>            2.2.2.2        0          100        0        ?
 *>     RT<20:1>           2.2.2.2        0          100        0        ?

```

**Table 1** Description of the **display bgp vpn-target routing-table peer advertised-routes** command output
| Item | Description |
| --- | --- |
| Advertised routes total | Number of routes sent to a specified peer. |
| BGP Local router ID is | Router ID of the local device, in the format of an IPv4 address. |
| Origin AS | Origin AS number of the route. |
| MED | Multi-exit discriminator (MED), which is used to determine the optimal route when traffic enters an AS. During route selection, the route with the smallest MED value is selected as the optimal route if all other attributes are the same. |
| LocPrf | Local\_Pref of the RT route. |
| PrefVal | PrefVal of the route. |