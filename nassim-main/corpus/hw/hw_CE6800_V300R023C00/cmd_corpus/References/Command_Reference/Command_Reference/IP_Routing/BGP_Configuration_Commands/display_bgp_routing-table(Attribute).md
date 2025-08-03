display bgp routing-table(Attribute)
====================================

display bgp routing-table(Attribute)

Function
--------



The **display bgp routing-table** command displays BGP public network route information based on specified attribute values.




Format
------

**display bgp routing-table**

**display bgp routing-table regular-expression** *strRegular*

**display bgp routing-table community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp routing-table large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **community** *communityNum* | Specifies a community number. | The value is an integer ranging from 0 to 4294967295. |
| **community** *strCommunityNum* | Specifies a community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP public network routes carrying the internet community attribute. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP public network routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community** *largeCommuStr* | Specifies the value of the Large-Community attribute. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **regular-expression** *strRegular* | Specifies an AS\_Path regular expression. | The value is a string of 1 to 80 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP public network routes based on specified multiple attribute values, run this command. Multiple attribute values can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all BGP public network routes.
```
<HUAWEI> display bgp routing-table
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn

 *>     10.1.1.0/24        10.1.123.2                     0                     0      200i
 *>     10.1.2.0/24        10.1.123.2                     0                     0      200i

```

# Display information about BGP public network routes with the Large-Community attribute.
```
<HUAWEI> display bgp routing-table large-community
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal LargeCommunity

 *>     10.1.1.0/24        10.1.123.2                     0                     0      <1:1:1>, <2:2:2>
 *>     10.1.2.0/24        10.1.123.2                     0                     0      <1:1:1>, <2:2:2>

```

# Display the BGP public network route information that matches the AS regular expression ^20.
```
<HUAWEI> display bgp routing-table regular-expression ^20
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn

 *>     10.1.1.0/24        10.1.123.2                     0                     0      200i
 *>     10.1.2.0/24        10.1.123.2                     0                     0      200i

```

# Display information about BGP public network routes with community attributes.
```
<HUAWEI> display bgp routing-table community
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Community

 *>     10.1.1.0/24        10.1.123.2                     0                     0      <1:1>, <2:2>
 *>     10.1.2.0/24        10.1.123.2                     0                     0      <1:1>, <3:3>

```

**Table 1** Description of the **display bgp routing-table(Attribute)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total Number of Routes | Total number of routes. |
| Network | Network address in the BGP routing table. |
| NextHop | Next hop address used to forward the packet. |
| MED | MED of the route. |
| LocPrf | Local preference. |
| PrefVal | PrefVal. |
| Path/Ogn | AS\_Path and Origin. |
| LargeCommunity | Large-Community attribute of a route. |
| Community | Community attribute contained in a route. |