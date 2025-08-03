reset ipv6 statistics
=====================

reset ipv6 statistics

Function
--------



The **reset ipv6 statistics** command clears IPv6 traffic statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 statistics**


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

**Usage Scenario**

If you want to collect IPv6 traffic statistics within a specified period, run the **reset ipv6 statistics** command beforehand to clear the existing IPv6 traffic statistics. You can then run the **display ipv6 statistics** command to view the collected IPv6 traffic statistics.

**Configuration Impact**

Running the **reset ipv6 statistics** command clears the specified IPv6 traffic statistics. Exercise caution when running this command.


Example
-------

# Clear IPv6 traffic statistics.
```
<HUAWEI> reset ipv6 statistics

```