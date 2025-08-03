display bgp instance vpnv6 vpn-instance routing-table time-range
================================================================

display bgp instance vpnv6 vpn-instance routing-table time-range

Function
--------



The **display bgp instance vpnv6 routing-table time-range** command displays information about BGP VPNv6 routes that flap within a specified time range.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp instance** *bgpName* **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** [ **peer** *remoteIpv6Addr* { **received-routes** | **advertised-routes** } ] **time-range** *time-range-start* *time-range-end*

**display bgp instance** *bgpName* **vpnv6** **all** **routing-table** **time-range** *time-range-start* *time-range-end*

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **time-range** *time-range-start* *time-range-end*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **peer** *remoteIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **received-routes** | Displays information about the routes received from the specified peer. | - |
| **advertised-routes** | Routes advertised to the remote peer. | - |
| *time-range-start* | Specifies the start time. | The formats of time-range-start and time-range-end both are xxdxxhxxmxxs.  The d indicates days. The value is an integer ranging from 0 to 10000.  The h indicates hours. The value is an integer ranging from 0 to 23.  The m indicates minutes. The value is an integer ranging from 0 to 59.  The s indicates seconds. The value is an integer ranging from 0 to 59. |
| *time-range-end* | Specifies the time that the device stopped to record the information. | The formats of time-range-start and time-range-end both are xxdxxhxxmxxs.  The d indicates days. The value is an integer ranging from 0 to 10000.  The h indicates hours. The value is an integer ranging from 0 to 23.  The m indicates minutes. The value is an integer ranging from 0 to 59.  The s indicates seconds. The value is an integer ranging from 0 to 59. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Display all information on VPNv6 and IPv6 VPN instance. | - |
| **route-distinguisher** *strRd* | X.X.X.X:number or number:number or number.number:number. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about BGP multi-instance VPNv6 routes that flap within a specified period, run the **display bgp instance vpnv6 routing-table time-range** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BGP VPNv6 routes that flap within a specified time range.
```
<HUAWEI> display  bgp instance a vpnv6 all  routing-table time-range 0d1h1m1s 2d1h1m1s
 
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete

 Route Distinguisher: 2:3

 *>     Network  : 2001:db8:1::1                            PrefixLen : 128 
        NextHop  : ::                                       Duration  : 1d01h17m02s
        Peer     : 10.1.1.2                                  
        Path/Ogn :  ?
 *>     Network  : 2001:db8:1::2                            PrefixLen : 128 
        NextHop  : ::                                       Duration  : 1d01h17m02s
        Peer     : 10.1.1.3                                  
        Path/Ogn :  ?
 *>     Network  : 2001:db8:1::3                            PrefixLen : 128 
        NextHop  : 2001:db8:1::10                           Duration  : 1d01h16m12s
        Peer     : 10.1.1.3                                  
        Path/Ogn : 200?
    
 VPN-Instance vrf1, Router ID 10.2.1.1:
 *>     Network  : 2001:db8:1::4                            PrefixLen : 128 
        NextHop  : ::                                       Duration  : 1d01h17m03s
        Peer     : ::                                       
        Path/Ogn :  ?
 *>     Network  : 2001:db8:1::5                            PrefixLen : 128 
        NextHop  : ::                                       Duration  : 1d01h17m03s
        Peer     : ::                                       
        Path/Ogn :  ?
 *>     Network  : 2001:db8:1::6                            PrefixLen : 128 
        NextHop  : 2001:db8:1::50                           Duration  : 1d01h16m13s
        Peer     : 10.1.1.4                                     
        Path/Ogn : 200?

```

**Table 1** Description of the **display bgp instance vpnv6 vpn-instance routing-table time-range** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | ID of the local BGP device, in the same format as an IPv4 address. |
| best | Indicates that the BGP route is the optimal route. |
| Origin | Origin attribute of the BGP route. It is classified into the following types:   * IGP: indicates that routing information is obtained through IGP. For example, the Origin attribute of the routes imported to the BGP routing table by using the network command is IGP. * EGP: indicates that the Origin attribute of the routes obtained through EGP is EGP. * Incomplete: The origin of the route cannot be identified. For example, the Origin attribute of the routes imported by BGP through the import-route command is Incomplete. |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Network | Indicates the destination network or host address of the route. |
| PrefixLen | Mask length of the destination network address or host address of the route. |
| NextHop | IPv6 address of the next hop. |
| Duration | Duration of a route. |
| Peer | Indicates the bgp peer. |
| Path/Ogn | Indicates the AS\_Path number and the Origin attribute of the route. |
| valid | Indicates that the BGP route is a valid route. |
| internal | Internal route. |