display cpu-usage monitor history(All views)
============================================

display cpu-usage monitor history(All views)

Function
--------



The **display cpu-usage monitor history** command displays historical CPU usage overload information.




Format
------

**display cpu-usage monitor history** [ **slot** *slotId* [ **cpu** *cpuid* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotId* | Specifies a slot ID. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |
| **cpu** *cpuid* | Specifies a CPU ID. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display cpu-usage monitor history command to view the historical overload information about the CPU usage and the CPU usage when the CPU is overloaded.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays the historical overload information of the CPU usage of the specified board.
```
<HUAWEI> display cpu-usage monitor history slot 1 cpu 0
Slot: 1    CPU:0
CPU Overload history:
System CPU use rate is : 91%
OverloadTime : 2020-08-10 15:46:45
--------------------------------

```

**Table 1** Description of the **display cpu-usage monitor history(All views)** command output
| Item | Description |
| --- | --- |
| CPU | CPU id. |
| CPU Overload history | CPU overload history. |
| System CPU use rate is | CPU usage when the overload occurs. |
| OverloadTime | Time of overload occurs. |
| Slot | Slot num. |