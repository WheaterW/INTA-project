display system resource usage
=============================

display system resource usage

Function
--------



The **display system resource usage** command displays KPI information.




Format
------

**display system resource usage** { **slot** *slotId* [ **cpu** *cpuID* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotId* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **cpu** *cpuID* | Specify the CPU ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **all** | Displays KPI information about all boards. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When you need to learn the overall running status of the device, run this command to view the key performance indicators (KPIs).

**Precautions**

1. If the value of Total/Used/Free in the Forward field is a number, the actual forwarding capability of the chip may be different from that of the device port.
2. If Total/Used/Free in the Forward field of the command output is -, the forwarding capability of the chip is related to the forwarding service model. The forwarding performance varies according to the forwarding process of different service packets. Therefore, the actual forwarding capability is not displayed, and only the forwarding capability usage is displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display KPI information in the specified slot.
```
<HUAWEI> display system resource usage slot 1
--------------------------------------------------------------------                                                                
Slot: 1    CPU:0                                                                                                                    
--------------------------------------------------------------------                                                                
Type           Total          Used           Free           Percent                                                                 
--------------------------------------------------------------------                                                                
CPU            100%           2%             98%            2%                                                                      
Memory         14540604       5867848        8672756        40%                                                                     
ACL            131072         0              131072         0%                                                                      
MAC            16384          0              16384          0%                                                                      
FIB4           2048000        6              2047994        0%                                                                      
FIB6           204800         0              204800         0%                                                                      
ARP            20480          1              20479          0%                                                                      
ND             4096           0              4096           0%                                                                      
--------------------------------------------------------------------

```

**Table 1** Description of the **display system resource usage** command output
| Item | Description |
| --- | --- |
| Type | KPI type, including CPU, memory, MAC, and ACL. |
| Total | Total number of KPIs. |
| Used | Current resource usage. |
| Free | Number of remaining resources. |
| Percent | Percentage of the current resource usage. |
| CPU | CPU ID. |
| Slot | Slot ID. |