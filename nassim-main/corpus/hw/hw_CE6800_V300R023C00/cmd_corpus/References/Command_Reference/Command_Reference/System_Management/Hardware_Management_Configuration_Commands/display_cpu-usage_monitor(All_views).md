display cpu-usage monitor(All views)
====================================

display cpu-usage monitor(All views)

Function
--------



The **display cpu-usage monitor** command is used to show the overload information of the CPU usage.




Format
------

**display cpu-usage monitor** { **slot** *slotID* [ **cpu** *cpuID* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotID* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **cpu** *cpuID* | Specify the CPU ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **all** | Display the CPU overload information on all boards. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When the CPU usage is high, run the display cpu monitor command to check whether the CPU is overloaded. If the CPU is overloaded, the administrator can take actions to reduce the CPU usage and ensure that the device is operating properly.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the CPU overload information of the specified board.
```
<HUAWEI> display cpu-usage monitor slot 1 cpu 0
CPU overload information
--------------------------------------------------------------------
Slot       CPU       Time                     State
--------------------------------------------------------------------
1         0         2019-09-18 07:41:51      Overload
--------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-usage monitor(All views)** command output
| Item | Description |
| --- | --- |
| CPU | CPU id. |
| CPU overload information | CPU overload information. |
| Slot | Slot num. |
| Time | The time when an overload or unoverload occurs. |
| State | CPU overload status. |