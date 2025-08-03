display bgp ipv6 routing-table(Attribute Filter)
================================================

display bgp ipv6 routing-table(Attribute Filter)

Function
--------



The **display bgp ipv6 routing-table** command displays information about BGP4+ public network routes based on specified multiple attribute filters.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp ipv6 routing-table community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp ipv6 routing-table large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer that ranges from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP4+ public network routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP4+ routes that match the AS\_Path filter pas.
```
<HUAWEI> display bgp ipv6 routing-table as-path-filter pas
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
 *>     Network  : 2001:DB8:1::                             PrefixLen : 64  
        NextHop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 200i
 *>     Network  : 2001:DB8:2::                             PrefixLen : 64  
        NextHop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 200i

```

# Display the BGP4+ routes that match the Large-Community attribute filter aaa.
```
<HUAWEI> display bgp ipv6 routing-table large-community-filter aaa
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
 *>     Network  : 2001:DB8:1::                             PrefixLen : 64  
        Nexthop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Large-Community : <1:1:1>, <2:2:2>
 *>     Network  : 2001:DB8:2::                             PrefixLen : 64  
        Nexthop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Large-Community : <1:1:1>, <2:2:2>

```

# Display the BGP4+ routes that match community filter 10.
```
<HUAWEI> display bgp ipv6 routing-table community-filter 10
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 1
 *>     Network  : 2001:DB8:2::                             PrefixLen : 64  
        Nexthop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Community : <1:1>, <3:3>

```

**Table 1** Description of the **display bgp ipv6 routing-table(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total Number of Routes | Total number of routes. |
| Network | Network address in the BGP public network routing table. |
| PrefixLen | Prefix length. |
| LocPrf | Local\_Pref. |
| MED | MED of a BGP route. |
| PrefVal | PrefVal. |
| Label | Label value. |
| Path/Ogn | AS\_Path number and the origin attribute. |
| Nexthop | Next hop IP address used to forward packets. |
| Large-Community | LargeCommunity attribute of a route. |
| Community | Community attribute of a route. |