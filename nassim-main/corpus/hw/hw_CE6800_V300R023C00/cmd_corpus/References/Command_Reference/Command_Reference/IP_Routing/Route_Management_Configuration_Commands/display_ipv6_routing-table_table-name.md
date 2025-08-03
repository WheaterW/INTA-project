display ipv6 routing-table table-name
=====================================

display ipv6 routing-table table-name

Function
--------



The **display ipv6 routing-table table-name** command displays the routes generated within a specified period.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table table-name msr** [ **time-range** *min\_age* *max\_age* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **time-range** | Indicates the route generation time range. | - |
| *min\_age* | Specifies the minimum age, in <0-10000>d<0-23>h<0-59>m<0-59>s format. | The value is a string of 1 to 15 case-sensitive characters. It cannot contain spaces. |
| *max\_age* | Specifies the maximum age, in <0-10000>d<0-23>h<0-59>m<0-59>s format. | The value is a string of 1 to 15 case-sensitive characters. It cannot contain spaces. |
| **msr** | Indicates the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Using the **display ipv6 routing-table table-name** command, you can view the routes generated within a specified period. The command output includes the prefix, mask, protocol type, priority, metric, next hop, outbound interface, and route flag.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the the routing table of the IPv6.
```
<HUAWEI> system-view
[~HUAWEI] display ipv6 routing-table table-name localmt
Routing Table : vrf1
         Destinations : 1        Routes : 1         

Destination  : 2001:db8:1::1                                     
PrefixLength : 64
NextHop      : ::                                      Preference   : 60
Cost         : 0                                       Protocol     : Static
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0                                   Flags        : DB

```

**Table 1** Description of the **display ipv6 routing-table table-name** command output
| Item | Description |
| --- | --- |
| Routing Table | The routing table is a VPN routing table. |
| Destinations | Total number of destination networks/hosts. |
| Routes | Total number of routes. |
| Destination | Destination network/host address. |
| PrefixLength | Prefix length. |
| NextHop | Next hop address. |
| Preference | Route preference. |
| Cost | Route cost. |
| Protocol | Routing protocol. |
| RelayNextHop | Recursive next hop. |
| TunnelID | Tunnel ID. The value 0x0 indicates that no tunnel is used or the tunnel fails to be established. |
| Interface | Outbound interface reachable to the next hop. |
| Flags | Route flags in the header of the routing table. |