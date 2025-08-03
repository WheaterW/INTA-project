info-center event logging all
=============================

info-center event logging all

Function
--------



The **info-center event logging all** command enables event log recording globally.

The **undo info-center event logging all** command disables event log recording globally.



By default, event log recording is disabled globally.


Format
------

**info-center event logging all**

**undo info-center event logging all**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a device is running, the system records device running information using logs. When encountering problems, you can query log information to know about what happened during device running. The information helps locate a fault. For a type of event log, only event traps are sent. Therefore, you cannot view these logs in the log file.To enable event log recording for this type of event log, run the **info-center event logging all** command.


Example
-------

# Enable event log recording is globally.
```
<HUAWEI> system-view
[~HUAWEI] info-center event logging all

```