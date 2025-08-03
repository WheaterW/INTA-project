display bgp vpnv6 all routing-table peer
========================================

display bgp vpnv6 all routing-table peer

Function
--------



The **display bgp vpnv6 vpn-instance routing-table peer** command displays BGP VPNv6 routes of a specified peer in a specified VPN instance.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **advertised-routes**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **received-routes**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **received-routes** **active**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **advertised-routes** **statistics**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **received-routes** **statistics**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **received-routes** **active** **statistics**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **advertised-routes** *ipv6-address* [ *masklen* ]

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **received-routes** *ipv6-address* [ *masklen* [ **original-attributes** ] ]

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **advertised-routes**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **received-routes**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** **statistics**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **received-routes** **statistics**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv6-address* [ *masklen* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remoteIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **advertised-routes** | Indicates the routes advertised to the peer. | - |
| **peer** | Peer routers. | - |
| **received-routes** | Displays routes received from the remote peer. | - |
| **active** | Displays active routes from the remote peer. | - |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *remoteIpv6Addr* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **statistics** | Displays route statistics. | - |
| *ipv6-address* | Specifies an ipv6 network address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *masklen* | Specifies an IP address mask length. | It is an integer ranging from 0 to 128. |
| **original-attributes** | Displays original route attributes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 all routing-table** command displays BGP VPNv6 routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display advertised BGP vrf6 routes.
```
<HUAWEI> display bgp vpnv6 vpn-instance vr1 routing-table peer 2001:DB8:2::2 advertised-routes
Total Number of Routes: 1

 BGP Local router ID is 10.2.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 *>  Network  : 2001:DB8:2001::                          PrefixLen : 64
     NextHop  : ::                                       LocPrf    :
     MED      : 0                                        PrefVal   : 0
     Label    : NULL
     Path/Ogn : ?

```

**Table 1** Description of the **display bgp vpnv6 all routing-table peer** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of BGP VPNv6 routes. |
| BGP Local router ID | ID of the local BGP device, in the same format as an IPv4 address. |
| Network | Indicates the destination network or host address of the route. |
| PrefixLen | Mask length of the destination network address or host address of the route. |
| NextHop | IPv6 address of the next hop. |
| Label | Indicates the label carried by the data packet destined for the destination network or host address of the route. |
| Path/Ogn | AS\_Path and Origin attributes of a route. |
| origin | Indicates the origin of the route. |