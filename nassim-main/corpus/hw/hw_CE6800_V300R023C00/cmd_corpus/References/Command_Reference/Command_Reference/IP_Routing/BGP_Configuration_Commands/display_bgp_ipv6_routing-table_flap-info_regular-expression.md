display bgp ipv6 routing-table flap-info regular-expression
===========================================================

display bgp ipv6 routing-table flap-info regular-expression

Function
--------



The **display bgp ipv6 routing-table flap-info regular-expression** command displays statistics about the flapping routes that match an AS\_Path regular expression.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table flap-info regular-expression** *as-regular-expression*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **regular-expression** *as-regular-expression* | Displays statistics about the flapping routes that match an AS\_Path regular expression. | The value is a string of 1 to 80 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view statistics about the flapping routes that match an AS\_Path regular expression, run the **display bgp ipv6 routing-table flap-info regular-expression** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the flapping routes that match an AS\_Path regular expression.
```
<HUAWEI> display bgp ipv6 routing-table flap-info regular-expression 8
 BGP Local router ID is 10.1.1.1
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete
 Total Number of Routes: 3
  d  Network : 2001:DB8:1:1:1::                          PrefixLen : 96
     From    : 2001:DB8:1:1:1::1                         Flaps     : 8
     Duration: 00:02:11                                  Reuse     : 00:49:21
     Path/Ogn: 1.1 100?
  d  Network : 2001:DB8:2::2                             PrefixLen : 128
     From    : 2001:DB8:1:1:1::1                         Flaps     : 5
     Duration: 00:00:18                                  Reuse     : 00:41:06
     Path/Ogn: 1.1 100?
  d  Network : 2001:DB8:2::3                             PrefixLen : 128
     From    : 2001:DB8:1:1:1::1                         Flaps     : 5
     Duration: 00:00:18                                  Reuse     : 00:41:06
     Path/Ogn: 1.1 100?

```

**Table 1** Description of the **display bgp ipv6 routing-table flap-info regular-expression** command output
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