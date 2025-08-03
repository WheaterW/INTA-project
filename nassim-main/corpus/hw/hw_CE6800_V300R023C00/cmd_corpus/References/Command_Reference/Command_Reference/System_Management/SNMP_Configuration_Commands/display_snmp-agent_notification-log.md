display snmp-agent notification-log
===================================

display snmp-agent notification-log

Function
--------



The **display snmp-agent notification-log** command displays alarm logs in an alarm buffer.




Format
------

**display snmp-agent notification-log** [ **logtime** *startTime* *startDate* **to** *endTime* *endDate* | **size** *size* ]

**display snmp-agent notification-log info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **logtime** | Time of recording logs. | - |
| *startTime* | Specifies the start time when a device logs alarms. | The value is in the HH:MM:SS format, where HH:MM:SS indicates the hour, minute, and second. HH ranges from 0 to 23; MM and SS range from 0 to 59. |
| *startDate* | Specifies the start date when a device logs alarms. | The value is in the format of YYYY/MM/DD. The YYYY value ranges from 2000 to 2099, the MM value ranges from 1 to 12, and the DD value ranges from 1 to 31. |
| **to** | Range link symbol. | - |
| *endTime* | Specifies the end time when a device stops logging alarms. | The value is in the HH:MM:SS format, where HH:MM:SS indicates the hour, minute, and second. HH ranges from 0 to 23; MM and SS range from 0 to 59. |
| *endDate* | Specifies the end date when a device stops logging alarms. | The value is in the YYYY/MM/DD format. YYYY/MM/DD indicates year/month/day. YYYY ranges from 2000 to 2099, MM ranges from 1 to 12, and DD ranges from 1 to 31. |
| **size** *size* | Specifies the recent alarm logs to be displayed. | The value is an integer that ranges from 1 to 15000. If the specified number of alarm logs to be displayed exceeds the number of alarm logs currently saved by the system, information on all alarm logs in the alarm buffer is displayed. |
| **info** | Indicates information in an alarm buffer. The information includes the number of global alarm logs in the alarm buffer, the number of discarded alarm logs, aging time of alarm logs, limitation on the number of alarm logs, total number of existing alarm logs, and enabling status of alarm logging. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can set the following conditions for displaying detailed information about alarm logs in the alarm buffer:

* A specific piece of alarm logs
* Alarm logs based on the time when alarms are logged
* All alarm logs by default

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about alarm logs.
```
<HUAWEI> display snmp-agent notification-log info
 Notification log information: 
 Notification Admin Status : enable
 GlobalNotificationsLogged : 0
 GlobalNotificationsBumped : 0
 GlobalNotificationsLimit  : 1000
 GlobalNotificationsAgeout : 36
 Total number of notification log(s): 0

```

**Table 1** Description of the **display snmp-agent notification-log** command output
| Item | Description |
| --- | --- |
| Notification Admin Status | Enabling status of alarm logging:   * enable. * disable. |
| Notification log information | Alarm log information. |
| GlobalNotificationsLogged | Number of global alarm logs. |
| GlobalNotificationsBumped | Number of globally discarded alarm logs. |
| GlobalNotificationsLimit | Global limitation on the number of alarm logs. |
| GlobalNotificationsAgeout | Global aging time of alarm logs that global alarm logs have timed-out. |
| Total number of notification log(s) | Total number of the current alarm logs. |