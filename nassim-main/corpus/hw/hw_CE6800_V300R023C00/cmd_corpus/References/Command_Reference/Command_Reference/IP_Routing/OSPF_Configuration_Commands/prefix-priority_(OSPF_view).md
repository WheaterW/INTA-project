prefix-priority (OSPF view)
===========================

prefix-priority (OSPF view)

Function
--------



The **prefix-priority** command sets a convergence priority for OSPF routes.

The **undo prefix-priority** command restores the default value.



By default, in the OSPF routing table, the convergence priority of public 32-bit host routes and default routes is medium, and the convergence priority of other OSPF routes is low. In the IP routing table, the convergence priority of OSPF public 32-bit host routes and default routes is high, and the convergence priority of other OSPF routes is medium.


Format
------

**prefix-priority** { **critical** | **high** | **medium** } **ip-prefix** *ip-prefix-name*

**undo prefix-priority** { **critical** | **high** | **medium** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **critical** | Sets the convergence priority of OSPF routes to critical. | - |
| **high** | Sets the convergence priority of OSPFv3 routes to high. | - |
| **medium** | Sets the convergence priority of OSPFv3 routes to medium. | - |
| **ip-prefix** *ip-prefix-name* | Specifies the prefix list name. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the convergence priority of OSPF routes based on a specified IP prefix list, run the **prefix-priority** command. The command takes effect on the public network only.After the **prefix-priority** command is used in the OSPF view, OSPF route calculation, link-state advertisement (LSA) flooding, and LSDB synchronization can be implemented according to the configured priority. Therefore, route convergence can be controlled.

**Configuration Impact**

The convergence priorities of OSPF routes can be critical, high, medium, low, and very-low. The priorities in the corresponding IP routing table are critical, high, high, medium, and low. The priorities are listed in descending order.When an LSA meets multiple priorities, the highest priority takes effect.OSPF calculates LSAs in the sequence of intra-area routes, inter-area routes, and AS external routes. This command enables OSPF to calculate the three types of routes separately according to the specified route calculation priorities. Convergence priorities are critical, high, medium, low and very-low. To speed up the processing of LSAs with the higher priority, during LSA flooding, the LSAs need to be placed into the corresponding critical, high, medium, low and very-low queues according to priorities.


Example
-------

# Set the convergence priority of OSPF routes of 10.0.0.0/8 to critical.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix critical-prefix index 10 permit 10.0.0.0 8
[*HUAWEI] ospf 1
[*HUAWEI-ospf-1] prefix-priority critical ip-prefix critical-prefix

```