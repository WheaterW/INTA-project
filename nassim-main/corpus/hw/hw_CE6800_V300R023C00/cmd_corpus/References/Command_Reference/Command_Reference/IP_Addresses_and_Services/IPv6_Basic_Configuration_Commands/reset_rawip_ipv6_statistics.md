reset rawip ipv6 statistics
===========================

reset rawip ipv6 statistics

Function
--------



The **reset rawip ipv6 statistics** command clears the statistics about IPv6 RawIP packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset rawip ipv6 statistics**


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

You need to clear the existing statistics about IPv6 RawIP packets before using the **display rawip ipv6 statistics** command to view the statistics about IPv6 RawIP packets in a specified period.

**Configuration Impact**

The **reset rawip ipv6 statistics** command clears the statistics about IPv6 RawIP packets. Therefore, confirm the action before running this command.


Example
-------

# Clear statistics about IPv6 RawIP packets.
```
<HUAWEI> reset rawip ipv6 statistics

```