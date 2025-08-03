display logbuffer
=================

display logbuffer

Function
--------



The **display logbuffer** command displays logs in a log buffer.




Format
------

**display logbuffer** [ **security** ] [ **slot** *slot-id* | **module** *module-name* | **starttime** *starttime-value* [ **endtime** *endtime-value* ] | **level** { *severity* | *severityEnum* } | **size** *value* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **security** | Indicates the log type as the security log. | - |
| **slot** *slot-id* | Specifies the slot number of logs to be displayed. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **module** *module-name* | Specifies a module name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **starttime** *starttime-value* | Displays logs recorded from the specified start time. | The value is in the format of YYYY/MM/DD,HH:MM:SS.   * YYYY-MM-DD indicates year/month/day. The value of YYYY ranges from 1970 to 9999, the value of MM ranges from 1 to 12, and the value of DD ranges from 1 to 31. * HH:MM:SS indicates hour:minute:second. The value of HH ranges from 0 to 23; the value of MM and SS ranges from 0 to 59. |
| **endtime** *endtime-value* | Displays logs recorded by the specified end time. | The value is in the format of YYYY/MM/DD,HH:MM:SS.   * YYYY-MM-DD indicates year/month/day. The value of YYYY ranges from 1970 to 9999, the value of MM ranges from 1 to 12, and the value of DD ranges from 1 to 31. * HH:MM:SS indicates hour:minute:second. The value of HH ranges from 0 to 23; the value of MM and SS ranges from 0 to 59. |
| **level** *severity* | Displays logs based on severities. | The value is an integer ranging from 0 to 7.   * 0: emergencies: an error of urgency level * 1: alert: an error that needs to be corrected immediately * 2: critical: a major error * 3: error: a minor error * 4: warning: a potential error * 5: notification: information that should be noticed * 6: informational: an informational message * 7: debugging: a debugging message |
| *severityEnum* | Displays logs based severity. | * emergencies: displays critical error information. * alert: displays information about errors that need to be corrected immediately. * critical: displays logs at the critical level. * error: displays information at a specified error level. * warning: displays logs of the warning level. * notification: displays information of the specified severity. * informational: displays logs of the informational level. * debugging: displays debugging information of a specified level. |
| **size** *value* | Specifies the number of logs to be displayed. | The value is an integer ranging from 1 to 102400. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To display logs in a log buffer, run the **display logbuffer** command.The number of logs to be displayed using the **display logbuffer** command is determined by the number specified using the **info-center logbuffer** command. If the number of logs in the log buffer is less than that specified using value, all existing logs are displayed.

The **display logbuffer** command can display service logs, event logs and logs of other types. For information about event logs and logs of other types, see Log Reference. If a log is mapped to an "event trap OID", the log is an event log paired with an event trap. Event logs and the paired event traps have the same contents, and event logs can be queried based on the event trap OIDs.

The **display logbuffer security** command displays logs with the security log attribute.

**Precautions**

The log buffer records log messages of levels 0 through 4 by default. You can run the**info-center log-severity** command to set the log severity as needed:

* Set the severity of log messages to a value ranging 5 through 7 so that the log buffer does not record these log messages.
* Set the severity of log messages to a value ranging 0 through 4 so that the log buffer records these log messages.If there are a large number of logs on the device, running the **display logbuffer** command to display logs based on the start time, end time, log severity, and number of logs to be displayed is recommended. Otherwise, the following problems may occur due to excessive logs:
* The displayed information is repeatedly refreshed, causing desired information unable to be located.
* The system does not respond because of long-time information traversing and searching.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the level 4 log information.
```
<HUAWEI> display logbuffer level 4
Allowed max buffer size : 10240
Actual buffer size : 512
Channel number : 4 , Channel name : logbuffer
Dropped messages : 0
Overwritten messages : 0
Current messages : 6

Dec 19 2020 18:11:33 HUAWEI %%01INFO/4/SUPPRESS_LOGINFO(s):CID=0x80600407;Log SSHS/CALLHOME_RECORD is suppressed 1 in last 1 seconds.

```

**Table 1** Description of the **display logbuffer** command output
| Item | Description |
| --- | --- |
| Allowed max buffer size | Maximum size of the trap buffer. |
| Actual buffer size | Used size of the trap buffer. |
| Channel number | Channel number. |
| Channel name | Channel name. |
| Dropped messages | Number of dropped messages. |
| Overwritten messages | Number of overwritten messages. |
| Current messages | Number of existing messages. |