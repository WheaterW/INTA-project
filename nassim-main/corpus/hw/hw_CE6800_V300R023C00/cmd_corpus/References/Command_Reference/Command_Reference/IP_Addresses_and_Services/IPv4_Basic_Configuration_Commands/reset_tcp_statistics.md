reset tcp statistics
====================

reset tcp statistics

Function
--------



The **reset tcp statistics** command clears IPv4 TCP packet statistics.




Format
------

**reset tcp statistics**


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



Before collecting the IPv4 TCP packet statistics in a specified period, you need to run the **reset tcp statistics** command to clear previous IPv4 TCP packet statistics. After that, run the **display tcp statistics** command to view IPv4 TCP packet statistics.



**Configuration Impact**



The **reset tcp statistics** command is used to clear IPv4 TCP packet statistics. Therefore, confirm the action before running this command.




Example
-------

# Clear IPv4 TCP packet statistics.
```
<HUAWEI> reset tcp statistics

```