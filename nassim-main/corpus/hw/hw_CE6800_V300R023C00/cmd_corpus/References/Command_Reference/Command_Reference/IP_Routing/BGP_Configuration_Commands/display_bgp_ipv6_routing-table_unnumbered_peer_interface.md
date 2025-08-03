display bgp ipv6 routing-table unnumbered peer interface
========================================================

display bgp ipv6 routing-table unnumbered peer interface

Function
--------



The **display bgp ipv6 routing-table unnumbered peer interface advertised-routes** command displays information about BGP IPv6 routes sent to unnumbered BGP peers.

The **display bgp ipv6 routing-table unnumbered peer interface received-routes** command displays BGP IPv6 routes received from unnumbered BGP peers.

The **display bgp ipv6 routing-table unnumbered peer interface accepted-routes** command displays the BGP IPv6 routes that are received from unnumbered BGP peers and match a routing policy.

The **display bgp ipv6 routing-table unnumbered peer interface not-accepted-routes** commnd displays the BGP IPv6 routes that are received from unnumbered BGP peers and fail to match a routing policy.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **advertised-routes**

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **advertised-routes** *networkIpv6* [ *mask-length* ]

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **received-routes** [ **active** ]

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **received-routes** *networkIpv6* [ *mask-length* [ **original-attributes** ] ]

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **accepted-routes** | **not-accepted-routes** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **advertised-routes** | Indicates the routes sent to the peer. | - |
| *networkIpv6* | Indicates the IPv6 network segment address. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| *mask-length* | Specifies the mask length of the network address. | The value is an integer ranging from 0 to 128. |
| **received-routes** | Indicates the route from the peer. | - |
| **active** | Displays the active routed from the peer. | - |
| **original-attributes** | Displays original attributes of specified routes. | - |
| **accepted-routes** | Indicates the routes that match the policy. | - |
| **not-accepted-routes** | Indicates the routes that do not match the policy. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp ipv6 routing-table unnumbered peer interface advertised-routes** command displays information about BGP IPv6 routes sent to unnumbered BGP peers.The **display bgp ipv6 routing-table unnumbered peer interface received-routes** command displays BGP IPv6 routes received from unnumbered BGP peers.The **display bgp ipv6 routing-table unnumbered peer interface accepted-routes** command displays the BGP IPv6 routes that are received from unnumbered BGP peers and match a routing policy.The display bgp ipv6 routing-table unnumbered peer interface not-accepted-routes commnd displays the BGP IPv6 routes that are received from unnumbered BGP peers and fail to match a routing policy.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP IPv6 routes received from BGP unnumbered peers.
```
<HUAWEI> display bgp ipv6 routing-table unnumbered peer interface 100GE 1/0/1 received-routes
 BGP local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete

 Total Number of Routes: 2
 *>i    Network  : 2001:DB8::6                              PrefixLen : 128 
        NextHop  : FE80::3AAE:90FF:FE11:309                 LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 55 66 77?

```

**Table 1** Description of the **display bgp ipv6 routing-table unnumbered peer interface** command output
| Item | Description |
| --- | --- |
| BGP local router ID is | Local router ID of BGP. |
| Total Number of Routes | Number of routes. |
| Network | BGP route prefix. |
| NextHop | Next-hop IP address. |
| LocPrf | Local\_Pref of the route. |
| MED | MED of the route. |
| PrefVal | PrefVal of the route. |
| Path/Ogn | List of ASs through which the message passes and the source of the message. |