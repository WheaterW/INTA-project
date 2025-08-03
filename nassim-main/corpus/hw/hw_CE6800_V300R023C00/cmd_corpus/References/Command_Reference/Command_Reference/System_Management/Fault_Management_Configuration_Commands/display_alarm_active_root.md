display alarm active root
=========================

display alarm active root

Function
--------



The **display alarm active root** command displays information about active root alarms.




Format
------

**display alarm active root**

**display alarm active root verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed information about active root alarms. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check information about active root alarms after you enable alarm correlation analysis using the **correlation-analyze enable** command, run the **display alarm active root** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about active root alarms.
```
<HUAWEI> display alarm active root
--------------------------------------------------------------------------------
Sequence   AlarmId    Severity Date Time  Description
--------------------------------------------------------------------------------
48         0xF102EE   Minor    2020-12-19 The number of available VTY channels i
                                16:00:38  s lower than the threshold.(currentLog
                                          inVTYs=12, totalVTYs=15)
--------------------------------------------------------------------------------

```

# Display detailed information about active root alarms.
```
<HUAWEI> display alarm active root verbose
Sequence    : 48
AlarmId     : 0xF102EE              AlarmName : hwVtyExceed
AlarmType   : quality_of_service    Severity  : Minor            State : active
RootKindFlag: Independent
StartTime   : 2020-12-19 16:00:38
Description : The number of available VTY channels is lower than the threshold.(currentLoginVTYs=12, totalVTYs=15)

```

**Table 1** Description of the **display alarm active root** command output
| Item | Description |
| --- | --- |
| Sequence | Alarm sequence number. |
| AlarmId | Alarm ID. |
| Date Time | Date and time when an alarm was generated. |
| Description | Alarm description. |
| Severity | Alarm severity. |
| AlarmName | Alarm name. |
| AlarmType | Type of a service for which an alarm is generated. |
| State | Alarm status:   * active. * cleared. |
| StartTime | Date and time when an alarm was generated. |
| RootKindFlag | Alarm generation type:   * Independent. * RootCause. * nonRootCause. |