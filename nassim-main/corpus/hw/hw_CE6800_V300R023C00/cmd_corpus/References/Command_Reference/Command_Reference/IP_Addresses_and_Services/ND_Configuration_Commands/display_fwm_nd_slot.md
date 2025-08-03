display fwm nd slot
===================

display fwm nd slot

Function
--------



The **display fwm nd slot** command displays ND table forwarding information in a specified slot.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display fwm nd slot** *slotid* **cpu** *cpuid* [ **next-ip** *nextip* { **interface** { *ifName* | *ifType* *ifNum* } | **vpn-instance** *vpnname* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cpu** *cpuid* | Specifies the CPU ID. | The value is an integer ranging from 0 to 4. |
| **next-ip** *nextip* | Specifies the prefix of an IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **interface** *ifName* | Specifies an interface name. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| *ifType* | Specifies the type of an interface. | The value is a string of 0 to 28 case-sensitive characters. It cannot contain spaces. |
| *ifNum* | Specifies the name of an interface. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **vpn-instance** *vpnname* | Specifies the name of a VPN instance. | The value is a string of 1 to 32 case-sensitive characters without spaces. |
| **slot** *slotid* | Specifies a slot ID. | The value is a string of 1 to 24 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to check ND table forwarding information in a specified slot.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed ND forwarding information in a specified slot.
```
<HUAWEI> display fwm nd slot 1 cpu 0
                                                                                                                                    
 ND Table:                                                                                                                          
 Total number: 2                                                                                                                    
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.1.1.1       OutIf:       Vlanif11        VrIndex:     0                                                           
VrfIndex:     0               MACAddr:     00e0-fc12-3456  peVID:       11                                                          
CeVID:        0               FrrFlag:     0               WorkOutIf:   Eth-Trunk1                                                  
WorkOutIfBak:   NULL0                                                                                                               
------------------------------------------------------------------------------------------------                                    
                                                                                                                                    
------------------------------------------------------------------------------------------------                                    
IPAddr:        10.1.1.1         OutIf:       Vlanif11        VrIndex:     0                                                           
VrfIndex:     0               MACAddr:     00e0-fc12-3456  peVID:       11                                                          
CeVID:        0               FrrFlag:     1               WorkOutIf:   Eth-Trunk10    (mlagId: 1 )                                 
                                                                                                                                    
WorkOutIfBak:   Eth-Trunk1                                                                                                          
------------------------------------------------------------------------------------------------

```

# Display detailed ND forwarding information based on the specified slot ID, IP address, and outbound interface.
```
<HUAWEI> display fwm nd slot 1 cpu 0 next-ip 2001:db8:1::1 interface Vlanif11
                                                                                                                                    
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.1.1.1        OutIf:       Vlanif11        VrIndex:     0                                                           
VrfIndex:     0               MACAddr:     00e0-fc12-3456  peVID:       11                                                          
CeVID:        0               FrrFlag:     1               WorkOutIf:   Eth-Trunk10    (mlagId: 1 )                                 
                                                                                                                                    
WorkOutIfBak:   Eth-Trunk1                                                                                                          
------------------------------------------------------------------------------------------------

```

# Display detailed ND forwarding information based on the specified slot ID, IP address, and VPN instance name.
```
<HUAWEI> display fwm nd slot 1 cpu 0 next-ip 2001:db8:1::1 vpn-instance vpn1
------------------------------------------------------------------------------------------------                                    
IPAddr:       10.1.1.1         OutIf:       Vlanif11        VrIndex:     0                                                           
VrfIndex:     4096             MACAddr:     00e0-fc12-3456  peVID:       11                                                          
CeVID:        0                FrrFlag:     1               WorkOutIf:   Eth-Trunk10    (mlagId: 1 )                                 
                                                                                                                                    
WorkOutIfBak:   Eth-Trunk1                                                                                                          
------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display fwm nd slot** command output
| Item | Description |
| --- | --- |
| ND Table | ND entry forwarding information. |
| Total number | Total number of ARP entries. |
| IPAddr | IPv4 address. |
| OutIf | Outbound interface. |
| VrIndex | Virtual router ID. |
| VrfIndex | VPN index. |
| MACAddr | MAC address. |
| peVID | Outer VLAN ID. |
| CeVID | Inner VLAN ID. |
| FrrFlag | FRR flag. |
| workOutIf | Outbound interface. |
| mlagId | MLAG ID. |
| WorkOutIfBak | Outbound interface of the standby link. |