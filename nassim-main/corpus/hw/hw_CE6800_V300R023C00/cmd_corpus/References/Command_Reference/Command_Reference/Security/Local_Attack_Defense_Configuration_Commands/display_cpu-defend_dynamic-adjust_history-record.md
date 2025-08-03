display cpu-defend dynamic-adjust history-record
================================================

display cpu-defend dynamic-adjust history-record

Function
--------



The **display cpu-defend dynamic-adjust history-record** command displays historical adaptive CPCAR adjustment records of protocol packets.




Format
------

For CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**display cpu-defend dynamic-adjust history-record** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-request** | **dhcp-reply** | **nd** } ] { **all** | **slot** *slot-id* }

For CE6885-LL (low latency mode):

**display cpu-defend dynamic-adjust history-record** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-request** | **dhcp-reply** } ] { **all** | **slot** *slot-id* }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display cpu-defend dynamic-adjust history-record** [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-discovery** | **dhcp-request** | **dhcp-reply** | **nd** } ] { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** | Specifies the packet type. | - |
| **arp-reply** | Specifies ARP reply packets. | - |
| **arp-request** | Specifies ARP request packets. | - |
| **arp-request-uc** | Specifies unicast ARP request packets. | - |
| **dhcp-discovery** | Specifies the broadcast packets sent by DHCP clients.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **dhcp-request** | Specifies the packets sent by DHCP servers. | - |
| **dhcp-reply** | Specifies the packets sent by DHCP clients. | - |
| **nd** | Specifies IPv6 neighbor discovery packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **all** | Specifies the device. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After adaptive CPCAR adjustment for protocol packets is enabled, you can run this command to view the historical adaptive CPCAR adjustment records of protocol packets. The information includes the adjustment time, CPCAR adjustments, and reason for the adjustments.You can use this command to check a maximum of 100 latest historical records.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display historical adaptive CPCAR adjustment records of protocol packets.
```
<HUAWEI> display cpu-defend dynamic-adjust history-record all
Dynamic-adjust history-record on slot 1:                                     
----------------------------------------------------------------------------------------                                                                        
Adjustment time     Packet type     Default/Previous/Current(pps) Reason       
2020-12-18 12:48:05 dhcp-request    1024    1408     1536          CPCAR drop packet                                                                            
2020-12-18 12:47:05 dhcp-request    1024    1280     1408          CPCAR drop packet                                                                            
2020-12-18 12:46:05 dhcp-request    1024    1152     1280          CPCAR drop packet                                                                            
2020-12-18 12:45:05 dhcp-request    1024    1024     1152          CPCAR drop packet                                                                            
----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend dynamic-adjust history-record** command output
| Item | Description |
| --- | --- |
| Dynamic-adjust history-record on slot 1 | Historical adaptive CPCAR adjustment records of protocol packets in a slot. |
| Adjustment time | Time when the CPCAR value was adjusted. |
| Packet type | Type of protocol packets. |
| Default/Previous/Current(pps) | Default: default CPCAR value (in pps).  Previous: CPCAR value after the last adjustment (in pps).  Current: current CPCAR value (in pps). |
| Reason | Reason for the adjustment:  CPCAR drop packet: Packet loss occurred due to CPCAR.  CPU queue drop packet: Packet loss occurred in the CPU queue.  CPU overload: The CPU was overloaded.  Set default: CPCAR was restored to the default value.  Main protocol change: The dynamic CAR of the main protocol changed. |