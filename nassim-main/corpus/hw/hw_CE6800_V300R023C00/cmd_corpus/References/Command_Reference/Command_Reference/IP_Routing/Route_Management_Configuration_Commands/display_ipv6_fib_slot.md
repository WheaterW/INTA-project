display ipv6 fib slot
=====================

display ipv6 fib slot

Function
--------



The **display ipv6 fib slot** command displays Forwarding Information Base (FIB) entries on a specified board.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 fib slot** *slotid* **all-vpn-instance** [ **statistics** | **verbose** ]

**display ipv6 fib slot** *slotid* [ **vpn-instance** *vpn-name* ] [ *destip* [ *destipmasklen* ] ] [ **verbose** ]

**display ipv6 fib slot** *slotid* [ **vpn-instance** *vpn-name* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slotid* | Specifies a slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **all-vpn-instance** | Displays information about FIB entries of all VPNs. | - |
| **statistics** | Displays statistics about FIB entries. | - |
| **verbose** | Displays detailed information about FIB entries. | - |
| **vpn-instance** *vpn-name* | Displays FIB entries of the VPN instance with a specified name. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. |
| *destip* | Specifies the prefix of an IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *destipmasklen* | Specifies the prefix length of an IPv6 address. | The value is an integer that ranges from 0 to 128. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ipv6 fib slot** command helps locate faults on the routing module. This command displays forwarding information in a list. Each line represents a route.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all FIB entries on slot 1.
```
<HUAWEI> display ipv6 fib slot 1 fc00:0:0:2001:: verbose
Route Flags: G - Gateway Route, H - Host Route,    U - Up Route                 
             S - Static Route,  D - Dynamic Route, B - Black Hole Route         
--------------------------------------------------------------------------------
IPv6 FIB Table: _public_                                                        
Total number of Routes: 1                                                       
                                                                                
Destination  : FC00:0:0:2001::                          PrefixLength : 64       
                                                                                
Flag         : U                                                                
Nexthop      : FC00:0:0:2001::1                         Interface    : Loopback0
                                                                                
Tunnel ID    : -                                        Label        : 0        
                                                                                
BgpNexthop   : 0                                        OriginAs     : 0        
                                                                                
PeerAs       : 0                                                                
NexthopBak   : ::                                       InterfaceBak : NULL0    
                                                                                
Tunnel ID Bak: -                                        LabelBak     : 0        
                                                                                
BgpNexthopBak: 0                                        OriginAs     : 0        
                                                                                
PeerAs       : 0

```

**Table 1** Description of the **display ipv6 fib slot** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flag. |
| IPv6 FIB Table | IPv6 forwarding table. |
| Total number of Routes | Total number of routes. |
| Destination | Destination address of a route. |
| PrefixLength | Prefix length of the destination address. |
| Flag | S, U, G, H, B, and D are used to describe route characteristics. For example:   * S: Static, * U: Up. * G: Gateway. * H: Host. * B: BlackHole. * D: Dynamic. |
| Nexthop | Next-hop device that forwards packets to the destination address. |
| Interface | Outbound interface for forwarding packets. |
| Tunnel ID | ID of the tunnel. If packets are forwarded through IP, the tunnel ID is 0. |
| Tunnel ID Bak | Tunnel ID backup. |
| Label | VPN label. |
| BgpNexthop | IP address of the BGP next hop. |
| OriginAs | Start AS number. |
| PeerAs | Neighboring AS number. |
| NexthopBak | Backup next hop. |
| InterfaceBak | Backup outbound interface. |
| LabelBak | VPN label backup. |
| BgpNexthopBak | IP address of the BGP backup next hop. |