display memory(All views)
=========================

display memory(All views)

Function
--------



The **display memory** command displays the memory usage of a specific card.




Format
------

**display memory** [ { **all** | **slot** *slotid* [ **cpu** *cpuID* ] } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays the memory usage of all boards. | - |
| **slot** *slotid* | Specifies the slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **cpu** *cpuID* | Specifies the CPU ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the memory usage of a specific card.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the memory usage of a card.
```
<HUAWEI> display memory
Slot: 1   CPU: 0                                                                                                                    
Total Physical Available Memory: 3857648 Kbytes                                                                                               
Total Physical Memory Used: 2297184 Kbytes                                                                                          
Physical Memory Using Percentage: 59%                                                                                               
State: Unoverload                                                                                                                   
Overload threshold:  95%, Overload clear threshold:  75%, Duration: 60s                                                           
-----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display memory(All views)** command output
| Item | Description |
| --- | --- |
| Total Physical Available Memory | Total available physical memory. |
| Total Physical Memory Used | Used physical memory. |
| Physical Memory Using Percentage | Physical memory usage. |
| Overload threshold | Memory overload threshold. |
| Overload clear threshold | Memory non-overload threshold. |
| Slot | Slot ID. |
| CPU | CPU ID. |
| State | Memory overloading status. |
| Duration | Interval for measuring the memory usage. |