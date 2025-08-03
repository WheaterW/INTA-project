callhome
========

callhome

Function
--------



The **callhome** command creates a callhome template and then displays the callhome template view or displays the view of an existing callhome template directly.

The **undo callhome** command deletes an existing callhome template.



By default, no callhome template is created.


Format
------

**callhome** *callhome-name*

**undo callhome** *callhome-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *callhome-name* | Specifies the name of a callhome template. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed in double quotation marks ("). |



Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an NMS does not support automatic device discovery, it cannot manage devices in time. To address this problem, you can configure proactive NETCONF registration for a device to send a NETCONF connection request to the NMS when the device goes online so that the NMS can manage the device.When configuring proactive NETCONF registration, you need to create a callhome template using the **callhome** command and create a NETCONF connection instance in the template using the **endpoint** command or configure an interval at which the device sends NETCONF connection requests to the NMS using the **reconnection interval** command.

**Precautions**

A device supports only one callhome template. To configure a new callhome template, run the **undo callhome** command to delete the existing one first.


Example
-------

# Create a callhome template named root and enter the callhome template view.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] callhome root
[*HUAWEI-netconf-callhome-root]

```