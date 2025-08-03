vni head-end peer-list (NVE interface view) (ipv6)
==================================================

vni head-end peer-list (NVE interface view) (ipv6)

Function
--------



The **vni head-end peer-list** command configures an ingress replication list that contains the IP addresses of those remote VTEPs for a VXLAN network identifier (VNI).

The **undo vni head-end peer-list** command deletes the ingress replication list of a VNI.



By default, no ingress replication list is configured for any VNI.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-id* **head-end** **peer-list** { *ipv6-address* } &<1-10>

**undo vni** *vni-id* **head-end** **peer-list** { *ipv6-address* } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI ID. | The value is an integer ranging from 1 to 16777215. |
| *ipv6-address* | Specifies an IPv6 address for a remote VTEP. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the ingress of a VXLAN tunnel receives broadcast, unknown unicast, and multicast (BUM) packets, it replicates these packets and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IP addresses to which the ingress of a VXLAN tunnel should send replicated BUM packets.If an underlay network is an IPv6 network, run the vni head-end peer-list (IPv6) command to configure an ingress replication list that contains IPv6 addresses of remote VTEPs, which is used to forward BUM traffic.

**Configuration Impact**

Ingress replication allows BUM packets to be transmitted in broadcast mode, independent of multicast routing protocols.

**Precautions**

Even if a source VTEP connects only to one remote IPv6 VTEP, you still need to run the vni head-end peer-list (IPv6) command to configure an ingress replication list with the remote VTEP's IP address specified.


Example
-------

# Configure an IPv6 ingress replication list for VNI 5020, with the remote VTEPs' IPv6 addresses being 2001:db8:1::1 and 2001:db8:1::2.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] vni 5020 head-end peer-list 2001:db8:1::1 2001:db8:1::2

```