shutdown (Maintenance assistant task view)
==========================================

shutdown (Maintenance assistant task view)

Function
--------



The **shutdown** command stops a maintenance assistant.

The **undo shutdown** command enables a maintenance assistant.



By default, a created assistant is enabled.


Format
------

**shutdown**

**undo shutdown**


Parameters
----------

None

Views
-----

Maintenance assistant task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To stop a maintenance assistant, run the **shutdown** command.

**Configuration Impact**

Services on the interface are intermittently interrupted after the **shutdown** command is run on the interface.


Example
-------

# Shutdown the maintenance assistant config.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant config
[*HUAWEI-ops-assistant-config] shutdown

```