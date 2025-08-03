display bgp vpnv6 routing-table(Attribute Filter)
=================================================

display bgp vpnv6 routing-table(Attribute Filter)

Function
--------



The **display bgp vpnv6 routing-table** command displays information about BGP VPNv6 routes and BGP4+ VPN routes based on specified multiple attribute filters.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **extcommunity-filter** { *basic-extcomm-flt-num* | *adv-extcomm-flt-num* | *extcommunity-filter-name* }

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community-filter** *largeComFilName* [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **extcommunity-filter** { *basic-extcomm-flt-num* | *adv-extcomm-flt-num* | *extcommunity-filter-name* }

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv6 routes and BGP4+ routes of VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays about the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **as-path-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer that ranges from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates exact match with specified large communities. | - |
| **extcommunity-filter** *basic-extcomm-flt-num* | Specifies the number of a basic extended community filter. | The value is an integer ranging from 1 to 199. |
| **extcommunity-filter** *adv-extcomm-flt-num* | Specifies the number of an advanced extcommunity filter. | The value is an integer that ranges from 200 to 399. |
| **extcommunity-filter** *extcommunity-filter-name* | Specifies the name of an extended community filter. | The value is a string of 1 to 51 characters. |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP VPNv6 routes and BGP4+ VPN routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP multi-instance VPNv6 routes that match AS path filter pas.
```
<HUAWEI> display bgp instance a vpnv6 all routing-table as-path-filter pas
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 
 Total number of routes from all PE: 1

 Route Distinguisher: 11:11


 *>     Network  : 2001:DB8:1::                             PrefixLen : 128 
        NextHop  : ::                                       LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 100 999i
    
 VPN-Instance vpna, Router ID 10.1.123.1:

 Total Number of Routes: 1
 *>     Network  : 2001:DB8:1::                             PrefixLen : 128 
        NextHop  : ::                                       LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 100 999i

```

**Table 1** Description of the **display bgp vpnv6 routing-table(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total number of routes from all PE | Number of VPNv6 routes. |
| Network | Network address in the BGP public network routing table. |
| PrefixLen | Prefix length. |
| LocPrf | Local\_Pref. |
| MED | MED of a BGP route. |
| PrefVal | PrefVal. |
| Label | Label value. |
| Path/Ogn | AS\_Path number and the origin attribute. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Nexthop | Next hop IP address used to forward packets. |