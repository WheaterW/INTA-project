display device alarm
====================

display device alarm

Function
--------



The **display device alarm hardware** command displays hardware alarms on a device.

The **display device alarm hardware history** command displays historical hardware alarms.




Format
------

**display device alarm hardware** [ **slot** *slotid* ]

**display device alarm hardware history** { **all** | **slot** *slotid* } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hardware** | Indicates the hardware alarm. | - |
| **slot** *slotid* | Specifies a slot ID. | You can enter a question mark (?) and select a value based on the prompt. |
| **history** | Indicates the historical alarm. | - |
| **all** | Displays all hardware alarms. | - |
| **verbose** | Indicates detailed alarm information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display device alarm hardware** command to view hardware alarms on the device. Historical hardware alarms refer to the hardware alarms that have been cleared in the system. You can run the **display device alarm hardware history** command to view historical hardware alarms of the current device.



**Precautions**

* You can run the **display device alarm hardware** command to view all active hardware alarms. To view all active alarms, run the **display alarm active** command.
* If a board is specified in the **display device alarm hardware** command, hardware alarms about the specified board are displayed. If no board is specified, all hardware alarms are displayed.


Example
-------

# Display details about historical hardware alarms.
```
<HUAWEI> display device alarm hardware history all verbose
--------------------------------------------------------------------------------
Index Level    StartDate  StartTime  ClearDate  ClearTime  Info                 
--------------------------------------------------------------------------------
1963  Major    2020-07-17 16:00:55   2020-07-25 20:29:39   The interface status 
                                                           changes. (ifName=Vlan
                                                           if200, AdminStatus=UP
                                                           , OperStatus=DOWN, Re
                                                           ason=Interface physic
                                                           al link is down, main
                                                           Ifname=Vlanif200)    
--------------------------------------------------------------------------------

```

# Display hardware alarms.
```
<HUAWEI> display device alarm hardware
--------------------------------------------------------------------------------
Index  Level    Date       Time           Info                                  
--------------------------------------------------------------------------------                             
1      Critical 2020-04-29 10:40:04       The power totally failed.(PowerID=POWE
                                          R slot 1, Reason=The power module wa
                                          s not present.)                       
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display device alarm** command output
| Item | Description |
| --- | --- |
| Index | Sequence number of an alarm. |
| Level | Alarm severity. |
| Date | Date when an alarm is generated. |
| Time | Time when an alarm is generated. |
| Info | Alarm details. |
| StartDate | Date when an alarm is generated. |
| StartTime | Date and time when the alarm was generated. |
| ClearDate | Date when the alarm is cleared. |
| ClearTime | Time when the alarm is cleared. |