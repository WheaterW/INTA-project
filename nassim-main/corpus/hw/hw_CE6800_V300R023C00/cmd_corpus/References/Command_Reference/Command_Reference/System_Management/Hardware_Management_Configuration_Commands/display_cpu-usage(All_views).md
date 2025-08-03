display cpu-usage(All views)
============================

display cpu-usage(All views)

Function
--------



The **display cpu-usage** command is used to show the CPU usage of boards and the CPU usage of services.




Format
------

**display cpu-usage** [ **slot** *slotid* [ **cpu** *cpuID* ] | **all** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotid* | Specifies an available slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **cpu** *cpuID* | Specifies the CPU ID. If this parameter is not specified, the cpu-usage of CPU 0 is displayed. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **all** | Displays the CPU usage information and service usage CPU information of all boards. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

CPU usage is an important index to evaluate device performance. A high CPU usage will cause service faults. You can use the display cpu command to view CPU usage to check whether devices are working properly.

**Precautions**

It is abnormal if the CPU usage remains high when services are not deployed on a large scale. In this case, check the device for the reason of the abnormality.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the CPU usage information of the specified board.
```
<HUAWEI> display cpu-usage slot 1 cpu 0
Slot: 1    CPU:0
CPU utilization statistics at 2019-12-07 13:57:10 689 ms
System CPU Using Percentage :  31%
Dataplane CPU Using Percentage :   13%
CPU utilization for five seconds: 39%, one minute: 38%, five minutes: 39%.
Max CPU Usage :                91%
Max CPU Usage Stat. Time : 2019-12-06 17:05:50 521 ms
State: Unoverload
Overload threshold:  90%, Overload clear threshold:  75%, Duration:  60s
---------------------------
CPU Usage Details
----------------------------------------------------------------
CPU     Current  FiveSec   OneMin  FiveMin  Max MaxTime
----------------------------------------------------------------
cpu0        35%      35%      35%      36%  95% 2019-12-06 17:05:10
cpu1        26%      26%      26%      26%  26% 2019-12-06 17:03:35
cpu2        16%      16%      13%      14%  89% 2019-12-06 18:14:50
cpu3        50%      50%      50%      50%  84% 2019-12-06 17:03:50
----------------------------------------------------------------

```

**Table 1** Description of the **display cpu-usage(All views)** command output
| Item | Description |
| --- | --- |
| CPU | CPU ID. |
| CPU utilization statistics at 2019-12-07 13:57:10 689 ms | Time when CPU usage information is obtained. |
| CPU utilization for five seconds | Indicates the CPU usage in five seconds. |
| CPU Usage Details | Detailed information about the usage of each CPU core. |
| System CPU Using Percentage | Indicates the CPU usage of the system. |
| Dataplane CPU Using Percentage | CPU usage of the data plane. |
| five minutes | Indicates the CPU usage within 5 minutes. |
| one minute | Indicates the CPU usage within one minute. |
| Max CPU Usage | Maximum CPU usage. |
| Max CPU Usage Stat. Time | Time when the maximum CPU usage is collected. |
| Max | Maximum CPU usage. |
| Overload threshold | Overload threshold. |
| Overload clear threshold | Overload clearance threshold. |
| Current | Current CPU usage. |
| FiveSec | CPU usage for five seconds. |
| OneMin | CPU usage for one minute. |
| FiveMin | CPU usage for 5 minutes. |
| MaxTime | Time when the maximum CPU usage occurs. |
| Slot | Slot ID. |
| State | Overload status. |
| Duration | Measurement interval. |
| CPUx | CPU core. |