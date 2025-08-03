reset fwm m-lag synchronization packet statistics
=================================================

reset fwm m-lag synchronization packet statistics

Function
--------



The **reset fwm m-lag synchronization packet statistics** command clears statistics about synchronization packets exchanged between the devices paired into a DFS group.




Format
------

**reset fwm m-lag synchronization packet statistics**


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

To check statistics about synchronization packets between the devices paired into a DFS group in a period of time, first use this command to clear existing statistics.

**Precautions**

The statistics cannot be restored once being cleared. Exercise caution when you use this command.


Example
-------

# Clear statistics about synchronization packets between the devices paired into a DFS group.
```
<HUAWEI> reset fwm m-lag synchronization packet statistics

```