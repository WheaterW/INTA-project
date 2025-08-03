clock daylight-saving-time (user view)
======================================

clock daylight-saving-time (user view)

Function
--------



The **clock daylight-saving-time** command sets the start time and end time of the daylight saving time.

The **undo clock daylight-saving-time** command deletes the daylight saving time setting.



By default, the daylight saving time is disabled.


Format
------

**clock daylight-saving-time** *dstname* **one-year** *start-time* *start-date* *end-time* *end-date* *offset*

**clock daylight-saving-time** *dstname* **repeating** *start-time* *repeat-start-date* *end-time* *repeat-end-date* *offset* [ *startyear* [ *endyear* ] ]

**clock daylight-saving-time** *dstname* **repeating** *start-time* { { **first** | **second** | **third** | **fourth** | **last** } *startweekday* *startmonth* *end-time* { **first** | **second** | **third** | **fourth** | **last** } *endweekday* *endmonth* } *offset* [ *startyear* [ *endyear* ] ]

**undo clock daylight-saving-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dstname* | Specifies the name of a DST zone. | The value is a string of 1 to 32 characters, spaces not supported. When quotation marks are used around the string, spaces are allowed in the string. |
| **one-year** *start-time* | Specifies the start time of the summer time to a certain year. It is in the format of HH:MM. The value of HH ranges from 0 to 23; the values of MM range from 0 to 59. | HH specifies the hour, which is an integer ranging from 0 to 23. MM specifies the minute, which is an integer ranging from 0 to 59. |
| *start-date* | specifies the start date, when configures summer time to a certain year. It is in the format of YYYY-MM-DD. The value of YYYY ranges from 2000 to 2037; the value of MM ranges from 1 to 12; the value of DD ranges from 1 to 31. | YYYY specifies the year, which is an integer ranging from 2000 to 2037. MM specifies the month, which is an integer ranging from 1 to 12. DD specifies the day, which is an integer ranging from 1 to 31. |
| *end-time* | specifies the end time. It is in the format of HH:MM. The value of HH ranges from 0 to 23; the values of MM range from 0 to 59. | HH specifies the hour, which is an integer ranging from 0 to 23. MM specifies the minute, which is an integer ranging from 0 to 59. |
| *end-date* | specifies the end date, when configures summer time to a certain year. It is in the format of YYYY-MM-DD. The value of YYYY ranges from 2000 to 2037; the value of MM ranges from 1 to 12, the value of DD ranges from 1 to 31. | YYYY specifies the year, which is an integer ranging from 2000 to 2037. MM specifies the month, which is an integer ranging from 1 to 12. DD specifies the day, which is an integer ranging from 1 to 31. |
| *offset* | Specifies the DST offset. | The value is in the format of HH:MM, where HH indicates the hour and MM indicates the minute. The value ranges from 00:01 to 02:00. |
| **repeating** *start-time* | Specifies the start time of the summer time to the years from a certain year. It is in the format of HH:MM. The value of HH ranges from 0 to 23; the values of MM range from 0 to 59. | HH specifies the hour, which is an integer ranging from 0 to 23. MM specifies the minute, which is an integer ranging from 0 to 59. |
| *repeat-start-date* | Specifies the start date, which is used to configure the periodic DST. | It is in the format of MM-DD. The value of MM ranges from 1 to 12; the value of DD ranges from 1 to 31. |
| *repeat-end-date* | Specifies the end date, which is used to configure the periodic DST. | It is in the format of MM-DD. The value of MM ranges from 1 to 12; the value of DD ranges from 1 to 31. |
| *startyear* | Specifies the start year, which is used to configure the periodic DST. | It is in the format of YYYY. The value of YYYY ranges from 2000 to 2037. |
| *endyear* | Specifies the end year, which is used to configure the periodic DST. The value of end-year must be greater than that of start-year. | It is in the format of YYYY. The value of YYYY ranges from 2000 to 2037. |
| **first** | Indicates the first working day in a specified month. | - |
| **second** | Indicates the second working day in a specified month. | - |
| **third** | Indicates the third working day in a specified month. | - |
| **fourth** | Indicates the fourth working day in a specified month. | - |
| **last** | Indicates the last working day in a specified month. | - |
| *startweekday* | Specifies the start weekday. | The value range is Mon, Tue, Wed, Thu, Fri, Sat, Sun. |
| *startmonth* | Specifies the start month. | The value range is Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov and Dec. |
| *endweekday* | Specifies the end weekday. | The value range is Mon, Tue, Wed, Thu, Fri, Sat, Sun. |
| *endmonth* | Specifies the end month. | The value range is Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov and Dec. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure rules for the daylight saving time based on the user's time zone, run the **clock daylight-saving-time** command. The configuration is invalid during 2000 to 2037. After the rules are configured, a device automatically uses the configured daylight saving time based on the rules.

**Configuration Impact**

Note the following issues:

* The time in messages such as logs and debugging information is the local time adjusted according to the time zone and the configured daylight saving time.
* The time in the output of the display commands is the local time adjusted based on the time zone and the configured daylight saving time.Before you remove the configuration of the daylight saving time, note the following points:
* If the configured daylight saving time has taken effect, after you remove the configuration of the daylight saving time, the device minus the offset of the daylight saving time.
* If the configured daylight saving time does not take effect, removing the configuration of the daylight saving time does not affect on the system time.

**Follow-up Procedure**

Run the **display clock** command to view detailed information about the system time after the configured daylight saving time takes effect.


Example
-------

# Set the daylight saving time named z2 starting from 2020-02-01, 11:22 and ending on 2020-08-11, 22:11, with an offset of 01:04.
```
<HUAWEI> clock daylight-saving-time z2 one-year 11:22 2020-02-01 22:11 2020-08-11 01:04

```

# Set the daylight saving time named z3 of repeating-date type with optional parameters start-year of 2012 and end-year of 2020 with an offset of 01:04.
```
<HUAWEI> clock daylight-saving-time z3 repeating 08:00 02-01 22:11 08-08 01:04 2012 2020

```