reset rawip statistics
======================

reset rawip statistics

Function
--------



The **reset rawip statistics** command clears the statistics about IPv4 RawIP packets.




Format
------

**reset rawip statistics**


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



You need to clear the existing statistics about IPv4 RawIP packets before using the **display rawip statistics** command to view the statistics about IPv4 RawIP packets in a specified period.



**Configuration Impact**



The **reset rawip statistics** command clears the statistics about IPv4 RawIP packets. Therefore, confirm the action before running this command.




Example
-------

# Clear statistics about IPv4 RawIP packets.
```
<HUAWEI> reset rawip statistics

```