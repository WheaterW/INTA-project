display alarm statistics
========================

display alarm statistics

Function
--------



The **display alarm statistics** command displays alarm statistics.




Format
------

**display alarm statistics name** *alarm-name*

**display alarm statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *alarm-name* | Displays statistics about an alarm with the specified name. This alarm must exist. | The value is a string of 1 to 63 characters, spaces not supported. If no alarm name is specified, statistics about all alarms in the system will be displayed. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If alarm-name is specified in the display alarm statistics command, only statistics about the specified alarm are displayed. Displayed alarm statistics will inform you of the numbers of different types of alarms generated and help you evaluate the device operating status and service quality.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about a specific alarm.
```
<HUAWEI> display alarm statistics name linkdown
----------------------------------------------------------------------------
AlarmName : linkDown
Active    : 0
All       : 142
----------------------------------------------------------------------------

```

# Display statistics about all alarms.
```
<HUAWEI> display alarm statistics
----------------------------------------------------------------------------
AlarmName : IsisAdjacencyChange
Active    : 0
All       : 1

AlarmName : linkDown
Active    : 0
All       : 142

AlarmName : mplsTunnelDown
Active    : 0
All       : 148
----------------------------------------------------------------------------

```

**Table 1** Description of the **display alarm statistics** command output
| Item | Description |
| --- | --- |
| AlarmName | Alarm name. |
| Active | Number of active alarms. |
| All | Number of alarms. |