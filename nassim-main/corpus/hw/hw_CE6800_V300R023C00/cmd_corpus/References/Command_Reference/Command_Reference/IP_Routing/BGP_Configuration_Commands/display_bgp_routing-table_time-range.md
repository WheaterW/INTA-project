display bgp routing-table time-range
====================================

display bgp routing-table time-range

Function
--------



The **display bgp routing-table time-range** command displays BGP routes that flap within the specified period.

The **display bgp routing-table unnumbered peer interface time-range** command displays BGP Unnumbered routes that flap within the specified period.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp routing-table peer** *remoteIpv4Addr* { **received-routes** **time-range** *time-range-start* *time-range-end* | **advertised-routes** **time-range** *time-range-start* *time-range-end* }

**display bgp routing-table time-range** *time-range-start* *time-range-end*

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **received-routes** **time-range** *time-range-start* *time-range-end* | **advertised-routes** **time-range** *time-range-start* *time-range-end* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp routing-table peer** *remoteIpv6Addr* { **received-routes** **time-range** *time-range-start* *time-range-end* | **advertised-routes** **time-range** *time-range-start* *time-range-end* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **received-routes** | Displays the public network routes received from a specified peer. | - |
| **time-range** *time-range-start* *time-range-end* | Displays BGP public network routes that flap within the specified period. For example, the value 0d0h5m0s of start-time indicates five minutes before the current time. The value 0d0h10m0s of end-time indicates 10 minutes before the current time. All BGP public network routes with the Keepalive time in the range of 5 to 10 minutes are displayed. | Both start-time and end-time are in the format of xxdxxhxxmxxs. d indicates the day, which is an integer ranging from 0 to 10000. h indicates the hour, which is an integer ranging from 0 to 23. m indicates the minute, which is an integer ranging from 0 to 59. s indicates the second, which is an integer ranging from 0 to 59. |
| **advertised-routes** | Displays the public network routes advertised to a specified peer. | - |
| **peer** *remoteIpv4Addr* | Displays the public network routes of a specified peer. | The value is in the dotted decimal format. |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *remoteIpv6Addr* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Using the **display bgp routing-table time-range** command, you can view the BGP routes that flap within the specified period. For example, if service traffic is abnormal or CPU usage of the device remains high within a period, you can run this command to check whether route flapping occurs within the period. The faulty route can be viewed in the command output, facilitating fault location.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP routes that flap within the specified period.
```
<HUAWEI> display bgp routing-table time-range 0d0h5m3s 1d1h1m1s

 BGP Local router ID is 10.77.144.15
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found

      Network            NextHop                        Peer                                      Duration        Path/Ogn

 *>   10.2.3.4/32         10.0.0.0                        0.0.0.0                                   0d01h10m05s      ?
 *>i  10.5.6.7/32         10.1.1.2                       10.1.1.2                                  0d01h08m16s      ?
 * i                     10.2.1.2                       10.2.1.2                                  0d01h08m14s      ?
 * i                     10.3.1.2                       10.3.1.2                                  0d01h08m14s     25 35 45?
 * i                     FE80::3A8A:9CFF:FE51:300       FE80::3A8A:9CFF:FE51:300(10GE1/0/1.1)       0d01h07m19s     55 66 77?
 * i                     FE80::3A8A:9CFF:FE51:301       FE80::3A8A:9CFF:FE51:301(10GE1/0/1.1)       0d01h07m21s     55 66 77?
   i                     10.22.11.1                     10.1.1.2                                  0d01h08m14s      ?

```

**Table 1** Description of the **display bgp routing-table time-range** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Network | Network address in the BGP routing table. |
| NextHop | Next-hop address used to send packets. |
| Peer | Peer IP address. If the peer address is an unnumbered peer address, the name of the unnumbered interface is also displayed. |
| Duration | Route duration. |
| Path/Ogn | AS-Path number and the Origin attribute. |