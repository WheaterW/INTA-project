area
====

area

Function
--------



The **area** command creates an OSPF area and displays the OSPF area view.

The **undo area** command deletes a specified area.



By default, no OSPF area is created.


Format
------

**area** { *area-id* | *area-idipv4* }

**undo area** { *area-id* | *area-idipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *area-id* | Specifies the area ID in decimal format. | The value is an integer from 0 to 4294967295.  A decimal value is automatically converted to a dotted-decimal notation value based on the following rules:   * For a value of 255 or less, it is padded directly with three zeros in the format X.X.X.X. For example, a value of 255 will be converted to 0.0.0.255. * For a value of 256 or greater, each X in the format X.X.X.X can be a maximum of 255. Starting from the right-most X, the X to its immediate left increments by 1 each time it reaches 256. For example, a value of 256 will be converted to 0.0.1.0, 511 will be converted to 0.0.1.255, and 65536 will be converted to 0.1.0.0. |
| *area-idipv4* | Specifies an area ID in IP address format. | The value is in the format X.X.X.X, where each X represents a value from 0 to 255 |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The number of devices increases with the network expansion, which leads to a large LSDB on each OSPF-enabled device on a large-scale network. Consequently, route flapping frequently occurs, and a large number of OSPF packets are transmitted on the network, which wastes bandwidth resources.OSPF addresses the preceding problem by logically partitioning an AS into different areas.

**Prerequisites**

Before creating and entering an OSPF area, you need to enter the OSPF process.

**Precautions**



After an AS is partitioned into different areas, not all areas are equal. The area with ID 0 is a backbone area. The backbone area is responsible for forwarding inter-area routes. In addition, the routing information between non-backbone areas must be forwarded through the backbone area.The first time the area command is run, an OSPF area is created and the OSPF area view is displayed; running the area command later enters the OSPF area view only.If the **undo area** command is run, all configurations in the OSPF area are deleted. Therefore, exercise caution when using the command.




Example
-------

# Enter the view of an OSPF area.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 0

```