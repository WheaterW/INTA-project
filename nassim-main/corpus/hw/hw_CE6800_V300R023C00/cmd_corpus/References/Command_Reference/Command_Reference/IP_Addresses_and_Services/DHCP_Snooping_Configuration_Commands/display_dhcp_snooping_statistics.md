display dhcp snooping statistics
================================

display dhcp snooping statistics

Function
--------



The **display dhcp snooping statistics** command displays statistics on the received DHCP messages.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display dhcp snooping statistics** { **global** | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **bridge-domain** *bd-id* }

For CE6820H, CE6820H-K, CE6820S, CE6885-LL (low latency mode):

**display dhcp snooping statistics** { **global** | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Displays global DHCP snooping statistics. | - |
| **interface** *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlan-id* | Displays statistics about DHCP messages received in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **bridge-domain** *bd-id* | Displays statistics about DHCP messages received in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display dhcp snooping statistics command to view statistics on various types of DHCP messages received by the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display global DHCP snooping statistics.
```
<HUAWEI> display dhcp snooping statistics global
 DHCP Snooping Statistics:                                                      
                                                                                
 Client Request:                                                                 
  Dhcp Discover:                  0                                             
  Dhcp Request:                   0                                             
  Dhcp Decline:                   0                                             
  Dhcp Release:                   0                                             
  Dhcp Inform:                    0                                             
 Server Reply:                                                                  
  Dhcp Offer:                     0                                             
  Dhcp Ack:                       0                                             
  Dhcp Nak:                       0                                             
 Drop Packet:                                                                   
  Dropped by mac-address check:   0                                             
  Dropped by untrust reply:       0                                             
  Dropped by request conflict:    0 
  Dropped by giaddr check:        0 
  Dropped by request check:       0 
  Dropped by no trust port:       0
  Dropped by max number check:    0
 Delete DHCP snooping table:    
  Receive release packet:         0   
  Receive decline packet:         0    
  Lease expired:                  0    
  User command:                   0    
  Client transfers:              0    
  Interface down:                 0

```

**Table 1** Description of the **display dhcp snooping statistics** command output
| Item | Description |
| --- | --- |
| dhcp inform | Number of DHCP inform packets. |
| dhcp release | Number of DHCP Release messages. |
| dhcp request | Number of DHCP request packets. |
| dhcp discover | Number of DHCP Discover packets. |
| dhcp ack | Number of DHCP ACK messages. |
| dhcp nak | Number of DHCP NAK messages. |
| dhcp decline | Number of DHCP decline packets. |
| dhcp offer | Number of DHCP Offer messages. |
| DHCP Snooping Statistics | DHCP snooping statistics. |
| Client Request | Packets sent by the DHCP client include:  · DHCP Discover packet.  · DHCP Request packet.  · DHCP Decline packets.  · DHCP Release packet.  · DHCP Inform packets. |
| Client transfers | Number of DHCP snooping binding entries deleted because the client connects to another interface on the device. |
| Server Reply | Messages returned by the DHCP server, including:  ·DHCP Offer.  ·DHCP ACK.  ·DHCP NAK. |
| Drop Packet | Number of discarded messages. |
| Dropped by mac-address check | Number of discarded DHCP messages whose MAC address is different from the CHADDR field. |
| Dropped by untrust reply | Number of untrusted reply messages that are discarded. |
| Dropped by request conflict | Number of packets that are discarded because the client and server MAC addresses conflict. |
| Dropped by giaddr check | Number of packets discarded because the IP address is different from the GIADDR. |
| Dropped by request check | Number of packets that are discarded because they do not match the binding table. |
| Dropped by no trust port | Number of messages discarded because no trusted interface is configured. |
| Delete DHCP snooping table | Number of DHCP snooping binding entries deleted by the device. |
| Receive release packet | Number of DHCP snooping binding entries deleted by the device after the device receives DHCP Release messages. |
| Receive decline packet | Number of DHCP snooping binding entries deleted by the device after the device receives DHCP Decline messages. |
| Lease expired | Number of DHCP snooping binding entries deleted by the device because of lease expiry. |
| User command | Number of DHCP snooping binding entries deleted using commands. |
| Interface down | Number of binding entries deleted because the interface is shut down. |