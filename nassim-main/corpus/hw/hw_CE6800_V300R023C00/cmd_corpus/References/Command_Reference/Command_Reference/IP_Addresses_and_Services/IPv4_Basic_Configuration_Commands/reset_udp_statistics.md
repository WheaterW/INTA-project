reset udp statistics
====================

reset udp statistics

Function
--------



The **reset udp statistics** command clears IPv4 UDP packet statistics.




Format
------

**reset udp statistics**


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



Before collecting the IPv4 UDP packet statistics in a specified period, you need to run the **reset udp statistics** command to clear previous IPv4 UDP packet statistics. After that, run the **display udp statistics** command to view the IPv4 UDP packet statistics.



**Configuration Impact**



The **reset udp statistics** command is used to clear IPv4 UDP packet statistics. Therefore, confirm the action before running this command.




Example
-------

# Clear IPv4 UDP packet statistics.
```
<HUAWEI> reset udp statistics

```