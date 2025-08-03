display bgp vpnv4 routing-table(Attribute Filter)
=================================================

display bgp vpnv4 routing-table(Attribute Filter)

Function
--------



The **display bgp vpnv4 routing-table** command displays information about BGP VPNv4 routes and BGP VPN routes based on specified multiple attribute filters.




Format
------

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community-filter** *largeComFilName* [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv4 routes and BGP routes of VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays about the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer that ranges from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP VPNv4 routes and BGP VPN routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP multi-instance VPNv4 routes that match AS path filter pas.
```
<HUAWEI> display bgp instance a vpnv4 all routing-table as-path-filter pas
 
 BGP Local router ID is 10.3.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 
 Total number of routes from all PE: 1

 Route Distinguisher: 11:11


        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn

 *>     10.1.1.0/24        10.2.123.2                     0                     0      200?
    
 VPN-Instance vrf, Router ID 10.3.123.1:

 Total Number of Routes: 0
    
 VPN-Instance vpna, Router ID 10.3.123.1:

 Total Number of Routes: 1
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn

 *>     10.1.1.0/24        10.2.123.2                     0                     0      200?

```

# Display BGP private routes that match large community filter aaa.
```
<HUAWEI> display bgp vpnv4 vpn-instance vrf routing-table large-community-filter aaa
 
 BGP Local router ID is 10.3.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

    
 VPN-Instance vrf, Router ID 10.1.123.1:

 Total Number of Routes: 1
        Network            NextHop                       MED        LocPrf    PrefVal LargeCommunity

 *>     10.1.1.0/24        10.1.123.2                     0                     0      <1:1:1>, <2:2:2>

```

# Display BGP VPNv4 routes that match community filter 10.
```
<HUAWEI> display bgp vpnv4 all routing-table community-filter 10
 
 BGP Local router ID is 10.3.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 
 Total number of routes from all PE: 2

 Route Distinguisher: 1:1


        Network            NextHop                       MED        LocPrf    PrefVal Community

 *>     10.1.1.0/24        10.1.123.2                     0                     0      <1:1>, <2:2>
 *>     10.1.2.0/24        10.1.123.2                     0                     0      <1:1>, <3:3>
    
 VPN-Instance vrf, Router ID 10.1.123.1:

 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Community

 *>     10.1.1.0/24        10.1.123.2                     0                     0      <1:1>, <2:2>
 *>     10.1.2.0/24        10.1.123.2                     0                     0      <1:1>, <3:3>

```

**Table 1** Description of the **display bgp vpnv4 routing-table(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total number of routes from all PE | Number of VPNv4 routes. |
| Total Number of Routes | Total number of routes. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Network | Network address in the BGP public network routing table. |
| NextHop | Next hop IP address used to forward packets. |
| MED | MED of a route. |
| LocPrf | Local\_Pref. |
| PrefVal | PrefVal. |
| Path/Ogn | AS\_Path number and the origin attribute. |
| VPN-Instance | Name of a VPN instance. |
| LargeCommunity | LargeCommunity attribute of a route. |
| Community | Community attribute of a route. |