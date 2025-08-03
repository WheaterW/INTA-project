display bgp evpn routing-table(prefix)
======================================

display bgp evpn routing-table(prefix)

Function
--------



The **display bgp evpn routing-table** command displays information about BGP EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn all routing-table** [ **peer** *ip-address* { **advertised-routes** | **received-routes** } ] { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix*

**display bgp evpn route-distinguisher** *route-distinguisher* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix*

**display bgp** [ **instance** *instance-name* ] **evpn** **all** **routing-table** [ **peer** *ip-address* { **advertised-routes** | **received-routes** } ] { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix*

**display bgp** [ **instance** *instance-name* ] **evpn** **route-distinguisher** *route-distinguisher* **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix*

**display bgp** [ **instance** *instance-name* ] **evpn** **all** **routing-table** **peer** *ipv6-address* { **advertised-routes** | **received-routes** } { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** | Specifies the EVPN peer. | - |
| *ip-address* | Specifies a peer IPv4 address. | The value is in dotted decimal notation. |
| **advertised-routes** | Displays the routes advertised to the peer. | - |
| **received-routes** | Displays the routes received by the peer. | - |
| **ad-route** | Displays information about all Ethernet auto-discovery routes. | - |
| **es-route** | Displays information about Ethernet segment routes. | - |
| **inclusive-route** | Displays information about inclusive multicast routes. | - |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| **prefix-route** | Displays information about prefix routes. | - |
| *prefix* | Specifies the prefix of an EVPN route. | An EVPN route prefix has the following formats:  Inclusive multicast route. The value is in the format of M:L:X.X.X.X, where:   * M is fixed at 0. * X.X.X.X indicates the source address configured for the device originating the route. * L indicates the mask length of the source address configured for the device originating the route.   MAC advertisement route. The value is in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X], where:   * E indicates the ID of the VLAN to which the MAC address belongs. * M is fixed at 48, indicating the length of the MAC address. * H-H-H indicates the MAC address. The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H contains 1 to 4 digits, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with 0s. For example, e0 is displayed as 00e0. * L is fixed at 0, indicating the mask length of the IP address corresponding to the MAC address. * X.X.X.X indicates the IP address corresponding to the MAC address. Currently, this part can only be displayed as 0.0.0.0. * X:X::X:X indicates the IPv6 address corresponding to the MAC address.   IP prefix route. The value is in the format of L:X.X.X.X:M or L:[X:X::X:X]:M, where:   * L is fixed at 0. * X.X.X.X indicates the IP address of host routes. * M indicates the mask length of host routes. * X:X::X:X indicates the IPv6 address of host routes. |
| **all** | Displays information about EVPN routes of all EVPN instances. | - |
| **route-distinguisher** *route-distinguisher* | Displays information about EVPN routes with the specified RD. | An RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535. The user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. That is, an RD cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. The user-defined number also ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. That is, an RD cannot be 0.0:0. * 32-bit IP address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255. The user-defined number ranges from 0 to 65535. |
| **instance** *instance-name* | Displays information about EVPN routes of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| *ipv6-address* | Specifies a peer IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can view only specific routing information by specifying different parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the Ethernet auto-discovery route with the prefix 0000.1111.2222.3333.4444:0.
```
<HUAWEI> display bgp evpn all routing-table ad-route 0000.1111.2222.3333.4444:0


 BGP local router ID : 172.16.1.1
 Local AS number : 100
 Total routes of Route Distinguisher(3:3): 1
 BGP routing table entry information of 0000.1111.2222.3333.4444:0:
 Label information (Received/Applied): 48066/NULL
 From: 10.1.1.1 (10.1.1.1) 
 Route Duration: 0d01h15m42s
 Relay IP Nexthop: 192.168.1.1
 Relay IP Out-Interface: 10GE1/0/1
 Relay Tunnel Out-Interface: 100GE1/0/1
 Original nexthop: 10.1.1.1
 Qos information : 0x0
 Ext-Community: RT <1 : 1>, RT <3 : 3>, SoO <10.1.1.1 : 0>
 AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
 Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
 ESI: 0000.1111.2222.3333.4444, Ethernet Tag ID: 0
 Not advertised to any peer yet
 
    

 EVPN-Instance evpnb:
 Number of A-D Routes: 1
 BGP routing table entry information of 0000.1111.2222.3333.4444:0:
 Route Distinguisher: 3:3
 Remote-Cross route
 Label information (Received/Applied): 48066/NULL
 From: 10.1.1.1 (10.1.1.1) 
 Route Duration: 0d01h15m43s
 Relay Tunnel Out-Interface: 100GE1/0/1
 Original nexthop: 10.1.1.1
 Qos information : 0x0
 Ext-Community: RT <1 : 1>, RT <3 : 3>, SoO <10.1.1.1 : 0>
 AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
 Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
 ESI: 0000.1111.2222.3333.4444, Ethernet Tag ID: 0
 Not advertised to any peer yet

```

# Display ES routes with the prefix 0000.1111.2222.3333.4444.
```
<HUAWEI> display bgp evpn all routing-table es-route 0000.1111.2222.3333.4444


 BGP local router ID : 2.2.2.1
 Local AS number : 100
 Total routes of Route Distinguisher(2.2.2.1:0): 1
 BGP routing table entry information of 0000.1111.2222.3333.4444:32:2.2.2.1:
 From: 0.0.0.0 (0.0.0.0) 
 Route Duration: 1d02h09m05s
 Direct Out-interface: NULL0
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 Ext-Community: SoO <2.2.2.1 : 0>, RT <0011-1122-2233>, DF Election <0 : 0 : 0>
 AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
 Route Type: 4 (Ethernet Segment Route)
 ESI: 0000.1111.2222.3333.4444, Originating IP:2.2.2.1/32
 Advertised to such 1 peers:
    1.1.1.1

    

 EVPN-Instance evpnb:
 Number of ES Routes: 1
 BGP routing table entry information of 0000.1111.2222.3333.4444:32:2.2.2.1:
 Route Distinguisher: 2.2.2.1:0
 Local-Cross route
 Route Duration: 1d02h09m06s
 Relay IP Nexthop: 0.0.0.0
 Relay IP Out-Interface: NULL0
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 Ext-Community: SoO <2.2.2.1 : 0>, RT <0011-1122-2233>, DF Election <0 : 0 : 0>
 AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
 Route Type: 4 (Ethernet Segment Route)
 ESI: 0000.1111.2222.3333.4444, Originating IP:2.2.2.1/32
 Not advertised to any peer yet

```

# Display information about inclusive multicast routes with the prefix 0:32:1.1.1.1.
```
<HUAWEI> display bgp evpn all routing-table inclusive-route 0:32:1.1.1.1


 BGP local router ID : 1.1.1.1
 Local AS number : 100
 Total routes of Route Distinguisher(3:3): 1
 BGP routing table entry information of 0:32:1.1.1.1:
 From: 0.0.0.0 (0.0.0.0) 
 Route Duration: 0d00h00m10s
 Direct Out-interface: NULL0
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 Ext-Community: RT <1 : 1>, RT <3 : 3>, SoO <1.1.1.1 : 0>
 AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
 PMSI: Flags 0, Ingress Replication, Label 0:0:0(0), Tunnel Identifier:1.1.1.1
 Route Type: 3 (Inclusive Multicast Route)
 Ethernet Tag ID: 0, Originator IP:1.1.1.1/32
 Advertised to such 1 peers:
    2.2.2.1
    

 EVPN-Instance evpnb:
 Number of Inclusive Multicast Routes: 1
 BGP routing table entry information of 0:32:1.1.1.1:
 Route Distinguisher: 3:3
 From: 0.0.0.0 (0.0.0.0) 
 Route Duration: 1d02h03m11s
 Relay IP Nexthop: 0.0.0.0
 Relay IP Out-Interface: NULL0
 Original nexthop: 127.0.0.1
 Qos information : 0x0
 AS-path Nil, origin incomplete, pref-val 0, valid, local, best, select, pre 255
 PMSI: Flags 0, Ingress Replication, Label 0:0:0(0), Tunnel Identifier:1.1.1.1
 Route Type: 3 (Inclusive Multicast Route)
 Ethernet Tag ID: 0, Originator IP:1.1.1.1/32
 Not advertised to any peer yet

```

# Display information about all EVPN routes.
```
<HUAWEI> display bgp evpn all routing-table
 Local AS number : 100

 BGP Local router ID is 1.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete


 EVPN address family:
 Number of A-D Routes: 1

 Route Distinguisher: 1:1
       Network(ESI/EthTagId)                                  NextHop
 *>    0010.1010.1010.1010.1010:0                             127.0.0.1       
   

 EVPN-Instance c1:
 Number of A-D Routes: 1
       Network(ESI/EthTagId)                                  NextHop
 *>    0010.1010.1010.1010.1010:0                             127.0.0.1      

 EVPN address family:
 Number of Inclusive Multicast Routes: 1

 Route Distinguisher: 1:1
       Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
 *>    0:32:1.1.1.1                                           127.0.0.1       
   

 EVPN-Instance c1:
 Number of Inclusive Multicast Routes: 1
       Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
 *>    0:32:1.1.1.1                                           127.0.0.1      

 EVPN address family:
 Number of ES Routes: 1

 Route Distinguisher: 1.1.1.1:0
       Network(ESI/IpAddrLen/OriginalIp)                                          NextHop
 *>    0010.1010.1010.1010.1010:32:1.1.1.1                               127.0.0.1       
   

 EVPN-Instance c1:
 Number of ES Routes: 1
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>    0010.1010.1010.1010.1010:32:1.1.1.1                               127.0.0.1

```

# Display information about the IP prefix route with the prefix 0:10.1.1.0:24.
```
<HUAWEI> display bgp evpn all routing-table prefix-route 0:10.1.1.0:24
 BGP local router ID : 10.0.12.2
 Local AS number : 100
 Total routes of Route Distinguisher(1:1): 1
 BGP routing table entry information of 0:10.1.1.0:24:
 Label information (Received/Applied): 1/NULL
 From: 0.0.0.0 (0.0.0.0) 
 Route Duration: 0d00h15m16s
 Direct Out-interface: LoopBack10 
 Original nexthop: 10.56.21.29
 Effective nexthop: 192.168.1.1
 Qos information : 0
 Ext-Community: RT <1 : 1>, Tunnel Type <VxLan>, Router's MAC <00e0-fc12-3456>
 AS-path Nil, origin igp, MED 0, pref-val 0, valid, local, best, select, pre 255
 Received path-id: 0
 Route Type: 5 (Ip Prefix Route)
 Ethernet Tag ID: 0, IP Prefix/Len: 10.1.1.0/24, ESI: 0000.0000.0000.0000.0000, GW IP Address: 0.0.0.0
 Advertised to such 1 peers:
    10.1.1.1

```

**Table 1** Description of the **display bgp evpn routing-table(prefix)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | Router ID of the local device. |
| BGP routing table entry information of | Routing entry information. |
| local | Local route. |
| Local AS number | Local AS number. |
| Total routes of Route Distinguisher | Total number of EVPN routes with a specified RD. |
| Route Distinguisher | RD of the EVPN routes. |
| Route Duration | Duration for route advertisement. |
| Route Type | EVPN route type:   * Ethernet auto-discovery route. * MAC advertisement route. * Inclusive multicast route. * Ethernet segment route. * IP prefix route. |
| Label information (Received/Applied) | Label information (received label/advertised label). |
| Label 0:0:0(0) | MPLS label value. 0:0:0 is a fixed value and is not used currently. (0) indicates the label value of BUM traffic. |
| Relay IP Nexthop | IP recursive next hop. |
| Relay Tunnel Out-Interface | Outbound interface of the recursive tunnel. |
| Tunnel Type | Tunnel type. |
| Tunnel Identifier | Tunnel ID, which is the source address of the current node. |
| Original nexthop | Original next hop IP address. |
| Qos Information | QoS information. |
| SoO | SoO extended community attribute. |
| AS-path | AS\_Path attribute (Nil indicates that the attribute value is null.). |
| origin | Origin attribute of a BGP route. |
| origin incomplete | Other attribute. |
| pref-val | Preferred value. |
| pre | The priority of the route. |
| IGP cost | IGP cost. |
| Ethernet Tag ID | Configured VLAN ID. The current value is always 0. |
| Not advertised to any peer yet | Route that is not advertised to any EVPN peer. |
| EVPN-Instance | EVPN instance name. |
| Number of A-D Routes | Number of Ethernet auto-discovery routes. |
| Number of Inclusive Multicast Routes | Number of inclusive multicast routes. |
| Number of ES Routes | Number of Ethernet segment routes. |
| Remote-Cross route | Route received from a peer and leaked into an EVPN instance. |
| best | Optimal route. |
| EVPN address family | EVPN address family. |
| NextHop | Next hop address. |
| MED | MED value of route. |
| GW IP Address | Gateway IP address. |
| Direct Out-interface | Directly connected interface. |
| DF Election | Extended community attribute of DF election. |
| Originating IP | IP address of the device that has originated routes. |
| Advertised to such 1 peers | Peers to which routes are advertised. |
| Local-Cross route | Locally leaked routes. |
| Flags 0 | Whether the current node is a leaf node. Currently, the value can only be 0. |
| Ingress Replication | BUM traffic is forwarded in ingress replication mode. |
| Originator | IP address of the device that has originated routes. |
| Effective nexthop | Actual next hop of the IP prefix route. |
| Router's MAC | MAC address received from an EVPN peer. |
| Received path-id | ID of the receive path. |
| Network | Reachable address. |
| ESI | ID of an Ethernet link network segment. |
| EthTagId | VLAN ID. |
| IpAddrLen | Mask length. |
| OriginalIp | Source IP address. |
| From | IP address of the device that sends the route. |
| Ext-Community | BGP EVPN extended community attribute. |
| valid | Valid route. |
| select | Local AS number. |
| PMSI | Provider Multicast Service Interface (PMSI) tunnel information. |