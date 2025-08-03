info-center timestamp
=====================

info-center timestamp

Function
--------



The **info-center timestamp** command sets the timestamp format for output information.

The **undo info-center timestamp** command restores the default timestamp format for output information.



The date format is used as the timestamp format for output information by default.


Format
------

**info-center timestamp log boot** [ **without-timezone** ]

**info-center timestamp trap boot** [ **without-timezone** ]

**info-center timestamp debugging boot** [ **without-timezone** ]

**info-center timestamp log date** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp log date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp log date precision-time millisecond** [ **without-timezone** ]

**info-center timestamp log short-date** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp log short-date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp log short-date precision-time millisecond** [ **without-timezone** ]

**info-center timestamp log format-date** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp log format-date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp log format-date precision-time millisecond** [ **without-timezone** ]

**info-center timestamp debugging date precision-time second** [ **without-timezone** ]

**info-center timestamp debugging date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp debugging date** [ **precision-time** **millisecond** ] [ **without-timezone** ]

**info-center timestamp debugging short-date precision-time second** [ **without-timezone** ]

**info-center timestamp debugging short-date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp debugging short-date** [ **precision-time** **millisecond** ] [ **without-timezone** ]

**info-center timestamp debugging format-date precision-time second** [ **without-timezone** ]

**info-center timestamp debugging format-date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp debugging format-date** [ **precision-time** **millisecond** ] [ **without-timezone** ]

**info-center timestamp trap date** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp trap date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp trap date precision-time millisecond** [ **without-timezone** ]

**info-center timestamp trap short-date** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp trap short-date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp trap short-date precision-time millisecond** [ **without-timezone** ]

**info-center timestamp trap format-date** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp trap format-date precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp trap format-date precision-time millisecond** [ **without-timezone** ]

**info-center timestamp log rfc-3339** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp log rfc-3339 precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp log rfc-3339 precision-time millisecond** [ **without-timezone** ]

**info-center timestamp trap rfc-3339** [ **precision-time** **second** ] [ **without-timezone** ]

**info-center timestamp trap rfc-3339 precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp trap rfc-3339 precision-time millisecond** [ **without-timezone** ]

**info-center timestamp debugging rfc-3339 precision-time second** [ **without-timezone** ]

**info-center timestamp debugging rfc-3339 precision-time tenth-second** [ **without-timezone** ]

**info-center timestamp debugging rfc-3339** [ **precision-time** **millisecond** ] [ **without-timezone** ]

**undo info-center timestamp log**

**undo info-center timestamp debugging**

**undo info-center timestamp trap**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **without-timezone** | Excludes time zone and DST information in the timestamp.   * If the without-timezone parameter is configured for logs, the log information sent to terminals, log files, log buffer, and log hosts does not carry time zone or DST information. * If the without-timezone parameter is configured for traps, the trap information sent to terminals, trap buffer, and log hosts does not carry time zone or DST information. * If the without-timezone parameter is configured for debugging information, the debugging information sent to terminals does not carry time zone or DST information. | - |
| **log** | Indicates logs. | - |
| **boot** | Uses relative time (the time elapsed since system startup) as the timestamp. The format is xxxxxx.yyyyyy. xxxxxx is the higher order 32 bits of the milliseconds elapsed since system startup; yyyyyy is the lower order 32 bits of the milliseconds elapsed since system startup. | - |
| **trap** | Indicates traps. | - |
| **debugging** | Indicates debugging information. | - |
| **date** | Uses the current system date and time in mm dd yyyy hh:mm:ss format. | - |
| **precision-time** | Sets the timestamp precision. | - |
| **second** | Sets the precision of the timestamp to seconds. | - |
| **tenth-second** | Sets the timestamp precision to 0.1 second. | - |
| **millisecond** | Sets the timestamp precision to milliseconds. | - |
| **short-date** | Uses the short date format. The short date format is almost the same as the date format, except that the year is not displayed in the short date format. | - |
| **format-date** | Uses the YYYY-MM-DD hh:mm:ss format. | - |
| **rfc-3339** | Uses the YYYY-MM-DD hh:mm:ss format. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The timestamp format of the information can be set to meet different time requirements in different places. For example, configure a format that does not include the year or uses the absolute time of system startup.The following are examples of the command output:

* Run the info-center timestamp { log | trap | debugging } date [ precision-time second ] command to set the date time format and time precision to second. A log example is as follows: Mar 26 2020 01:00:35+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } date without-timezone command to set the date time format to filter the timezone and DST information of the timestamp. A log example is as follows: Mar 26 2020 01:03:53 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } date precision-time millisecond command to set the date time format and time precision to millisecond. A log example is as follows: Mar 26 2020 01:10:05.720+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } date precision-time tenth-second command to set the date time format and time precision to 0.1s. A log example is as follows: Mar 26 2020 01:12:29.7+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } boot command to set the boot time format. A log example is as follows: 0.261958727 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } format-date [ precision-time second ] command to set the format-date time format and time precision to second. A log example is as follows: 2020-03-26 01:15:14+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } format-date without-timezone command to set the format-date to filter the timezone and DST information of the timestamp. A log example is as follows: 2020-03-26 01:15:58 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } format-date precision-time millisecond command to set the format-date time format and time precision to millisecond. A log example is as follows: 2020-03-26 01:17:05.726+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } format-date precision-time tenth-second command to set the format-date time format and time precision to 0.1s. A log example is as follows: 2020-03-26 01:18:17.7+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } short-date [ precision-time second ] command to set the short-date time format and time precision to second. A log example is as follows: Mar 26 01:20:17+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } short-date without-timezone command to set the short-date time format to filter the timezone and DST information of the timestamp. A log example is as follows: Mar 26 01:21:30 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } short-date precision-time millisecond command to set the short-date time format and time precision to millisecond. A log example is as follows: Mar 26 01:22:29.771+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } short-date precision-time tenth-second command to set the short-date time format and time precision to 0.1s. A log example is as follows: Mar 26 01:24:02.7+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } rfc-3339 [ precision-time second ] command to set the RFC 3339 time format and time precision to second. A log example is as follows: 2020-03-25T17:25:23+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } rfc-3339 without-timezone command to set the RFC 3339 time format to filter the timezone and DST information of the timestamp. A log example is as follows: 2020-03-25T17:53:28 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } rfc-3339 precision-time millisecond command to set the RFC 3339 time format and time precision to millisecond. A log example is as follows: 2020-03-26T01:26:32.809+08:00 HUAWEI \*\*\*.
* Run the info-center timestamp { log | trap | debugging } rfc-3339 precision-time tenth-second command to set the RFC 3339 time format and time precision to 0.1s. A log example is as follows: 2020-03-26T01:27:29.8+08:00 HUAWEI \*\*\*.

**Precautions**



When the precision of the timestamp precision is 0.1 second or a matter of milliseconds, timestamps are added to the information generated at a time in the information generation sequence.




Example
-------

# Set the timestamp format of the information to boot.
```
<HUAWEI> system-view
[~HUAWEI] info-center timestamp trap boot

```

# Set the precision of the timestamp.
```
<HUAWEI> system-view
[~HUAWEI] info-center timestamp log date precision-time millisecond
[~HUAWEI] info-center timestamp debugging date precision-time tenth-second
[~HUAWEI] info-center timestamp trap date precision-time millisecond

```