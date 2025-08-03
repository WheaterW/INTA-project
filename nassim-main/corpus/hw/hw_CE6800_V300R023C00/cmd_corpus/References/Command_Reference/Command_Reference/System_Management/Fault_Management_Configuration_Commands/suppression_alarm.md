suppression alarm
=================

suppression alarm

Function
--------



The **suppression alarm** command configures a suppression period for an alarm.

The **undo suppression alarm** command deletes a suppression period.



By default, suppression time is 0.


Format
------

**suppression alarm** *alarm-name* { **cause-period** *cause-seconds* | **clear-period** *clear-seconds* }

**undo suppression alarm** *alarm-name* **cause-period**

**undo suppression alarm** *alarm-name* **clear-period**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *alarm-name* | Specifies the name of an alarm. This alarm must exist. | The value is a string of 1 to 63 characters, spaces not supported. |
| **cause-period** *cause-seconds* | Specifies the period after which an alarm is generated. If an alarm is repeatedly reported during cause-period, the system does not report the alarm until cause-period expires. | The value is an integer that ranges from 0 to 600, in seconds. |
| **clear-period** *clear-seconds* | Specifies the period after which an alarm is cleared. If a clear alarm is repeatedly reported during clear-period, the system reports the clear alarm until cause-period expires. | The value is an integer that ranges from 0 to 600, in seconds. |



Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can configure a suppression period to prevent an alarm from being frequently reported.Alarms for each application can be assigned a specific suppression period. Alarm suppression can be disabled for some alarms generated for hardware and devices.

**Configuration Impact**

If the suppression period is set too short, you do not give full play to the suppression effect; if the suppression period is set too long, faults cannot be detected in time. For most alarms, the default suppression period is recommended. You can set the suppression period to 0s for alarms that must be immediately reported, such as alarms about hardware and ambient environments.


Example
-------

# Set the suppression period for reporting the alarm named linkDown to 5s and the suppression period for clearing the alarm to 15s.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] suppression alarm linkDown cause-period 5
[*HUAWEI-alarm] suppression alarm linkDown clear-period 15

```