clock timezone (System view)
============================

clock timezone (System view)

Function
--------



The **clock timezone** command configures the local time zone.

The **undo clock timezone** command restores default Universal Time Coordinated (UTC).

If you do not specify the time zone name, the system uses the name of DefaultZoneName.



The default local time zone is Universal Time Coordinated (UTC).


Format
------

**clock timezone** *time-zone-name* { **add** | **minus** } *offset*

**undo clock timezone**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-zone-name* | Specifies the name of a time zone. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  If quotation marks are used around the string, spaces are allowed in the string. |
| **add** | Indicates that the offset is added to the value of the specified time zone, and the result is equal to the Universal Time Coordinated (UTC) time. Conversely, the default UTC time minus offset is equal to the time of time-zone-name. | The value ranges from 0 to 18. |
| **minus** | Indicates that the UTC time is equal to the time zone minus the offset. Conversely, the sum of the default UTC time, and offset is equal to the time of time-zone-name. | The value ranges from 0 to 18. |
| *offset* | Specifies the offset between the time of the specified time zone and the UTC time. It is in the format of HH:MM:SS. HH specifies hours. MM and SS indicate minutes and seconds, respectively. | HH ranges from 0 to 18. MM and SS range from 0 to 59. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you do not specify the time zone, a device uses the name of the default time zone.The time must be specified in the 24-hour format. If you do not specify MM or SS, their value is 0. You must enter at least one digit number to specify HH. For example, when you enter 0, the time is 00:00:00.After the configurations take effect, run the **display clock** command to view the configurations. The time in logs and diagnostic information uses the local time adjusted based on the time zone and DST.

**Precautions**

The specified time must be in 24-hour format.


Example
-------

# In Beijing, set the local time zone name to BJ.
```
<HUAWEI> system-view
[~HUAWEI] clock timezone BJ add 08:00:00

```