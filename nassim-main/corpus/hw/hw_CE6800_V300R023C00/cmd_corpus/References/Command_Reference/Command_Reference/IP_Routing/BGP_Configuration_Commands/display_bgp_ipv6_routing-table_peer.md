display bgp ipv6 routing-table peer
===================================

display bgp ipv6 routing-table peer

Function
--------



The **display bgp ipv6 routing-table peer** command displays public network routes of the specified BGP4+ peer.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } **advertised-routes**

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } { **accepted-routes** | **not-accepted-routes** }

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } **received-routes**

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } **received-routes** **active**

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } **advertised-routes** *networkIpv6* [ *mask-length* ]

**display bgp ipv6 routing-table peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } **received-routes** *networkIpv6* [ *mask-length* [ **original-attributes** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remoteIpv4Addr* | Specify an IPv4 peer address. | The value is in dotted decimal notation. |
| **advertised-routes** *networkIpv6* | Displays the BGP4+ public network routes advertised to a specified peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **peer** *remoteIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **accepted-routes** | Displays routes accepted by routing policy. | - |
| **not-accepted-routes** | Displays routes not accepted by routing policy.  Information about the routes that fail to match the route-policy can be displayed only after the keep-all-routes or peer keep-all-routes command is configured. | - |
| **received-routes** *networkIpv6* | Displays the BGP4+ public network routes received from the specified peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **active** | Displays information about the active routes received from a specified peer. | - |
| *mask-length* | Specifies the mask length of a network address. | It is an integer ranging from 0 to 128. |
| **original-attributes** | Displays original attributes of specified routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can specify different parameters to view the specific routing information of peer.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the IPv6 routing information of the peer accepted by routing policy.
```
<HUAWEI> display bgp ipv6 routing-table peer 2001:DB8:9:3::1 accepted-routes
 
 BGP Local router ID is 10.3.3.3
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
 *>i    Network  : 2001:DB8:9:1::                           PrefixLen : 64  
        NextHop  : 2001:db8:9:3::1                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn :  i
   i    Network  : 2001:DB8:9:3::                           PrefixLen : 64  
        NextHop  : 2001:db8:9:3::1                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn :  i

```

**Table 1** Description of the **display bgp ipv6 routing-table peer** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes in the routing table. |
| Network | Network address in the BGP4+ routing table. |
| NextHop | Indicates the next-hop address of the packet. |
| LocPrf | Local\_Pref of the route. |
| MED | Indicates the MED of the route. |
| PrefVal | Preferred value of a protocol. |
| Label | Label value. |
| Path/Ogn | AS\_Path and Origin. |