display ipv6 routing-table statistics
=====================================

display ipv6 routing-table statistics

Function
--------



The **display ipv6 routing-table statistics** command displays integrated route statistics of the IPv6 routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table all-routes statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-routes** | Displays integrated route statistics of all IPv6 routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Integrated route statistics include:

* Total number of routes that are added or deleted through the routing protocol
* Number of active routes or inactive routes that are labeled for deletion but have not been deleted

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display integrated route statistics.
```
<HUAWEI> display ipv6 routing-table all-routes statistics
Summary Prefixes : 2
Protocol   route       active      added       deleted     freed
DIRECT     2           2           2           0           0           
STATIC     0           0           0           0           0           
RIPng      0           0           0           0           0           
OSPFv3     0           0           0           0           0           
IS-IS      0           0           0           0           0           
BGP        0           0           0           0           0           
UNR        0           0           0           0           0           
Total      2           2           2           0           0

```

**Table 1** Description of the **display ipv6 routing-table statistics** command output
| Item | Description |
| --- | --- |
| Summary Prefixes | Total number of route prefixes in the routing table. |
| Protocol | Routing protocol.   * DIRECT: displays direct routes. * STATIC: displays static routes. * RIP: displays RIP routes. * OSPF: displays OSPF routes. * IS-IS: displays IS-IS routes. * BGP: displays BGP routes. * UNR: displays UNR routes. |
| active | Number of active routes in the routing table. |
| added | Number of active and inactive routes added to the routing table. |
| deleted | Number of routes deleted from the routing table. |
| freed | Number of routes permanently deleted from the routing table. |
| routes | Number of routes in the routing table. |