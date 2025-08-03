assign forward nvo3 disable
===========================

assign forward nvo3 disable

Function
--------



The **assign forward nvo3 disable** command configures a device not to send OSPF/OSPFv3 multicast packets received through a VXLAN tunnel to the local device CPU for processing.

The **undo assign forward nvo3 disable** command configures a device to send OSPF or OSPFv3 multicast packets received through a VXLAN tunnel to the local device CPU for processing.



By default, a device forwards the OSPF/OSPFv3 multicast packets received from a tunnel to the local device for processing, and OSPF/OSPFv3 neighbor relationships can be established.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign forward nvo3** { **ospf** | **ospfv3** } **disable**

**undo assign forward nvo3** { **ospf** | **ospfv3** } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ospf** | Disables the device from establishing an OSPF neighbor relationship through a VXLAN tunnel. | - |
| **ospfv3** | Disables the device from establishing an OSPFv3 neighbor relationship through a VXLAN tunnel. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After OSPF/OSPFv3 multicast packets enter the local device through a VXLAN tunnel, these packets are sent to the local device CPU for processing before being forwarded by default. If the local device does not need to establish an OSPF or OSPFv3 neighbor relationship through a VXLAN tunnel, that is, the local device only needs to forward OSPF/OSPFv3 multicast packets received from a VXLAN tunnel without processing them, run this command.


Example
-------

# Enable a device to establish an OSPF neighbor relationship through a VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] undo assign forward nvo3 ospf disable

```

# Configure a device not to establish an OSPF neighbor relationship through a VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] assign forward nvo3 ospf disable

```