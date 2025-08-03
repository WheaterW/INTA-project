display memory threshold(All views)
===================================

display memory threshold(All views)

Function
--------



The **display memory threshold** command is used to query the memory usage threshold for generating an alarm and the memory usage threshold for clearing the alarm.




Format
------

**display memory threshold** [ **slot** *slotId* [ **cpu** *cpuID* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotId* | Specifies a CPU ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **cpu** *cpuID* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can view the memory usage threshold to view the conditions for triggering alarms.

* When the memory usage reaches the threshold, the system generates an alarm.
* When the memory usage falls below the threshold, the system clears the alarm.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the memory overload configuration of the specified board.
```
<HUAWEI> display memory threshold slot 1 cpu 0
memory-monitor configuration         
------------------------------------------------------------------------  
Slot   CPU    MonitorNum  MonitorCycle  UnovloadLimit  OvloadLimit    
------------------------------------------------------------------------   
1      0               6     10000(ms)            75%          95%

```

**Table 1** Description of the **display memory threshold(All views)** command output
| Item | Description |
| --- | --- |
| MonitorNum | The number of sampling points. |
| MonitorCycle | The sampling period. |
| UnovloadLimit | The restore overload threshold of memory usage. |
| OvloadLimit | Overload threshold for memory usage. |