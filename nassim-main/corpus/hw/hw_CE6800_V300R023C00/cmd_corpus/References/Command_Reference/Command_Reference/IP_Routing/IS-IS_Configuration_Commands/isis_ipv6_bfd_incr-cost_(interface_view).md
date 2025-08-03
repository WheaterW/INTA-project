isis ipv6 bfd incr-cost (interface view)
========================================

isis ipv6 bfd incr-cost (interface view)

Function
--------



The **isis ipv6 bfd incr-cost** command configures an interface to adjust its cost based on the status of an associated IPv6 BFD session.

The **undo isis ipv6 bfd incr-cost** command cancels this configuration.

The **isis ipv6 bfd incr-cost block** command blocks an interface from adjusting its cost based on the status of an associated IPv6 BFD session.

The **undo isis ipv6 bfd incr-cost block** command cancels this configuration.



By default, an IS-IS interface does not adjust its cost based on the status of an associated BFD session.

By default, an IS-IS interface is not blocked from adjusting its cost based on the status of an associated IPv6 BFD session.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 bfd incr-cost** { *cost-value* | **max-reachable** }

**isis ipv6 bfd incr-cost block**

**undo isis ipv6 bfd incr-cost** [ *cost-value* | **max-reachable** ]

**undo isis ipv6 bfd incr-cost block**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost-value* | Specifies a cost increment value for the interface. | The value is an integer ranging from 1 to 16777213. |
| **max-reachable** | Changes the cost of the interface to the maximum value 16777214. | - |
| **block** | Blocks the IS-IS interface from adjusting its cost based on the status of an associated BFD session. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Either a link fault or topology change on a network will cause routes to be re-calculated within an area. As such, speeding up the convergence of a routing protocol is critical to improving the network performance.As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. This includes associating BFD with a routing protocol to speed up convergence of the routing protocol once a link fault occurs.On a network where BFD detects a link fault, even if the fault is rectified quickly, the involved interface is disconnected due to the fact that the associated BFD session is down. As a result, the link is unstable and traffic is lost. To ensure network reliability and solve the preceding problems, run the **isis ipv6 bfd incr-cost** command on an IS-IS interface to adjust the link cost. When the IS-IS interface detects that IPv6 BFD goes Down, the IS-IS interface automatically increases the link cost, the link whose IPv6 BFD status is Down is not preferentially selected, and traffic can be transmitted over other links.When an interface detects that an IPv6 BFD session goes Up, the cost of the interface is automatically restored to the original value. To prevent frequent BFD status changes caused by link quality, traffic loss may occur due to link instability. To solve the preceding problem, you can set the isis ipv6 bfd incr-cost wtr parameter on an IS-IS interface to set a delay in recovering the link cost. If the IPv6 BFD session status changes within the delay, route calculation does not change. This ensures network reliability.

**Prerequisites**

IPv6 BFD has been enabled on the interface using the **isis ipv6 bfd enable** command.

**Precautions**

The cost associated with IPv6 BFD configured on an interface takes precedence over that associated with IPv6 BFD configured in a process.The IPv6 BFD cost recovery delay configured on an interface takes precedence over the IPv6 BFD cost recovery delay configured in a process.If no IPv6 BFD cost recovery delay is configured on an interface but an IPv6 BFD cost recovery delay is configured in a process, delayed recovery is not started on the interface.The isis ipv6 bfd incr-cost and **isis ipv6 bfd incr-cost block** commands are mutually exclusive. The latest configuration overrides the previous one.The link cost of an interface depends on the cost style:

* When the cost style is narrow, narrow-compatible, or compatible, the value ranges from 1 to 63.
* If the cost style is wide or wide-compatible, the value ranges from 1 to 16777214.

Example
-------

# Configure an interface to adjust its cost based on the status of an associated IPv6 BFD session, with the cost increment set to 2. If the associated IPv6 BFD session goes down, the interface increases its cost by 2.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 bfd incr-cost 2

```