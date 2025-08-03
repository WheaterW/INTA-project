display alarm active
====================

display alarm active

Function
--------



The **display alarm active** command displays information about active alarms.




Format
------

**display alarm active**

**display alarm active verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed information about an alarm. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check information about active alarms on a device, run the **display alarm active** command. The information includes the alarm sequence number, generation time, clearance time, ID, name, severity, status, and description. To check detailed information about active alarms, run the display alarm active verbose command.

**Precautions**

The **display alarm active** command displays the alarms that are not cleared. To query the cleared alarms, run the **display alarm history** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about all active alarms.
```
<HUAWEI> display alarm active verbose
Sequence    : 24        
AlarmId     : 0x8520003             AlarmName : linkDown                      
AlarmType   : processing_error      Severity  : Major            State : active
RootKindFlag: Independent                       
StartTime   : 2020-01-18 13:27:43+08:00 DST           
Description : The interface status changes. (ifName=Ethernet1/0/2, AdminStatus=DOWN, OperStatus=DOWN, Reason=The interface is shut down.)

Sequence    : 23        
AlarmId     : 0x8520003             AlarmName : linkDown                      
AlarmType   : processing_error      Severity  : Major            State : active                      
RootKindFlag: Independent
StartTime   : 2020-01-18 13:05:02+08:00 DST           
Description : The interface status changes. (ifName=Ethernet1/0/1, AdminStatus=DOWN, OperStatus=DOWN, Reason=The interface is shut down.)

```

# Display information about all active alarms.
```
<HUAWEI> display alarm active
--------------------------------------------------------------------------------
Sequence   AlarmId    Severity Date Time  Description                              
--------------------------------------------------------------------------------
1          0x8272004  Minor    2020-01-18 Administrator type users login failed 
                                15:00:38  too frequently.(failed times=0, statis
                                          tic period=0 minutes)

```

**Table 1** Description of the **display alarm active** command output
| Item | Description |
| --- | --- |
| Sequence | Alarm sequence number. |
| AlarmId | Alarm ID. |
| AlarmName | Alarm name. |
| AlarmType | Alarm type. |
| Severity | Alarm severity:   * Critical. * Major. * Minor. * Warning. |
| State | Current alarm status:   * active: The alarm is active. * cleared: The alarm is cleared. |
| StartTime | Time when the alarm is generated. |
| Description | Alarm description. |
| Date | Date when the alarm was generated. |
| Time | Time when the alarm was generated. |
| RootKindFlag | Alarm correlation type. |