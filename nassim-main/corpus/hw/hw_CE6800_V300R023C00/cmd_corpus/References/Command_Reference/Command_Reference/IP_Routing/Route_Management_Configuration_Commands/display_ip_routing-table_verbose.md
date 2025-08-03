display ip routing-table verbose
================================

display ip routing-table verbose

Function
--------



The **display ip routing-table verbose** command displays detailed information about active and inactive routes in the IPv4 routing table.




Format
------

**display ip routing-table** [ **table-name** **msr** ] [ **time-range** *min-age* *max-age* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies a table of a producer. | - |
| **msr** | Indicates a multicast static routing table. | - |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a character string in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a character string in the format of XXdXXhXXmXXs. |
| **verbose** | Displays detailed information about active and inactive routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ip routing-table verbose** command displays detailed information about active and inactive routes in the IPv4 routing table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the current routing table.
```
<HUAWEI> display ip routing-table verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 1        Routes : 1         

Destination: 1.1.1.1/32          
     Protocol: Static             Process ID: 0              
   Preference: 60                       Cost: 0              
      NextHop: 10.12.26.18         Neighbour: 0.0.0.0
        State: Active Adv Relied         Age: 00h01m12s           
          Tag: 0                    Priority: medium         
        Label: NULL                  QoSInfo: 0x0           
   IndirectID: 0x10000CF            Instance:                                 
 RelayNextHop: 10.12.26.18         Interface: NULL0
     TunnelID: 0x0                     Flags: RD             
   RouteColor: 0

```

**Table 1** Description of the **display ip routing-table verbose** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing table. |
| Destinations | Number of the destination networks or hosts. |
| Routes | Total number of routes. |
| Process ID | Process ID. |
| Destination | Address and mask length of the destination network or host. |
| Protocol | Route Protocol. |
| Preference | EXP value. |
| Cost | Route cost. |
| Flags | Route flag in the heading of the routing table. |
| NextHop | Next hop information. |
| Interface | Indicates the egress where the next hop can be reachable. |
| State | Route status:   * Active: active route. * Invalid: invalid route. * Inactive: inactive route. * NoAdv: routes that cannot be advertised. * Adv: routes that can be advertised. * Del: route to be deleted. * GotQ: route that is successfully recursed. * WaitQ: route that has not been recursed successfully. * Stale: route with the Stale flag, which is used in GR. * Relied: route that is recursed to the next hop and outbound interface, or the route that is recursed to a tunnel. |
| IndirectID | Keyword of indirect next hop. |
| RelayNextHop | Iterated next hop address. If the corresponding static route reaches the next hop through a tunnel, this item is displayed as 0.0.0.0. This item is displayed only when the next hop of the route is configured but the outbound interface of the route is not configured. |
| TunnelID | Tunnel ID. |
| Neighbour | Neighbor Information. |
| Age | Time when the route is created. |
| Tag | Indicates the administrative tag for routes. |
| Label | Label value. |
| Priority | EXP value. |
| QoSInfo | Indicates QoS information. |
| Instance | instance. |
| RouteColor | Color value of the forwarding plane. The value is related to the network slice configuration function. The related command is color network-slice. |