display default-parameter interface
===================================

display default-parameter interface

Function
--------



The **display default-parameter interface** command displays the default configurations of an interface, including the interface status, maximum transmission unit (MTU), interval at which Request messages are sent to the peer, interval at which traffic statistics are collected, trap threshold, interface description, whether the alarm function is enabled to send an alarm to the network management system (NMS) when the interface status changes.




Format
------

**display default-parameter interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the default name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



If the default configurations of an interface are modified, to view the default configurations of the interface, run the display default-parameter interface command.



**Precautions**



Only created interfaces can be displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the default configurations of an interface.
```
<HUAWEI> display default-parameter interface 100GE 1/0/1
Interface state: undo shutdown
 Flow-stat interval: 300s
 Trap-threshold: input-rate 90, output-rate 90
 Snmp trap updown: enable
 Description:

```

**Table 1** Description of the **display default-parameter interface** command output
| Item | Description |
| --- | --- |
| Interface state | Default status of an interface:   * shutdown: The shutdown command is configured in the interface view by default. * undo shutdown: The undo shutdown command is configured in the interface view by default.   You can run the shutdown command or the undo shutdown command in the interface view to change the status of the interface. |
| Flow-stat interval | Interval at which traffic statistics are collected on the interface.  You can run the set flow-stat interval command in the interface view to set the interval for collecting the traffic statistics on the interface. |
| Snmp trap updown | Whether an alarm message is sent to the NMS if the interface status changes:   * disable: No alarm message is sent to the NMS if the interface status changes. * enable: An alarm message is sent to the NMS if the interface status changes.   You can run the enable snmp trap updown command in the interface view to enable the sending of an alarm message to the NMS when the interface status changes. |
| Trap-threshold | Trap threshold for the outbound and inbound bandwidth utilization on the interface. |
| Description | Description of the interface.  If the description command is not used to configure the interface description, the description is empty by default. |