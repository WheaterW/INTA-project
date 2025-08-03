history record-wrap disable
===========================

history record-wrap disable

Function
--------



The **history record-wrap disable** command disables the wrapping function of historical alarms.

The **undo history record-wrap disable** command enables the wrapping function.



By default, the wrapping function is enabled.


Format
------

**history record-wrap disable**

**undo history record-wrap disable**


Parameters
----------

None

Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the wrapping function of historical alarms is enabled, new alarms replace the earliest alarms in the alarm list when the number of recorded alarms reaches the upper limit. If the wrapping function of historical alarms is disabled, new alarms are discarded when the number of recorded alarms reaches the upper limit.


Example
-------

# Disable the wrapping function of historical alarms.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] history record-wrap disable

```