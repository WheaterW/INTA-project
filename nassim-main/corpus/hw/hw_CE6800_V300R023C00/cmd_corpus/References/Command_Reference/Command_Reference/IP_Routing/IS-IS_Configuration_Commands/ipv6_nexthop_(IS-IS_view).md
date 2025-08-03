ipv6 nexthop (IS-IS view)
=========================

ipv6 nexthop (IS-IS view)

Function
--------



The **ipv6 nexthop weight** command sets a weight for an IPv6 IS-IS equal-cost route.

The **undo ipv6 nexthop** command cancels the weight set for an IPv6 IS-IS equal-cost route.



By default, no weight is set for IPv6 IS-IS equal-cost routes, and IS-IS forwards packets in load balancing mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nexthop** *ip-address* **weight** *weight-value*

**undo ipv6 nexthop** *ip-address* [ **weight** *weight-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a next-hop IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **weight** *weight-value* | Specifies a next-hop weight. | The value is an integer that ranges from 1 to 254. The default value is 255. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When multiple redundant links exist on an IPv6 IS-IS network, multiple equal-cost IPv6 IS-IS routes may exist. That is, there are multiple equal-cost paths to a destination network segment.You can run the **ipv6 nexthop weight** command to set a weight for the next hop so that the next hop can be specified without changing the interface cost. The smaller the weight value, the higher the priority.

**Prerequisites**

An IS-IS process has been created using the **isis** command, and IPv6 has been enabled for this process using the **ipv6 enable** command.

**Configuration Impact**

After the nexthop command is run, an IS-IS device does not forward traffic in load balancing mode to a specific destination network segment, but forwards traffic to the next hop with the highest priority.


Example
-------

# In the IS-IS view, set the weight of the next hop with the IPv6 address 2001:DB8:1::1 to 1 for the equal-cost route.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 nexthop 2001:DB8:1::1 weight 1

```