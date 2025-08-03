display bgp vpnv4 routing-table(Attribute)
==========================================

display bgp vpnv4 routing-table(Attribute)

Function
--------



The **display bgp vpnv4 routing-table** command displays information about BGP VPNv4 routes and BGP VPN routes based on specified multiple attribute values.




Format
------

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table**

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **regular-expression** *strRegular*

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table**

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **regular-expression** *strRegular*

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv4 routes and BGP routes of VPN instances. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Displays about the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **community** *communityNum* | Specifies the community number. | The value is an integer that ranges from 0 to 4294967295. |
| **community** *strCommunityNum* | Specifies the community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP routes carrying the internet community attribute. | - |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community** *largeCommuStr* | Specifies a value of the Large-Community attribute. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **regular-expression** *strRegular* | Specifies the regular expression that matches AS\_Path. | The value is a string of 1 to 80 characters. |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 80 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP VPNv4 routes and BGP VPN routes based on specified multiple attribute values, run this command. Multiple attribute values can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP VPNv4 routes information.
```
<HUAWEI> display bgp vpnv4 all routing-table
 
 BGP Local router ID is 10.3.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 
 Total number of routes from all PE: 7

 Route Distinguisher: 1:1


        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn

 *>     10.1.1.0/24        10.1.123.2                     0                     0      200i
 *>     10.1.2.0/24        10.1.123.2                     0                     0      200i
    
 VPN-Instance vrf, Router ID 10.1.123.1:

 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn

 *>     10.1.1.0/24        10.1.123.2                     0                     0      200i
 *>     10.1.2.0/24        10.1.123.2                     0                     0      200i

```

# Display BGP private network routes with community attribute.
```
<HUAWEI> display bgp vpnv4 vpn-instance vrf routing-table community
 
 BGP Local router ID is 10.3.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

    
 VPN-Instance vrf, Router ID 10.1.123.1:

 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Community

 *>     10.1.1.0/24        10.1.123.2                     0                     0      <1:1>, <2:2>
 *>     10.1.2.0/24        10.1.123.2                     0                     0      <1:1>, <3:3>

```

**Table 1** Description of the **display bgp vpnv4 routing-table(Attribute)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total number of routes from all PE | Number of VPNv4 routes. |
| Total Number of Routes | Total number of routes. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Network | Network address in the BGP public network routing table. |
| NextHop | Next hop IP address used to forward packets. |
| MED | MED of a BGP route. |
| LocPrf | Local\_Pref. |
| PrefVal | PrefVal. |
| Path/Ogn | AS\_Path number and the origin attribute. |
| VPN-Instance | Name of a VPN instance. |
| Community | Community attribute of a route. |