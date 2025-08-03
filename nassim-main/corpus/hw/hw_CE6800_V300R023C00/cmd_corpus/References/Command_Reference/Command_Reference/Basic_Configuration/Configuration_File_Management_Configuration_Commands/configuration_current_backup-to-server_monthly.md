configuration current backup-to-server monthly
==============================================

configuration current backup-to-server monthly

Function
--------



The **configuration current backup-to-server monthly** command enables the function to upload a configuration file to the server on a specific date and time every month.

The **undo configuration current backup-to-server monthly** command disables this function.



By default, the function to upload a configuration file to the server on a specific date and time every month is disabled.


Format
------

**configuration current backup-to-server monthly date** *date-value* [ **time** *time-value* ]

**undo configuration current backup-to-server monthly**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **time** *time-value* | Specifies a time point. | The value is expressed in the format of HH:MM:SS, where HH:MM:SS indicates a second-specific time point. HH ranges from 0 to 23, and MM and SS both range from 0 to 59. The default value is 00:00:00. |
| **date** *date-value* | Specifies a date. | The value is an integer ranging from 1 to 31. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To upload a configuration file to the server on a specific date and time every month, run the configuration current backup-to-server monthly command.The configuration file generated after this command is a .dat file, and the generated time is local time.


Example
-------

# Upload a configuration file to the server at 12:12:12 on the first day every month.
```
<HUAWEI> system-view
[~HUAWEI] configuration current backup-to-server monthly date 1 time 12:12:12

```