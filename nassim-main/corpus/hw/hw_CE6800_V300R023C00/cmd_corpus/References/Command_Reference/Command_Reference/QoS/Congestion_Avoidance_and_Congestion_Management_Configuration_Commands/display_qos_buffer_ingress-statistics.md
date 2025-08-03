display qos buffer ingress-statistics
=====================================

display qos buffer ingress-statistics

Function
--------



The **display qos buffer ingress-statistics** command displays information about discarded incoming packets in the buffer.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM:

**display qos buffer ingress-statistics** [ **slot** *slot-id* ]

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode):

**display qos buffer ingress-statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | - |
| **interface** *interface-name* | Specifies an interface name.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies an interface type.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *interface-number* | Specifies an interface number.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to check information about discarded incoming packets in the buffer of a chip, including the number of discarded packets, packet loss time, and interface where packet loss occurs. This helps monitor incoming traffic.

**Precautions**



For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL and CE6885-T models, if incoming traffic is discarded on an outbound interface, the statistics about discarded packets in the buffer in the inbound direction include the statistics about discarded packets in the outbound direction.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about discarded incoming packets in the buffer of a chip on the board in slot 1.
```
<HUAWEI> display qos buffer ingress-statistics slot 1
Slot : 1                                                                                                                            
  Chip                : 0                                                                                                          
  Dropped packets     : 89                                                                                                         
  Last dropping time  : 2020-10-09 23:49:08                                                                                        
  Tail drop occurs    : yes                                                                                                        
  WRED drop occurs    : yes 
  WRED drop interface : 100GE1/0/3   100GE1/0/4

```

# Display information about discarded incoming packets in the buffer on a specified interface.
```
<HUAWEI> display qos buffer ingress-statistics interface 100GE 1/0/1
Interface                   Dropped        Drop Rate   Drop Time
                     (Packets/Bytes)        (pps/bps)
----------------------------------------------------------------
100GE1/0/1                  78600000            44800 2023-05-06
                         10060800000         45875200   20:01:37
----------------------------------------------------------------

```

**Table 1** Description of the **display qos buffer ingress-statistics** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Chip | Chip ID. |
| Dropped packets | Number of discarded packets except tail dropped packets, including packets that are unexpectedly discarded due to WRED drop, packet reassembly error drop, and packet sorting error drop. |
| Dropped (Packets/Bytes) | Number of discarded packets and bytes. |
| Last dropping time | Last time when packets (excluding tail drop packets) are dropped. |
| Tail drop occurs | Whether tail drop occurs. |
| WRED drop interface | Interface where WRED drop occurs. |
| WRED drop occurs | Whether WRED drop occurs. |
| Interface | Interface type and number. |
| Drop Rate | Rate at which packets are discarded. |
| Drop Time | Last time when packet loss is detected. |