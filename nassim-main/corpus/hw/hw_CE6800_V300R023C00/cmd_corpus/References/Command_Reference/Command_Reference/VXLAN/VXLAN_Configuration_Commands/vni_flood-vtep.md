vni flood-vtep
==============

vni flood-vtep

Function
--------



The **vni flood-vtep** command configures a centralized replication list for a VNI.

The **undo vni flood-vtep** command deletes a centralized replication list from a VNI.



By default, no centralized replication list is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-id* **flood-vtep** { *ip-address* } &<1-10>

**undo vni** *vni-id* **flood-vtep** { *ip-address* } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI ID. | The value is an integer ranging from 1 to 16777215. |
| *ip-address* | Specifies an IP address in the centralized replication list.  A VNI can configure a maximum of 16 IP address. | The value is in dotted decimal notation. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a source VTEP on a VXLAN connects to multiple remote VTEPs on the same VXLAN segment, run the **vni flood-vtep** command to configure a centralized replication list that contains the IP addresses of those remote VTEPs. Among the remote VTEP IP addresses, only one is in the working state, and others are in the backup state. After the source NVE receives broadcast, unknown unicast, and multicast (BUM) packets, the local VTEP sends a copy of the BUM packets to a replicator. The replicator then sends the BUM packets to other VTEPs with the same VNI except for the source VTEP.If BFD detects that the master VTEP is unavailable, it re-selects an available backup VTEP to function as the centralized replicator.

**Precautions**

Centralized replication takes precedence over ingress replication. If both the vni flood-vtep and **vni head-end peer-list** commands are run on a device, VXLAN tunnels use the centralized replication mode for packet forwarding.


Example
-------

# Configure a centralized replication list for VNI 1 with VTEP address 1.1.1.1 contained in the list.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] vni 1 flood-vtep 1.1.1.1

```