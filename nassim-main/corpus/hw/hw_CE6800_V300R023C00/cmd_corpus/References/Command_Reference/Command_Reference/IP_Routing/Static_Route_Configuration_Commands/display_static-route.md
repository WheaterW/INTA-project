display static-route
====================

display static-route

Function
--------



The **display static-route** command displays static routes.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display static-route routing-table** [ **vpn-instance** *vpn-instance-name* ] [ *destination-address* [ *mask-length* ] ]

**display static-route statistics**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display static-route ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] [ *ipv6-destination-address* [ *prefix-length* ] ]

**display static-route multicast ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] [ *ipv6-destination-address* [ *prefix-length* ] ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display static-route multicast routing-table** [ **vpn-instance** *vpn-instance-name* ] [ *destination-address* [ *mask-length* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *destination-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the length of the prefix. | The value is an integer ranging from 0 to 32. |
| **routing-table** | Displays the information of static routes. | - |
| **ipv6** | Display IPv6 unicast static routes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *ipv6-destination-address* | Specifies a destination IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of the prefix.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 128. |
| **statistics** | Display the maximum number of static routes that can be configured and the number of existing static routes. | - |
| **multicast** | Display multicast static routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check configured static routes, run the **display static-route routing-table** command.To check the maximum number of static routes that can be configured and the number of existing static routes, run the **display static-route statistics** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv4 unicast static routes in the base topology of the public network.
```
<HUAWEI> display static-route ip routing-table
Summary Destinations : 1        Routes : 1

Destination   : 1.1.1.1/32
Preference    : 60                                      Tag            : 0
Interface     : NULL0                                   InterfaceState : UP
OriginNextHop : 0.0.0.0                                 BfdDetect      : Disable
BfdSession    : 0                                       
BfdType       : --
NQAAdminName  : --                                      NQATestName    : --
NQADetect     : Disable                                 Label          : NULL
EFMDetect     : Disable                                 EfmInterface   : --
State         : Active Primary                          TunnelPolicy   : 0
Cost          : 0                                       
IndirectID    : 0x10000CD                               RelayType      : NO
IIDFlags      : BlackHole                               RelayDepth     : 0
LocalAddress  : 0.0.0.0
RemoteIp      : 0.0.0.0
SourceVrfName : --
UserInfo      : 0
DownReason    : 0x0
NQAGroupName  : --

```

# Display the maximum number of static routes that can be configured and the number of existing static routes.
```
<HUAWEI> display static-route statistics
--------------------------------------------------------------------------------
Max IPv4 route number                : 100000
Max IPv6 route number                : 100000
Current configured IPv4 route number : 1
Current configured IPv6 route number : 0

```

# Display the IPv6 multicast static routes that match a specified destination IPv6 address.
```
<HUAWEI> display static-route multicast ipv6 routing-table

Multicast Routing Table
Routes : 1

 Mroute 2001:db8:1::/24
          Interface = Ethernet1/0/1         RPF Neighbor = 2001:db8:2::2
          Preference = 1
 Running Configuration = ipv6 rpf-route-static 2001:db8:1:: 24 2001:db8:2::2
<HUAWEI>

```

# Display IPv4 multicast static routes in the base topology of the public network.
```
<HUAWEI> display static-route multicast routing-table
Multicast Routing Table
Routes : 1

 Mroute 1.1.1.1/32
          Interface = NULL0         RPF Neighbor = 2.2.2.2
          Preference = 1
 Running Configuration = ip rpf-route-static 1.1.1.1 32 2.2.2.2

```

# Display the multicast static routes that match a specified destination IP address.
```
<HUAWEI> display static-route multicast routing-table 10.1.1.1 24
Multicast Routing Table
Routes : 1

 Mroute 1.1.1.1/32
          Interface = NULL0         RPF Neighbor = 3.3.3.3
          Preference = 1
 Running Configuration = ip rpf-route-static 1.1.1.1 32 3.3.3.3

```

# Display VPN multicast static routes.
```
<HUAWEI> display static-route multicast routing-table vpn-instance vrf1
Multicast Routing Table
Routes : 1

 Mroute 1.1.1.1/32
          Interface = NULL0         RPF Neighbor = 4.4.4.4
          Preference = 1
 Running Configuration = ip rpf-route-static vpn-instance vrf1 1.1.1.1 32 4.4.4.4

```

**Table 1** Description of the **display static-route** command output
| Item | Description |
| --- | --- |
| Summary Destinations | Total number of destination network prefixes or host prefixes. |
| Routes | Total number of routes. |
| Destination | Destination Address/Mask Length. |
| Preference | Route preference. |
| Tag | Administrative tag for routes. |
| Interface | Outbound interface configured for a route. If no outbound interface is configured for a route, this item is displayed as "-". |
| InterfaceState | Interface status. If no interface is configured, this item is displayed as "-". |
| OriginNextHop | Next hop configured for a route. If no next hop is configured for a route, this item is displayed as "::". |
| BfdDetect | BFD detection result:   * Disable: indicates that the BFD detection is not enabled. * UP: indicates that the BFD session is Up and that routing entries can be delivered. * DOWN: indicates that the detection result is Down and that routing entries cannot be delivered. * unknown: indicates that the detection result is unknown and that routing entries cannot be delivered. * unknown(AdminStatus=Down): indicates that the detection result is unknown, the administration status is Down, and that routing entries can be delivered. |
| BfdSession | Name of the BFD session. |
| BfdType | Type of the BFD session:   * STATIC: static BFD detection. * DYNAMIC: dynamic BFD detection. |
| NQAAdminName | Administrator of an NQA test instance. |
| NQATestName | Name of an NQA test instance. |
| NQADetect | Result of the NQA detection:   * Disable: indicates that the NQA detection is not enabled. * UP: indicates that the detection result is Up and that routing entries can be delivered. * DOWN: indicates that the detection result is Down and that routing entries cannot be delivered. * UNKNOWN: indicates that the detection result is unknown and that routing entries can be delivered. |
| Label | labeling. |
| EFMDetect | Possible values are as follows:   * Disable: indicates that EFM detection is not enabled. * UP: indicates that the detection result is Up and the routing entry can be delivered. * DOWN: indicates that the detection result is Down and the routing entry cannot be delivered. * --: indicates that the detection result is unknown and the routing entry can be delivered. |
| EfmInterface | Interface to which EFM is bound. |
| State | Route selection result:   * Active Primary: indicates an active primary route. * Active Backup: indicates an active backup route. * Inactive Valid: indicates a route that takes part in the route selection but is not preferred. * Inactive Invalid: indicates a route that cannot take part in the route selection. |
| TunnelPolicy | Indicates that the ID of the tunnel policy used by the routes. The value of routes that are not iterated to tunnels is 0. |
| Cost | Route cost. |
| IndirectID | Keyword of indirect next hop. |
| RelayType | Indicates the actual iteration type:   * IP: Indicates that routes are iterated to IP addresses. * NO: Indicates that routes are not iterated. |
| IIDFlags | Keyword flags of indirect next hop, including BlackHole and GateWay. |
| RelayDepth | Recursion depth. |
| LocalAddress | IPv6 address of the local interface. If no IPv6 address is configured for the local interface, this item is displayed as "::". This item is displayed only when the outbound interface of the corresponding route is configured. |
| RemoteIp | IPv6 address of the remote P2P interface. If no IPv6 address is configured for the remote P2P interface, this item is displayed as "::". This item is displayed only when the outbound interface of the corresponding route is configured. |
| SourceVrfName | Displays the name of the configured VPN instance. |
| UserInfo | Service data. |
| DownReason | Reason why the static route is inactive:   * 0x0: initializing. * 0x1: The interface is Down. * 0x2: The NQA session is Down. * 0x4: The BFD session is Down. * 0x8: The EFM session is Down. * 0x10: The iteration depth exceeds the upper limit. * 0x20: The route is iterated to the default route. * 0x40: The route is iterated to a supernet route. * 0x80: No IIDs are obtained. * 0x100: The LDP session is Down. * 0x200: The route fails to be iterated to another route or tunnel. * 0x400: The route is iterated to a local host route. * 0x800: The static route is reachable but is not selected as the optimal route according to the route selection rules. * 0x1000: The route is iterated to a non-host route. * 0xFFFFFFFF: The route is inactive due to an unknown reason. |
| NQAGroupName | Name of an NQA group. |
| Max IPv4 route number | Maximum number of static IPv4 routes that can be configured. |
| Max IPv6 route number | Maximum number of static IPv6 routes that can be configured. |
| Current configured IPv4 route number | Number of existing static IPv4 routes. |
| Current configured IPv6 route number | Number of existing static IPv6 routes. |
| Mroute | Multicast route. |
| RPF Neighbor | The address of RPF neighbor. |
| Running Configuration | Recursive route. |