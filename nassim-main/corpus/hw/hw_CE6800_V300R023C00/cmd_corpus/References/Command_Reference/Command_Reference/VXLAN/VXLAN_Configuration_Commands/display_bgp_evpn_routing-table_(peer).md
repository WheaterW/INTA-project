display bgp evpn routing-table (peer)
=====================================

display bgp evpn routing-table (peer)

Function
--------



The **display bgp evpn routing-table** command displays information about BGP EVPN routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn all routing-table** [ **peer** *ip-address* { **advertised-routes** | **received-routes** } ] { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** }

**display bgp evpn** { **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** }

**display bgp evpn all routing-table** [ **peer** *ip-address* { **advertised-routes** | **received-routes** } ]

**display bgp evpn all routing-table extcommunity** { **rt** *extcommunity* } &<1-33>

**display bgp evpn all routing-table extcommunity** { **rt** *extcommunity* } &<1-33> **match-any**

**display bgp evpn all routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33>

**display bgp evpn all routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33> **match-any**

**display bgp instance** *instance-name* **evpn** **all** **routing-table** **extcommunity** { **rt** *extcommunity* } &<1-33>

**display bgp instance** *instance-name* **evpn** **all** **routing-table** **extcommunity** { **rt** *extcommunity* } &<1-33> **match-any**

**display bgp instance** *instance-name* **evpn** **all** **routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33>

**display bgp instance** *instance-name* **evpn** **all** **routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33> **match-any**

