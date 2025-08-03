circuit-cost (IS-IS view)
=========================

circuit-cost (IS-IS view)

Function
--------



The **circuit-cost** command sets a link cost for all IS-IS interfaces.

The **undo circuit-cost** command restores the default value.

The **ipv6 circuit-cost** command sets an IPv6 cost for the Shortest Path First (SPF) calculation, which is valid for all Level-1 and Level-2 IPv6 interfaces.

The **undo ipv6 circuit-cost** command deletes the configured cost.



By default, the link cost for IS-IS loopback interfaces is 0, and the default link cost for other interfaces is 10.

By default, the configured cost is applicable to all Level-1 and Level-2 IPv6 interfaces. The default cost is 10.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**circuit-cost** { *cost* } [ **level-1** | **level-2** ]

**undo circuit-cost** [ *cost* ] [ **level-1** | **level-2** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 circuit-cost** { *cost* } [ **level-1** | **level-2** ]

**undo ipv6 circuit-cost** [ *cost* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost* | Specifies a link cost for IS-IS interfaces. | The value is an integer.   * The value ranges from 1 to 63 when the cost type is narrow, narrow-compatible, or compatible. * The value ranges from 1 to 16777214 when the cost type is wide or wide-compatible. The cost type can be configured using the cost-style command. |
| **level-1** | Sets a link cost for all Level-1 interfaces. | - |
| **level-2** | Sets a link cost for all Level-2 interfaces.  If Level-1 or Level-2 is not specified in the command, the link cost is set for Level-1-2 interfaces by default. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On large networks, there may be multiple valid routes to the same destination. IS-IS uses the SPF algorithm to calculate an optimal route and transmits traffic over it, which brings the problem that all traffic is transmitted over the optimal route, causing load imbalance.To solve the preceding problems, run the **circuit-cost** command to set a link cost for interfaces so that traffic can be transmitted over different physical links.The cost of an IPv6 interface takes precedence over the global IPv6 cost.Before using the ipv6 **circuit-cost** command in an IS-IS process, enable IPv6 in the IS-IS process. For details, see the **isis ipv6 enable** command.



**Prerequisites**



An IS-IS process has been created using the **isis** command.



**Configuration Impact**



If the link cost of an interface is changed, routes will be re-calculated on the whole network, causing the changes in traffic forwarding paths.



**Precautions**



The priority of the **circuit-cost** command is lower than that of the **isis cost** command.To allow the link cost of IS-IS routes to reflect the actual link cost, configuring a proper link cost for an interface is recommended.




Example
-------

# Set the default cost of all interfaces to 30.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] circuit-cost 30

```

# Set the global IPv6 cost for the SPF calculation to 20.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 circuit-cost 20

```