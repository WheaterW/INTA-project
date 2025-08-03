display bgp evpn routing-table flap-info
========================================

display bgp evpn routing-table flap-info

Function
--------



The **display bgp evpn routing-table flap-info** command displays statistics about BGP EVPN route flapping.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **flap-info** [ **mac-route** | **prefix-route** ]

**display bgp instance** *instance-name* **evpn** { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** **flap-info** [ **mac-route** | **prefix-route** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays information about EVPN routes of all EVPN instances. | - |
| **route-distinguisher** *route-distinguisher* | Displays information about EVPN routes with the specified RD. | An RD can be in either of the following formats:   * 2-byte AS number: 4-byte user-defined number, such as 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. Specifically, an RD cannot be 0:0. * 4-byte AS number: 2-byte user-defined number, such as 65537:3. The AS number ranges from 65536 to 4294967295, and the user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation: 2-byte user-defined number, such as 0.0:3 or 0.1:0. The AS number is in the format of x.y, where x and y are integers ranging from 0 to 65535. The user-defined number also ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. Specifically, an RD cannot be 0.0:0. * 4-byte IP address: 2-byte user-defined number, such as 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. |
| **mac-route** | Displays information about MAC advertisement routes. | - |
| **prefix-route** | Displays information about prefix routes. | - |
| **instance** *instance-name* | Displays information about EVPN routes of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics about BGP EVPN route flapping, run the **display bgp evpn all routing-table flap-info** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP EVPN route flapping.
```
<HUAWEI> display bgp evpn all routing-table flap-info

 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
               Origin : i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V - valid, I - invalid, N - not-found
 
 EVPN address family:
 Number of Mac Routes: 2
 Route Distinguisher: 1:1
       Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  From                          Flaps  Duration  Reuse     Path/Ogn
  di   0:48:0002-0002-0002:0:0.0.0.0                         10.2.2.2                       4      00:10:22  00:28:40  600i
  di   0:48:38ba-a703-7902:0:0.0.0.0                         10.2.2.2                       4      00:10:10  00:28:46  600i

```

**Table 1** Description of the **display bgp evpn routing-table flap-info** command output
| Item | Description |
| --- | --- |
| BGP Local router ID | Router ID of the local BGP device. |
| Number of Mac Routes | Number of MAC Routes. |
| Route Distinguisher | The route distinguisher. |
| From | IP address of the peer from which a route is learned. |
| Flaps | Total number of times of route flapping. |
| Duration | Flapping duration. |
| Reuse | Reuse value. |
| Path/Ogn | AS\_Path number and the Origin attribute. |
| Network | The network information of the route. |