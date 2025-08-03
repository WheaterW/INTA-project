display bgp vpnv6 vpn-instance routing-table
============================================

display bgp vpnv6 vpn-instance routing-table

Function
--------



The **display bgp vpnv6 vpn-instance routing-table** command displays BGP VPNv6 routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **routing-table** [ **peer** *ipv6-address* { **received-routes** | **advertised-routes** } ] **time-range** *start-time* *end-time*

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **time-range** *start-time* *end-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-distinguisher** *route-distinguisher* | Specifies the remote RD. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |
| **peer** | Peer routers. | - |
| *ipv6-address* | Specify an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **received-routes** | Routes received from the remote peer. | - |
| **advertised-routes** | Routes advertised to the remote peer. | - |
| **time-range** *start-time* | Starting time. | The formats is xxdxxhxxmxxs.   * The d indicates days. The value is an integer ranging from 0 to 10000. * The h indicates hours. The value is an integer ranging from 0 to 23. * The m indicates minutes. The value is an integer ranging from 0 to 59. * The s indicates seconds. The value is an integer ranging from 0 to 59. |
| **time-range** *end-time* | Ending time. | The formats is xxdxxhxxmxxs.   * The d indicates days. The value is an integer ranging from 0 to 10000. * The h indicates hours. The value is an integer ranging from 0 to 23. * The m indicates minutes. The value is an integer ranging from 0 to 59. * The s indicates seconds. The value is an integer ranging from 0 to 59. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 vpn-instance routing-table** command displays BGP VPNv6 routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all BGP VPNv6 routes.
```
<HUAWEI> display bgp vpnv6 all routing-table
BGP Local router ID is 192.168.7.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 Total number of routes from all PE: 3
 Route Distinguisher: 100:1


 *>  Network  : 2001:DB8:1::1                            PrefixLen : 128
     NextHop  : ::                                       LocPrf    :
     MED      : 0                                        PrefVal   : 0
     Label    : 
     Path/Ogn : ?

 Route Distinguisher: 200:1


 *>i Network  : 2001:DB8:1::1                            PrefixLen : 128
     NextHop  : ::FFFF:192.168.100.10                    LocPrf    : 100
     MED      : 0                                        PrefVal   : 0
     Label    : 15362
     Path/Ogn : 33 55 ?
 *>i Network  : 2001:DB8:2::2                            PrefixLen : 128
     NextHop  : ::FFFF:192.168.100.10                    LocPrf    : 100
     MED      : 0                                        PrefVal   : 0
     Label    : 15363
     Path/Ogn : 33 55 ?

 Total routes of vpn-instance vrf1: 3
 *>  Network  : 2001:DB8:1::1                            PrefixLen : 128
     NextHop  : ::                                       LocPrf    :
     MED      : 0                                        PrefVal   : 0
     Label    : 
     Path/Ogn : ?
 * i
     NextHop  : ::FFFF:192.168.100.10                    LocPrf    : 100
     MED      : 0                                        PrefVal   : 0
     Label    : 15362
     Path/Ogn : 33 55 ?
 *>i Network  : 2001:DB8:2::2                            PrefixLen : 128
     NextHop  : ::FFFF:192.168.100.10                    LocPrf    : 100
     MED      : 0                                        PrefVal   : 0
     Label    : 15363
     Path/Ogn : 33 55 ?

```

# Display the routes of an IPv6 address family-enabled VPN instance named vpn1 on the local device.
```
<HUAWEI> display bgp vpnv6 vpn-instance vpn1 routing-table
Total Number of Routes: 5

 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 *>  Network  : 2001:DB8:2000::                          PrefixLen : 64
     NextHop  : ::                                       LocPrf    :
     MED      : 0                                        PrefVal   : 0
     Label    : 15360/NULL
     Path/Ogn : ?

 *>  Network  : 2001:DB8:2000::1                         PrefixLen : 128
     NextHop  : ::                                       LocPrf    :
     MED      : 0                                        PrefVal   : 0
     Label    :
     Path/Ogn : ?

 *>i Network  : 2001:DB8:2001::                          PrefixLen : 64
     NextHop  : ::FFFF:10.2.2.2                          LocPrf    : 100
     MED      : 0                                        PrefVal   : 0
     Label    : NULL/15360
     Path/Ogn : ?

 *>i Network  : 2001:DB8:3000::1                         PrefixLen : 128
     NextHop  : ::FFFF:10.2.2.2                          LocPrf    : 100
     MED      : 0                                        PrefVal   : 0
     Label    : NULL/15361
     Path/Ogn : 65420 ?

 *>  Network  : FE80::                                   PrefixLen : 10
     NextHop  : ::                                       LocPrf    :
     MED      : 0                                        PrefVal   : 0
     Label    :
     Path/Ogn : ?

```

**Table 1** Description of the **display bgp vpnv6 vpn-instance routing-table** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | ID of the local BGP device. The ID is in the same format as an IPv4 address. |
| Total Number of Routes | Total number of routes. |
| Total number of routes from all PE | Number of VPNv4 routes. |
| Route Distinguisher | Specified RD. |
| Network | Destination network or host address of the route. |
| PrefixLen | Prefix length of the destination network or host address of the route. |
| NextHop | IPv6 address of the next hop. |
| LocPrf | Local\_Pref of a BGP route. The default value is 100. |
| MED | MED of a route. The default value is 0. |
| PrefVal | PrefVal of a route. |
| Label | Label carried by the data packet destined for the destination network or host address of the route. |
| Path/Ogn | AS\_Path number and the Origin attribute of the route. |