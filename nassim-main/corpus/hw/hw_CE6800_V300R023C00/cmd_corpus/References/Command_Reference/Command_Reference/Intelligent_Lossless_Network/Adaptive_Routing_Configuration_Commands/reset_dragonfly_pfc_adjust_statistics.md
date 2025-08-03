reset dragonfly pfc adjust statistics
=====================================

reset dragonfly pfc adjust statistics

Function
--------



The **reset dragonfly pfc adjust statistics** command clears statistics on dragonfly deadlock prevention.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

For CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**reset dragonfly abs-pfc adjust statistics**

For CE8855, CE8851-32CQ4BQ:

**reset dragonfly pfc adjust statistics**


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

You can run this command to clear statistics on dragonfly deadlock prevention.

**Precautions**

After you run this command, statistics on dragonfly deadlock prevention are cleared and cannot be restored. Exercise caution when you run this command.


Example
-------

# Clear statistics on dragonfly deadlock prevention.
```
<HUAWEI> reset dragonfly abs-pfc adjust statistics

```

# Clear statistics on dragonfly deadlock prevention.
```
<HUAWEI> reset dragonfly pfc adjust statistics

```