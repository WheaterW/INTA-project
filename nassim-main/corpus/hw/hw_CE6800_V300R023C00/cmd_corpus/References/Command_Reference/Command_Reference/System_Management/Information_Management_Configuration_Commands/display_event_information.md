display event information
=========================

display event information

Function
--------



The **display event information** command displays specified or all event information.




Format
------

**display event information**

**display event information name** *event-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *event-name* | The name of event. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view specified event information or information about all events in the system, such as the event name and level, run the display event information command.

If an event name is not specified using name event-name, information about all events in the system will be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display registration information about the CFG\_FILE\_CHANGE event.
```
<HUAWEI> display event information name CFG_FILE_CHANGE
-----------------------------------------------------------------------------
Feature    : CONFIGURATION
EventId    : 0x8150001
EventName  : CFG_FILE_CHANGE
EventLevel : informational
-----------------------------------------------------------------------------

```

# Display registration information about all events in the system.
```
<HUAWEI> display event information
-----------------------------------------------------------------------------
Feature         : CONFIGURATION
EventId         : 0x8150016
EventName       : RUNNING_CFG_CHANGE
EventLevel      : informational

Feature         : NETCONF
EventId         : 0x818104F
EventName       : NCA_SYNC_CONFIG_FAIL
EventLevel      : error
-----------------------------------------------------------------------------

```

**Table 1** Description of the **display event information** command output
| Item | Description |
| --- | --- |
| Feature | Event feature. |
| EventId | Event ID. |
| EventName | Event name. |
| EventLevel | Event level. |