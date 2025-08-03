vni mcast-group
===============

vni mcast-group

Function
--------



The **vni mcast-group** command enables the multicast replication mode for forwarding BUM packets and sets the multicast replication address of a specific VNI.

The **undo vni mcast-group** command restores the default setting.



By default, BUM packets are forwarded in ingress replication mode, and no multicast replication address is set.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-id* **mcast-group** *ip-address*

**undo vni** *vni-id* **mcast-group** *ip-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI. | The value is an integer ranging from 1 to 16777215. |
| *ip-address* | Specifies a multicast replication address. | The value is a multicast IP address in dotted decimal notation and ranges from 224.0.1.0 to 239.255.255.255. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Using the ingress replication mode to forward a large number of Broadcast&Unknown-unicast&Multicast (BUM) packets on a VXLAN network increases the network load and consumes lots of network bandwidth resources. To resolve the issue, run the **vni mcast-group** command on each VTEP to configure the multicast replication mode. In multicast replication mode, all VTEPs with the same VNI join the same multicast group. A multicast routing protocol, such as PIM, is used to create a multicast forwarding entry for the multicast group. When a VTEP receives a BUM packet from a local VM, it adds a multicast destination IP address to the BUM packet before sends the packet to the remote VTEPs based on the created multicast forwarding entry.After you run the **vni mcast-group** command, mappings between VNIs and multicast groups are established. After receiving a VXLAN multicast packet, the VTEP checks the UNI in the packet. If no matching mapping between the VNI and multicast group is found, the VTEP will discard the packet.

**Precautions**

* This command is mutually exclusive with the **vni flood-vtep** command. In other words, multicast replication and centralized replication of BUM packets cannot be configured together.
* After configuring multicast replication, you can still run the **vni head-end peer-list** command to generate a remote VTEP address list for VXLAN tunnel establishment. However, multicast replication, instead of ingress replication, is used for BUM packets.
* One VNI can be configured with only one multicast replication address, and multiple VNIs can share one multicast replication address. That is, one VNI can correspond to only one multicast group, but one multicast group can correspond to multiple VNIs.
* This command cannot be used if BIDIR-PIM or PIM-DM has been enabled.
* If a VXLAN VNI has been configured in the BD view and IGMP snooping has been enabled in the BD view, multicast replication of BUM packets for the VNI cannot be enabled on an NVE interface.
* If a VXLAN VNI has been configured in the BD view and IGMP has been enabled (using the igmp enable command) in the VBDIF view of the BD, multicast replication of BUM packets for the VNI cannot be enabled on an NVE interface.
* The multicast replication address of a VNI specified on an NVE interface cannot be the same as the share-group address (multicast-domain share-group).
* A multicast group address in the switch-MDT switch-address pool (multicast-domain switch-group-pool) cannot be used as a multicast replication address for a specified VNI on an NVE's interface.

Example
-------

# Configure multicast replication address 224.1.1.1 for VNI 10.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] vni 10 mcast-group 224.1.1.1

```