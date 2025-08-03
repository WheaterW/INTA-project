display arp packet statistics
=============================

display arp packet statistics

Function
--------



The **display arp packet statistics** command displays the statistics about Address Resolution Protocol (ARP) packets.




Format
------

**display arp packet statistics** [ **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays the ARP packets sent and received by a specified Layer 3 interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To locate and rectify ARP faults, you need to view statistics about ARP packets sent and received by the device.



**Precautions**

Run the **display arp packet statistics interface** command to view the interfaces that send and receive ARP packets and the statistics about the ARP packets.

* The displayed statistics on an interface are the accumulative statistics about ARP packets sent and received by this interface.
* For example, if an interface sends a gratuitous ARP reply packet, the interface records the packet in the statistics about ARP reply packets as well as in the statistics about gratuitous ARP packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about all ARP packets sent and received by the device.
```
<HUAWEI> display arp packet statistics
ARP Packets Received
  Total:                       10989
  Learnt Count:                    0
  Discard For Entry Limit:         0
  Discard For Speed Limit:         0
  Discard For Proxy Suppress:      0
  Discard For Other:           10989
  MAC Invalid Count:            0
ARP Packets Sent 
  Total:                           0
  Request:                         0
  Reply:                           0
  Gratuitous ARP:                  0
ARP-Miss Message Received:  
  Total:                           0
  Discard For Speed Limit:         0
  Discard For Other:               0

```

# Display detailed statistics about ARP packets sent and received by a device.
```
<HUAWEI> display arp packet statistics interface 10ge 1/0/1
ARP Packets Received     
  Request:                              22  
  Reply:                                0   
  Gratuitous ARP:                       6   
ARP Packets Sent     
  Request:                              3  
  Reply:                                0  
  Gratuitous ARP:                       3  
ARP-Miss Message Received   
  Total:                                0    
  Discard For Invalid Table:            0  
  Discard For Speed Limit:              0  
  Discard For Other:                    0

```

# Display the interfaces that send and receive ARP packets and the statistics about the ARP packets.
```
<HUAWEI> display arp packet statistics interface
Interface                 R-request   R-reply  R-gratis  S-request   S-reply S-gratis
--------------------------------------------------------------------------------
10GE1/0/1                       5          0         3          0          0      0
Vlanif2                       100          0       100          0          5      5
Eth-Trunk2.1                  400        200       400        400        200    100

```

**Table 1** Description of the **display arp packet statistics** command output
| Item | Description |
| --- | --- |
| ARP Packets Received | Number of received ARP packets. |
| ARP Packets Sent | Number of sent ARP packets. |
| Learnt Count | Number of learned ARP entries. |
| Discard For Speed Limit | Number of packets discarded for the speed limit. |
| Discard For Proxy Suppress | Number of packets discarded for ARP proxy. |
| Discard For Other | Number of packets discarded for other reasons. |
| Discard For Entry Limit | Number of discarded packets. |
| Discard For Invalid Table | Number of packets discarded due to invalid static ARP entries. |
| MAC Invalid Count | Number of packets discarded due to MAC address inconsistency.  After the arp validate command is configured on an interface to enable MAC address consistency check, when the interface receives an ARP packet, it checks whether the source/destination MAC address in the ARP packet header is the same as the source/destination MAC address in the data field of the ARP packet. |
| Gratuitous ARP | Number of sent gratuitous ARP packets. |
| ARP-Miss Message Received | Number of ARP Miss messages received. |
| Interface | Interfaces that send and receive ARP packets. |
| R-request | Number of ARP request packets received by an interface. |
| R-reply | Number of ARP reply packets received by an interface. |
| R-gratis | Number of ARP request packets received by an interface. |
| S-request | Number of ARP request packets sent by an interface. |
| S-reply | Number of ARP reply packets sent by an interface. |
| S-gratis | Number of gratuitous ARP packets sent by an interface. |
| Total | Number of total. |
| Request | Number of sent ARP request packets. |
| Reply | Number of sent ARP reply packets. |