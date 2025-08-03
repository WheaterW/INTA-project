correlation-analyze enable
==========================

correlation-analyze enable

Function
--------



The **correlation-analyze enable** command enables alarm correlation analysis.

The **undo correlation-analyze enable** command disables alarm correlation analysis.



By default, alarm correlation analysis is disabled.


Format
------

**correlation-analyze enable**

**undo correlation-analyze enable**


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

Alarms are classified as root alarms, independent alarms, and correlative alarms.The system marks the sequence number of the root alarm on correlative alarms.


Example
-------

# Enable alarm correlation analysis.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] correlation-analyze enable

```