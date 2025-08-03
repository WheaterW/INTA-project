display time-range
==================

display time-range

Function
--------

The **display time-range** command displays a specified or all time ranges.



Format
------

**display time-range** *time-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-name* | Specifies the name of a time range. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. The value must start with a letter.   * The name of a user-defined time range cannot be set to all. * The display time-range all command displays information about all user-defined time ranges configured in the system. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To check detailed information about a time range, check whether a time range takes effect, or filter packets based on time ranges, run the **display time-range** command.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display information about all time ranges.
```
<HUAWEI> display time-range all
Current time is 2020-06-23 09:12:30 Tuesday

Time-range : time1 ( Inactive )
 10:00 to 12:00 daily

```


**Table 1** Description of the
**display time-range** command output

| Item | Description |
| --- | --- |
| Current time | Current time of the system. |
| Time-range | Time range name. |
| Inactive | The time range is inactive at the current time. The status of a time range can be inactive or active. |