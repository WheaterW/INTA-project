time-range
==========

time-range

Function
--------



The **time-range** command sets a time range to describe a certain period of time.

The **undo time-range** command deletes a time range.



By default, no time range is configured.


Format
------

**time-range** *time-name* [ { *time1* **to** *time2* { *days* } &<1-7> | **from** *time1* *date1* [ **to** *time2* *date2* ] } ]

**undo time-range** *time-name* [ *time1* **to** *time2* { *days* } &<1-7> | **from** *time1* *date1* [ **to** *time2* *date2* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-name* | Specifies a time range name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with an uppercase or lowercase letter. In addition, the word all cannot be specified as a time range name. |
| *time1* | Specifies the start time. | The value is in the format of hh:mm. hh stands for hour, and the value of hh ranges from 0 to 23. mm stands for minute, and the value of mm ranges from 0 to 59. If the parameter is configured more than once, all configurations take effect. |
| **to** *time2* | Specifies the end time. | The value is in the format of hh:mm. hh stands for hour, and the value of hh ranges from 0 to 23. mm stands for minute, and the value of mm ranges from 0 to 59. If the parameter is configured more than once, all configurations take effect. |
| **to** *time2* *date2* | Specifies a time on a day when a time range ends. The end time must be later than the start time. | The value of time-date1 is in the format of hh:mm. hh stands for hour, and the value of hh ranges from 0 to 23. mm stands for minute, and the value of mm ranges from 0 to 59. time-date2 is in the format of YYYY/MM/DD. DD stands for day, and its value is an integer ranging from 1 to 31. MM stands for month, and its value is an integer ranging from 1 to 12. YYYY stands for year, and its value is an integer ranging from 2000 to 2037.  * If the parameter is configured more than once, all configurations take effect. * If the end time is not specified, the system uses the allowed maximum value. |
| *days* | Specifies the days in a week when a time range takes effect. | The value can be set to any of the following:   * 0 to 6 * Any day in a week * Workdays: any day from Monday to Friday * Weekend: Sunday or Saturday * Daily: all days in a week |
| **from** *time1* *date1* | Specifies a time on a day when a time range starts. | The value of time-date1 is in the format of hh:mm. hh stands for hour, and the value of hh ranges from 0 to 23. mm stands for minute, and the value of mm ranges from 0 to 59. time-date2 is in the format of YYYY/MM/DD. DD stands for day, and its value is an integer ranging from 1 to 31. MM stands for month, and its value is an integer ranging from 1 to 12. YYYY stands for year, and its value is an integer ranging from 2000 to 2037. If the parameter is configured more than once, all configurations take effect. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When certain services or functions need to take effect at a specified time or during a specified period, run the **time-range** command to set a time range as required. When a time range takes effect or expired, a configuration change event is generated and the configuration change log is recorded.

* A relative time range, also called a cyclic time range, is cyclic and the cycle is one week. A cyclic time range is defined by start-time and end-time. days specifies the day in a week when a cyclic time range takes effect.
* An absolute time range is defined by from and to. Absolute time ranges are not cyclic.Usually, absolute and relative time ranges are used together. An absolute time range defines a time range, and a relative time range specifies the day in a week when the defined time range takes effect.

**Follow-up Procedure**

Run the **rule** command with time-range configured to set a validity period for an ACL.

**Precautions**

Multiple time ranges that share one name can be set to specify a time range. Time ranges under the same name can be set based on the following principles:

* The combination of time ranges is used if there are only absolute or relative time ranges. If the current time of the device matches a relative or absolute time range, the matched time range takes effect. For example, Monday and Wednesday are two relative time ranges. The time range takes effect both every Monday and Wednesday.
* When both absolute and relative time ranges exist, the intersection of the combination of absolute time ranges and the combination of relative time ranges is used. If the current time of the device matches both a relative time range and an absolute time range, the overlapping part of the matched time ranges takes effect. For example, January 2009 is an absolute time range, and each Monday is a relative time range. In this case, the time range takes effect only on each Monday of January 2009.To ensure the validity of the time range referenced by services, configure the time range as the validity period of the specified ACL rule.You can configure a time range instance without specifying a relative or absolute time range. For example, you can configure a time range instance aa using the **time-range aa** command. If a relative or absolute time range that needs to be deleted is the last record of a time range instance, the time range instance is deleted synchronously. For example, when you delete a time range record using the undo time-range aa 12:00 to 18:00 daily command, the time range instance aa is deleted synchronously if the time range to be deleted is the last record of the instance.

Example
-------

# Set the time range named test to take effect from 08:00 to 18:00 on Monday through Friday every week.
```
<HUAWEI> system-view
[~HUAWEI] time-range test 8:00 to 18:00 working-day

```

# Set the time range named test to take effect from 8:30 a.m. of January 1, 2013 to 6 p.m. of December 31, 2013.
```
<HUAWEI> system-view
[~HUAWEI] time-range test from 08:30 2013/1/1 to 18:00 2013/12/31

```

# Set the time range named test to take effect at 00:00 on January 1, 2009 and remains valid till the allowed maximum time value of the system.
```
<HUAWEI> system-view
[~HUAWEI] time-range test from 0:0 2009/1/1

```

# Set the time range named test to take effect from 14:00 to 18:00 on every Saturday and Sunday.
```
<HUAWEI> system-view
[~HUAWEI] time-range test 14:00 to 18:00 off-day

```