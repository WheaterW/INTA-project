display mrt ipv6 routing-table statistics
=========================================

display mrt ipv6 routing-table statistics

Function
--------



The **display mrt ipv6 routing-table statistics** command displays statistics about the MRT routing table on the main control board.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mrt ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays routing information with multicast receivers belonging to a specific VPN instance in an MVPN extranet scenario. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics about the MRT routing table of a VPN instance on the main control board, run the **display mrt ipv6 routing-table vpn-instance statistics** command. The command output contains the total number of routes in the current routing table of different protocols, the number of active routes in the routing table, the number of added routes in the routing table, the number of deleted routes in the routing table, and the number of permanently deleted routes in the routing table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics of the MRT routing table.
```
<HUAWEI> system-view
[~HUAWEI] display mrt ipv6 routing-table statistics
Proto     total      active      added        deleted      freed
          routes     routes      routes       routes       routes
MSTATIC      1          0           1            0            0

```

**Table 1** Description of the **display mrt ipv6 routing-table statistics** command output
| Item | Description |
| --- | --- |
| Proto | Route protocol. |
| total routes | Total number of routes in the current routing table. |
| active routes | Number of active routes in the routing table. |
| added routes | Number of active and inactive routes added in the routing table. |
| deleted routes | Number of routes deleted from the routing table. |
| freed routes | Number of released routes that are deleted forever from the routing table. |
| MSTATIC | Static multicast routing table. |