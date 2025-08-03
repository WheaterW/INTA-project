bfd all-interfaces incr-cost (IS-IS view)
=========================================

bfd all-interfaces incr-cost (IS-IS view)

Function
--------



The **bfd all-interfaces incr-cost** command configures each interface in an IS-IS process to adjust its cost based on the status of an associated BFD session.

The **undo bfd all-interfaces incr-cost** command restores the default configuration.



By default, no interface in an IS-IS process adjusts its cost based on the status of an associated BFD session.

By default, an IS-IS process does not cancel the cost adjusted by BFD after a delay.




Format
------

**bfd all-interfaces incr-cost** { *cost-value* | **max-reachable** }

**undo bfd all-interfaces incr-cost** [ *cost-value* | **max-reachable** ]


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

Either a link fault or topology change on a network will cause routes to be re-calculated within an area. As such, speeding up the convergence of a routing protocol is critical to improving the network performance.As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly resolve such issues. This includes associating BFD with a routing protocol to speed up convergence of the routing protocol once a link fault occurs.On a network where BFD detects a link fault, even if the fault is rectified quickly, the involved interface is disconnected due to the fact that the associated BFD session is down. As a result, the link is unstable and traffic is lost. To ensure network reliability and solve the preceding problems, you can run the **bfd all-interfaces incr-cost** command in an IS-IS process to adjust the link cost. When an interface in the IS-IS process detects that the BFD session goes Down, the interface automatically increases the link cost, the link whose BFD status is Down is not preferentially selected, and traffic can be transmitted over other links.When an interface detects that a BFD session goes Up, the cost of the interface is automatically restored to the original value. To prevent frequent BFD status changes caused by link quality, traffic loss may occur due to link instability. To solve the preceding problem, you can set the bfd all-interfaces incr-cost wtr parameter in the IS-IS process to delay the interface cost recovery. A BFD status change within the delay does not cause a path calculation change, ensuring network reliability.

**Prerequisites**

BFD has been enabled in the IS-IS process using the **bfd all-interfaces enable** command.

**Precautions**

If the function of adjusting the cost based on the status of an associated BFD session is configured both for an IS-IS process and an interface, the configuration on the interface takes precedence.The cost recovery delay configured for BFD association on an interface takes precedence over the cost recovery delay configured for BFD association in a process.If the association between BFD and cost is not configured on an interface but is configured in a process, delayed recovery is not started on the interface.The link cost of an interface depends on the cost style:

* When the cost style is narrow, narrow-compatible, or compatible, the value ranges from 1 to 63.
* If the cost style is wide or wide-compatible, the value ranges from 1 to 16777214.

Example
-------

# Configure each interface in an IS-IS process to adjust its cost based on the status of an associated BFD session, with the cost increment set to 5. If a BFD session goes down, the associated interface increases its cost by 5.
```
<HUAWEI> system-view
[~HUAWEI] isis 100
[*HUAWEI-isis-100] bfd all-interfaces incr-cost 5

```