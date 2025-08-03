display bgp vpnv6 routing-table peer
====================================

display bgp vpnv6 routing-table peer

Function
--------



The **display bgp vpnv6 routing-table peer** command displays BGP VPNv6 routes of a specified peer.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **received-routes** *ipv6-address* [ *masklen* ]

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* { **accepted-routes** | **not-accepted-routes** }

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv6-address* [ *masklen* [ **longer-prefixes** ] ]

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **advertised-routes** *ipv6-address* [ *masklen* [ **longer-prefixes** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remoteIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **received-routes** | Displays routes received from the remote peer. | - |
| *ipv6-address* | Specifies an IPv6 network segment address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *masklen* | Specifies an IPv6 address prefix length. | It is an integer ranging from 0 to 128. |
| **accepted-routes** | Displays the routes that match a routing policy. | - |
| **not-accepted-routes** | Displays the routes that do not match a routing policy. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| *remoteIpv6Addr* | Specifies an IPv6 peer address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **advertised-routes** | Indicates the routes advertised to the peer. | - |
| **longer-prefixes** | Allows match against longer masks. | - |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 routing-table peer** command displays BGP VPNv6 routes of a specified peer.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display received BGP VPNv6 routes.
```
<HUAWEI> display bgp vpnv6 all routing-table peer 10.1.1.2 accepted-routes
BGP Local router ID is 172.16.1.1
Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
 h - history, i - internal, s - suppressed, S - Stale
 Origin : i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V - valid, I - invalid, N - not-found

Total Number of Routes: 3
Route Distinguisher: 100:1

*>i Network : 2001:DB8:11::11 PrefixLen : 128 
 NextHop : ::FFFF:192.168.1.1 LocPrf : 
 MED : PrefVal : 0
 Label : 32860/32868
 Path/Ogn : 100?
*>i Network : 2001:DB8:2000::1 PrefixLen : 128 
 NextHop : ::FFFF:192.168.1.1 LocPrf : 
 MED : PrefVal : 0
 Label : 32860/32867
 Path/Ogn : 100?
 
Route Distinguisher: 100:3

*> Network : 2001:DB8:3::3 PrefixLen : 128
 NextHop : ::FFFF:192.168.1.1 LocPrf :
 MED : 0 PrefVal : 0
 Label : NULL/32860
 Path/Ogn : 100?

```

**Table 1** Description of the **display bgp vpnv6 routing-table peer** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | ID of the local BGP device, in the same format as an IPv4 address. |
| Total Number of Routes | Total number of BGP VPNv6 routes. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Network | Indicates the destination network or host address of the route. |
| PrefixLen | Mask length of the destination network address or host address of the route. |
| NextHop | IPv6 address of the next hop. |
| LocPrf | Local\_Pref of a BGP route. The default value is 100. |
| MED | Indicates the MED of the route. The default value is 0. |
| PrefVal | PrefVal. |
| Label | Indicates the label carried by the data packet destined for the destination network or host address of the route. |
| Path/Ogn | AS\_Path and Origin attributes of a route. |