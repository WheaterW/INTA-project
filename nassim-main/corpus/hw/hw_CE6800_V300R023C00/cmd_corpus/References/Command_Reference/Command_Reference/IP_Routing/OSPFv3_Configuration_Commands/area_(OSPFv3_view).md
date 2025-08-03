area (OSPFv3 view)
==================

area (OSPFv3 view)

Function
--------



The **area** command creates an OSPFv3 area and displays the OSPFv3 area view.

The **undo area** command deletes the specified OSPFv3 area.



By default, no OSPFv3 area is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**area** { *area-id* | *area-idipv4* }

**undo area** { *area-id* | *area-idipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *area-id* | Specifies the area ID in decimal format. | The value is an integer that ranges from 0 to 4294967295. |
| *area-idipv4* | The value is an area ID in dotted decimal notation. | The value is in dotted decimal notation. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The number of devices increases with the network expansion, which leads to a large LSDB on each OSPFv3-enabled device on a large-scale network. Consequently, route flapping frequently occurs, and a large number of OSPFv3 packets are transmitted on the network, which wastes bandwidth resources.OSPFv3 addresses the preceding problem by logically partitioning an AS into different areas.

**Prerequisites**

Before creating and entering an OSPFv3 area, you need to enter the OSPFv3 process.

**Precautions**

After an AS is partitioned into different areas, not all areas are equal. The area with ID 0 is a backbone area. The backbone area is responsible for forwarding inter-area routes. In addition, the routing information between non-backbone areas must be forwarded through the backbone area.The first time the area command is run, an OSPFv3 area is created and the OSPFv3 area view is displayed; running the area command later enters the OSPFv3 area view only.If the **undo area** command is run, all configurations in the OSPFv3 area are deleted. Therefore, exercise caution when using the command.


Example
-------

# Enter the OSPFv3 area 0 view.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 0
[*HUAWEI-ospfv3-1-area-0.0.0.0]

```