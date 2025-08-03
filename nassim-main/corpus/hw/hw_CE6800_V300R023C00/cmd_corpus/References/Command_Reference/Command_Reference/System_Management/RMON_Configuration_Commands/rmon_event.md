rmon event
==========

rmon event

Function
--------



The **rmon event** command configures a way to process an event: to record a log or send trap messages.

The **undo rmon event** cancels the configuration.



By default, no event is triggered. Therefore, no log is recorded, and no trap message is sent.


Format
------

**rmon event** *entry-number* [ **description** *string* ] { **log** | **trap** *object* | **log-trap** *object* | **none** } [ **owner** *owner-name* ]

**undo rmon event** *entry-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Specifies the index number of an event MIB entry. | The value is an integer ranging from 1 to 65535. |
| **description** *string* | Specifies an event description. | The value is a string of 1 to 127 characters.  If spaces are used, the string must start and end with double quotation marks ("). |
| **log** | Logs an event. | - |
| **trap** *object* | Indicates that events are processed by sending trap messages to the NMS with the specified community name or user name. | The value is a string of 1 to 127 characters. |
| **log-trap** *object* | The event is processed by recording logs and sending trap messages to the NMS with the specified community name or user name. | The value is a string of 1 to 127 characters. |
| **none** | Indicates events that do not trigger actions. If such an event occurs, the system will not handle it. | - |
| **owner** *owner-name* | Specifies the creator of the event entry. | The value is a string of 1 to 127 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The RMON threshold alarm function triggers events. The rmon event command can be used to set a way to process the events, to record a log or send trap messages to the NMS.

**Prerequisites**



An alarm object has been configured using the **rmon alarm** command after you configure the way to process a specified event.




Example
-------

# Enable a device to send a trap message about event 10 to an NMS.
```
<HUAWEI> system-view
[~HUAWEI] rmon event 10 trap public

```