display bgp routing-table(Attribute Filter)
===========================================

display bgp routing-table(Attribute Filter)

Function
--------



The **display bgp routing-table** command displays BGP public network route information based on specified multiple attribute filters.




Format
------

**display bgp routing-table as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp routing-table community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp routing-table large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | It is an integer ranging from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer ranging from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer ranging from 100 to 199. |
| **whole-match** | Indicates that the specified attribute filter is fully matched. | - |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query information about BGP public network routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP routes that match community filter 10.
```
<HUAWEI> display bgp routing-table community-filter 10
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Total Number of Routes: 1
        Network            NextHop                       MED        LocPrf    PrefVal Community

 *>     10.1.2.0/24        10.1.123.2                     0                     0      <1:1>, <3:3>

```

# Display the BGP routes that match the Large-community filter aaa.
```
<HUAWEI> display bgp routing-table large-community-filter aaa
 
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

# Display BGP routes that match the AS\_Path filter named pas.
```
<HUAWEI> display bgp routing-table as-path-filter pas
 
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

**Table 1** Description of the **display bgp routing-table(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Total Number of Routes | Total number of routes. |
| Network | Indicates the network address in the BGP routing table. |
| NextHop | Next hop address used to forward the packet. |
| MED | Indicates the MED of the route. |
| LocPrf | Local preference of a route. |
| PrefVal | PrefVal of a BGP route. |
| Community | Community attribute contained in a route. |
| LargeCommunity | Large-Community attribute of a route. |
| Path/Ogn | AS-Path number and the Origin attribute. |