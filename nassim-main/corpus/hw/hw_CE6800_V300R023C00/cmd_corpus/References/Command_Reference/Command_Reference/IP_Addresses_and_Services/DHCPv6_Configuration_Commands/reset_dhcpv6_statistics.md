reset dhcpv6 statistics
=======================

reset dhcpv6 statistics

Function
--------



The **reset dhcpv6 statistics** command clears DHCPv6 packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset dhcpv6 statistics**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Collecting statistics about the DHCPv6 messages sent and received within a specified period helps you locate DHCPv6 faults. Before collecting new statistics, run the **reset dhcpv6 statistics** command to clear the existing message statistics. After clearing existing statistics, run the **display dhcpv6 statistics** command to view latest message statistics. Collecting statistics about the DHCPv6 messages sent and received within a specified period helps you locate DHCPv6 faults. Before collecting new statistics, run the **reset dhcpv6 statistics** command to clear the existing message statistics. After clearing existing statistics, run the **display dhcpv6 statistics** command to view latest message statistics.


Example
-------

# Clear DHCPv6 message statistics.
```
<HUAWEI> reset dhcpv6 statistics

```