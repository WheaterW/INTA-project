display bgp vpnv4 routing-table large-community
===============================================

display bgp vpnv4 routing-table large-community

Function
--------



The **display bgp vpnv4 routing-table large-community** command displays the BGP VPNv4 route and the BGP private network route information of the specified BGP large-community in the routing table.




Format
------

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **large-community** [ *aa:bb:cc* ] &<1-33>

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community** [ *aa:bb:cc* ] &<1-33>

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **large-community** [ *aa:bb:cc* ] &<1-33> **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community** [ *aa:bb:cc* ] &<1-33> **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **large-community-filter** *large-community-filter-name*

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community-filter** *large-community-filter-name*

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **large-community-filter** *large-community-filter-name* **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community-filter** *large-community-filter-name* **whole-match**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *route-distinguisher* | Specifies an RD of a remote route. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |
| **large-community** *aa:bb:cc* | Specifies large community values, with each value ranging from 0 to 4294967295. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **vpnv4** | Indicates the VPNv4 address family. | - |
| **statistics** | Displays statistics about BGP routes. | - |
| **whole-match** | Indicates exact match with specified communities. | - |
| **large-community-filter** *large-community-filter-name* | Specifies the large community filter name. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv4 routing-table large-community** command displays the BGP VPNv4 route and the BGP private network route information of the specified BGP large-community in the routing table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP VPNv4 routes and the BGP private network routes with large-community attribute.
```
<HUAWEI> display bgp vpnv4 route-distinguisher 1:1 routing-table large-community
 
 BGP Local router ID is 10.1.123.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found


 Route Distinguisher: 1:1

 Total Number of Routes: 3
        Network            NextHop                       MED        LocPrf    PrefVal LargeCommunity

 *>     10.11.11.11/32     10.20.0.1                      0                     0      <1:1:1>
 *>     10.22.22.22/32     10.2.123.2                     0                     0      <1:1:1>, <2:2:2>
 *>     10.33.33.33/32     10.2.123.3                     0                     0      <1:1:1>, <3:3:3>
    
 VPN-Instance vrf, Router ID 10.1.123.1:

 Total Number of Routes: 3
        Network            NextHop                       MED        LocPrf    PrefVal LargeCommunity

 *>     10.11.11.11/32     0.0.0.0                        0                     0      <1:1:1>
 *>     10.22.22.22/32     10.2.123.2                     0                     0      <1:1:1>, <2:2:2>
 *>     10.33.33.33/32     10.2.123.3                     0                     0      <1:1:1>, <3:3:3>

```

**Table 1** Description of the **display bgp vpnv4 routing-table large-community** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes. |
| Network | Indicates the network address in the BGP routing table. |
| NextHop | Next hop address used to forward the packet. |
| MED | Indicates the MED of the route. |
| LocPrf | Local preference of a route. |
| PrefVal | PrefVal of a BGP route. |
| LargeCommunity | Large-community attribute of a route. |