display cpu-defend rate
=======================

display cpu-defend rate

Function
--------



The **display cpu-defend rate** command displays the rate of sending protocol packets to the CPU.




Format
------

**display cpu-defend rate** [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Specifies the packet type. | The packet type information displayed on the device prevails. You can run the display cpu-defend configuration command to check the supported packet types and rate limit. |
| **all** | Specifies all cards. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display cpu-defend rate command to view the rate of sending protocol packets to the CPU when checking the configuration of an attack defense policy. In this way, you can determine which type of protocols may attack the CPU based on the rate.To ensure normal operation of other services and protect the CPU, the rate of incremental protocol packets is calculated only in a specified period after you run the display cpu-defend rate command and displayed on the terminal. After you run this command, a message is displayed to wait for a while.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the rate of ARP request packets sent to the CPU.
```
<HUAWEI> display cpu-defend rate packet-type arp-request slot 1
Rate(PPS) on slot 1 :                                                                                                               
---------------------------------------------------------------                                                                     
PacketType                         Passed              Dropped                                                                      
---------------------------------------------------------------                                                                     
arp-request                             0                    0                                                                      
---------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend rate** command output
| Item | Description |
| --- | --- |
| Rate(PPS) on slot | Rate of packets to the CPU on the slot. |
| PacketType | Packet type. |
| Passed | Number of forwarded packets within one second. |
| Dropped | Number of discarded packets within one second. |