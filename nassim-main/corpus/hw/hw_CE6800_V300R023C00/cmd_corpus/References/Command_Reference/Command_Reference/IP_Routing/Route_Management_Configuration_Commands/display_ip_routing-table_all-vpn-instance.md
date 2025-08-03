display ip routing-table all-vpn-instance
=========================================

display ip routing-table all-vpn-instance

Function
--------

The **display ip routing-table all-vpn-instance** command displays information about IPv4 routing tables of all VPN instances.



Format
------

**display ip routing-table all-vpn-instance** [ **verbose** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed information about all the routes in the routing table, including active and inactive routes. If this parameter is not specified, only brief information about active routes is displayed. | - |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

When the verbose parameter is not specified, information about only one route is displayed in each line. The contents include the destination address, mask length, protocol, priority, route cost, route flag, next hop, and outbound interface. This command displays only the preferred routes.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Displays information about routes of all VPN instances.
```
<HUAWEI> display ip routing-table all-vpn-instance
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : __dcn_vpn__
         Destinations : 5        Routes : 5         

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
     10.128.0.0/16  Direct  0    0             D   10.128.240.168  LoopBack1023
 10.128.240.168/32  Direct  0    0             D   127.0.0.1       LoopBack1023
 10.128.255.255/32  Direct  0    0             D   127.0.0.1       LoopBack1023
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
------------------------------------------------------------------------------
Routing Table : vpna
         Destinations : 2        Routes : 2         

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
------------------------------------------------------------------------------
Routing Table : vpnb
         Destinations : 2        Routes : 2         
                
Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0

```


**Table 1** Description of the
**display ip routing-table all-vpn-instance** command output

| Item | Description |
| --- | --- |
| Route Flags | Route tag.  ?R: indicates that the route is a recursive route.  ?D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing table. |
| Destinations | Destination network/host address. |
| Routes | Total number of active and inactive routes. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Proto | Protocol used to learn routes. |
| Pre | Priority. |
| Cost | Route cost. |
| Flags | Route flags in the header of the routing table. |
| NextHop | Next-hop address. |
| Interface | Outbound interface through which the next hop is reachable. |