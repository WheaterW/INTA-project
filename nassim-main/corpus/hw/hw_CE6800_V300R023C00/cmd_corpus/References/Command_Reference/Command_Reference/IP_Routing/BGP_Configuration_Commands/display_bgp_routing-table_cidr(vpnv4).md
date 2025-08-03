display bgp routing-table cidr(vpnv4)
=====================================

display bgp routing-table cidr(vpnv4)

Function
--------



The **display bgp vpnv4 routing-table cidr** command displays information about classless inter-domain routing (CIDR).




Format
------

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **cidr**

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **cidr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays statistics about all BGP VPNv4 routes. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **cidr** | Displays information about classless inter-domain routing (CIDR) routes. | - |
| **instance** *instance-name* | Specifies a BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv4 routing-table cidr** command displays information about classless inter-domain routing (CIDR).


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about classless inter-domain routing (CIDR) routes in the BGP-VPNv4 address family.
```
<HUAWEI> display bgp vpnv4 all routing-table cidr
   BGP Local router ID is 192.168.7.1
   Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                 h - history, i - internal, s - suppressed, S - Stale
                 Origin : i - IGP, e - EGP, ? - incomplete
   RPKI validation codes: V - valid, I - invalid, N - not-found
   Total number of routes from all PE: 3
   Route Distinguisher: 100:1 
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   *>   1.1.1.1/32         0.0.0.0         0                     0      ?
   Route Distinguisher: 200:1
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   *>i 1.1.1.1/32         192.168.100.10 0          100        0      33 55?
   *>i 2.2.2.2/32         192.168.100.10 0          100        0      33 55?
  VPN-Instance vrf1, router ID 1.1.1.9:
   Total number of routes: 3
        Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   *>   1.1.1.1/32         0.0.0.0         0                     0      ?
   * i                     192.168.100.10  0          100        0      33 55?
   *>i  2.2.2.2/32         192.168.100.10  0          100        0      33 55?

```

**Table 1** Description of the **display bgp routing-table cidr(vpnv4)** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of routes from all Pes. |
| Total number of routes | Total number of routes. |
| Route Distinguisher | Specified RD. |
| Network | Indicates the network address in the BGP routing table. |
| NextHop | Next hop address used to forward the packet. |
| MED | Indicates the MED of the route. |
| LocPrf | Local preference of a route. |
| Path/Ogn | Indicates the AS\_Path number and the Origin attribute of the route. |