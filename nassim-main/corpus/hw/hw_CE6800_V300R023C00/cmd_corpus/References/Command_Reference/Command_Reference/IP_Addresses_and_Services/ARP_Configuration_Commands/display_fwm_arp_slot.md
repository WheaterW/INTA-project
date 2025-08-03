display fwm arp slot
====================

display fwm arp slot

Function
--------



The **display fwm arp slot** command displays ARP entry forwarding information in a specified slot.




Format
------

**display fwm arp slot** *slotid* **cpu** *cpuid* [ **next-ip** *nextip* { **interface** { *ifName* | *ifType* *ifNum* } | **vpn-instance** *vpnname* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cpu** *cpuid* | Specifies the CPU ID. | The value is an integer ranging from 0 to 4. |
| **next-ip** *nextip* | Specifies an IP address. | The value is in dotted decimal notation. |
| **interface** *ifName* | Specifies an interface name. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| *ifType* | Specifies the type of an interface. | The value is a string of 0 to 28 case-sensitive characters. It cannot contain spaces. |
| *ifNum* | Specifies an interface number. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **vpn-instance** *vpnname* | Specifies the name of a VPN instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **slot** *slotid* | Specifies a slot ID. | The value is a string of 1 to 24 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to view ARP entry forwarding information in a specified slot.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed ARP forwarding information based on the specified slot ID, IP address, and VPN instance name.
```
<HUAWEI> display fwm arp  slot 1 cpu 0 next-ip 10.3.1.1 vpn-instance vpn1
                                                                                                                                    
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.3.1.1        OutIf:       10GE1/0/1       VrIndex:     0                                                           
VrfIndex:     4096            MACAddr:     00e0-fc12-3456  peVID:       11                                                           
CeVID:        0               FrrFlag:     1               WorkOutIf:   10GE1/0/1   (mlagId: 1 )                                                
WorkOutIfBak:   NULL0                                                                                                               
------------------------------------------------------------------------------------------------                                                                                                                                     
------------------------------------------------------------------------------------------------

```

# Display detailed ARP forwarding information on a specified slot, IP address, and outbound interface.
```
<HUAWEI> display fwm arp  slot 1 cpu 0 next-ip 10.3.1.1 interface 10g1/0/1
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.3.1.1       OutIf:       10g1/0/1        VrIndex:     0                                                           
VrfIndex:     0               MACAddr:     00e0-fc12-3546  peVID:       11                                                          
CeVID:        0               FrrFlag:     1               WorkOutIf:   Eth-Trunk10    (mlagId: 1 )                                 
                                                                                                                                    
WorkOutIfBak:   Eth-Trunk1                                                                                                          
------------------------------------------------------------------------------------------------

```

# Display detailed ARP forwarding information in a specified slot.
```
<HUAWEI> display fwm arp slot  1 cpu 0
                                                                                                                                    
 ARP Table:                                                                                                                         
 Total number: 2                                                                                                                    
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.2.1.1     OutIf:       MEth0/0/0       VrIndex:     0                                                           
VrfIndex:     0               MACAddr:     00e0-fc12-3456  peVID:       0                                                           
CeVID:        0               FrrFlag:     0               WorkOutIf:   MEth0/0/0                                                   
WorkOutIfBak:   NULL0                                                                                                               
------------------------------------------------------------------------------------------------                                    
                                                                                                                                    
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.2.1.2        OutIf:       Vlanif11        VrIndex:     0                                                           
VrfIndex:     0               MACAddr:     00e0-fc12-3546  peVID:       11                                                          
CeVID:        0               FrrFlag:     1               WorkOutIf:   Eth-Trunk10    (mlagId: 1 )                                 
                                                                                                                                    
WorkOutIfBak:   Eth-Trunk1                                                                                                          
------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display fwm arp slot** command output
| Item | Description |
| --- | --- |
| ARP Table | ARP entry forwarding information. |
| Total number | Total number of ARP entries. |
| IPAddr | IPv4 address. |
| OutIf | Layer 3 outbound interface. |
| VrIndex | Virtual router ID. |
| VrfIndex | VPN index. |
| MACAddr | MAC address. |
| peVID | Outer VLAN ID. |
| CeVID | Inner VLAN ID. |
| FrrFlag | FRR flag. |
| WorkOutIf | Outbound interface. |
| mlagId | MLAG ID. |
| WorkOutIfBak | Outbound interface of the standby link. |