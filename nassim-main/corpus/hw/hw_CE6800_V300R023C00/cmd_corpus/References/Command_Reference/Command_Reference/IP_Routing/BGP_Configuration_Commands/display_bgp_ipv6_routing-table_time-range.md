display bgp ipv6 routing-table time-range
=========================================

display bgp ipv6 routing-table time-range

Function
--------



The **display bgp ipv6 routing-table time-range** command displays BGP IPv6 routes that flap within the specified period.

The **display bgp ipv6 routing-table unnumbered peer interface** command displays BGP IPv6 Unnumbered routes that flap within the specified period.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table** [ **peer** { *remoteIpv4Addr* | *remoteIpv6Addr* } { **received-routes** | **advertised-routes** } ] **time-range** *time-range-start* *time-range-end*

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **received-routes** | **advertised-routes** } **time-range** *time-range-start* *time-range-end*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *remoteIpv6Addr* | Specifies the IPv6 address of a peer. | The value is in the format X:X:X:X:X:X:X:X. |
| *remoteIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **received-routes** | Displays the BGP4+ public network routes received from a specified peer. | - |
| **advertised-routes** | Displays the BGP4+ public network routes advertised to a specified peer. | - |
| **time-range** *time-range-start* *time-range-end* | Displays BGP public network routes that flap within the specified period. For example, the value 0d0h5m0s of start-time indicates five minutes before the current time. The value 0d0h10m0s of end-time indicates 10 minutes before the current time. All BGP public network routes with the Keepalive time in the range of 5 to 10 minutes are displayed. | The values of start-time and end-time are in the format of xxdxxhxxmxxs. d specifies the day, which is an integer ranging from 0 to 10000. h specifies the hour, which is an integer ranging from 0 to 23. m specifies the minute, which is an integer ranging from 0 to 59. s specifies the second, which is an integer ranging from 0 to 59. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies the type of an interface. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp ipv6 routing-table time-range** command displays BGP IPv6 routes that flap within the specified time period. You can view information about specified routes by specifying different keywords or parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP4+ routes that flap within the specified time period.
```
<HUAWEI> display bgp ipv6 routing-table time-range 0d0h0m0s 1d5h0m0s

 BGP Local router ID is 10.10.10.15
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

 *>     Network  : 2001:DB8:1::1                            PrefixLen : 128
        NextHop  : ::                                       Duration  : 0d01h20m11s
        Peer     : ::
        Path/Ogn :  ?
 *>i    Network  : 2001:DB8:2::2                            PrefixLen : 128
        NextHop  : FE80::3A8A:9CFF:FE51:300                 Duration  : 0d01h17m25s
        Peer     : FE80::3A8A:9CFF:FE51:300(10GE1/0/1.1)
        Path/Ogn : 55 66 77?
 * i
        NextHop  : FE80::3A8A:9CFF:FE51:301                 Duration  : 0d01h17m27s
        Peer     : FE80::3A8A:9CFF:FE51:301(10GE1/0/1.1)
        Path/Ogn : 55 66 77?
   i
        NextHop  : ::FFFF:10.1.1.2                          Duration  : 0d01h18m22s
        Peer     : 10.1.1.2
        Path/Ogn :  ?

```

**Table 1** Description of the **display bgp ipv6 routing-table time-range** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Network | Network address in the BGP4+ public network routing table. |
| PrefixLen | Prefix length. |
| NextHop | Next-hop address of the packet. |
| Duration | Route duration. |
| Peer | Peer IP address. If the peer address is an unnumbered peer address, the name of the unnumbered interface is also displayed. |
| Path/Ogn | AS\_Path and Origin attributes. |
| Prefix | IP prefix. |