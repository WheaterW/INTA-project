clock datetime
==============

clock datetime

Function
--------



The **clock datetime** command sets the date and clock of a device.




Format
------

**clock datetime** [ **utc** ] *time* *date*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **utc** | Indicates the Universal Time Coordinated (UTC) time. | - |
| *time* | Specifies the current clock time in HH:MM:SS format. | HH specifies the hour, which is an integer ranging from 0 to 23. MM specifies the minute, which is an integer ranging from 0 to 59. SS specifies the second, which is an integer ranging from 0 to 59. |
| *date* | Specifies the current date in YYYY-MM-DD format. | YYYY specifies the yea, which is an integer ranging from 2000 to 2037. MM specifies the month, which is an integer ranging from 1 to 12. DD specifies the day, which is an integer ranging from 1 to 31. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In the application environment where absolute time is strictly required, the current date and clock of the device must be set. To set the date and clock of a device, run the clock datetime command.


Example
-------

# Set the date to 0:0:0 2020-01-01 for the Router.
```
<HUAWEI> clock datetime 0:0:0 2020-01-01

```