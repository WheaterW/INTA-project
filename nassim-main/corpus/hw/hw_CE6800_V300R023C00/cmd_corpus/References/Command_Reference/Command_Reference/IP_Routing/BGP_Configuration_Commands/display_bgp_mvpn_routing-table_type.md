display bgp mvpn routing-table type
===================================

display bgp mvpn routing-table type

Function
--------



The **display bgp mvpn routing-table type** command displays the routing information of BGP MVPN and multicast VPN instances.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp mvpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **type** { **1** | **2** | **3** | **5** | **6** | **7** } *network*

**display bgp mvpn vpn-instance** *vpn-instance-name* **routing-table** **type** { **1** | **2** | **3** | **5** | **6** | **7** } *network*

**display bgp mvpn all routing-table peer** *ipv4-address* **advertised-routes** **type** { **1** | **2** | **3** | **5** | **6** | **7** } *network*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all BGP MVPN routes. | - |
| **route-distinguisher** *route-distinguisher* | Displays BGP routes of the specified Route Distinguisher (RD). | The RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. If both the AS number and user-defined number are 0, that is, the RD is 0:0, the MVPN instance is a public network MVPN instance. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. |
| **1** | Displays intra-AS I-PMSI A-D routes. | - |
| **2** | Displays inter-AS I-PMSI A-D routes. | - |
| **3** | Displays S-PMSI A-D routes. | - |
| **5** | Displays Source Active A-D routes. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **6** | Displays information about Shared Tree Join C-multicast routes. | - |
| **7** | Displays information about Source Tree Join C-multicast routes. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *network* | Specifies the type of A-D route.   * Type 1: displays intra-AS I-PMSI A-D routes. * Type 2: displays inter-AS I-PMSI A-D routes. * Type 3: displays S-PMSI A-D routes. * Type 4: displays Leaf A-D routes. * Type 5: displays Source Active A-D routes. * Type 6: displays C-multicast routes. * Type 7: displays C-multicast routes. | Different A-D routes have different values:   * Type 1:The value is the IP address of the source device, in dotted decimal notation. * Type 2:The value is the source AS number. The value is an integer ranging from 1 to 4294967295. * Type 3:The value is in the format of X.X.X.X-Y.Y.Y.Y-Z:Z::Z:Z. X.X.X.X represents the multicast source address in an (S, G) entry, in dotted decimal notation.  Y.Y.Y.Y represents the multicast group address in an (S, G) entry, in dotted decimal notation. The value ranges from 224.0.0.0 to 239.255.255.255.  Z.Z.Z.Z indicates the IP address of the source device, in dotted decimal notation. * Type 4:For the value, see the display bgp mvpn routing-table type 4 route-key-type command. * Type 5:The value is in the format of X.X.X.X:Y.Y.Y.Y. X.X.X.X represents the multicast source address in an (S, G) entry, in dotted decimal notation.  Y.Y.Y.Y represents the multicast group address in an (S, G) entry, in dotted decimal notation. The value ranges from 224.0.0.0 to 239.255.255.255. * Type 6 and Type 7:The value is in the format of AS number:X.X.X.X:Y.Y.Y.Y. AS number: The value is an integer ranging from 1 to 4294967295.  X.X.X.X represents the multicast source address in an (S, G) entry, in hexadecimal.  Y.Y.Y.Y represents the multicast group address in an (S, G) entry, in hexadecimal. The value ranges from 224.0.0.0 to 239.255.255.255.   Different A-D routes have different values(Include IPv6):   * Type 1:The value is the IPv6 address of the source device, in hexadecimal. * Type 2:The value is the source AS number. The value is an integer ranging from 1 to 4294967295. * Type 3:The value is in the format of X.X.X.X-Y.Y.Y.Y-Z:Z::Z:Z. X.X.X.X represents the multicast source address in an (S, G) entry, in dotted decimal notation.  Y.Y.Y.Y represents the multicast group address in an (S, G) entry, in dotted decimal notation. The value ranges from 224.0.0.0 to 239.255.255.255.  Z:Z::Z:Z represents the IPv6 address of the source device, in hexadecimal. * Type 4:For the value, see the display bgp mvpn routing-table type 4 route-key-type command. * Type 5:The value is in the format of X.X.X.X:Y.Y.Y.Y. X.X.X.X represents the multicast source address in an (S, G) entry, in dotted decimal notation.  Y.Y.Y.Y represents the multicast group address in an (S, G) entry, in dotted decimal notation. The value ranges from 224.0.0.0 to 239.255.255.255. * Type 6 and Type 7:The value is in the format of AS number:X.X.X.X:Y.Y.Y.Y. AS number: The value is an integer ranging from 1 to 4294967295.  X.X.X.X represents the multicast source address in an (S, G) entry, in hexadecimal.  Y.Y.Y.Y represents the multicast group address in an (S, G) entry, in hexadecimal. The value ranges from 224.0.0.0 to 239.255.255.255. |
| **vpn-instance** *vpn-instance-name* | Displays statistics about the BGP routes with the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **peer** *ipv4-address* | Displays the routes of the specified BGP peer. | The value is in dotted decimal notation. |
| **advertised-routes** | Displays the routes advertised to the specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view BGP MVPN routes, run the display bgp mvpn routing-table type command. You can specify different parameters to view the specific routing information.When BGP MVPN routing table is displayed, if the length of the destination address mask of an IPv4 route is the same as that of its natural mask, the mask length is not displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display intra-AS I-PMSI A-D routes of the VPN instance VPNA.
```
<HUAWEI> display bgp mvpn vpn-instance VPNA routing-table type 1
 BGP Local router ID is 10.2.3.4
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total number of routes of IPv4-MVPN-family for vpn-instance VPNA: 3
        Network(Originator IP Addr)                             NextHop
 *>     10.2.2.2                                                 10.0.0.0
 *>i    10.3.3.3                                                 10.3.3.3
 *>i    10.4.4.4                                                 10.4.4.4

```

