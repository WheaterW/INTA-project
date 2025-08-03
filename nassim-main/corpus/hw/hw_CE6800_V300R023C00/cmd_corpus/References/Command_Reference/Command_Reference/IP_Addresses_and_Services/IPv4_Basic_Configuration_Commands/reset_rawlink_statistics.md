reset rawlink statistics
========================

reset rawlink statistics

Function
--------



The **reset rawlink statistics** command clears the statistics about RawLink packets.




Format
------

**reset rawlink statistics**


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



To view the statistics about RawLink packets in a specified period, you need to clear the existing statistics about RawLink packets. Then, the system starts to collect the statistics from zero. After the specified period, you can run the **display rawlink statistics** command to view the statistics about RawLink packets in the specified period.



**Configuration Impact**



The **reset rawlink statistics** command clears the statistics about RawLink packets. Therefore, confirm the action before running this command.




Example
-------

# Clear the statistics about RawLink packets.
```
<HUAWEI> reset rawlink statistics

```