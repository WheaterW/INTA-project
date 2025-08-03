display op-route routing-table
==============================

display op-route routing-table

Function
--------



The **display op-route routing-table** command displays op-routes.




Format
------

**display op-route ip routing-table** [ **vpn-instance** *vpn-instance-name* | **topology** *topology-name* ] [ *prefix4* [ *mask4* ] ]

**display op-route ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* | **topology** *topology-name* ] [ *prefix6* [ *mask6* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **topology** *topology-name* | Specifies the name of a topology. | The value is a string of 1 to 31 case-sensitive characters. The name must start with an English letter (a to z, or A to Z) and can be a mixture of English letters, digits, hyphens (-), or underlines (\_). If spaces are used, the string must start and end with double quotation marks ("). |
| *prefix4* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *mask4* | Specifies a mask length. | The value is an integer ranging from 0 to 32. |
| **ip** | Ipv4 route. | - |
| **ipv6** | Ipv6 route. | - |
| *prefix6* | Specifies a destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *mask6* | Specifies a mask length. | The value is an integer ranging from 1 to 128. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check configured op-routes, run the **display op-route routing-table** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display op-routes in the public network.
```
<HUAWEI> display op-route ip routing-table
Summary Destinations : 784608        Routes : 784608

Destination   : 1.1.1.1/32
Preference    : 0                                       Tag            : 0
Interface     : --                                      InterfaceState : --
OriginNextHop : 10.1.1.2                                
State         : Active Primary                          
Cost          : 0                                       
IndirectID    : 0x2000002                               RelayType      : IP
IIDFlags      : GateWay                                 RelayDepth     : 1
DestVrf       : _public_                                DestTopo       : 
SourceVrfName : --
UserInfo      : 0
DownReason    : 0x0
RelayNextHop  : 10.1.1.2                                RelayInterface : Loopback0
TunnelID      : --                                      BrasCID        : 0x0

```

**Table 1** Description of the **display op-route routing-table** command output
| Item | Description |
| --- | --- |
| Summary Destinations | Indicates the total number of destination network prefixes or host prefixes. |
| Routes | Total number of routes. |
| Destination | Indicates the destination address/mask length. |
| Preference | Route priority. |
| Tag | Route management tag. |
| Interface | Indicates the outbound interface configured for a route. If no outbound interface is configured for a route, this item is displayed as "-". |
| InterfaceState | Indicates the interface status. If no interface status is configured, the item is displayed as "-". |
| OriginNextHop | Indicates the next hop configured for a route. If no next hop is configured for a route, this item is displayed as "::". |
| State | Indicates the route selection result:   * Active Primary: indicates an active primary route. * Active Backup: indicates an active backup route. * Inactive Valid: indicates a route that takes part in the route selection but is not preferred. * Inactive Invalid: indicates a route that cannot take part in the route selection. |
| Cost | Route cost. |
| IndirectID | Indicates the keyword of indirect next hop. |
| RelayType | Indicates the actual iteration type:   * IP: Indicates that routes are iterated to IP addresses. * NO: Indicates that routes are not iterated. |
| IIDFlags | Flag of indirect next hop, including BlackHole and ShortCut. |
| RelayDepth | Recursion depth. |
| DestVrf | Indicates the name of the VPN instance to which the next hop address belongs. This item is displayed only when the next hop of the corresponding static route is configured but the outbound interface of the route is not configured. |
| DestTopo | Indicates the name of the destination topology to which the next hop address belongs. This item is displayed only when the next hop of the corresponding static route is configured but the outbound interface of the route is not configured. |
| SourceVrfName | Source Vrf Name. |
| UserInfo | Client information. |
| DownReason | Reason why the op-route is inactive:   * 0x0: initializing. * 0x1: The interface is Down. * 0x2: The NQA session is Down. * 0x4: The BFD session is Down. * 0x10: The iteration depth exceeds the upper limit. * 0x20: The route is iterated to the default route. * 0x40: The route is iterated to a supernet route. * 0x80: No IIDs are obtained. * 0x200: The route fails to be iterated to another route or tunnel. * 0x400: The route is iterated to a local host route. * 0x800: The static route is reachable but is not selected as the optimal route according to the route selection rules. * 0x1000: The route is iterated to a non-host route. * 0xFFFFFFFF: The route is inactive due to an unknown reason. |
| RelayNextHop | Indicates the iterated next hop address. If the corresponding static route reaches the next hop through a tunnel, this item is displayed as ::. This item is displayed only when the next hop of the route is configured but the outbound interface of the route is not configured. |
| RelayInterface | Indicates the name of an iterated outbound interface. If the corresponding static route reaches the next hop through a tunnel, this item is displayed as a tunnel name. This item is displayed only when the next hop of the route is configured but the outbound interface of the route is not configured. |
| TunnelID | Tunnel ID. The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| BrasCID | CID of a UNR route received from the BRAS, expressed in hexadecimal notation. If no UNR is received, this item is displayed as "--". |