# Display statistics about Intra-AS I-PMSI A-D MSID routes with the source IP address 2001:db8:1::1 on an NG.
```
<HUAWEI> display bgp mvpn all routing-table type 1 2001:db8:1::1

BGP local router ID : 10.84.173.212
Local AS number : 100
Total routes of Route Distinguisher(100:1): 1
BGP routing table entry information of 2001:db8:1::1
From: 2001:db8:1::4 (10.1.1.2)
Route Duration: 0d01h44m00s
Relay IP Nexthop: ::
Relay IP Out-Interface:
Original nexthop: 2001:db8:1::2
Qos information : 0x0
Ext-Community: RT <1 : 1>
Multicast Service Identifier: 2001:db8:1::2, Prefix Len: 80, MSID Len: 16
As-path Nil, origin incomplete, MED 0, localpref 100,pref-val 0, valid, internal, best, select, pre 255
Route Type: 1 (Intra-AS I-PMSI AD Route)
Originator IP: 2001:db8:1::1
PMSI: Flags 0x1, Label 0:0:0(0), subdomain ID: 0, BFR prefix:  2001:db8:1::10
Not advertised to any peer yet 

Total number of routes of IPv4-MVPN-family for vpn-instance vpn1: 1
BGP routing table entry information of 2001:db8:1::1
From: 2001:db8:1::4 (10.1.1.2)
Route Duration: 0d07h39m23s
Original nexthop: 2001:db8:1::2
Qos information : 0x0
Ext-Community: RT <1 : 1>
Multicast Service Identifier: 2001:db8:1::2, Prefix Len: 80, MSID Len: 16
As-path Nil, origin incomplete, MED 0, localpref 100,pref-val 0, valid, internal, best, select, pre 255
Route Type: 1 (Intra-AS I-PMSI AD Route)
Originator IP: 2001:db8:1::1
PMSI: Flags 0x1, Label 0:0:0(0), subdomain ID: 0, BFR prefix:  2001:db8:1::10
Not advertised to any peer yet

```

# Display intra-AS I-PMSI A-D routes (including IPv6) of the VPN instance vrf1.
```
<HUAWEI> display bgp mvpn vpn-instance vrf1 routing-table type 1
 
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete


 Total number of routes of IPv4-MVPN-family for vpn-instance vrf1: 2
        Network(Originator IP Addr)                                       NextHop
 *>     10.1.1.1                                                           10.0.0.0             
 *>i    2001:db8:1::3                                                              2001:db8:1::3

```

