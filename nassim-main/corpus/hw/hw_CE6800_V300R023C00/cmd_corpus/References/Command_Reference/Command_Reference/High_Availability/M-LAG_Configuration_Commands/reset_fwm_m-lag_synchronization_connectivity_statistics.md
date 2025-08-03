reset fwm m-lag synchronization connectivity statistics
=======================================================

reset fwm m-lag synchronization connectivity statistics

Function
--------



The **reset fwm m-lag synchronization connectivity statistics** command clears statistics about connectivity detection packets exchanged between the devices paired into a DFS group.




Format
------

**reset fwm m-lag synchronization connectivity statistics**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To view the number of connectivity detection packets exchanged between the devices paired into a DFS group in a specified period, run this command to clear historical statistics.

**Precautions**

After this command is run, all statistics about connectivity detection packets exchanged between the devices paired into a DFS group are cleared and cannot be restored. Exercise caution when you run this command.


Example
-------

# Clear all statistics about connectivity detection packets exchanged between the devices paired into a DFS group.
```
<HUAWEI> reset fwm m-lag synchronization connectivity statistics

```