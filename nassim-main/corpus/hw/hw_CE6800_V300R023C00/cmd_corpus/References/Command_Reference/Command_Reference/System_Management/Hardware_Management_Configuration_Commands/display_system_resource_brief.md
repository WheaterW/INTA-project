display system resource brief
=============================

display system resource brief

Function
--------



The **display system resource brief** command displays brief CPU and memory information.




Format
------

**display system resource brief**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check brief CPU and memory information, run the display system resource brief command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Summarize CPU and memory information.
```
<HUAWEI> display system resource brief
----------------------------------------------------------------------------------------                                            
Slot                        CPU Usage  Memory Usage(Used/Total)     DataPlane CPU Usage                                             
----------------------------------------------------------------------------------------                                            
1     MPU(Master)           21%        22%   6084MB/27001MB         0%                                                              
----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display system resource brief** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID of a board. |
| CPU Usage | System CPU usage. |
| Memory Usage(Used/Total) | System memory usage. |
| DataPlane CPU Usage | CPU usage of the data plane. |