# Display Intra-AS I-PMSI A-D route statistics of VPN instance ng with the source IP address 10.1.1.2.
```
<HUAWEI> display bgp mvpn vpn-instance ng routing-table type 1 10.1.1.2
BGP local router ID : 10.1.1.4
 Local AS number : 100
 BGP routing table entry information of 10.1.1.2:
 Route Distinguisher: 100:1
 Remote-Cross route
 From: 10.1.1.2 (10.1.1.2) 
 Route Duration: 0d00h00m12s
 Original nexthop: 10.1.1.2
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
 Route Type: 1 (Intra-AS I-PMSI AD Route)
 Originator IP: 10.1.1.2
 PMSI: Flags 0x0,RSVP-TE P2MP LSP, Label 0:0:0(0), P2MP ID: 0x63000002, Tunnel ID: 49153, Extended tunnel ID: 10.1.1.2
 Not advertised to any peer yet

```

# Display statistics about Intra-AS I-PMSI A-D routes with the source IP address 2001:db8:1::3 in the VPN instance named ng.
```
<HUAWEI> display bgp mvpn vpn-instance vrf1 routing-table type 1 2001:db8:1::3


 BGP local router ID : 10.1.1.1
 Local AS number : 100
 BGP routing table entry information of 2001:db8:1::3:
 Route Distinguisher: 1:1
 Remote-Cross route
 From: 2001:db8:1::2 (10.2.2.2) 
 Route Duration: 0d01h30m02s
 Original nexthop: 2001:db8:1::3
 Qos information : 0x0
 Ext-Community: RT <1 : 1>
 Prefix-sid: SRC-DT4 2001:db8:1::10
 AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
 Originator: 10.3.3.3
 Route Type: 1 (Intra-AS I-PMSI AD Route)
 Originator IP: 2001:db8:1::3
 PMSI: Flags 0x1, Label 0:0:0(0), subdomain ID: 0, BFR ID: 1, BFR prefix: 2001:db8:1::3
 Cluster list: 10.2.2.2
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp mvpn routing-table type** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local BGP device, in the same format as an IPv4 address. |
| BGP routing table entry information of | Indicates that the following information is about routing entries. |
| Local AS number | Local AS number. |
| best | Optimal route. |
| NextHop | Next hop address of a packet. |
| local | Local route. |
| Route Distinguisher | Route distinguisher (RD). |
| Route Duration | Duration for route advertisement. |
| Route Type | Route type. |
| Relay IP Nexthop | Next hop of IP recursion. |
| Original nexthop | Original next hop IP address. |
| Qos information | QoS information. |
| Multicast Service Identifier | Multicast service identifier. |
| origin incomplete | Origin:   * IGP: The Origin attribute of the routes that are added to the BGP routing table by using the network (BGP) command is IGP. * EGP: indicates that the Origin attribute of the routes obtained through EGP is EGP. * Incomplete: The origin of the route cannot be identified. The origin property of the routes that are added to the BGP routing table by using the import-route (BGP) command is Incomplete. |
| MED | MED value of a route. |
| pre 255 | The preference of the BGP route is 255. |
| Originator IP | Source IP address. |
| Originator | Router ID of the route originator. |
| Not advertised to any peer yet | The BGP route has not been advertised to any peer yet. |
| AS-path Nil | AS\_Path attribute (Nil indicates that the attribute value is null.). |
| pref-val | PrefVal of a route. |
| Cluster list | Cluster list. |
| Network | Network address or AS number in the BGP routing table. |
| From | IP address of the device that sends the route. |
| valid | The route is a valid route. |
| select | Selected route. |
| PMSI | In NG MVPNs, the logical channel that carries VPN multicast services on the public network is called a P-Multicast Service Interface (PMSI) tunnel:   * Flags: flag bit. * RSVP-TE P2MP LSP: P2MP tunnel created using RSVP-TE. * Label: label of a PMSI tunnel. * P2MP ID: P2MP ID of a P2MP tunnel. * Tunnel ID: ID of a P2MP tunnel. * Extended tunnel ID: extended ID of a P2MP tunnel. |
| Prefix-sid | Prefix SID. |
| Ext-Community | Extended community attribute. |