assign forward nvo3 packet discard
==================================

assign forward nvo3 packet discard

Function
--------



The **assign forward nvo3 packet discard** command configures a device to discard OSPF/OSPFv3 multicast packets received over a VXLAN tunnel.

The **undo assign forward nvo3 packet discard** command configures a device not to discard OSPF/OSPFv3 multicast packets received over a VXLAN tunnel.



By default, the device does not discard the OSPF/OSPFv3 multicast packets received from the tunnel, and the OSPF/OSPFv3 neighbor relationship can be established.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign forward nvo3** { **ospf** | **ospfv3** } **packet** **discard**

**undo assign forward nvo3** { **ospf** | **ospfv3** } **packet** **discard**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ospf** | Indicates that the device discards network-side OSPF packets. | - |
| **ospfv3** | Indicates that the device discards network-side OSPFv3 packets. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After OSPF/OSPFv3 multicast packets enter the local device from a VXLAN tunnel, the packets are sent to the local device CPU for processing before being forwarded by default. If a local device does not need to establish an OSPF/OSPFv3 neighbor relationship over a VXLAN tunnel and the number of irrelevant OSPF/OSPFv3 packets received by the IPU needs to be reduced, run this command to configure the local device to discard OSPF/OSPFv3 multicast packets received from a VXLAN tunnel.


Example
-------

# Configure the device to discard the OSPF packets received through the VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] assign forward nvo3 ospf packet discard

```

# Configure the device not to discard the OSPF packets received through the VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] undo assign forward nvo3 ospf packet discard

```