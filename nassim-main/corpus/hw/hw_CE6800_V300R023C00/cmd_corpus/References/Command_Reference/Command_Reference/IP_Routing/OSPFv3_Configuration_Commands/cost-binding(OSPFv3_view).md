cost-binding(OSPFv3 view)
=========================

cost-binding(OSPFv3 view)

Function
--------



The **cost-binding** command associates a specified interface and the router ID of a route originator.

The **undo cost-binding** command deletes the association.



By default, an interface is not associated with the router ID of a route originator.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**cost-binding interface** { *interfaceName* | *interfaceType* *interfaceNum* } **route-source-routerid** *router-id-value*

**undo cost-binding interface** { *interfaceName* | *interfaceType* *interfaceNum* } **route-source-routerid** *router-id-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interfaceType* | Specifies the interface type. | - |
| *interfaceNum* | Specifies the interface number. | - |
| **route-source-routerid** *router-id-value* | Specify the router ID of a route originator. | The value is in dotted decimal notation. |
| **interface** *interfaceName* | Specifies an interface name. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To associate a specified interface and the router ID of a route originator, run the **cost-binding** command. If the interface fails, the cost of each intra-area route learned from the associated route originator is changed to the maximum value 65534. When the interface recovers, the cost of each such route is changed back to the original value.If an M-LAG member interface fails, downstream traffic is transmitted through the peer-link, consuming bandwidth. To prevent this issue, run the **cost-binding** command to associate the M-LAG member interface and the router ID of the route originator so that downstream traffic will not be transmitted through the peer-link.

**Precautions**

A single OSPFv3 process or an IPv6 device running OSPFv3 multi-process supports a maximum of 2000 **cost-binding** command configurations.


Example
-------

# Associate a specified interface and the router ID of a route originator.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] cost-binding interface Eth-Trunk 2 route-source-routerid 1.1.1.1

```