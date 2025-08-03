display ip routing-table all-routes
===================================

display ip routing-table all-routes

Function
--------



The **display ip routing-table all-routes** command displays information about the routes of public and all VPN instances.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display ip routing-table all-routes**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display ipv6 routing-table all-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Specifies IPv6 routes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |

None


Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display ip routing-table all-routes command displays information about the routes of public and all VPN instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays information about the IPv4 routes of public and all VPN instances.
```
<HUAWEI> display ip routing-table all-routes
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 4        Routes : 4        

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0

Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Routing Table : vrfa
         Destinations : 1        Routes : 1        

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0

```

**Table 1** Description of the **display ip routing-table all-routes** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing Table. |
| Destinations | Total number of destination networks or hosts. |
| Routes | Total number of routes. |
| Proto | Protocol through which routes are learned. |
| Pre | Priority. |
| Cost | Route cost. |
| Flags | Route flags. |
| NextHop | Next-hop address. |
| Interface | Outbound interface through which the next hop is reachable. |