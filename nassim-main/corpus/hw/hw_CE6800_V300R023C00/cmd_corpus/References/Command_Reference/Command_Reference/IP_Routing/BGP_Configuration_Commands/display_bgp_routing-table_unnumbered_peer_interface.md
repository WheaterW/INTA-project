display bgp routing-table unnumbered peer interface
===================================================

display bgp routing-table unnumbered peer interface

Function
--------



The **display bgp routing-table unnumbered peer interface advertised-routes** command displays BGP routes sent to unnumbered BGP peers.

The **display bgp routing-table unnumbered peer interface received-routes** command displays BGP routes received from unnumbered peers.

The **display bgp routing-table unnumbered peer interface accepted-routes** command displays BGP routes that are received from unnumbered BGP peers and match a route-policy.

The **display bgp routing-table unnumbered peer interface not-accepted-routes** command displays BGP routes that are received from unnumbered BGP peers and fail to match a route-policy.




Format
------

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **advertised-routes**

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **advertised-routes** *ipv4-address* [ { *mask-length* | *mask-ipv4* } [ **longer-prefixes** ] ]

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **received-routes** [ **active** ]

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **received-routes** *ipv4-address* [ { *mask-length* | *mask-ipv4* } [ **original-attributes** ] ]

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **accepted-routes** | **not-accepted-routes** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **advertised-routes** | Indicates the routes sent to the peer. | - |
| *ipv4-address* | Specifies an IPv4 network segment address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies a mask length of an IP address. | The value is an integer that ranges from 0 to 32. |
| *mask-ipv4* | Specifies the mask of the IPv4 network segment. | The value is in dotted decimal notation. |
| **longer-prefixes** | Allows match against longer masks. | - |
| **received-routes** | Indicates the route from the peer. | - |
| **active** | Displays active routes from the peer. | - |
| **original-attributes** | Displays original route attributes. | - |
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

**Usage Scenario**



The **display bgp routing-table unnumbered peer interface advertised-routes** command displays BGP routes sent to unnumbered BGP peers.The **display bgp routing-table unnumbered peer interface received-routes** command displays BGP routes received from unnumbered peers.The **display bgp routing-table unnumbered peer interface accepted-routes** command displays BGP routes that are received from unnumbered BGP peers and match a route-policy.The **display bgp routing-table unnumbered peer interface not-accepted-routes** command displays BGP routes that are received from unnumbered BGP peers and fail to match a route-policy.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP routes received from the BGP unnumbered peer.
```
<HUAWEI> display bgp routing-table unnumbered peer interface 100GE 1/0/1 received-routes
 BGP local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete

 Total Number of Routes: 1
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
 *>i    10.1.1.2/32        FE80::3AAE:90FF:FE11:309       0          100        0      55 66 77?

```

**Table 1** Description of the **display bgp routing-table unnumbered peer interface** command output
| Item | Description |
| --- | --- |
| BGP local router ID is | Local router ID of BGP. |
| Total Number of Routes | Number of routes. |
| Network | BGP route prefix. |
| NextHop | Next-hop IP address. |
| MED | MED of the route. |
| LocPrf | Local\_Pref of the route. |
| PrefVal | PrefVal of the route. |
| Path/Ogn | List of ASs through which the message passes and the source of the message. |