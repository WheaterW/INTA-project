clock timezone
==============

clock timezone

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
| **add** | Indicates that the value of time-zone-name is the sum of the Universal Time Coordinated (UTC) time and offset. | The offset value ranges from 0 to 18. |
| **minus** | Indicates that the value of time-zone-name is the UTC time minus the offset. | The offset value ranges from 0 to 18. |
| *offset* | Specifies the offset between the time of the specified time zone and the UTC time. The value is in the format of HH:MM:SS, where HH specifies the hour, MM specifies the minute, and SS specifies the second. | The value of HH is an integer ranging from 0 to 18. The value of MM or SS is an integer ranging from 0 to 59. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you do not specify the time zone, a device uses the name of the default time zone.

**Precautions**

The specified time must be in 24-hour format.


Example
-------

# In Beijing, set the local time zone name to BJ.
```
<HUAWEI> clock timezone BJ add 08:00:00

```