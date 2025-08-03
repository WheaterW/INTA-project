ipv6 bfd all-interfaces incr-cost (IS-IS view)
==============================================

ipv6 bfd all-interfaces incr-cost (IS-IS view)

Function
--------



The **ipv6 bfd all-interfaces incr-cost** command configures each interface in an IPv6 IS-IS process to adjust its cost based on the status of an associated BFD session.

The **undo ipv6 bfd all-interfaces incr-cost** command restores the default configuration.



By default, an IPv6 IS-IS process does not adjust the cost based on BFD.

By default, an IS-IS process does not delay withdrawing the cost adjusted by IPv6 BFD.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 bfd all-interfaces incr-cost** { *cost-value* | **max-reachable** }

**undo ipv6 bfd all-interfaces incr-cost** [ *cost-value* | **max-reachable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost-value* | Specifies a cost increment value for all interfaces in the IS-IS process. | The value is an integer ranging from 1 to 16777213. |
| **max-reachable** | Changes the cost of each interface in the IS-IS process to the maximum value 16777214. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Either a link fault or topology change on a network will cause routes to be re-calculated within an area. As such, speeding up the convergence of a routing protocol is critical to improving the network performance.As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. This includes associating BFD with a routing protocol to speed up convergence of the routing protocol once a link fault occurs.On a network where BFD detects a link fault, even if the fault is rectified quickly, the involved interface is disconnected due to the fact that the associated BFD session is down. As a result, the link is unstable and traffic is lost. To ensure network reliability and solve the preceding problems, you can run the **ipv6 bfd all-interfaces incr-cost** command in the IPv6 IS-IS process to adjust the link cost. When an interface in the IPv6 IS-IS process detects that the BFD session goes Down, the cost of the interface is automatically increased, the link whose BFD status is Down is not preferentially selected, and traffic can be transmitted over other links.When an interface detects that an IPv6 BFD session goes Up, the cost of the interface is automatically restored to the original value. To prevent frequent BFD status changes caused by link quality, traffic loss may occur due to link instability. To solve the preceding problem, you can set the ipv6 bfd all-interfaces incr-cost wtr parameter in the IS-IS process to set a delay for restoring the interface cost. If the IPv6 BFD session status changes within the delay, route calculation does not change. This ensures network reliability.

**Prerequisites**

BFD has been enabled in the IPv6 IS-IS process using the **ipv6 bfd all-interfaces enable** command.

**Precautions**

If the function of adjusting the cost based on the status of an associated BFD session is configured both for an IS-IS process and an interface, the configuration on the interface takes precedence.The cost recovery delay configured for BFD association on an interface takes precedence over the cost recovery delay configured for BFD association in a process.If the association between BFD and cost is not configured on an interface but is configured in a process, delayed recovery is not started on the interface.The link cost of an interface depends on the cost style:

* When the cost style is narrow, narrow-compatible, or compatible, the value ranges from 1 to 63.
* If the cost style is wide or wide-compatible, the value ranges from 1 to 16777214.

Example
-------

# Configure each interface in an IPv6 IS-IS process to adjust its cost based on the status of an associated BFD session, with the cost increment set to 5. If a BFD session goes down, the associated interface increases its cost by 5.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] ipv6 enable topology ipv6
[*HUAWEI-isis-100] ipv6 bfd all-interfaces incr-cost 5

```