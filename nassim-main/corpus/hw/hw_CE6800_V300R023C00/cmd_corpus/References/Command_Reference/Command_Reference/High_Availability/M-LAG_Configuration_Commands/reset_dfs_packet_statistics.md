reset dfs packet statistics
===========================

reset dfs packet statistics

Function
--------



The **reset dfs packet statistics** command clears the statistics about received and sent packets about M-LAG member interface status changes.




Format
------

**reset dfs packet statistics**


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

You can run the **reset dfs packet statistics** command to clear the statistics about received and sent packets about M-LAG member interface status changes.

**Precautions**

The statistics cannot be restored once being cleared. Exercise the caution when you use this command.


Example
-------

# Clear statistics about received and sent packets about M-LAG member interface status changes.
```
<HUAWEI> reset dfs packet statistics

```