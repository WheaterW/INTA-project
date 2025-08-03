vni (NVE interface view)
========================

vni (NVE interface view)

Function
--------



The **vni** command configures a VXLAN network identifier (VNI) for an NVE interface.

The **undo vni** command deletes the VNI for an NVE interface, and deletes all configurations for the same VNI on the current NVE interface.

The **vni head-end peer-list** command configures an ingress replication list that contains the IP addresses of those remote VTEPs for a VXLAN network identifier (VNI).

The **undo vni head-end peer-list** command deletes the ingress replication list of a VNI.



By default, no VNI is configured for an NVE interface, no ingress replication list is configured for any VNI.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-id* [ **head-end** **peer-list** { *ip-address* } &<1-10> ]

**undo vni** *vni-id* [ **head-end** **peer-list** { *ip-address* } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI ID. | The value is an integer ranging from 1 to 16777215. |
| *ip-address* | Specifies the IP address of a remote VXLAN tunnel endpoint (VTEP). | The value is in dotted decimal notation. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

VNIs are similar to VLAN IDs. VXLAN uses VNIs to differentiate VXLAN segments and identify tenants. A VNI identifies only one tenant. Even if multiple terminal users belong to the same VNI, they are considered one tenant. Run this command to configure a VNI for an NVE interface.After the ingress of a VXLAN tunnel receives broadcast, unknown unicast, and multicast (BUM) packets, it replicates these packets and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IP addresses to which the ingress of a VXLAN tunnel should send replicated BUM packets.If a source VTEP on a VXLAN connects to multiple remote VTEPs on the same VXLAN segment, run the **vni head-end peer-list** command to configure an ingress replication list that contains the IP addresses of those remote VTEPs. After the source NVE receives BUM packets, the local VTEP sends a copy of the BUM packets to every VTEP in the list.

**Configuration Impact**

Ingress replication allows BUM packets to be transmitted in broadcast mode, independent of multicast routing protocols.

**Precautions**

Even if a source VTEP connects only to one remote VTEP, you still need to run the **vni head-end peer-list** command to configure an ingress replication list with the remote VTEP's IP address specified.If other configurations are performed for the same VNI on the current NVE interface, the command configuration will be overwritten.


Example
-------

# Configure an ingress replication list for VNI 5010, with the remote VTEPs' IP addresses being 2.2.2.2 and 3.3.3.3.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] vni 5010 head-end peer-list 2.2.2.2 3.3.3.3

```

# Configures a VNI for an NVE interface.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] vni 10

```