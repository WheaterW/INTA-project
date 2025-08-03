ipv6 prefix-priority (IS-IS view)
=================================

ipv6 prefix-priority (IS-IS view)

Function
--------



The **ipv6 prefix-priority** command sets a convergence priority for IPv6 IS-IS routes.

The **undo ipv6 prefix-priority** command restores the default value.



By default, in IP routing table, the priority of IS-IS host routes and default routes is high; the convergence priority of the other IS-IS routes is medium.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 prefix-priority** [ **level-1** | **level-2** ] { **critical** | **high** | **medium** | **very-low** } { **ipv6-prefix** *prefix-name* | **tag** *tag-value* }

**undo ipv6 prefix-priority** [ **level-1** | **level-2** ] { **critical** | **high** | **medium** | **very-low** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Sets a convergence priority for Level-1 IS-IS routes. | - |
| **level-2** | Sets a convergence priority for Level-2 IS-IS routes. | - |
| **critical** | Sets the convergence priority of IS-IS routes to critical. | - |
| **high** | Sets the convergence priority of IS-IS routes to high. | - |
| **medium** | Sets the convergence priority of IS-IS routes to medium. | - |
| **very-low** | Sets the convergence priority of IS-IS routes to very-low. | - |
| **ipv6-prefix** *prefix-name* | Specifies the name of an IPv6 prefix list to filter routes. You can set a convergence priority for the IS-IS routes that match the specified IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters. |
| **tag** *tag-value* | Specifies the tag value to filter routes. You can set a convergence priority for the IS-IS routes with the specified tag value. | The value is an integer ranging from 1 to 4294967295. There is no default value. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a routing table has a large number of routing entries on an IS-IS device, it takes a long time to implement the SPF calculation on the device. The ipv6 **prefix-priority** command can be used to allow some key routes to be preferentially calculated.The command takes effect only on the basic IPv6 topology on the public network.

**Prerequisites**

If a tag value is used to filter IPv6 IS-IS routes and configure a convergence priority for the matched routes, it is required that these routes carry tag values.

**Configuration Impact**

The convergence priorities of IS-IS routes can be critical, high, medium, low, and very-low. The priorities in the corresponding IP routing table are critical, high, high, medium, and low. The priorities are listed in descending order.The convergence priority of IS-IS routes is used as follows:

* For the existing IS-IS routes, IS-IS resets the convergence priority for the routes based on the **prefix-priority** command.
* For the newly added IS-IS routes, IS-IS sets the convergence priority for the routes based on the filtering result of the **prefix-priority** command.
* If an IS-IS route matches the matching rules of multiple convergence priorities, the highest convergence priority is used.
* If an IS-IS route matches tags of multiple convergence priorities, the highest convergence priority is used.
* If the route level is not specified, IS-IS configures convergence priorities for both Level-1 routes and Level-2 routes.

**Precautions**

The convergence priority of IS-IS routes (including the IS-IS host routes and default routes) can be specified or changed using the **prefix-priority** command. After the **prefix-priority** command is run, the convergence priority of the routes (including the IS-IS host routes and default routes) unspecified by the command is changed to low.


Example
-------

# In a basic IPv6 topology, set the convergence priority of IS-IS Level-1 routes with the tag 3 to critical.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 prefix-priority level-1 critical tag 3

```