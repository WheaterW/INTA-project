display pm statistics
=====================

display pm statistics

Function
--------



The **display pm statistics** command displays the collected performance statistics.




Format
------

**display pm statistics** *taskname* **data-index** *index* [ **instance-type** *instance-type-name* [ **measure** *measure-name* | **instance** { *vpn-instance-name* } &<1-8> ] \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *taskname* | Displays the performance statistics of a specified performance statistics task. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |
| **data-index** *index* | Displays the performance statistics collected at a specified interval. | The value is an integer ranging from 0 to 16. |
| **instance-type** *instance-type-name* | Specifies the type of an instance bound to a performance statistics task. The instance type is predefined in a specific feature. Each instance type maps a feature. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| **measure** *measure-name* | Displays the performance statistics based on a specified counter. The performance counter is predefined for each feature. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| **instance** *vpn-instance-name* | Specifies the name of an instance of a specific type. The format of the instance name is predefined in each feature. | The value is a string of 1 to 255 case-insensitive characters, spaces supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the existing or historical performance statistics, run the display pm statistics command. The system can display the existing performance statistics and historical performance statistics collected at a maximum of 16 intervals.

**Prerequisites**

An instance has been bound to the existing performance statistics task and statistics counters have been configured.The performance statistics function has been enabled for the existing performance statistics task.

**Precautions**

To view the existing performance statistics, ensure that the performance statistics task is running.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the existing performance statistics of the performance statistics task a.
```
<HUAWEI> display pm statistics a data-index 0
Total measures count: 29
--------------------------------------------------------------------------------
Instance Type        : interface
Instance Name        : 10GE1/0/1
Measure Name         : in-discards
Measure Data         : 10
Valid Flag           : valid
Timestamp            : 2011-04-23 18:16:30 UTC-08:00

......

```

**Table 1** Description of the **display pm statistics** command output
| Item | Description |
| --- | --- |
| Total measures count | Total number of measures. |
| Instance Type | Type of an instance bound to a performance statistics task. |
| Instance Name | Type of an instance bound to a performance statistics task. |
| Measure Name | Name of a performance statistics counter. |
| Measure Data | Statistics counter.  0: The statistics counter is not supported. |
| Valid Flag | Valid flag of the performance statistics:   * no statistics: The performance statistics are not collected. * valid: The performance statistics are valid. * incredible value: The performance statistics are not reliable. * measure not configured: The statistics counter is disabled. |
| Timestamp | Date and time when the performance statistics were collected. The value is in the following format:   * YYYY-MM-DD HH:MM:SS. * YYYY-MM-DD HH:MM:SS UTC±HH:MM DST. * YYYY-MM-DD HH:MM:SS UTC±HH:MM. * YYYY-MM-DD HH:MM:SS DST.   UTC±HH:MM indicates that a time zone is set using the clock timezone command; DST indicates that the daylight saving time is set using the clock daylight-saving-time command. |