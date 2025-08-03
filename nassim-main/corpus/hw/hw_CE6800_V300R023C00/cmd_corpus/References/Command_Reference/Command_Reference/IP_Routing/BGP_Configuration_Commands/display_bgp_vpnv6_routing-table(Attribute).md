display bgp vpnv6 routing-table(Attribute)
==========================================

display bgp vpnv6 routing-table(Attribute)

Function
--------



The **display bgp vpnv6 routing-table** command displays information about BGP VPNv6 routes and BGP4+ VPN routes based on specified multiple attribute values.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table**

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **regular-expression** *strRegular*

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33> [ **match-any** ]

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table**

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **regular-expression** *strRegular*

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33> [ **match-any** ]

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv6 routes and BGP4+ routes of VPN instances. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Displays about the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **community** *communityNum* | Specifies a community number. | The value is an integer that ranges from 0 to 4294967295. |
| **community** *strCommunityNum* | Specifies a community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP routes carrying the internet community attribute. | - |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **extcommunity** | Displays information about the routes with a specified extended community attribute. | - |
| **rt** | Displays information about the routes with the route target (RT) extended community attribute. | - |
| **soo** | Displays information about BGP routes with the source of origin (SoO) extended community attribute. | - |
| *strExtCommunity* | Specifies an extended community attribute value. | The attribute value can be expressed in one of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number cannot both be set to 0. That is, the SoO must not be 0:0. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. The AS number and user-defined number must not be both 0s. That is, the SoO must not be 0.0:0. |
| **match-any** | Displays information about BGP routes with any of the specified extended community attributes. | - |
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

To query information about BGP VPNv6 routes and BGP4+ VPN routes based on specified multiple attribute values, run this command. Multiple attribute values can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP multi-instance VPNv6 routes that match the AS\_Path regular expression ^20.
```
<HUAWEI> display bgp instance a vpnv6 all routing-table regular-expression ^20
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 
 Total number of routes from all PE: 1

 Route Distinguisher: 11:11


 *>     Network  : 2001:DB8:1::                             PrefixLen : 128 
        NextHop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 200 999i
    
 VPN-Instance vpna, Router ID 10.1.123.1:

 Total Number of Routes: 1
 *>     Network  : 2001:DB8:1::                             PrefixLen : 128 
        NextHop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 200 999i

```

**Table 1** Description of the **display bgp vpnv6 routing-table(Attribute)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total number of routes from all PE | Number of VPNv6 routes. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Network | Network address in the BGP public network routing table. |
| PrefixLen | Prefix length. |
| LocPrf | Local\_Pref. |
| MED | MED of a BGP route. |
| PrefVal | PrefVal. |
| Label | Label value. |
| Path/Ogn | AS\_Path number and the origin attribute. |
| Nexthop | Next hop IP address used to forward packets. |