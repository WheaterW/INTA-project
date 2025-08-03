shutdown (IS-IS view)
=====================

shutdown (IS-IS view)

Function
--------



The **shutdown** command suppresses IS-IS and disables an IS-IS process.

The **undo shutdown** command re-enables the IS-IS process.



By default, the IS-IS process is enabled.


Format
------

**shutdown**

**undo shutdown**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an IS-IS fault occurs, run the **shutdown** command to disable the faulty IS-IS process temporarily.After the **shutdown** command is run, the system saves IS-IS configurations, stops IS-IS-related calculation, and deletes the dynamic IS-IS databases, including the LSDBs, neighbors, and routes.

**Precautions**

After the **shutdown** command is run on the local device, the neighbor relationship is interrupted and routes begin to converge only after the neighbor hold time expires. During this period, services may be interrupted.


Example
-------

# Disable IS-IS process 1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0000.0000.0001.00
[*HUAWEI-isis-1] shutdown

```