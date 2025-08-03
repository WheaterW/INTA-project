display alarm history
=====================

display alarm history

Function
--------



The **display alarm history** command displays alarm history.




Format
------

**display alarm history**

**display alarm history verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed alarm history. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Alarm history refers to information about cleared alarms. The system stores a maximum of 1024 alarms. Therefore, the **display alarm history** command displays a maximum of 1024 alarm history records.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display alarm history.
```
<HUAWEI> display alarm history
--------------------------------------------------------------------------------
Sequence   AlarmId    Severity Date Time  Description                              
--------------------------------------------------------------------------------
1          0x8272004  Minor    2020-01-18 Administrator type users login failed 
                                15:00:38  too frequently.(failed times=0, statis
                                          tic period=0 minutes)

```

# Display detailed alarm history.
```
<HUAWEI> display alarm history verbose
Sequence    : 24        
AlarmId     : 0x8520003             AlarmName : linkDown                      
AlarmType   : processing_error      Severity  : Major            State : cleared         
StartTime   : 2012-12-27 13:27:43+08:00 DST           
Description : The interface status changes. (ifName=Ethernet1/0/2, AdminStatus=DOWN, OperStatus=DOWN, Reason=The interface is shut down.)
ClearTime   : 2012-12-27 13:30:08+08:00 DST           
ClearType   : service_resume      
ClearReason : The interface status changes. (ifName=Ethernet1/0/2, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is Up.)

Sequence    : 23        
AlarmId     : 0x8520003             AlarmName : linkDown                      
AlarmType   : processing_error      Severity  : Major            State : cleared                     
StartTime   : 2012-12-27 13:05:02+08:00 DST           
Description : The interface status changes. (ifName=Ethernet1/0/1, AdminStatus=DOWN, OperStatus=DOWN, Reason=The interface is shut down.)
ClearTime   : 2012-12-27 13:30:00+08:00 DST           
ClearType   : service_resume      
ClearReason : The interface status changes. (ifName=Ethernet1/0/1, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is Up.)

```

**Table 1** Description of the **display alarm history** command output
| Item | Description |
| --- | --- |
| Sequence | Sequence number. |
| AlarmId | Alarm ID. |
| Date | Date when the alarm was generated. |
| Date Time | Date and time when an alarm is generated. |
| Time | Time when the alarm was generated. |
| Description | Alarm description. |
| Severity | Alarm severity:   * 1: Critical. * 2: Major. * 3: Minor. * 4: Warning. |
| AlarmName | Alarm name. |
| AlarmType | Alarm type. |
| State | Current alarm status:   * active: The alarm is active. * cleared: The alarm is cleared. |
| StartTime | Time when an alarm is generated. |
| ClearTime | Time when the alarm was cleared. |
| ClearType | Cleared alarm type. |
| ClearReason | Reason of the alarm clearance. |