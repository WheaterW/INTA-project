display ip fib slot all-vpn-instance
====================================

display ip fib slot all-vpn-instance

Function
--------



The **display ip fib slot all-vpn-instance** command displays information about the forwarding tables of all VPN instances on a specified board.




Format
------

**display ip fib slot** *slot-id* **all-vpn-instance** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slot-id* | Displays information about the FIB table in a specified slot ID. | The value is a string of 1 to 23 case-sensitive characters. It cannot contain spaces. |
| **verbose** | Displays detailed information about the FIB table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

* The **display ip fib slot all-vpn-instance** command is used to locate the fault of the routing module,displays information about the FIB table. Each row represents a route.
* The display ip fib slot all-vpn-instance verbose command is used to display the details of the forwarding table

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about FIB tables of all VPN instances in a specified slot.
```
<HUAWEI> display ip fib slot 1 all-vpn-instance
Route Flags: G - Gateway Route, H - Host Route,    U - Up Route
             S - Static Route,  D - Dynamic Route, B - Black Hole Route
--------------------------------------------------------------------------------
 FIB Table : _public_
 Total number of Destinations : 11
Destination/Mask    Nexthop          Flag   Interface       TunnelID                   
       10.1.1.0/24  10.2.1.1         DGU    Vlanif2220       -                    
       10.2.1.0/24  10.2.1.2         U      Vlanif2220       -                    
       10.2.1.2/32  127.0.0.1        HU     Vlanif2220       -           
     10.2.1.255/32  127.0.0.1        U      Vlanif2220       -      
       10.3.1.1/32  10.2.1.1         DGHU   Vlanif2220      0x0000000001004c4b42     
       10.3.1.8/32  10.2.1.1         DGHU   Vlanif2220      0x0000000001004c4b43  
       10.8.8.8/32  127.0.0.1        HU     LoopBack8        -                    
      127.0.0.0/8   127.0.0.1        U      InLoopBack0      -            
      127.0.0.1/32  127.0.0.1        HU     InLoopBack0      -                               
127.255.255.255/32  127.0.0.1        U      InLoopBack0      -
255.255.255.255/32  127.0.0.1        U      InLoopBack0      -

```

# Display detailed information about the FIB tables of all VPN instances in a specified slot.
```
<HUAWEI> display ip fib slot 1 all-vpn-instance verbose
                                                                   
 FIB Table: _public_                                               
 Total number of Routes: 4                                         
                                                                   
 Destination:  127.0.0.0            Mask     :  255.0.0.0          
 NHP        :  127.0.0.1            OutIf    :  InLoopBack0        
 LocalAddr  :  0.0.0.0              LocalMask:  0.0.0.0            
 Flags      :  U                    Age      :  0                  
 ATIndex    :  0                    Slot     :                     
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

**Table 1** Description of the **display ip fib slot all-vpn-instance** command output
| Item | Description |
| --- | --- |
| Route Flags | Routeflags. |
| FIB Table | Display FIB table information. |
| Total number of Routes | Total number of FIB entries. |
| Total number of Destinations | Total number of destination addresses. |
| Destination/Mask | Destination Address/Mask Length. |
| Nexthop | Next hop information. |
| Flag | Route characteristics. |
| Interface | Outbound interface to the destination address. |
| TunnelID | Indicates the forwarding entry index. It is used to connect the forwarding entry between the uplink board and the downlink board.  When the value is not 0, it means that the packets matching the item are forwarded through the tunnel.  When the value is 0, it means that the packet is not forwarded through the tunnel. |
| Mask | Mask. |
| NHP | Next hop information. |
| OutIf | Outbound interface name. |
| LocalAddr | Local address, not displayed in current version. |
| Flags | Route characteristics. |
| Age | Lifetime of a route, in seconds. This field is not displayed in the current version. |
| ATIndex | Index of the virtual connection between the local device and gateway, which is not displayed in the current version. |
| Slot | Slot ID of the outbound interface. |
| LspFwdFlag | LSP forwarding flag, not displayed in current version. |
| LspToken | LSP forwarding ID. |
| OutLabel | VPN-LSP outer label. |
| OriginAs | Start autonomous domain number, not displayed in current version. |
| BGPNhp | BGP next hop address, not displayed in current version. |
| PeerAs | Peer AS number, which is not displayed in the current version. |
| QosInfo | Number of QoS information, which is not displayed in the current version. |
| VlanID | VLAN index. |
| BGPKey | BGP key. |
| BGPKeyBak | BGP key backup. |
| NhpBak | Next hop backup. |
| OutIfBak | Outbound interface backup. |
| LspToken\_ForInLabelBak | Backup LSP ID of the backup inner label of the VPN-LSP, which is not displayed in the current version. |
| Nexthop\_ForLspTokenBak | Next hop of the LSP ID backup. The current version is not displayed. |
| OutIf\_ForLspTokenBak | Outbound interface of the LSP ID backup, which is not displayed in the current version. |
| Nexthop\_ForLspToken\_ForInLabelBak | The next hop of the LSP ID backup of the VPN-LSP inner label backup. The current version is not displayed. |
| OutIf\_ForLspToken\_ForInLabelBak | Outbound interface for the LSP ID for the VPN-LSP inner label, which is not displayed in the current version. |
| LspType | LSP type, not displayed in the current version. |
| Label\_ForLspTokenBak | LSP backup label, not displayed in current version. |
| MplsMtu | MTU value of MPLS packets, which is not displayed in the current version. |
| Gateway\_ForLspTokenBak | Backup next hop of the LSP. The current version is not displayed. |
| NextToken | Tunnel token, not displayed in current version. |
| IfIndex\_ForLspTokenBak | Backup outbound interface of the LSP, which is not displayed in the current version. |
| Label\_NextToken | Tunnel label, not displayed in current version. |
| Label | Label of the current LSP, which is not displayed in the current version. |
| LspBfdState | BFD session status obtained by detecting LSPs. The current version is not displayed. |
| Destination | Destination addresses. |
| LocalMask | Local mask, not displayed in current version. |
| OriginQos | Start number of QoS information, which is not displayed in the current version. |
| LspTokenBak | Backup LSP ID. |
| OutLabelBak | VPN-LSP outer label backup. |
| Weight | Weight. The value 0 indicates a non-UCMP scenario, and other values indicate a UCMP scenario. |