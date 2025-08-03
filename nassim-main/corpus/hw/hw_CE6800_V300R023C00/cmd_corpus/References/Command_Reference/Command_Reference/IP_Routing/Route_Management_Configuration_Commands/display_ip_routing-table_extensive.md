display ip routing-table extensive
==================================

display ip routing-table extensive

Function
--------



The **display ip routing-table extensive** command displays detailed information about routes with a specified prefix.




Format
------

**display ip routing-table** [ **vpn-instance** *vpn-instance-name* ] *prefix* [ *mask* | *masklength* ] **extensive**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *prefix* | Displays information about routes with a specified IP prefix list. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of a destination IP address. | The value is in dotted decimal notation. |
| *masklength* | Specifies the mask length. A 32-bit mask is represented by consecutive 1s, and the mask in dotted decimal notation can be replaced by the mask length. | The value is an integer ranging from 0 to 32. |
| **extensive** | Extensive verbose information of the routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check detailed information about routes with a specified prefix, run the **display ip routing-table extensive** command. If the routes recurse to tunnels, information about the recursive tunnels will be displayed in the command output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about routes (with a specified prefix) that recurse to GRE tunnels.
```
<HUAWEI> display ip routing-table 10.10.10.10 extensive
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vrf1
Summary Count : 2

Destination: 10.10.10.10/32      
     Protocol: Static          Process ID: 0              
   Preference: 60                    Cost: 0              
      NextHop: 1.2.3.4          Neighbour: 0.0.0.0        
        State: Active Adv Relied      Age: 00h00m14s           
          Tag: 0                 Priority: low            
        Label: NULL               QoSInfo: 0x0           
   IndirectID: 0x10000F4         Instance:                                 
 RelayNextHop: 0.0.0.0          Interface: tunnel14
     TunnelID: 0x000000000500000003 Flags: RD              
   RouteColor: 0
   TunnelType: gre

```

# Display detailed information about routes (with a specified prefix) that recurse to VXLAN tunnels.
```
<HUAWEI> display ip routing-table vpn-instance vpn1 10.1.1.1 extensive
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vpn1
Summary Count : 1

Destination: 10.1.1.1/32         
     Protocol: IBGP               Process ID: 0              
   Preference: 255                      Cost: 0              
      NextHop: 1.1.1.1             Neighbour: 1.1.1.1
        State: Active Adv Relied         Age: 00h00m29s           
          Tag: 0                    Priority: low            
        Label: NULL                  QoSInfo: 0x0           
   IndirectID: 0x1000118            Instance:                                 
 RelayNextHop: 0.0.0.0             Interface: VXLAN
     TunnelID: 0x0000000027f0000001    Flags: RD             
   RouteColor: 0
   TunnelType: vxlan_nvo3                Vni: 5010
   GatewayIP : 10.4.1.2

```

# Display detailed information about the routes that are not recursed to a tunnel.
```
<HUAWEI> display ip routing-table vpn-instance vpn1 10.10.10.10 extensive
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vpn1
Summary Count : 1

Destination: 10.10.10.10/32
     Protocol: Static          Process ID: 0
   Preference: 60                    Cost: 0
      NextHop: 10.1.1.1      Neighbour: 0.0.0.0
        State: Active Adv             Age: 11d00h51m05s
          Tag: 0                 Priority: low
        Label: NULL               QoSInfo: 0x0
   IndirectID: 0x100035B         Instance:
 RelayNextHop: 0.0.0.0          Interface: NULL0
     TunnelID: 0x0                  Flags: DB
   RouteColor: 0

```

**Table 1** Description of the **display ip routing-table extensive** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flag:   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB. * T: indicates that the next hop is a VPN instance. * B: indicates a blackhole route. |
| Routing Table | Routing table. |
| Summary Count | Number of summary routes. |
| Process ID | Process ID of the routing protocol. |
| GatewayIP | Gateway address of the VXLAN tunnel. |
| Destination | Destination address. |
| Protocol | Routing protocol type. |
| Preference | Priority of the routing protocol. |
| Cost | Cost of the route. |
| NextHop | Next-hop IP address. |
| Neighbour | Peer. |
| State | Route status.   * Active: indicates that the route is active. * Invalid: indicates that the route is invalid. * Inactive: indicates that the route is inactive. * NoAdv: indicates that the route cannot be advertised. * Adv: indicates that the route can be advertised. * Del: indicates that the route is to be deleted. * Relied: indicates that the route recurses to a next hop and an outbound interface or recurses to a tunnel. * Stale: indicates the routes with the Stale flag, which are used in GR. |
| Age | Time when the route is generated. |
| Tag | Tag for importing routes. |
| Priority | Priority. |
| Label | VPN label. |
| QoSInfo | QoS information. |
| IndirectID | Keyword of the indirect next hop, which is generated by the system. If the route is not a recursive route, the value is 0x0. If the route is a recursive route, the value is 0x0. |
| Instance | Instance. |
| RelayNextHop | Recursive next hop. |
| Interface | Outbound interface through which the next hop of a route can be reached. |
| TunnelID | Tunnel ID. The value 0x0 indicates that no tunnel is used or the tunnel fails to be established. |
| Flags | Route flags in the header of the routing table. |
| TunnelType | Tunnel type. |
| Vni | VXLAN tunnel network identifier. |
| RouteColor | Color value of the forwarding plane. The value is related to the network slice configuration function. The related command is color network-slice. |