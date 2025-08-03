display rmon eventlog
=====================

display rmon eventlog

Function
--------



The **display rmon eventlog** command displays detailed information about an RMON event log.




Format
------

**display rmon eventlog** [ *entry-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Displays an RMON log with the index number of a specified event log table. If no index number is specified, logs about all events will be displayed. | The value is an integer ranging from 1 to 65535. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the **rmon event** command is used to configure to record a log when an event occurs, the system will automatically save the records of the event when it is triggered. To view the details about a log table, including the event index in the event table, current status, time when the event generates the log (in seconds since the system startup), and the event description, run the display rmon eventlog command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the log of RMON event 1.
```
<HUAWEI> display rmon eventlog 1
Event table 1 owned by User is valid.
  Generates eventLog 1.1 at 0days 00h:00m:07s.10th.
  Description: The 1.3.6.1.2.1.16.1.1.1.4.1 defined in alarm table 1 is less than or equal to 100 with alarm value 0. Alarm sample type is delta.

```

**Table 1** Description of the **display rmon eventlog** command output
| Item | Description |
| --- | --- |
| Event table 1 owned by User is valid. | Current status of the event log with the index number being entry-number created by the owner is status.   * entry-number: An index number of the event log. * owner: An owner. * status: * undercreation: The entry corresponding to the index is invalid. * valid: The entry corresponding to the index is valid. * invalid: The entry corresponding to the index is deleted. |
| Generates eventLog | Time elapsed from the time a device started to the time a log was generated. |
| Description | Event description. |