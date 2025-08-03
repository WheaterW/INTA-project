display logfile list
====================

display logfile list

Function
--------



The **display logfile list** command displays log files generated in the specified time range.




Format
------

**display logfile** [ **security** | **log** | **diagnose** ] **list** **starttime** *starttime-value* **endtime** *endtime-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **security** | Displays security log files generated in the specified time range. | - |
| **log** | Displays user log files generated in the specified time range. | - |
| **diagnose** | Displays diagnostic log files generated in the specified time range. | - |
| **list** | Displays diagnostic log files generated in the specified time range. | - |
| **starttime** *starttime-value* | Specifies the start time for the query of log files. | The value is in the YYYY/MM/DD,HH:MM:SS format.   * YYYY indicates the year and is an integer ranging from 1970 to 9999. * MM indicates the month and is an integer ranging from 1 to 12. * DD indicates the day and is an integer ranging from 1 to 31. * HH indicates the hour and is an integer ranging from 0 to 23. * MM indicates the minute and is an integer ranging from 0 to 59. * SS indicates the second and is an integer ranging from 0 to 59. * If YYYY/MM/DD is not specified, the system year, month, and day are used by default. * The value of starttime-value must be earlier than that of endtime-value. |
| **endtime** *endtime-value* | Specifies the end time for the query of log files. | The value is in the YYYY/MM/DD,HH:MM:SS format.   * YYYY indicates the year and is an integer ranging from 1970 to 9999. * MM indicates the month and is an integer ranging from 1 to 12. * DD indicates the day and is an integer ranging from 1 to 31. * HH indicates the hour and is an integer ranging from 0 to 23. * MM indicates the minute and is an integer ranging from 0 to 59. * SS indicates the second and is an integer ranging from 0 to 59. * If YYYY/MM/DD is not specified, the system year, month, and day are used by default. * The value of endtime-value must be later than that of starttime-value. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To check device running status, run the **display logfile list** command to display log files generated in the specified time range. If no log file type (log/diagnose/security) is specified, the command displays all types of log files generated in the specified time range.Log files of the log type are automatically named in the log.log format. You can access the flash: directory to view this type of log files. If the size of a log file exceeds the upper threshold, the system automatically saves the file as a historical compression one and changes the file name to log\_SlotID\_time.log.zip. In the file name, SlotID and time indicate the slot ID and log generation time, respectively.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display log files of the log type generated from 08:12:12 on February 1, 2020 to 12:17:43 on February 2, 2020.
```
<HUAWEI> display logfile log list starttime 2020/2/1,08:12:12 endtime 2020/2/2,12:17:43
--------------------------------------------------------------------------------
LogType    LogFilePath                                       
--------------------------------------------------------------------------------
log        1#flash:/log.log 
log        1#flash:/log_17_20200202061829.log.zip                                              
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display logfile list** command output
| Item | Description |
| --- | --- |
| LogType | Log file type:   * log. * diagnose. * security. * operation. * debug. * maintain. |
| LogFilePath | Log file path. |