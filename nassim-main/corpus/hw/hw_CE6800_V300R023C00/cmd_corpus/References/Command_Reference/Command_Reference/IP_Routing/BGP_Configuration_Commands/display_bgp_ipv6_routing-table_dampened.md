display bgp ipv6 routing-table dampened
=======================================

display bgp ipv6 routing-table dampened

Function
--------



The **display bgp ipv6 routing-table dampened** command displays BGP dampened routes and statistics about the routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table dampened**

**display bgp ipv6 routing-table statistics dampened**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display bgp ipv6 routing-table statistics dampened** command displays BGP dampened routes and statistics about the routes.

**Precautions**

If a routing loop occurs, some routes may have not converged. Therefore, the route statistics displayed using the command may be different from the actual number.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dampened BGP IPv6 routes.
```
<HUAWEI> display bgp ipv6 routing-table dampened

 Total Number of Routes: 4

 BGP Local router ID is 10.0.0.2
 Status codes: * - valid, > - best, d - damped, a - add path,
               h - history,  i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete

  d  Network : 2001:DB8:1::                              PrefixLen : 48
     From    : 2001:DB8:5::                              Reuse     : 01:06:26
     Path/Ogn: 65001?

  d  Network : 2001:DB8:2::                              PrefixLen : 48
     From    : 2001:DB8:5::                              Reuse     : 01:06:26
     Path/Ogn: 65001?

  d  Network : 2001:DB8:3::                              PrefixLen : 48
     From    : 2001:DB8:5::                              Reuse     : 01:06:26
     Path/Ogn: 65001?

  d  Network : 2001:DB8:4::                              PrefixLen : 48
     From    : 2001:DB8:5::                              Reuse     : 01:06:26
     Path/Ogn: 65001?

```

**Table 1** Description of the **display bgp ipv6 routing-table dampened** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes. |
| Network | Indicates the network address in the BGP routing table. |
| PrefixLen | Prefix length. |
| From | Indicates the IP address of the peer that receives the routes. |
| Reuse | Reuse value (in seconds). |
| Path/Ogn | Indicates the AS\_Path number and the Origin attribute of the route. |