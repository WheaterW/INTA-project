ipv6 maximum load-balancing
===========================

ipv6 maximum load-balancing

Function
--------

By default, load balancing is supported. For details about the maximum number of equal-cost routes, see the parameter value range.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 maximum load-balancing** *number*

**undo ipv6 maximum load-balancing**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the number of equal-costs for load balancing. | The value is an integer. The value ranges from 1 to 128. The default value is 128. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IPv6 has been enabled for the IS-IS process using the **ipv6 enable** command in the IS-IS view.

**Precautions**

When the number of equal-cost routes on the network is greater than the value specified in the **ipv6 maximum load-balancing** command, valid routes are selected for load balancing according to the following rules:

1. Route weight: Routes with small weight values (high priority) are selected for load balancing.
2. Next-hop system ID: If routes have the same weight, those with small system IDs are selected for load balancing.
3. Outbound interface index: If routes have the same weight and system ID, those with small outbound interface indexes are selected for load balancing.
4. Next-hop IP address: If the weights, next-hop system IDs, and interface indexes of the routes are the same, their next-hop IP addresses are compared. The routes with high IP addresses are selected for load balancing.

Example
-------

# Set the maximum number of IS-IS IPv6 routes for load balancing to 1.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] ipv6 enable
[*HUAWEI-isis-100] ipv6 maximum load-balancing 1

```