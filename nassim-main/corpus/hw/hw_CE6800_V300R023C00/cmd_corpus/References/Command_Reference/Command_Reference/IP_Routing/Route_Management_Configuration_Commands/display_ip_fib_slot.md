display ip fib slot
===================

display ip fib slot

Function
--------



The **display ip fib slot** command displays information about the FIB table on the specified interface board.




Format
------

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display ip fib slot** *slot-id* **cpuid** *cpuid* [ **vpn-instance** *vpn-instance-name* ] [ *dest-ip* [ *dest-ip-mask-len* | *dest-ip-mask* ] ] [ **verbose** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display ip fib slot** *slot-id* [ **vpn-instance** *vpn-instance-name* ] [ *dest-ip* [ *dest-ip-mask-len* | *dest-ip-mask* ] ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slot-id* | Displays information about the FIB table in a specified slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| *dest-ip* | Displays information about the FIB table with the specified destination IP address. | The value is in dotted decimal notation. |
| *dest-ip-mask-len* | Specifies the mask length of the destination IP address. | The value is an integer in the range from 0 to 32. |
| *dest-ip-mask* | Specifies the mask of the destination IP address. | The value is in dotted decimal notation. |
| **verbose** | Displays detailed information about the FIB table. | - |
| **cpuid** *cpuid* | Displays information about the FIB table in a specified cpu ID.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Displays information about the FIB table of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. "\_public\_" is reserved and cannot be used as a VPN instance name. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

* The **display ip fib slot** command displays information about the FIB table. Each row represents a route.
* If there are lots of routes, using wildcard (|, begin, exclude, include, or regular-expression) to display information or details lasts a long time. You can press Ctrl+C to terminate information display.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display summary information of forwarding information table
```
<HUAWEI> display ip fib slot 1
Route Flags: G - Gateway Route, H - Host Route,    U - Up Route
             S - Static Route,  D - Dynamic Route, B - Black Hole Route
--------------------------------------------------------------------------------
 FIB Table: _public_
 Total number of Routes: 4

 Destination/Mask   Nexthop          Flag   Interface               TunnelID    
      127.0.0.0/8   127.0.0.1        U      InLoopBack0              -          
      127.0.0.1/32  127.0.0.1        HU     InLoopBack0              -          
127.255.255.255/32  127.0.0.1        U      InLoopBack0              -          
255.255.255.255/32  127.0.0.1        U      InLoopBack0              -

```
```
<HUAWEI> display ip fib slot 1 cpuid 0
Route Flags: G - Gateway Route, H - Host Route,    U - Up Route
             S - Static Route,  D - Dynamic Route, B - Black Hole Route
--------------------------------------------------------------------------------
 FIB Table: _public_
 Total number of Routes: 4

 Destination/Mask   Nexthop          Flag   Interface               TunnelID    
      127.0.0.0/8   127.0.0.1        U      InLoopBack0              -          
      127.0.0.1/32  127.0.0.1        HU     InLoopBack0              -          
127.255.255.255/32  127.0.0.1        U      InLoopBack0              -          
255.255.255.255/32  127.0.0.1        U      InLoopBack0              -

```

# Display the detailed information of the FIB forwarding table on the specified slot.
```
<HUAWEI> display ip fib slot 1 127.0.0.1 verbose
 FIB Table: _public_
 Total number of Routes: 4 
 
 Destination:  127.0.0.1            Mask     :  255.255.255.255    
 NHP        :  127.0.0.1            OutIf    :  InLoopBack0        
 LocalAddr  :  0.0.0.0              LocalMask:  0.0.0.0            
 Flags      :  HU                   Age      :  0           
 ATIndex    :  0                    Slot     :  1                  
 LspFwdFlag :  0                    LspToken :  0x0                
 OutLabel   :  0                    OriginAs :  0                  
 BGPNhp     :  0                    PeerAs   :  0                  
 QosInfo    :  0                    OriginQos:  0                  
 VlanID     :  0                    
 BGPKey     :  0                    
 BGPKeyBak  :  0                    
 NhpBak     :  0.0.0.0              OutIfBak   :  NULL0            
 LspTokenBak:  0x0                  OutLabelBak:  0                
 LspToken_ForInLabelBak     : 0x0                 
 Nexthop_ForLspTokenBak     : 0.0.0.0             
 OutIf_ForLspTokenBak       : [No Intf]           
 Nexthop_ForLspToken_ForInLabelBak   : 0.0.0.0             
 OutIf_ForLspToken_ForInLabelBak     : [No Intf]     
 LspType         : 0               Label_ForLspTokenBak   : 0x0
 MplsMtu         : 0               Gateway_ForLspTokenBak : 0.0.0.0
 NextToken       : 0               IfIndex_ForLspTokenBak : 0
 Label_NextToken : 0               Label : 0
 LspBfdState     : 0               Weight: 0

```
```
<HUAWEI> display ip fib slot 1 cpuid 0 127.0.0.1 verbose
 FIB Table: _public_
 Total number of Routes: 4 
 
 Destination:  127.0.0.1            Mask     :  255.255.255.255    
 NHP        :  127.0.0.1            OutIf    :  InLoopBack0        
 LocalAddr  :  0.0.0.0              LocalMask:  0.0.0.0            
 Flags      :  HU                   Age      :  0           
 ATIndex    :  0                    Slot     :  1                  
 LspFwdFlag :  0                    LspToken :  0x0                
 OutLabel   :  0                    OriginAs :  0                  
 BGPNhp     :  0                    PeerAs   :  0                  
 QosInfo    :  0                    OriginQos:  0                  
 VlanID     :  0                    
 BGPKey     :  0                    
 BGPKeyBak  :  0                    
 NhpBak     :  0.0.0.0              OutIfBak   :  NULL0            
 LspTokenBak:  0x0                  OutLabelBak:  0                
 LspToken_ForInLabelBak     : 0x0                 
 Nexthop_ForLspTokenBak     : 0.0.0.0             
 OutIf_ForLspTokenBak       : [No Intf]           
 Nexthop_ForLspToken_ForInLabelBak   : 0.0.0.0             
 OutIf_ForLspToken_ForInLabelBak     : [No Intf]     
 LspType         : 0               Label_ForLspTokenBak   : 0x0
 MplsMtu         : 0               Gateway_ForLspTokenBak : 0.0.0.0
 NextToken       : 0               IfIndex_ForLspTokenBak : 0
 Label_NextToken : 0               Label : 0
 LspBfdState     : 0               Weight: 0

```

**Table 1** Description of the **display ip fib slot** command output
| Item | Description |
| --- | --- |
| FIB Table | Display FIB table information. |
| Total number of Routes | Display the total number of FIB entries. |
| Destination/Mask | Destination address / mask length. |
| Nexthop | Next hop. |
| Flag | Route characteristics. |
| Interface | Outbound interface to the destination address. |
| TunnelID | Indicates the forwarding entry index. It is used to connect the forwarding entry between the uplink board and the downlink board.  When the value is not 0, it means that the packets matching the item are forwarded through the tunnel.  When the value is 0, it means that the packet is not forwarded through the tunnel. |
| Mask | Mask. |
| NHP | Next hop. |
| OutIf | Outbound interface. |
| LocalAddr | Local address, not displayed in current version. |
| Flags | Route characteristics. |
| Age | Indicates the time that the route exists, in seconds. The current version is not displayed. |
| ATIndex | Index of the virtual link between the local and the gateway, not displayed in the current version. |
| Slot | Outlet interface slot number. |
| LspFwdFlag | LSP forwarding flag, not displayed in current version. |
| LspToken | LSP forwarding ID. |
| OutLabel | VPN-LSP outer label. |
| OriginAs | Start autonomous domain number, not displayed in current version. |
| BGPNhp | BGP next hop address, not displayed in current version. |
| PeerAs | Adjacent autonomous domain number, not displayed in current version. |
| QosInfo | Service quality information number, not displayed in current version. |
| VlanID | VLAN ID. |
| BGPKey | The key value of the BGP route. It is not displayed in the current version. |
| BGPKeyBak | Backup key value of BGP routes, not displayed in the current version. |
| NhpBak | Next hop backup. |
| OutIfBak | Outbound interface backup. |
| LspToken\_ForInLabelBak | LSP ID backup of VPN-LSP inner label backup, not displayed in current version. |
| Nexthop\_ForLspTokenBak | Next hop of the LSP ID backup. The current version is not displayed. |
| OutIf\_ForLspTokenBak | Outbound interface of the LSP ID backup, which is not displayed in the current version. |
| Nexthop\_ForLspToken\_ForInLabelBak | The next hop of the LSP ID backup of the VPN-LSP inner label backup. The current version is not displayed. |
| OutIf\_ForLspToken\_ForInLabelBak | Outbound interface of LSP ID backup of VPN-LSP inner label backup, not displayed in current version. |
| LspType | LSP type, not displayed in the current version. |
| Label\_ForLspTokenBak | LSP backup label, not displayed in current version. |
| MplsMtu | MTU value of MPLS packets, which is not displayed in the current version. |
| Gateway\_ForLspTokenBak | Backup next hop of the LSP. The current version is not displayed. |
| NextToken | Tunnel token, not displayed in current version. |
| IfIndex\_ForLspTokenBak | LSP backup outbound interface, not displayed in current version. |
| Label\_NextToken | Tunnel label, not displayed in current version. |
| Label | Label of the current LSP. The current version is not displayed. |
| LspBfdState | BFD session status obtained by detecting LSPs. The current version is not displayed. |
| Destination | Destination address. |
| LocalMask | Local mask, not displayed in current version. |
| OriginQos | Starting quality of service information number, not displayed in current version. |
| LspTokenBak | LSP ID backup. |
| OutLabelBak | VPN-LSP outer label backup. |
| Weight | Weight, 0--identifies that it is not a UCMP scenario, non-zero--identifies that it is a UCMP scenario. |