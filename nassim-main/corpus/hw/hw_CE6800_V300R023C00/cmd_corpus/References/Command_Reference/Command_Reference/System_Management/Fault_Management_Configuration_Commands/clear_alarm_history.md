clear alarm history
===================

clear alarm history

Function
--------



The **clear alarm history** command clears a specific or all historical alarms.




Format
------

**clear alarm history** { **all** | **sequence-number** *sequence-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears all historical alarms. | - |
| **sequence-number** *sequence-number* | Clears the sequence number of a historical alarm. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a historical alarm that has been triggered by a fault is not needed because the fault has been rectified, run the clear alarm history command to clear the historical alarm.

**Configuration Impact**



After a historical alarm is cleared from the alarm list, the alarm cannot be restored.



**Follow-up Procedure**

Run the **display alarm history** command to view whether a historical alarm has been cleared.


Example
-------

# Clear all historical alarms.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] clear alarm history all

```

# Clear the historical alarm with the sequence number of 1.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] clear alarm history sequence-number 1

```