display bgp instance vpnv4 routing-table peer
=============================================

display bgp instance vpnv4 routing-table peer

Function
--------



The **display bgp instance vpnv4 routing-table peer** command displays peer information about BGP VPNv4 routes.




Format
------

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **peer** *remoteIpv4Addr* { **accepted-routes** | **not-accepted-routes** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all BGP VPNv4 routes. | - |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **peer** *remoteIpv4Addr* | Displays the routes of a specified IPv6 peer. | The address is a 32-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **accepted-routes** | Displays routes accepted by routing policy. | - |
| **not-accepted-routes** | Displays routes not accepted by routing policy.  Information about the routes that fail to match the route-policy can be displayed only after the keep-all-routes or peer keep-all-routes command is configured. | - |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



The **display bgp instance vpnv4 routing-table peer** command displays peer information about BGP VPNv4 routes.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BGP routes that are received from a specified peer and then accepted by a route-policy in the BGP-VPNv4 address family.
```
<HUAWEI> display bgp instance aaa vpnv4 all routing-table peer 192.168.1.2 accepted-routes
 BGP Local router ID is 172.16.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found
 Total number of routes from all PE: 5
 Route Distinguisher: 100:1
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
 *>     10.4.4.4/32         0.0.0.0         0                     0      ?
 *>i    10.11.11.11/32     10.1.1.9         0          100        0      ?
 Route Distinguisher: 100:3
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
 *>     10.3.3.3/32         0.0.0.0         0                     0      ?
 Route Distinguisher: 200:1
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
 *>i    10.11.11.12/32     10.1.1.9         0          100        0      ?
 Route Distinguisher: 300:1
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
 *>i    10.11.11.13/32     10.1.1.9         0          100        0      ?

```

**Table 1** Description of the **display bgp instance vpnv4 routing-table peer** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | Router ID of the local device, in the format of an IPv4 address. |
| Total number of routes from all PE | Number of routes from all PEs. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Network | Network address in the BGP routing table. |
| NextHop | Next hop address used to forward the packet. |
| MED | MED of the route. |
| LocPrf | Local\_Pref of the route. |
| PrefVal | PrefVal of the route. |
| Path/Ogn | AS\_Path and Origin of the route. |