display ipv6 routing-table route-number
=======================================

display ipv6 routing-table route-number

Function
--------



The **display ipv6 routing-table statistics** command displays integrated route statistics of the IPv6 routing table.

The **display ipv6 routing-table route-number** command displays the number of routes on a public network or in a VPN instance enabled with an IPv6 address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table all-vpn-instance statistics**

**display ipv6 routing-table statistics**

**display ipv6 routing-table vpn-instance** *vpn-instance-name* **statistics**

**display ipv6 routing-table route-number**

**display ipv6 routing-table vpn-instance** *vpn-instance-name* **route-number**

**display ipv6 routing-table vpn-instance** *vpn-instance-name* [ **table-name** **msr** ] **statistics**

**display ipv6 routing-table** [ **table-name** **msr** ] **statistics**

**display ipv6 routing-table** [ **table-name** **msr** ] **route-number**

**display ipv6 routing-table vpn-instance** *vpn-instance-name* [ **table-name** **msr** ] **route-number**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies the name of a routing table. | - |
| **statistics** | Displays integrated route statistics in the routing table of the IPv6 address family-enabled VPN instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance enabled with an IPv6 address family. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **route-number** | Displays the number of routes. | - |
| **all-vpn-instance** | All VPN instances. | - |
| **msr** | Indicates the multicast static routing table. | - |



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
* Number of active routes or inactive routes that are labeled for deletion but have not been deletedThis command is used to view the number of routes on a public network or in a VPN instance enabled with an IPv6 address family.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display integrated route statistics about the IPv6 routes of all VPN instances.
```
<HUAWEI> display ipv6 routing-table all-vpn-instance statistics
Protocol   route       active      added       deleted     freed
DIRECT     3           3           3           0           0           
STATIC     1           1           1           0           0           
RIPng      0           0           0           0           0           
OSPFv3     0           0           0           0           0           
IS-IS      0           0           0           0           0           
BGP        0           0           0           0           0           
Total      4           4           4           0           0

```

# Display integrated route statistics.
```
<HUAWEI> display ipv6 routing-table statistics
Summary Prefixes : 15
Protocol   total      active     added      deleted
           routes     routes     routes     routes
DIRECT     12         12         18         6
STATIC     0          0          0          0
RIPng      0          0          0          0
OSPFv3     0          0          0          0
IS-IS      4          3          4          0
BGP        0          0          0          0
Total      16         15         22         6

```

**Table 1** Description of the **display ipv6 routing-table route-number** command output
| Item | Description |
| --- | --- |
| Protocol | Routing protocol.   * DIRECT: displays direct routes. * STATIC: displays static routes. * RIPng: displays RIPng routes. * OSPFv3: displays OSPFv3 routes. * IS-IS: displays IS-IS routes. * BGP: displays BGP routes. * UNR: displays UNR routes. |
| active | Number of active routes in the routing table. |
| added | Number of routes (active and inactive) added to the routing table. |
| deleted | Number of deleted routes. |
| freed | Number of routes that are permanently deleted from the routing table. |
| Summary Prefixes | Total number of route prefixes in the routing table. |
| routes | Total number of routes in the routing table. |