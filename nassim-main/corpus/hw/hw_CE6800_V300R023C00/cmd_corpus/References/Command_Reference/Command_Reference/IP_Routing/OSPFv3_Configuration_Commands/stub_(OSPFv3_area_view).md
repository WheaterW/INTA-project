stub (OSPFv3 area view)
=======================

stub (OSPFv3 area view)

Function
--------



The **stub** command configures an area as a stub area.

The **undo stub** command cancels the configuration.



By default, no area is configured as a stub area.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**stub**

**stub** { **default-route-advertise** **backbone-peer-ignore** | **no-summary** } \*

**undo stub**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default-route-advertise** | Controls the default route's advertisement. | - |
| **backbone-peer-ignore** | Prevents the ABR from checking the neighbor status. | - |
| **no-summary** | Applies only to the ABR in the stub area. After the parameter is specified, the ABR advertises only one summary LSA of the default route to the area, and does not generate any other summary LSAs (this area is also called a totally stub area). | - |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure an area as an OSPFv3 stub area, you must run the stub command in the OSPFv3 area view on all the devices in the area.You can run the default-cost command in the OSPFv3 area view to set the cost of the default summary route that an ABR transmits to a stub area. This command takes effect only on an ABR.If an interface in the Up state exists in the stub area and a neighbor in the Full state exists in the backbone area, the device advertises the default route.If default-route-advertise backbone-peer-ignore is specified in the command and an interface in the Up state exists in the stub area, the device does not check the neighbor status in the backbone area and advertises the default route.


Example
-------

# Configure OSPFv3 area 1 as a stub area.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 1
[*HUAWEI-ospfv3-1-area-0.0.0.1] stub

```