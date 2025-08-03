display cpu-defend auto-port-defend statistics
==============================================

display cpu-defend auto-port-defend statistics

Function
--------



The **display cpu-defend auto-port-defend statistics** command displays packet statistics about port attack defense.




Format
------

**display cpu-defend auto-port-defend statistics** [ **slot** *slot-id* ]


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

You can run this command to view statistics about the packets discarded and accepted in the port attack defense service. The statistics help you understand protocol packet processing status and promptly adjust the attack defense policy.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display packet statistics on the interfaces of the device.
```
<HUAWEI> display cpu-defend auto-port-defend statistics
Statistics on Slot 1 :                                                                                                              
--------------------------------------------------------------------------------                                                    
Protocol             Queue    Car(pps)    Pass(Packet/Byte)    Drop(Packet/Byte)                                                    
--------------------------------------------------------------------------------                                                    
arp-reply            15       2048        23095                3                                                                    
                                          NA                   NA                                                                   
arp-request          15       2048        0                    0                                                                    
                                          NA                   NA                                                                   
arp-request-uc       15       2048        0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-reply           15       760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-request         15       760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcpv6-discovery     15       380         0                    0                                                                    
                                          NA                   NA                                                                   
dhcpv6-reply         15       760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcpv6-request       15       760         0                    0                                                                    
                                          NA                   NA                                                                   
icmp                 15       512         0                    0                                                                    
                                          NA                   NA                                                                   
igmp                 16       256         0                    0                                                                    
                                          NA                   NA                                                                   
ip-fragment          15       1536        0                    0                                                                    
                                          NA                   NA                                                                   
isis                 23       1024        0                    0                                                                    
                                          NA                   NA                                                                   
isis-overlay         23       512         0                    0                                                                    
                                          NA                   NA                                                                   
lacp                 47       512         0                    0                                                                    
                                          NA                   NA                                                                   
nd                   15       2000        0                    0                                                                    
                                          NA                   NA                                                                   
ospf                 23       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospf-hello           23       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospf-hello-overlay   23       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospf-overlay         23       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospfv3               23       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospfv3-overlay       23       512         0                    0                                                                    
                                          NA                   NA                                                                   
pim                  16       256         0                    0                                                                    
                                          NA                   NA                                                                   
vrrp                 47       512         0                    0                                                                    
                                          NA                   NA                                                                   
vrrp6                47       512         0                    0                                                                    
                                          NA                   NA                                                                   
--------------------------------------------------------------------------------

```
```
<HUAWEI> display cpu-defend auto-port-defend statistics
Statistics on Slot 1 :                     
--------------------------------------------------------------------------------                                                    
Protocol             Queue    Car(pps)    Pass(Packet/Byte)    Drop(Packet/Byte)                                                    
--------------------------------------------------------------------------------                                                    
arp-reply            7        2048        23905                3                                                                    
                                          NA                   NA                                                                   
arp-request          7        2048        0                    0                                                                    
                                          NA                   NA                                                                   
arp-request-uc       7        2048        0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-discovery       7        380         0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-reply           7        760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-request         7        760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcpv6-discovery     7        380         0                    0                                                                    
                                          NA                   NA                                                                   
dhcpv6-reply         7        760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcpv6-request       7        760         0                    0                                                                    
                                          NA                   NA                                                                   
icmp                 7        512         0                    0                                                                    
                                          NA                   NA                                                                   
igmp                 8        256         0                    0                                                                    
                                          NA                   NA                                                                   
ip-fragment          7        1536        0                    0                                                                    
                                          NA                   NA                                                                   
isis                 11       1024        0                    0                                                                    
                                          NA                   NA                                                                   
isis-overlay         11       512         0                    0                                                                    
                                          NA                   NA                                                                   
lacp                 23       512         0                    0                                                                    
                                          NA                   NA                                                                   
nd                   7        2000        0                    0                                                                    
                                          NA                   NA                                                                   
ospf                 11       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospf-hello           11       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospf-hello-overlay   11       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospf-overlay         11       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospfv3               11       512         0                    0                                                                    
                                          NA                   NA                                                                   
ospfv3-overlay       11       512         0                    0                                                                    
                                          NA                   NA                                                                   
pim                  8        256         0                    0                                                                    
                                          NA                   NA                                                                   
vrrp                 23       512         0                    0                                                                    
                                          NA                   NA                                                                   
vrrp6                23       512         0                    0                                                                    
                                          NA                   NA                                                                   
--------------------------------------------------------------------------------

```
```
<HUAWEI> display cpu-defend auto-port-defend statistics
Statistics on Slot 1 :                                                                                                              
--------------------------------------------------------------------------------                                                    
Protocol             Queue    Car(pps)    Pass(Packet/Byte)    Drop(Packet/Byte)                                                    
--------------------------------------------------------------------------------                                                    
arp-reply            15       2048        23095                3                                                                    
                                          NA                   NA                                                                   
arp-request          15       2048        0                    0                                                                    
                                          NA                   NA                                                                   
arp-request-uc       15       2048        0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-reply           15       760         0                    0                                                                    
                                          NA                   NA                                                                   
dhcp-request         15       760         0                    0                                                                    
                                          NA                   NA                                                                                                                                    
icmp                 15       512         0                    0                                                                    
                                          NA                   NA                                                                   
igmp                 16       256         0                    0                                                                    
                                          NA                   NA                                                                   
ip-fragment          15       1536        0                    0                                                                    
                                          NA                   NA                                                                   
isis                 23       1024        0                    0                                                                    
                                          NA                   NA                                                                                                                                    
lacp                 47       512         0                    0                                                                    
                                          NA                   NA                                                                                                                                
ospf                 23       512         0                    0                                                                    
                                          NA                   NA                                                                                                                                                                                                                                                                                                                                                                                                                
pim                  16       256         0                    0                                                                    
                                          NA                   NA
pim-mc               16       256         0                    0                                                                    
                                          NA                   NA                                                                   
vrrp                 47       512         0                    0                                                                    
                                          NA                   NA                                                                                                                                    
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend auto-port-defend statistics** command output
| Item | Description |
| --- | --- |
| Statistics on Slot 1 | Packet statistics on the interfaces of the device. |
| Protocol | Attack packet type. |
| Queue | Queue from which attack packets are sent. |
| Car(pps) | Protocol rate limit. |
| Pass(Packet/Byte) | Number and bytes of attack packets that pass through the device.  The value 23095 indicates the number of accepted packets. The value NA indicates that the device does not support statistics collection by byte. |
| Drop(Packet/Byte) | Number and bytes of attack packets discarded by the device.  The value 3 indicates the number of discarded packets. The value NA indicates that the device does not support statistics collection by byte. |