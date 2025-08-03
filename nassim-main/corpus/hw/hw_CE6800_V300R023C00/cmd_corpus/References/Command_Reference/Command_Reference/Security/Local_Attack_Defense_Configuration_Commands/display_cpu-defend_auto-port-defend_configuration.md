display cpu-defend auto-port-defend configuration
=================================================

display cpu-defend auto-port-defend configuration

Function
--------



The **display cpu-defend auto-port-defend configuration** command displays the configuration of port attack defense.




Format
------

**display cpu-defend auto-port-defend configuration** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the configuration of port attack defense, use this command.

**Precautions**



If slot is not specified, the default threshold is displayed as --, indicating that 80% of the default CAR value of the protocol is used as the rate threshold. You can specify slot to obtain the threshold.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of port attack defense on the local device.
```
<HUAWEI> display cpu-defend auto-port-defend configuration
-----------------------------------------------------------------------                                                             
 Name  : 1                                                                                                                          
 Related slot : <1>                                                                                                                 
 Auto-port-defend                               : enable                                                                            
 Auto-port-defend sample                        : 8                                                                                 
 Auto-port-defend aging-time                    : 300 second(s)                                                                     
 Auto-port-defend alarm                         : enable                                                                            
 Auto-port-defend arp-reply threshold           : -- pps(enable)                                                                    
 Auto-port-defend arp-request threshold         : -- pps(enable)                                                                    
 Auto-port-defend arp-request-uc threshold      : -- pps(enable)                                                                    
 Auto-port-defend dhcp-reply threshold          : -- pps(enable)                                                                    
 Auto-port-defend dhcp-request threshold        : -- pps(enable)                                                                    
 Auto-port-defend dhcpv6-discovery threshold    : -- pps(enable)                                                                    
 Auto-port-defend dhcpv6-reply threshold        : -- pps(enable)                                                                    
 Auto-port-defend dhcpv6-request threshold      : -- pps(enable)                                                                    
 Auto-port-defend icmp threshold                : -- pps(enable)                                                                    
 Auto-port-defend igmp threshold                : -- pps(enable)                                                                    
 Auto-port-defend ip-fragment threshold         : -- pps(enable)                                                                    
 Auto-port-defend isis threshold                : -- pps(enable)                                                                    
 Auto-port-defend isis-overlay threshold        : -- pps(enable)                                                                    
 Auto-port-defend lacp threshold                : -- pps(enable)                                                                    
 Auto-port-defend nd threshold                  : -- pps(enable)                                                                    
 Auto-port-defend ospf threshold                : -- pps(enable)                                                                    
 Auto-port-defend ospf-hello threshold          : -- pps(enable)                                                                    
 Auto-port-defend ospf-hello-overlay threshold  : -- pps(enable)                                                                    
 Auto-port-defend ospf-overlay threshold        : -- pps(enable)                                                                    
 Auto-port-defend ospfv3 threshold              : -- pps(enable)                                                                    
 Auto-port-defend ospfv3-overlay threshold      : -- pps(enable)                                                                    
 Auto-port-defend pim threshold                 : -- pps(enable)                                                                    
 Auto-port-defend vrrp threshold                : -- pps(enable)                                                                    
 Auto-port-defend vrrp6 threshold               : -- pps(enable)                                                                    
-----------------------------------------------------------------------

```
```
<HUAWEI> display cpu-defend auto-port-defend configuration
-----------------------------------------------------------------------                                                             
 Name  : 1                                                                                                                          
 Related slot : <1>                                                                                                                  
 Auto-port-defend                               : enable                                                                            
 Auto-port-defend sample                        : 8                                                                                 
 Auto-port-defend aging-time                    : 300 second(s)                                                                     
 Auto-port-defend alarm                         : enable                                                                            
 Auto-port-defend arp-reply threshold           : -- pps(enable)                                                                    
 Auto-port-defend arp-request threshold         : -- pps(enable)                                                                    
 Auto-port-defend arp-request-uc threshold      : -- pps(enable)                                                                    
 Auto-port-defend dhcp-discovery threshold      : -- pps(enable)                                                                    
 Auto-port-defend dhcp-reply threshold          : -- pps(enable)                                                                    
 Auto-port-defend dhcp-request threshold        : -- pps(enable)                                                                    
 Auto-port-defend dhcpv6-discovery threshold    : -- pps(enable)                                                                    
 Auto-port-defend dhcpv6-reply threshold        : -- pps(enable)                                                                    
 Auto-port-defend dhcpv6-request threshold      : -- pps(enable)                                                                    
 Auto-port-defend icmp threshold                : -- pps(enable)                                                                    
 Auto-port-defend igmp threshold                : -- pps(enable)                                                                    
 Auto-port-defend ip-fragment threshold         : -- pps(enable)                                                                    
 Auto-port-defend isis threshold                : -- pps(enable)                                                                    
 Auto-port-defend isis-overlay threshold        : -- pps(enable)
 Auto-port-defend lacp threshold                : -- pps(enable) 
 Auto-port-defend nd threshold                  : -- pps(enable)                                                                    
 Auto-port-defend ospf threshold                : -- pps(enable)                                                                    
 Auto-port-defend ospf-hello threshold          : -- pps(enable)                                                                    
 Auto-port-defend ospf-hello-overlay threshold  : -- pps(enable)                                                                    
 Auto-port-defend ospf-overlay threshold        : -- pps(enable)                                                                    
 Auto-port-defend ospfv3 threshold              : -- pps(enable)                                                                    
 Auto-port-defend ospfv3-overlay threshold      : -- pps(enable)                                                                    
 Auto-port-defend pim threshold                 : -- pps(enable)                                                                    
 Auto-port-defend vrrp threshold                : -- pps(enable)                                                                    
 Auto-port-defend vrrp6 threshold               : -- pps(enable)                                                                    
-----------------------------------------------------------------------

```
```
<HUAWEI> display cpu-defend auto-port-defend configuration
-----------------------------------------------------------------------                                                             
 Name  : 1                                                                                                                          
 Related slot : <1>                                                                                                                 
 Auto-port-defend                               : enable                                                                            
 Auto-port-defend sample                        : 8                                                                                 
 Auto-port-defend aging-time                    : 300 second(s)                                                                     
 Auto-port-defend alarm                         : enable                                                                            
 Auto-port-defend arp-reply threshold           : -- pps(enable)                                                                    
 Auto-port-defend arp-request threshold         : -- pps(enable)                                                                    
 Auto-port-defend arp-request-uc threshold      : -- pps(enable)                                                                    
 Auto-port-defend dhcp-reply threshold          : -- pps(enable)                                                                    
 Auto-port-defend dhcp-request threshold        : -- pps(enable)                                                                                                                                      
 Auto-port-defend icmp threshold                : -- pps(enable)                                                                    
 Auto-port-defend igmp threshold                : -- pps(enable)                                                                    
 Auto-port-defend ip-fragment threshold         : -- pps(enable)                                                                    
 Auto-port-defend isis threshold                : -- pps(enable)                                                                                                                                 
 Auto-port-defend lacp threshold                : -- pps(enable)                                                                                                                                      
 Auto-port-defend ospf threshold                : -- pps(enable)                                                                                                                                                                                                                                                                                
 Auto-port-defend pim threshold                 : -- pps(enable)
 Auto-port-defend pim-mc threshold              : -- pps(enable)                                                                    
 Auto-port-defend vrrp threshold                : -- pps(enable)                                                                                                                                   
-----------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend auto-port-defend configuration** command output
| Item | Description |
| --- | --- |
| Name | Name of an attack defense policy. |
| Related slot | Slot ID of the attack defense policy is applied. |
| Auto-port-defend | Whether port attack defense is enabled.  To enable the port attack defense function, run the auto-port-defend enable command. |
| Auto-port-defend sample | Sampling ratio for protocol packets.  To set this parameter, run the auto-port-defend sample command. |
| Auto-port-defend aging-time | Aging time for port attack defense.  To set this parameter, run the auto-port-defend aging-time command. |
| Auto-port-defend arp-request threshold | Whether port attack defense is applied to ARP Request packets and rate threshold.  To set this parameter, run the auto-port-defend protocol arp-request and auto-port-defend protocol arp-request threshold threshold commands. |
| Auto-port-defend arp-request-uc threshold | Whether port attack defense is applied to Unicast ARP Request packets and rate threshold.  To set this parameter, run the auto-port-defend protocol arp-request-uc and auto-port-defend protocol arp-request-uc threshold threshold commands. |
| Auto-port-defend arp-reply threshold | Whether port attack defense is applied to ARP Reply packets and rate threshold.  To set this parameter, run the auto-port-defend protocol arp-reply and auto-port-defend protocol arp-reply threshold threshold commands. |
| Auto-port-defend dhcp-request threshold | Whether port attack defense is applied to DHCP server packets and rate threshold.  To set this parameter, run the auto-port-defend protocol dhcp-request and auto-port-defend protocol dhcp-request threshold threshold commands. |
| Auto-port-defend dhcp-reply threshold | Whether port attack defense is applied to DHCP client packets and rate threshold.  To set this parameter, run the auto-port-defend protocol dhcp-reply and auto-port-defend protocol dhcp-reply threshold threshold commands. |
| Auto-port-defend dhcpv6-discovery threshold | Whether port attack defense is applied to DHCPv6 discovery packets and rate threshold.  To set this parameter, run the auto-port-defend protocol dhcpv6-discovery and auto-port-defend protocol dhcpv6-discovery threshold threshold commands. |
| Auto-port-defend dhcpv6-reply threshold | Whether port attack defense is applied to DHCPv6 reply packets and rate threshold.  To set this parameter, run the auto-port-defend protocol dhcpv6-reply and auto-port-defend protocol dhcpv6-reply threshold threshold commands. |
| Auto-port-defend dhcpv6-request threshold | Whether port attack defense is applied to DHCPv6 request packets and rate threshold.  To set this parameter, run the auto-port-defend protocol dhcpv6-request and auto-port-defend protocol dhcpv6-request threshold threshold commands. |
| Auto-port-defend icmp threshold | Whether port attack defense is applied to ICMP packets and rate threshold.  To set this parameter, run the auto-port-defend protocol icmp and auto-port-defend protocol icmp threshold threshold commands. |
| Auto-port-defend ip-fragment threshold | Whether port attack defense is applied to IP fragment packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ip-fragment and auto-port-defend protocol ip-fragment threshold threshold commands. |
| Auto-port-defend nd threshold | Whether port attack defense is applied to ND packets and rate threshold.  To set this parameter, run the auto-port-defend protocol nd and auto-port-defend protocol nd threshold threshold commands. |
| Auto-port-defend ospf threshold | Whether port attack defense is applied to OSPF packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ospf and auto-port-defend protocol ospf threshold threshold commands. |
| Auto-port-defend ospf-hello threshold | Whether port attack defense is applied to OSPF hello packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ospf-hello and auto-port-defend protocol ospf-hello threshold threshold commands. |
| Auto-port-defend ospf-overlay threshold | Whether port attack defense is applied to overlay OSPF packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ospf-overlay and auto-port-defend protocol ospf-overlay threshold threshold commands. |
| Auto-port-defend ospf-hello-overlay threshold | Whether port attack defense is applied to overlay OSPF hello packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ospf-hello-overlay and auto-port-defend protocol ospf-hello-overlay threshold threshold commands. |
| Auto-port-defend ospfv3 threshold | Whether port attack defense is applied to OSPFv3 packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ospfv3 and auto-port-defend protocol ospfv3 threshold threshold commands. |
| Auto-port-defend ospfv3-overlay threshold | Whether port attack defense is applied to overlay OSPFv3 packets and rate threshold.  To set this parameter, run the auto-port-defend protocol ospfv3-overlay and auto-port-defend protocol ospfv3-overlay threshold threshold commands. |
| Auto-port-defend vrrp threshold | Whether port attack defense is applied to VRRP packets and rate threshold.  To set this parameter, run the auto-port-defend protocol vrrp and auto-port-defend protocol vrrp threshold threshold commands. |
| Auto-port-defend vrrp6 threshold | Whether port attack defense is applied to VRRP6 packets and rate threshold.  To set this parameter, run the auto-port-defend protocol vrrp6 and auto-port-defend protocol vrrp6 threshold threshold commands. |
| Auto-port-defend isis threshold | Whether port attack defense is applied to ISIS packets and rate threshold.  To set this parameter, run the auto-port-defend protocol isis and auto-port-defend protocol isis threshold threshold commands. |
| Auto-port-defend isis-overlay threshold | Whether port attack defense is applied to Overlay ISIS packets and rate threshold.  To set this parameter, run the auto-port-defend protocol isis-overlay and auto-port-defend protocol isis-overlay threshold threshold commands. |
| Auto-port-defend alarm | Whether the report of port attack defense events is enabled.  To set this parameter, run the auto-port-defend alarm enable command. |
| Auto-port-defend lacp threshold | Whether port attack defense is applied to Lacp packets and rate threshold.  To set this parameter, run the auto-port-defend protocol lacp and auto-port-defend protocol lacp threshold threshold commands. |
| Auto-port-defend dhcp-discovery threshold | Whether port attack defense is applied to DHCP discovery packets and rate threshold.  To set this parameter, run the auto-port-defend protocol dhcp-discovery and auto-port-defend protocol dhcp-discovery threshold threshold commands. |
| Auto-port-defend igmp threshold | Whether port attack defense is applied to igmp packets and rate threshold.  To set this parameter, run the auto-port-defend protocol igmp and auto-port-defend protocol igmp threshold threshold commands. |
| Auto-port-defend pim threshold | Whether port attack defense is applied to pim packets and rate threshold.  To set this parameter, run the auto-port-defend protocol pim and auto-port-defend protocol pim threshold threshold commands. |