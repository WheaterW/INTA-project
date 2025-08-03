display ip routing-table route-number
=====================================

display ip routing-table route-number

Function
--------



The **display ip routing-table route-number** command displays the number of routes on a public network or in a VPN instance enabled with an IPv4 address family.

The **display ip routing-table statistics** command displays integrated route statistics of the IPv4 routing table.




Format
------

**display ip routing-table vpn-instance** *vpn-instance-name* **statistics**

**display ip routing-table vpn-instance** *vpn-instance-name* **route-number**

**display ip routing-table** [ **table-name** **msr** ] **route-number**

**display ip routing-table** [ **table-name** **msr** ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies a table of a producer. | - |
| **statistics** | Routing statistics. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **msr** | Displays integrated route statistics of the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The display ip routing-table route-number command is used to view the number of routes on a public network or in a VPN instance enabled with an IPv4 address family.Integrated route statistics include:

* Total number of routes that are added or deleted through the routing protocol
* Number of active routes or inactive routes that are labeled for deletion but have not been deleted


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display integrated route statistics.
```
<HUAWEI> system-view
[~HUAWEI] display ip routing-table statistics
Summary Prefixes : 8
Proto      total      active     added      deleted    freed
           routes     routes     routes     routes     routes
DIRECT     7          7          7          0          0
STATIC     1          1          1          0          0
RIP        0          0          0          0          0
OSPF       0          0          0          0          0
IS-IS      0          0          0          0          0
BGP        0          0          0          0          0
UNR        0          0          0          0          0
OPR        0          0          0          0          0
Total      8          8          8          0          0

```

**Table 1** Description of the **display ip routing-table route-number** command output
| Item | Description |
| --- | --- |
| Summary Prefixes | Total number of route prefixes in the routing table. |
| Proto | Routing protocol.   * DIRECT: displays direct routes. * STATIC: displays static routes. * RIP: displays RIP routes. * OSPF: displays OSPF routes. * IS-IS: displays IS-IS routes. * BGP: displays BGP routes. * UNR: displays UNR routes. * OPR: displays OPR routes. |
| total routes | Total number of routes in the current routing table. |
| active routes | Number of active routes in the routing table. |
| added routes | Number of active and inactive routes added in the routing table. |
| deleted routes | Number of routes to be deleted from the routing table. |
| freed routes | Number of released routes that are deleted forever from the routing table. |