reset bgp unnumbered peer interface flapping-count
==================================================

reset bgp unnumbered peer interface flapping-count

Function
--------



The **reset bgp unnumbered peer interface flapping-count** command clears the flapping count of BGP unnumbered peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **flapping-count**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset bgp ipv6 unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **flapping-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **ipv6** | Indicates the IPv6 unicast address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP peer flapping affects the stability of a BGP network and BGP route convergence.The **reset bgp unnumbered peer interface flapping-count** command can be used to clear the flapping count of BGP unnumbered peers so that the device can re-collect the flapping count of the BGP peers to monitor and locate BGP network problems.

**Configuration Impact**

After the **reset bgp unnumbered peer interface flapping-count** command is run, the flapping statistics about unnumbered BGP peers are cleared and cannot be displayed.

**Follow-up Procedure**

After running the **reset bgp unnumbered peer interface flapping-count** command to clear the flapping count of BGP unnumbered peers, you can run the **display bgp unnumbered peer interface verbose** command to view the flapping count of the BGP peers and locate the fault on the BGP network according to the new statistics.


Example
-------

# Clear the flapping count of BGP unnumbered peers.
```
<HUAWEI> reset bgp unnumbered peer interface 100GE 1/0/1 flapping-count

```