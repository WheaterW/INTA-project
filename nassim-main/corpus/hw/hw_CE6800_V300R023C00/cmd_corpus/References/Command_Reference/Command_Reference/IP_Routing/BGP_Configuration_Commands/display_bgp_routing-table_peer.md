display bgp routing-table peer
==============================

display bgp routing-table peer

Function
--------



The **display bgp routing-table peer** command displays the BGP routing information of a specified peer.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp routing-table peer** *remoteIpv4Addr* { **accepted-routes** | **not-accepted-routes** }

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* { **accepted-routes** | **not-accepted-routes** }

**display bgp vpnv4 all routing-table peer** *remoteIpv4Addr* { **accepted-routes** | **not-accepted-routes** }

**display bgp routing-table peer** *remoteIpv4Addr* **advertised-routes** [ **statistics** ]

**display bgp routing-table peer** *remoteIpv4Addr* **received-routes** **statistics**

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** [ **statistics** ]

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **received-routes** [ **statistics** ]

**display bgp routing-table peer** *remoteIpv4Addr* **received-routes** **active** [ **statistics** ]

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **received-routes** **active** [ **statistics** ]

**display bgp routing-table peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **longer-prefixes** ] ]

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **longer-prefixes** ] ]

**display bgp routing-table peer** *remoteIpv4Addr* **received-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **original-attributes** ] ]

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **received-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **original-attributes** ] ]

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** [ **statistics** ]

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **received-routes** [ **statistics** ]

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **received-routes** **active** [ **statistics** ]

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **longer-prefixes** ] ]

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* **received-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **original-attributes** ] ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp routing-table peer** *remoteIpv6Addr* { **accepted-routes** | **not-accepted-routes** }

**display bgp routing-table peer** *remoteIpv6Addr* **advertised-routes** [ **statistics** ]

**display bgp routing-table peer** *remoteIpv6Addr* **advertised-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **longer-prefixes** ] ]

**display bgp routing-table peer** *remoteIpv6Addr* **received-routes** *ipv4-address* [ { *mask-length* | *mask* } [ **original-attributes** ] ]

**display bgp routing-table peer** *remoteIpv6Addr* **received-routes** **statistics**

**display bgp routing-table peer** *remoteIpv6Addr* **received-routes** **active** [ **statistics** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remoteIpv6Addr* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **advertised-routes** | Indicates the routes advertised to the peer. | - |
| **statistics** | Indicates route statistics. | - |
| **vpnv4** | Indicates the VPNv4 address family. | - |
| **all** | Displays all information about all VPNv4 and VPN instances. | - |
| *ipv4-address* | Specifies an IPv4 network address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies an IP address mask length. | The value is an integer ranging from 0 to 32. |
| *mask* | Specifies an IPv4 network mask. | The value is in dotted decimal notation. |
| **longer-prefixes** | Allows longer mask matching. The queried route data is filtered, and the number of routes is not filtered. | - |
| **received-routes** | Displays routes received from the remote peer. | - |
| **active** | Displays active routes from the remote peer. | - |
| **accepted-routes** | Displays the routes that match a routing policy. | - |
| **not-accepted-routes** | Displays the routes that do not match a routing policy. | - |
| **original-attributes** | Indicates original route attributes. | - |
| *remoteIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies the name of a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display bgp routing-table peer** command displays the BGP routing information of a specified peer. You can view only specific routing information by specifying different parameters.

**Precautions**

This command does not display the default route that is configured to be advertised to peers using the **peer default-route-advertise** command.By default, if **accepted-routes** or **received-routes** is specified, the routes that match the configured import policy are displayed. If **not-accepted-routes** is specified, no information is displayed. After the keep-all-routes or **peer keep-all-routes** command is run to configure the device to save all BGP routing updates from a specified peer after a BGP connection is established:

* If **received-routes** is specified, all routes received from peers are displayed.
* If **accepted-routes** is specified, the routes that match the configured import policy are displayed.
* If **not-accepted-routes** is specified, the routes that do not match the configured import policy are displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BGP routes received from a specified peer, with the routes carrying a specified destination address and the entropy label.
```
<HUAWEI> display bgp routing-table peer 10.1.1.1 received-routes 10.1.1.1

 BGP local router ID : 10.2.2.2
 Local AS number : 100
 BGP routing table entry information of 10.1.1.1/32:
 RR-client route.
 Label information (Received/Applied): 48288/NULL
 From: 10.1.1.1 (10.1.1.1)
 Route Duration: 0d05h28m03s
 Relay IP Nexthop: 10.2.2.2
 Relay IP Out-Interface: Tunnel1
 Relay Tunnel Out-Interface:
 Original nexthop: 10.1.1.1
 Qos information : 0x0
 Community: <1:1>
 Ext-Community: Color <0 : 3>
 Large-Community: <1:1:1>
 Entropy-label padding value : AB 6A F2
 AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, valid, internal, best, select, supernet, pre 255, IGP cost 1
 Originator: 10.3.1.1
 Cluster list: 0.0.0.100
 Not advertised to any peer yet

```

# Display the BGP routing information accepted from a specified peer.
```
<HUAWEI> display bgp routing-table peer 10.1.1.1 accepted-routes
BGP Local router ID is 10.1.1.2
Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
 h - history, i - internal, s - suppressed, S - Stale
 Origin : i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V - valid, I - invalid, N - not-found

Total Number of Routes: 3 
 Network NextHop MED LocPrf PrefVal Path/Ogn
*>i 10.9.9.9/32 10.1.1.2 0 100 0 ?
* ixa 10.1.1.2 0 100 0 ?
* i a 10.1.1.2 0 100 0 ?

```

**Table 1** Description of the **display bgp routing-table peer** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | Router ID of the local BGP device. |
| Local AS number | Local AS number. |
| Label information (Received/Applied) | Label information (received label/advertised label). |
| Route Duration | Duration for route advertisement. |
| Relay IP Nexthop | Recursive next hop. |
| Relay Tunnel Out-Interface | Name of the tunnel to which a route recurses. |
| Original nexthop | Original next-hop address for sending messages. |
| Qos information | Qos information. |
| Entropy-label padding value | Entropy label attribute value.  This field can be displayed only after the entropy-label command is configured. |
| MED | MED of the route. |
| Cluster list | Cluster\_List. |
| Origin | Route origin. |
| Total Number of Routes | Total number of received, advertised, received, or unreceived routes. |
| Network | Prefix in the BGP routing table. |
| LocPrf | Local\_Pref of the route. |
| PrefVal | PrefVal of the route. |
| Path/Ogn | AS\_Path and Origin. |
| Nexthop | Next-hop IP address. |
| From | Source peer for route advertisement. |
| Community | Community attribute of a route. |
| Ext-Community | Extended community attribute. |
| Large-Community | The large community attribute is displayed in routing information. |
| Originator | Router ID of the route initiator. |