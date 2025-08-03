display cpu-usage threshold
===========================

display cpu-usage threshold

Function
--------



The **display cpu-usage threshold** command is used to show the CPU usage overload threshold and recovery threshold.




Format
------

**display cpu-usage threshold** [ **slot** *slotId* [ **cpu** *cpuid* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotId* | Specifies an available slot ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **cpu** *cpuid* | Specifies an available CPU ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays the alarm threshold and alarm clear threshold.

* When CPU usage reaches the alarm threshold, the system generates a CPU usage alarm.
* When CPU usage falls below the alarm clear threshold, the system generates a clear alarm.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the CPU overload configuration of the specified board.
```
<HUAWEI> display cpu-usage threshold slot 1 cpu 0
CPU monitor configuration                                                       
------------------------------------------------------------------------        
Slot      CPU         Interval  MonitorCycle  UnovloadLimit  OvloadLimit        
------------------------------------------------------------------------        
1         0             8(min)     10000(ms)            75%          90%

```

**Table 1** Description of the **display cpu-usage threshold** command output
| Item | Description |
| --- | --- |
| CPU | CPU number. |
| Slot | Slot number. |
| Interval | The statistical period. |
| MonitorCycle | The sampling period. |
| UnovloadLimit | The restore overload threshold of CPU usage. |
| OvloadLimit | Overload threshold for CPU usage. |