display cpu-defend statistics
=============================

display cpu-defend statistics

Function
--------



The **display cpu-defend statistics** command displays statistics on packets sent to the CPU.




Format
------

**display cpu-defend statistics** [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Displays statistics on the specified type of protocol packets. packet-type specifies the packet type.   * If packet-type is specified, statistics on the specified type of protocol packets are displayed. * If packet-type is not specified, statistics on all protocol packets are displayed. | The packet type information displayed on the device prevails. You can run the display cpu-defend configuration command to check the supported packet types and rate limit. |
| **all** | Displays statistics on all slots. | - |
| **slot** *slot-id* | Specifies the ID of the device. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The display cpu-defend statistics command displays statistics on packets sent to the CPU, including the number of forwarded and discarded packets. This helps the network administrator configure attack defense policies.

**Precautions**

When the ICMP fast reply function is enabled, statistics on ICMPv4 and ICMPv6 packets are not differentiated. The total number of ICMPv4 and ICMPv6 packets is recorded in the icmp field.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all CAR statistics on the devices.
```
<HUAWEI> display cpu-defend statistics all
Statistics(packets) on slot 1 :                                                                                                     
--------------------------------------------------------------------------------                                                    
PacketType               Total Passed        Total Dropped   Last Dropping Time                                                     
                    Last 5 Min Passed   Last 5 Min Dropped                                                                          
--------------------------------------------------------------------------------                                                    
arp-miss                            0                    0   -                                                                      
                                    0                    0                                                                          
arp-reply                           1                    0   -                                                                      
                                    1                    0                                                                          
arp-request                      1387                    0   -                                                                      
                                  100                    0                                                                          
arp-request-uc                      3                    0   - 
....

```

**Table 1** Description of the **display cpu-defend statistics** command output
| Item | Description |
| --- | --- |
| Statistics(packets) on slot | Packet statistics on the slot. |
| PacketType | Packet type. |
| Total Passed | Total number of forwarded packets. |
| Total Dropped | Total number of discarded packets. |
| Last 5 Min Passed | Number of packets forwarded in the last 5 minutes. |
| Last 5 Min Dropped | Number of packets discarded in the last 5 minutes. |
| Last Dropping Time | Last packet discarding time. |