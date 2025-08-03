display bgp ipv6 routing-table flap-info
========================================

display bgp ipv6 routing-table flap-info

Function
--------



The **display bgp ipv6 routing-table flap-info** command displays statistics about BGP4+ route flapping.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table flap-info** [ **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } | *network-address* [ *prefix-length* [ **longer-match** ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **as-path-filter** *as-path-filter-number* | Specifies the number of an AS\_Path filter. | The value is a decimal integer ranging from 1 to 256. |
| *network-address* | Specifies the network address of dampened routes. | The value is in dotted decimal notation. |
| *prefix-length* | Specify network prefix length. | It is an integer ranging from 0 to 128. |
| **longer-match** | Allows longer prefix length match. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics about BGP4+ route flapping, run the **display bgp ipv6 routing-table flap-info** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP4+ route flapping.
```
<HUAWEI> display bgp ipv6 routing-table flap-info

 Total Number of Routes: 3

 BGP Local router ID is 10.53.53.53
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete

  d  Network : 2001:DB8:1:1:1::                          PrefixLen : 96
     From    : 2001:DB8:1:1:1::1                         Flaps     : 8
     Duration: 00:02:11                                  Reuse     : 00:49:21
     Path/Ogn: 100?

  d  Network : 2001:DB8:2::2                             PrefixLen : 128
     From    : 2001:DB8:1:1:1::1                         Flaps     : 5
     Duration: 00:00:18                                  Reuse     : 00:41:06
     Path/Ogn: 100?

  d  Network : 2001:DB8:2::3                             PrefixLen : 128
     From    : 2001:DB8:1:1:1::1                         Flaps     : 5
     Duration: 00:00:18                                  Reuse     : 00:41:06
     Path/Ogn: 100?

```

**Table 1** Description of the **display bgp ipv6 routing-table flap-info** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes. |
| Network | Indicates the network address in the BGP routing table. |
| PrefixLen | Mask length of the destination network address or host address of the route. |
| From | Indicates the IP address of the peer that receives the routes. |
| Flaps | Total number of route flappings. |
| Reuse | Reuse value. |
| Duration | Total duration of route flapping. |
| Path/Ogn | AS\_Path and Origin. |