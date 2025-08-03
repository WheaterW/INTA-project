display traffic-analysis udp cache
==================================

display traffic-analysis udp cache

Function
--------



The **display traffic-analysis udp cache** command displays detailed information about intelligent traffic analysis results for UDP flows.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-analysis udp cache** [ **source-ip** *source-ip-address* | **destination-ip** *destination-ip-address* | **vni** *vniid* | **interface** { *iftype* *interface-number* | *ifname* } ] \* **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-ip** *source-ip-address* | Specifies the source IP address. | The value is in dotted decimal notation. |
| **destination-ip** *destination-ip-address* | Specifies the destination IP address. | The value is in dotted decimal notation. |
| **vni** *vniid* | Specifies a VXLAN network identifier (VNI). | The value is an integer that ranges from 1 to 16777215. |
| **interface** | Specifies an interface. | - |
| *iftype* | Specifies the interface type. | - |
| *interface-number* | Specifies the interface index. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| *ifname* | Specifies the interface name. | - |
| **slot** *slot-id* | Specifies the ID of a device. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view detailed information about intelligent traffic analysis results for UDP flows on a switch in real time. If a UDP flow arrives at the same switch again from another interface, the system records a new flow table. If the UDP flow arrives at this switch from a third or more other interfaces, the system will not update the existing two flow tables.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed information about intelligent traffic analysis results for UDP flows on a switch.
```
<HUAWEI> display traffic-analysis udp cache slot 1
Source IP           : 10.1.1.1            
Destination IP      : 172.16.1.1            
Source Port         : 8                   
Destination Port    : 9                   
Direction           : InBound              
Interface           : 10GE1/0/1            
Flow Start Time     : 2023-06-21 17:14:06 
VNI                 : --                   
-----------------------------------------------------------------------------------------
Status              Block Id     Block Timestamp     Receive Packets       Receive Bytes
-----------------------------------------------------------------------------------------
Previous                  88           703941389                 256               22016 
Current                   89           871065860                 133               11438
-----------------------------------------------------------------------------------------
Source IP           : 10.1.1.1            
Destination IP      : 172.16.1.1            
Source Port         : 3                   
Destination Port    : 6                   
Direction           : InBound              
Interface           : 10GE1/0/1            
Flow Start Time     : 2023-06-21 17:14:06 
VNI                 : --                   
-----------------------------------------------------------------------------------------
Status              Block Id     Block Timestamp     Receive Packets       Receive Bytes
-----------------------------------------------------------------------------------------
Previous                  --                  --                  --                  -- 
Current                    0           596944031               34342            25497796
-----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-analysis udp cache** command output
| Item | Description |
| --- | --- |
| Source IP | Source IP address of a UDP flow. |
| Source Port | Source port number of a UDP flow. |
| Destination IP | Destination IP address of a UDP flow. |
| Destination Port | Destination port number of a UDP flow. |
| Direction | Traffic direction. InBound indicates the inbound direction, and outBound indicates the outbound direction. |
| Interface | Inbound interface for collecting UDP packets. |
| Flow Start Time | Time when a UDP flow is created in the flow table. |
| VNI | VNI of inner UDP packets encapsulated in VXLAN packets. |
| Status | Status corresponding to the block ID. Previous indicates the previous block ID, and Current indicates the current block ID. |
| Block Id | ID of the block corresponding to the status. A complete UDP service flow can be divided into multiple blocks, and one block consists of multiple UDP packets. |
| Block Timestamp | Timestamp of the block corresponding to the status. For the same UDP flow, the timestamp increases with the block ID. |
| Receive Packets | Number of UDP packets in a block of the corresponding status collected on the inbound interface. |
| Receive Bytes | Number of bytes of UDP packets in a block of the corresponding status collected on the inbound interface. |