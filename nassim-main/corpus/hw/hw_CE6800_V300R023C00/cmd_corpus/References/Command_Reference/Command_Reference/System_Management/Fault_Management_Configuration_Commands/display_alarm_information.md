display alarm information
=========================

display alarm information

Function
--------



The **display alarm information** command displays alarm information.




Format
------

**display alarm information name** *alarm-name*

**display alarm information**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *alarm-name* | Specifies the name of an alarm. This alarm must exist. | The value is a string of 1 to 63 characters. If no alarm name is specified, information about all alarms in the system will be displayed. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To obtain information about alarms in the system, run the display alarm information command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the basic configuration of the alarm item APPDATA\_NOT\_SYN.
```
<HUAWEI> display alarm information name APPDATA_NOT_SYN
--------------------------------------------------------------------------------------
Feature             : CONFIGURATION
AlarmName           : APPDATA_NOT_SYN
AlarmId             : 0x8152022
Severity            : Major
Cause suppress time : 10
Clear suppress time : 10
--------------------------------------------------------------------------------------

```

**Table 1** Description of the **display alarm information** command output
| Item | Description |
| --- | --- |
| Feature | Feature for which the alarm is generated. |
| AlarmName | Alarm name. |
| AlarmId | Alarm ID. |
| Severity | Alarm severity. |
| Cause suppress time | Suppression period after which an alarm can be generated. |
| Clear suppress time | Suppression period after which an alarm can be cleared. |