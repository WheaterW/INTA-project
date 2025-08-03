display qos configuration
=========================

display qos configuration

Function
--------



The **display qos configuration** command displays the QoS configuration on an interface.




Format
------

**display qos configuration interface** [ *interface-type* *interface-number* | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the interface number. | - |
| **interface** *interface-name* | Specifies the number of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display qos configuration command displays QoS configurations on a specified interface or all interfaces or in a specified VLAN. The command output helps you check the QoS configuration and locate QoS faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the QoS configuration on the 100GE1/0/1.
```
<HUAWEI> display qos configuration interface 100GE 1/0/1
 interface 100GE1/0/1    
 --------------------------------------------------------------------------    
 trust flag        : outer 8021p   
 diffserv domain   : default      
 dei enable        : disable
 port priority     : 0           
 phb marking 8021p : enable       
 phb marking dscp  : disable      
 phb marking exp   : -
 port wred         : -             
 port lr           : cir = -, cbs = -   
 port car inbound  : -                                                                                                              
 port car outbound : -    
 schedule profile  : -
 --------------------------------------------------------------------------                                                         
 queue          shaping       schedule     wred    
             cir       pir      
             cbs       pbs       
 -------------------------------------------------------------------------- 
 0             -         -    pq           -    
               -         -                  
                                              
 1             -         -    pq           -   
               -         -                    
                                              
 2             -         -    pq           -   
               -         -                     
                                               
 3             -         -    pq           -   
               -         -                     
                                               
 4             -         -    pq           -   
               -         -                     
                                              
 5             -         -    pq           -  
               -         -                   
                                                
 6             -         -    pq           -   
               -         -                                 
 7             -         -    pq           -   
               -         -                          
 --------------------------------------------------------------------------

```

**Table 1** Description of the **display qos configuration** command output
| Item | Description |
| --- | --- |
| trust flag | External priority (802.1p priority, DSCP priority, or EXP priority) mapped to the internal priority (DiffServ CoS and color). |
| diffserv domain | Name of the DiffServ domain applied to the interface or VLAN. |
| dei enable | Whether to map the DEI field in a VLAN tag to the drop priority. |
| port priority | Default 802.1p priority added to untagged packets by the interface. |
| port wred | Name of the WRED drop profile applied to the interface. |
| port lr | Traffic shaping rate on the interface. |
| port car inbound | CAR in the inbound direction of an interface. |
| port car outbound | CAR in the outbound direction of an interface. |
| phb marking 8021p | Whether the mapping from PHBs to 802.1p priorities is enabled for outgoing packets on the interface. |
| phb marking dscp | Whether PHB mapping is enabled for DSCP priorities in outgoing packets on an interface. |
| wred | Drop profile bound to an interface queue. |
| cir | Committed information rate (CIR) for shaping. |
| cbs | Committed burst size (CBS). |
| schedule | Scheduling mode of an interface queue. |
| queue | Interface queue index. |
| shaping | Traffic shaping configuration of the interface queue. |
| pir | Peak information rate (PIR) for shaping. |
| pbs | Peak burst size (PBS). |