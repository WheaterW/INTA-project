display bgp routing-table (condition)
=====================================

display bgp routing-table (condition)

Function
--------



The **display bgp routing-table** command displays related information about BGP routes.




Format
------

**display bgp routing-table** *network* { *mask-length* | *mask* }

**display bgp routing-table** *network* { *mask-length* | *mask* } **longer-prefixes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *network* | Specifies a destination IPv4 address. | It is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of the destination IP address. | The value is an integer in the range from 0 to 32. |
| *mask* | Specifies the mask of an IPv4 address. | The value is in dotted decimal notation. |
| **longer-prefixes** | Matches according to the mask longer than the specified length. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the information about routes in the BGP routing table, run the display bgp routing-table command with specified parameters.

**Precautions**

If a routing loop occurs, some routes may have not converged. Therefore, the route statistics displayed using the command may be different from the actual number.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display public network routes.
```
<HUAWEI> display bgp routing-table 10.1.1.1
 
 BGP local router ID : 10.1.1.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 10.1.1.1/32:
 Label information (Received/Applied): 48073/NULL
 From: 10.10.1.1 (10.1.1.2)  
 Route Duration: 0d00h45m10s
 Relay IP Nexthop: 10.1.1.1
 Relay IP Out-Interface: Loopback0
 Relay Tunnel Out-Interface: Loopback0
 Original nexthop: 10.10.1.1
 Qos information : 0x0
 Community: <1:1>
 Ext-Community: Color <0 : 3>
 Large-Community: <1:1:1>
 AS-path Nil, origin incomplete, MED 33, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10
 Originator: 10.3.1.1
 Cluster list: 0.0.0.100
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp routing-table (condition)** command output
| Item | Description |
| --- | --- |
| Route Duration | Timestamp of a route. |
| Relay IP Nexthop | Relay IP Nexthop. |
| Relay Tunnel Out-Interface | Name of the tunnel to which a route recurses. |
| IP Out-Interface | Name of a route's outbound interface. |
| MED | MED of the route. |
| Cluster list | Cluster\_List. |
| Origin | Route origin. |
| From | Source peer for route advertisement. |