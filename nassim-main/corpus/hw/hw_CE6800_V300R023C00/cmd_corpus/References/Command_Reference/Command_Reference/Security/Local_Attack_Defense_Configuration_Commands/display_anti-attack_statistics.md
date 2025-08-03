display anti-attack statistics
==============================

display anti-attack statistics

Function
--------



The **display anti-attack statistics** command displays statistics about a specified type of attack defense.




Format
------

**display anti-attack statistics** [ **abnormal** | **fragment** | **tcp-syn** | **udp-flood** | **icmp-flood** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **abnormal** | Displays the statistics about defense against malformed packets. | - |
| **fragment** | Displays the statistics about defense against packet fragments. | - |
| **tcp-syn** | Displays the statistics about defense against TCP SYN flood. | - |
| **udp-flood** | Displays the statistics about defense against UDP flood. | - |
| **icmp-flood** | Displays the statistics about defense against ICMP flood. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The AntiAtkType field in the output includes Abnormal, Fragment, TCP-Syn, UDP-flood, or ICMP-flood.The content of the command output includes the total number of packets, number of passing packets, and number of discarded packets.If no parameter is specified, the display anti-attack statistics command displays statistics about attack packets of all types.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display attack defense statistics.
```
<HUAWEI> display anti-attack statistics
Packets Statistic Information:                                                  
------------------------------------------------------------------------------- 
AntiAtkType  TotalPacketNum        DropPacketNum         PassPacketNum          
             (H)        (L)        (H)        (L)        (H)        (L)         
------------------------------------------------------------------------------- 
Abnormal      0          0          0          0          0          0          
Fragment      0          0          0          0          0          0          
Icmp-flood    0          0          0          0          0          0          
Tcp-syn       0          58         0          0          0          58         
Udp-flood     0          0          0          0          0          0          
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display anti-attack statistics** command output
| Item | Description |
| --- | --- |
| Packets Statistic Information | Packets statistics. |
| AntiAtkType | Indicates attack defense types, including:  * Abnormal: defense against malformed packets. * Fragment: defense against packet fragments. * Tcp-syn: defense against TCP SYN flood. * Udp-flood: defense against UDP flood. * Icmp-flood: defense against ICMP flood. |
| TotalPacketNum | Total number of packets. |
| DropPacketNum | Number of packets that are discarded. |
| PassPacketNum | Number of packets that pass through. |
| (H) | Highest-order bit display. |
| (L) | Lowest-order bit display. |