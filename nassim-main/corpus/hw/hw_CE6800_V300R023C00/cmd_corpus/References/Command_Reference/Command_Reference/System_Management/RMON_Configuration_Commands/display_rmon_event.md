display rmon event
==================

display rmon event

Function
--------



The **display rmon event** command displays RMON event configurations.




Format
------

**display rmon event** [ *entry-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Displays RMON event configurations with the index number of a specified entry in the event table. If no index number is specified, configurations about all events will be displayed. | The value is an integer ranging from 1 to 65535. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After configuring an RMON event table, to view the description of a configured event, whether a log is generated or trap messages are sent, and the latest time that an event occurred, run the display rmon event command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RMON event configurations.
```
<HUAWEI> display rmon event
Event table 1 owned by Huawei is valid.
  Description: null.
  Will cause log  when triggered, last triggered at 0days 00h:24m:10s.22th

```

**Table 1** Description of the **display rmon event** command output
| Item | Description |
| --- | --- |
| Event table 1 owned by Huawei is valid. | Current status of the event with the index number being entry-number created by the owner is status.   * entry-number: An index number of the event table entry. * owner: An owner. * status: * undercreation: The entry corresponding to the index is invalid. * valid: The entry corresponding to the index is valid. * invalid: The entry is deleted. |
| Will cause log when triggered | Behaviors triggered by an event, recording a log or sending trap messages.  The corresponding behaviors triggered by an event are as follows:   * none: No action is taken. * log: Records a log. * snmp-trap: Sends trap messages to the NMS. * log-trap: Records a log and sending trap messages to the NMS. |
| last triggered at | Date and time when the latest event occurred. |
| Description | Event description. |