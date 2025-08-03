display cpu-defend filter statistics
====================================

display cpu-defend filter statistics

Function
--------



The **display cpu-defend filter statistics** command displays statistics about packets discarded by filters.




Format
------

**display cpu-defend filter statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display cpu-defend filter statistics** command displays discarded packets. This helps the network administrator configure attack defense policies.

**Precautions**

For loopback packets, only the number of lost packets can be collected, and the number of discarded bytes cannot.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays statistics about packets discarded by filters.
```
<HUAWEI> display cpu-defend filter statistics
--------------------------------------------------------------------------------                                                   
CPU defend policy 1 filter 1                                                                                                        
Slot 1                                                                                                                              
---------------------------------------------------------------------------------                                                   
  rule 1 deny ip source 1.1.1.1 0                                                                                                   
  Dropped Packets                     0, Dropped Bytes                          0                                                   
---------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend filter statistics** command output
| Item | Description |
| --- | --- |
| CPU defend policy | Applied cpu-defend policy. |
| Slot | Slot ID. |
| Dropped Packets | Number of discarded packets. |
| Dropped Bytes | Number of discarded bytes. |