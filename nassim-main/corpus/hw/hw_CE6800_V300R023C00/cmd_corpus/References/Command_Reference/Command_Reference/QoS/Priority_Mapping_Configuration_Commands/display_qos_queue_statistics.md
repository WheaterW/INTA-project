display qos queue statistics
============================

display qos queue statistics

Function
--------



The **display qos queue statistics** command displays queue-based traffic statistics on an interface.




Format
------

**display qos queue statistics** { **interface** *interface-name* | **interface** *interface-type* *interface-number* | **slot** *slotid* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **slot** *slotid* | Displays statistics about traffic in queues on all interfaces of a specified slot. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check whether packets in each queue on an interface are forwarded or discarded because of congestion, view the statistics on each queue on the interface.

**Precautions**

* Queue-based traffic statistics collection on an interface is accurate to 2 minutes. That is, the statistics are correct after 2 minutes.
* If the function of capturing discarded packets is enabled, statistics on discarded packets cannot be collected.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display queue-based traffic statistics on all interfaces of the device.
```
<HUAWEI> display qos queue statistics slot 1
 Queue statistics info: interface 10GE1/0/1                                                                                       
 ----------------------------------------------------------------------------------------------                                     
 Queue   CIR/PIR              Passed     Pass Rate             Dropped     Drop Rate  Drop Time                                     
     (% or kbps)     (Packets/Bytes)     (pps/bps)     (Packets/Bytes)     (pps/bps)                                                
 ----------------------------------------------------------------------------------------------                                     
     0         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     1         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     2         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     3         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     4         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     5         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     6         0                1330             0                   0             0          -                                     
       100000000              195356           152                   0             0                                                
 ----------------------------------------------------------------------------------------------                                     
     7         0                   0             0                   0             0          -                                     
       100000000                   0             0                   0             0                                                
 ----------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display qos queue statistics** command output
| Item | Description |
| --- | --- |
| Queue | Queue index. |
| Queue statistics info | Queue-based traffic statistics. |
| Passed | Number of forwarded packets and bytes. |
| Pass Rate | Rate of forwarded packets, in pps or bit/s. If the information is displayed as -, the statistics on this item cannot be collected. |
| Drop Rate | Number of discarded packets and bytes. |
| Drop Time | Last time packet loss was detected. |
| CIR | Committed information rate. By default, the CIR is displayed as 0. If the CIR is configured for queue shaping, the configured CIR is displayed. |
| PIR | Peak information rate. By default, the maximum bandwidth of an interface is displayed. If the PIR is configured for queue shaping, the configured PIR is displayed. |
| Dropped(Packets/Bytes) | Number of discarded packets and bytes. |