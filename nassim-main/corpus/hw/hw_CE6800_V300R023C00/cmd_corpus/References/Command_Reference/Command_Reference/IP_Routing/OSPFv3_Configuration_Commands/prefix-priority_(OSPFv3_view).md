prefix-priority (OSPFv3 view)
=============================

prefix-priority (OSPFv3 view)

Function
--------



The **prefix-priority** command sets a convergence priority for OSPFv3 routes.

The **undo prefix-priority** command restores the default value.



By default, in an OSPFv3 routing table, the convergence priority of public 128-bit host routes and default routes is medium, and the convergence priority of other OSPFv3 routes is low. In the IP routing table, the convergence priority of OSPFv3 public 32-bit host routes and default routes is high, and the convergence priority of other OSPFv3 routes is medium.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**prefix-priority** { **critical** | **high** | **medium** } **ipv6-prefix** *ipv6-prefix-name*

**undo prefix-priority** { **critical** | **high** | **medium** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **critical** | Sets the convergence priority of OSPF routes to critical. | - |
| **high** | Sets the convergence priority of OSPFv3 routes to high. | - |
| **medium** | Sets the convergence priority of OSPFv3 routes to medium. | - |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set a convergence priority of OSPFv3 routes based on a specified IPv6 prefix list, run the **prefix-priority** command. The command takes effect on the public network only.After the **prefix-priority** command is used in the OSPFv3 view, OSPFv3 route calculation, link-state advertisement (LSA) flooding, and LSDB synchronization can be implemented according to the configured priority, which accelerates route convergence.

**Configuration Impact**

The convergence priorities of OSPFv3 routes can be critical, high, medium, low, and very-low. The priorities in the corresponding IP routing table are critical, high, high, medium, and low. The priorities are listed in descending order.When an LSA meets multiple priorities, the highest priority takes effect.OSPFv3 calculates LSAs in the sequence of intra-area routes, inter-area routes, and AS external routes. This command enables OSPFv3 to calculate the three types of routes separately according to the specified route calculation priorities. Convergence priorities are critical, high, medium, low and very-low. Tvery-o speed up the processing of LSAs with the higher priority, during LSA flooding, the LSAs need to be placed into the corresponding critical, high, medium, low and very-low queues according to priorities.


Example
-------

# Set the convergence priority of OSPFv3 routes of 2001:DB8:1::1/64 to critical.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix critical-prefix index 10 permit 2001:DB8:1::1 64
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] prefix-priority critical ipv6-prefix critical-prefix

```