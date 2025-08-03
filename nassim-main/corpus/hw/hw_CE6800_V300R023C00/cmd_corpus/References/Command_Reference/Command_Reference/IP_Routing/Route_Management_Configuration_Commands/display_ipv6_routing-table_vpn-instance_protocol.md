display ipv6 routing-table vpn-instance protocol
================================================

display ipv6 routing-table vpn-instance protocol

Function
--------



The **display ipv6 routing-table vpn-instance protocol** command displays the routing table of an IPv6 address family-enabled VPN instance.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table vpn-instance** *vpn-instance-name* **protocol** { **bgp** | **direct** | **isis** | **ospfv3** | **ripng** | **static** } [ **time-range** *min-age* *max-age* ] [ **inactive** | **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Displays routes of a specified protocol. | - |
| **bgp** | displays BGP IPv6 routes. | - |
| **direct** | displays direct IPv6 routes. | - |
| **isis** | displays IS-IS IPv6 routes. | - |
| **ospfv3** | displays OSPFv3 routes. | - |
| **ripng** | displays RIPng routes. | - |
| **static** | displays static IPv6 routes. | - |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| **inactive** | Displays the summary of inactive routes only. | - |
| **verbose** | Displays detailed information about active and inactive routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If neither verbose nor inactive is specified, only the summary of active routes of each routing protocol is displayed. To learn the detailed information about the active and inactive routes, specify verbose.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the direct routes of the IPv6 address family-enabled VPN instance named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] display ipv6 routing-table vpn-instance vrf1 protocol direct
vrf1 Routing Table : Direct
Summary Count : 1

Direct routing table status : <Active>
Summary Count : 1

Destination  : FE80::                                  PrefixLength : 10
NextHop      : ::                                      Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0                                   Flags        : DB
                
Direct routing table status : <Inactive>
Summary Count : 0

```

**Table 1** Description of the **display ipv6 routing-table vpn-instance protocol** command output
| Item | Description |
| --- | --- |
| vrf1 Routing Table | vrf1 routing table. |
| Direct routing table status | Status of direct routes:   * Inactive. * Active. |
| Summary Count | Number of summary routes. |
| Destination | Address of the destination network or host. |
| PrefixLength | Length of the prefix. |
| NextHop | IPv6 address of the adjacent next hop through which the packet reaches the destination. |
| Preference | Priority of the route. |
| Cost | Route cost. |
| Protocol | Routing protocol. |
| RelayNextHop | Indicates the iterated next hop address. |
| TunnelID | Tunnel ID.  The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Outbound interface through which the next hop is reachable. |
| Flags | Route flags. |