**display bgp evpn** { **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33>

**display bgp evpn** { **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33> **match-any**

**display bgp instance** *instance-name* **evpn** { **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33>

**display bgp instance** *instance-name* **evpn** { **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **inclusive-route** | **mac-route** | **prefix-route** } **extcommunity** { **rt** *extcommunity* } &<1-33> **match-any**

**display bgp instance** *instance-name* **evpn** **all** **routing-table** [ **peer** { *ip-address* | *ipv6-address* } { **advertised-routes** | **received-routes** } ] { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** }

**display bgp instance** *instance-name* **evpn** { **route-distinguisher** *route-distinguisher* } **routing-table** { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** }

**display bgp instance** *instance-name* **evpn** **all** **routing-table** [ **peer** { *ip-address* | *ipv6-address* } { **advertised-routes** | **received-routes** } ]

**display bgp evpn all routing-table peer** *ipv6-address* { **advertised-routes** | **received-routes** } { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** }

**display bgp evpn all routing-table peer** *ipv6-address* { **advertised-routes** | **received-routes** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ip-address* | Specifies a peer IP address. | The value is in dotted decimal notation. |
| **advertised-routes** | Specifies the routes to be advertised to a specified peer. | - |
| **received-routes** | Displays the routes received from the specified peer. | - |
| **ad-route** | Displays information about all Ethernet auto-discovery routes. | - |
| **es-route** | Displays information about Ethernet segment routes. | - |
| **inclusive-route** | Displays information about inclusive multicast routes. | - |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| **prefix-route** | Displays information about prefix routes. | - |
| **all** | Displays EVPN routes of all EVPN instances. | - |
| **route-distinguisher** *route-distinguisher* | Displays information about BGP EVPN routes with a specified RD. | An RD can be in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535. The user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. That is, an RD cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. The user-defined number also ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. That is, an RD cannot be 0.0:0. * 32-bit IP address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255. The user-defined number ranges from 0 to 65535. |
| **extcommunity** | Displays the routes with the specified extended community attribute. | - |
| **rt** *extcommunity* | Specifies the extended community attribute of the VPN-Target type. | The options are as follows:   * as-number:nn * 4as-number:nn * ipv4-address:nn   as-number specifies the AS number. The value is an integer that ranges from 0 to 65535.  4as-number is a 4-byte AS number, which can be:   * The value is an integer that ranges from 65536 to 4294967295. * The value is in the format of x.y, where x and y are integers ranging from 0 to 65535.   ipv4-address is an IPv4 address in dotted decimal notation. nn is an integer. For as-number and 4as-number, the value ranges from 0 to 4294967295. For ipv4-address, the value ranges from 0 to 65535. |
| **match-any** | Displays information about the routes that match any of the specified extended community attributes. | - |
| **instance** *instance-name* | Displays the routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| *ipv6-address* | Specifies the peer IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about EVPN routes, including active and inactive routes, run the **display bgp evpn routing-table** command.Information about specified EVPN routes can be displayed by specifying different parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the IP prefix route advertised to peers.
```
<HUAWEI> display bgp evpn all routing-table peer 10.1.1.1 advertised-routes prefix-route


 Local AS number : 100

 BGP Local router ID is 10.2.2.2
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete

 
 EVPN address family:
 Number of Ip Prefix Routes: 1
 Route Distinguisher: 1:1
       Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
 *>    0:10.22.22.22:32                                       10.2.2.2

```

# Display the information of EVPN routes in specified BGP multi-instance.
```
<HUAWEI> display bgp instance p1 evpn all routing-table
 Local AS number : 100
 BGP Local router ID is 10.1.1.1
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
 *>    0:32:10.1.1.1                                           127.0.0.1       
 EVPN-Instance c1:
 Number of Inclusive Multicast Routes: 1
       Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
 *>    0:32:10.1.1.1                                           127.0.0.1      
 EVPN address family:
 Number of ES Routes: 1
 Route Distinguisher: 10.1.1.1:0
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>    0010.1010.1010.1010.1010:32:10.1.1.1                               127.0.0.1       
 EVPN-Instance c1:
 Number of ES Routes: 1
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>    0010.1010.1010.1010.1010:32:10.1.1.1                               127.0.0.1       
<HUAWEI> display bgp instance p1 evpn all routing-table statistics
 Total number of routes from all PE: 6
 Number of A-D Routes: 2
 Number of Mac Routes: 0
 Number of Inclusive Multicast Routes: 2
 Number of ES Routes: 2
<HUAWEI> display bgp instance p1 evpn all routing-table es-route
 Local AS number : 100
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 EVPN address family:
 Number of ES Routes: 3
 Route Distinguisher: 10.1.1.1:0
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>    0010.1010.1010.1010.1010:32:10.1.1.1                               127.0.0.1      
 Route Distinguisher: 10.2.2.2:0
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>i   0010.1010.1010.1010.1010:32:10.2.2.2                               10.2.2.2        
 Route Distinguisher: 10.3.3.3:0
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>i   0010.1010.1010.1010.1010:32:10.3.3.3                               10.3.3.3         
 EVPN-Instance c1:
 Number of ES Routes: 3
       Network(ESI/IpAddrLen/OriginalIp)                                           NextHop
 *>    0010.1010.1010.1010.1010:32:10.1.1.1                               127.0.0.1       
 *>    0010.1010.1010.1010.1010:32:10.2.2.2                                                          10.2.2.2         
 *>    0010.1010.1010.1010.1010:32:10.3.3.3                              10.3.3.3         
<HUAWEI> display bgp instance p1 evpn all routing-table ad-route
 Local AS number : 100
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 EVPN address family:
 Number of A-D Routes: 6
 Route Distinguisher: 1:1
       Network(ESI/EthTagId)                                  NextHop
 *>    0010.1010.1010.1010.1010:0                             127.0.0.1      
 Route Distinguisher: 2:2
       Network(ESI/EthTagId)                                  NextHop
 *>i   0010.1010.1010.1010.1010:0                             10.2.2.2        
 Route Distinguisher: 3:3
       Network(ESI/EthTagId)                                  NextHop
 *>i   0010.1010.1010.1010.1010:0                             10.3.3.3        
 Route Distinguisher: 10.1.1.1:0
       Network(ESI/EthTagId)                                  NextHop
 *>    0010.1010.1010.1010.1010:4294967295                    127.0.0.1      
 Route Distinguisher: 10.2.2.2:0
       Network(ESI/EthTagId)                                  NextHop
 *>i   0010.1010.1010.1010.1010:4294967295                    10.2.2.2        
 Route Distinguisher: 10.3.3.3:0
       Network(ESI/EthTagId)                                  NextHop
 *>i   0010.1010.1010.1010.1010:4294967295                    10.3.3.3         
 EVPN-Instance c1:
 Number of A-D Routes: 5
       Network(ESI/EthTagId)                                  NextHop
 *>    0010.1010.1010.1010.1010:0                             127.0.0.1       
 * i                                                          10.2.2.2         
 * i                                                          10.3.3.3         
 *>i   0010.1010.1010.1010.1010:4294967295                    10.2.2.2         
 * i                                                          10.3.3.3

```

**Table 1** Description of the **display bgp evpn routing-table (peer)** command output
| Item | Description |
| --- | --- |
| Local AS number | Local AS number. |
| BGP Local router ID | Router ID of the local device. |
| BGP routing table entry information of | Routing entry information. |
| best | Optimal route. |
| EVPN address family | EVPN address family. |
| Number of A-D Routes | Number of A-D routes. |
| Number of Inclusive Multicast Routes | Number of inclusive multicast routes. |
| Number of ES Routes | Number of ES routes. |
| Number of Mac Routes | Number of MAC routes. |
| Number of Ip Prefix Routes | Number of IP prefix routes. |
| Route Duration | Duration for route advertisement. |
| Route Distinguisher | RD of a route. |
| NextHop | Next hop information about routes. |
| EVPN-Instance | EVPN instance name. |
| Total routes of Route Distinguisher | Total number of EVPN routes with a specified RD. |
| Total number of routes from all PE | Total number of routes. |
| From | IP address of the device that sends the route. |
| Original nexthop | Original next hop IP address. |
| Qos information | Qos information. |
| Ext-Community | BGP EVPN extended community attribute. |
| origin | Origin attribute of a BGP route. |
| valid | Valid route. |
| local | Local route. |
| pre | The priority of the route. |
| Advertised to such 1 peers | Peers to which routes are advertised. |
| Direct Out-interface | Directly connected interface. |
| Effective nexthop | Actual next hop of the IP prefix route. |
| Advertised nexthop | Next hop to which the IP prefix route is re-iterated after being sent. |
| Sent path-id | ID of the transmit path. |
| Label information (Received/Applied) | Label information (received label/advertised label). |
| Tunnel Type | Tunnel type. |
| Router's MAC | MAC address received from an EVPN peer. |
| GW IP Address | Gateway IP address. |
| MED | MED value of a route. |
| Ethernet Tag ID | Configured VLAN ID. The current value is always 0. |
| IP Prefix/Len | IP prefix address and its length. |
| ESI | ID of an Ethernet link network segment. |
| localpref | Local preference. |
| Network | Network information of the route. |