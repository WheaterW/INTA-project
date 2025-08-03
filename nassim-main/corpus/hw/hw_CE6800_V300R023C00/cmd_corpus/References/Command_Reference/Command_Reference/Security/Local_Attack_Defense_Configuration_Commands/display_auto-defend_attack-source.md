display auto-defend attack-source
=================================

display auto-defend attack-source

Function
--------



The **display auto-defend attack-source** command displays the attack sources.




Format
------

**display auto-defend attack-source** [ **slot** *slot-id* ]

**display auto-defend attack-source** [ **history** [ **slot** *slot-id* ] ]

**display auto-defend attack-source trace-type** { **source-mac** | **source-ip** | **source-portvlan** } [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |
| **history** | Displays the history attack source information.  If history is not specified, all existing attack source information is displayed. | - |
| **trace-type** | Specifies trace type. | - |
| **source-mac** | Displays the history attack source information based on source MAC addresses. | - |
| **source-ip** | Displays the history attack source information based on source IP addresses. | - |
| **source-portvlan** | Displays the history attack source information based on source port and vlan information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display auto-defend attack-source** command displays the attack source list.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the attack source list of source-mac trace type.
```
<HUAWEI> display auto-defend attack-source trace-type source-mac
  Attack Source User Table on Slot 1 :                                                                                                
  --------------------------------------------------------------------------------                                                    
  MAC Address       Interface         PacketType   VLAN:Outer/Inner         Total                                                     
  --------------------------------------------------------------------------------                                                    
  00e0-fc12-3456    100GE1/0/1        ARP          100/--                    3056                                                     
  --------------------------------------------------------------------------------                                                    
  Total: 1

```

# Display the attack source history record.
```
<HUAWEI> display auto-defend attack-source history
 Attack History User Table on Slot 1 :                                                                                               
 --------------------------------------------------------------------------------                                                    
 AttackTime             MAC Address    Interface         VLAN:O/I    PacketType                                                      
 --------------------------------------------------------------------------------                                                    
 S:2020-06-07 14:07:24  00e0-fc12-3456 100GE1/0/1        100/--      ARP                                                             
 E:2020-06-07 14:07:25                                                                                                               
 --------------------------------------------------------------------------------                                                    
 Total: 1                                                                                                                            
 Attack History IP Table on Slot 1 :                                                                                                 
 -----------------------------------------------------------------------------                                                       
 AttackTime             IP Address                                PacketType                                                         
 -----------------------------------------------------------------------------                                                       
 S:2020-06-07 14:06:14  10.1.1.10                                 ARP                                                                
 E:2020-06-07 14:06:17                                                                                                               
 -----------------------------------------------------------------------------                                                       
 Total: 1                                                                                                                            
 Attack History Port Table on Slot 1 :                                                                                               
 -----------------------------------------------------------------                                                                   
 AttackTime             Interface         VLAN:O/I    PacketType                                                                     
 -----------------------------------------------------------------                                                                   
 S:2020-06-07 14:06:17  100GE1/0/1        100/--      ARP                                                                            
 E:2020-06-07 14:06:38                                                                                                                                                                                                                           
 -----------------------------------------------------------------                                                                   
 Total: 1

```

**Table 1** Description of the **display auto-defend attack-source** command output
| Item | Description |
| --- | --- |
| Attack Source User Table on Slot 1 | Source tracing information of the specified slot, which is distinguished according to the attack user. |
| Attack History User Table on Slot 1 | Information about attack sources on the specified slot, which is distinguished according to attackers. |
| Attack History Port Table on Slot 1 | Information about attack sources on the specified slot, which is distinguished according to attacked interfaces. |
| Attack History IP Table on Slot 1 | Information about attack sources on the specified slot, which is distinguished according to attacked source IP addresses. |
| Interface | Name of the interface that initiates the attack. |
| PacketType | Packet type of attract source. |
| Total | Total number of packets received by the device. |
| AttackTime | Time information of attack source:  S: Start time of attack.  E: End time of attack. |
| Vlan:Outer/Inner | ID of the VLAN that an interface belongs to. Outer indicates the outer VLAN ID and Inner indicates the inner VLAN ID.  For attack source tracing entries on Layer 3 interfaces, "-" is displayed. |
| Vlan:O/I | ID of the VLAN that an interface belongs to. The value O indicates the outer VLAN ID and the value I indicates the inner VLAN ID. |