display bgp ipv6 routing-table (Attribute)
==========================================

display bgp ipv6 routing-table (Attribute)

Function
--------



The **display bgp ipv6 routing-table** command displays information about BGP4+ public network routes based on specified multiple attribute values.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table**

**display bgp ipv6 routing-table regular-expression** *strRegular*

**display bgp ipv6 routing-table community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp ipv6 routing-table large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **community** *communityNum* | Specifies the community number. | The value is an integer ranging from 0 to 4294967295. |
| **community** *strCommunityNum* | Specifies the community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP routes carrying the internet community attribute. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Displays routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community** *largeCommuStr* | Specifies a value of the Large-Community attribute. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **regular-expression** *strRegular* | Specifies the regular expression that matches AS\_Path. | The value is a string of 1 to 80 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP4+ public network routes based on specified multiple attribute values, run this command. Multiple attribute values can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP4+ public network routes that match the AS regular expression ^20.
```
<HUAWEI> display bgp ipv6 routing-table regular-expression ^20
 
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

# Display BGP4+ public network routes.
```
<HUAWEI> display bgp ipv6 routing-table
 
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

# Display BGP4+ public network routes with the community attribute.
```
<HUAWEI> display bgp ipv6 routing-table community
 
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
        Community : <1:1>, <2:2>
 *>     Network  : 2001:DB8:2::                             PrefixLen : 64  
        Nexthop  : 2001:DB8:8::8                            LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Community : <1:1>, <3:3>

```

# Display the BGP4+ public network routes with the Large-Community attribute.
```
<HUAWEI> display bgp ipv6 routing-table large-community
 
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

**Table 1** Description of the **display bgp ipv6 routing-table (Attribute)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total Number of Routes | Total number of routes. |
| Network | Network address in the BGP public network routing table. |
| PrefixLen | Prefix length. |
| LocPrf | Local\_Pref. |
| MED | MED of a route. |
| PrefVal | PrefVal. |
| Label | Label value. |
| Path/Ogn | AS\_Path number and the origin attribute. |
| Nexthop | Next hop address of the packet. |
| Community | Community attribute of a route. |
| Large-Community | LargeCommunity attribute of a route. |