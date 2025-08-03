l2protocol-tunnel group-mac
===========================

l2protocol-tunnel group-mac

Function
--------



The **l2protocol-tunnel group-mac** command configures a device to replace the multicast destination MAC addresses in Layer 2 PDUs with a specified multicast MAC address.

The **undo l2protocol-tunnel** command deletes the multicast destination MAC address of Layer 2 PDUs (except STP BPDUs that use the default multicast MAC address) or restores the default multicast destination MAC address of STP BPDUs.



By default, the group MAC address of STP BPDUs is 0100-0ccd-cdd0, and Layer 2 PDUs of all Layer 2 protocols except STP do not have a default group MAC address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**l2protocol-tunnel** *protocol* **group-mac** { *group-mac* | **default-group-mac** }

**undo l2protocol-tunnel** *protocol*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *protocol* | Replaces the destination MAC address in Layer 2 PDUs of a specified protocol with a specified multicast MAC address. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * pvst+ * stp * udld * vtp   You must select at least one protocol and at most all protocols. |
| **group-mac** *group-mac* | Specifies the multicast MAC address which is used to replace the destination MAC address in Layer 2 PDUs. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. group-mac must start with 0x01 and cannot be any of the following multicast MAC addresses:   * Multicast MAC addresses that are in use on the local device * 0180-C200-0000 to 0180-C200-002F, which are used for BPDUs * 010F-E200-0004, which is used for Smart Link packets * 0100-0CCC-CCCC and 0100-0CCC-CCCD, which are reserved for specific purposes |
| **default-group-mac** | Indicates the default group MAC address, which has a fixed value of 0100-0ccd-cdd0.  Most Layer 2 protocols can be identified by protocol type. You can configure a group MAC address for this type of protocol to reduce configuration workload. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Some Layer 2 protocols running between user networks, such as Multiple Spanning Tree Protocol (MSTP) and Link Aggregation Control Protocol (LACP), must traverse a backbone network to perform Layer 2 protocol calculation.Generally, the destination MAC addresses in Layer 2 PDUs of the same Layer 2 protocol are the same. For example, the MSTP PDUs have a destination MAC address 0180-C200-0000. When a Layer 2 PDU reaches an edge device on a backbone network, the edge device cannot identify whether the PDU comes from a user network or the backbone network and sends the PDU to the CPU to calculate a spanning tree. As a result, the user network devices calculate a spanning tree with backbone network edge devices but not with user network devices.To resolve this problem, run the l2protocol-tunnel group-mac command on backbone network edge devices to replace the multicast destination MAC addresses in Layer 2 PDUs with a specified multicast MAC address (group MAC address). This configuration allows Layer 2 PDUs to be tunneled so that user network devices can calculate a spanning tree.

**Follow-up Procedure**

The backbone network edge devices determine whether to add an outer VLAN tag to the Layer 2 PDUs with a specified multicast MAC address (group MAC address) based on the configured Layer 2 protocol tunneling type.

**Precautions**

The specified multicast MAC address must be different from the multicast MAC address of a well-known protocol. This prevents Layer 2 PDUs from being sent to the CPU for processing.


Example
-------

# Configure the device to replace the destination MAC address of STP BPDUs with 01e0-fc12-3456 when transparently transmitting STP BPDUs.
```
<HUAWEI> system-view
[~HUAWEI] l2protocol-tunnel stp group-mac 01e0-fc12-3456

```