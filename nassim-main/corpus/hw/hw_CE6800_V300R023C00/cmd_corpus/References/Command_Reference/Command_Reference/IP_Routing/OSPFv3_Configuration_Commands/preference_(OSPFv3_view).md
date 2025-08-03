preference (OSPFv3 view)
========================

preference (OSPFv3 view)

Function
--------



The **preference** command sets a priority for OSPFv3 routes.

The **undo preference** command restores the default value.



By default, the priority of OSPF routes is 10. When ASE is specified, the default value is 150.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**preference** { *preference* | { **route-policy** *route-policy-name* } } \*

**preference ase** { *preference* | { **route-policy** *route-policy-name* } } \*

**undo preference**

**undo preference ase**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *preference* | Specifies a priority for OSPFv3 routes. | The value is an integer in the range from 1 to 255. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ase** | Sets a priority for AS external routes or NSSA routes. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Multiple dynamic routing protocols may be run on the device. The system needs to set a default priority for each routing protocol. If different protocols have routes to the same destination, the protocol with the higher priority is selected to forward IP packets. To set a priority for OSPFv3 routes, run the preference command.The smaller the priority value, the higher the priority.

**Precautions**

When a device runs multiple routing protocols, changing the OSPFv3 preference may change the inter-protocol route selection result in the routing table.


Example
-------

# Set a priority for OSPFv3 routes.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] preference 5

```