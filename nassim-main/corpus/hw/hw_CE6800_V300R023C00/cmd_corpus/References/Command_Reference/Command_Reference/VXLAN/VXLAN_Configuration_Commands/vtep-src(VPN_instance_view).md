vtep-src(VPN instance view)
===========================

vtep-src(VPN instance view)

Function
--------



The **vtep-src** command configures a source VXLAN tunnel endpoint (VTEP) address for a VXLAN tunnel in a VPN instance.

The **undo vtep-src** command restores the default configuration.



By default, a VXLAN tunnel in a VPN instance uses the source address configured on an NVE interface as the source VTEP address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vtep-src** *ip-address*

**undo vtep-src** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Configures an IP address for the source VTEP of the VXLAN tunnel bound to a VPN instance. | The value is in dotted decimal notation. |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring a VXLAN tunnel, first configure an IP address for the source VTEP. This IP address serves as the source IP address of VXLAN packets. Because a VXLAN tunnel is established between a source VTEP and a peer VTEP, a different IP address also needs to be configured for the peer VTEP. This IP address serves as the destination IP address in VXLAN packets.In a VXLAN application scenario, to enable two VXLAN tunnels that are based on different physical paths between two nodes to load service data and optimize traffic, run the vxlan tunnel source vtep address command on both ends to specify the source VTEP address for the VXLAN tunnel in a VPN instance.

**Precautions**

In a multi-VTEP VXLAN scenario, the advertisement of IRB or IP prefix routes depends on NVE interfaces.


Example
-------

# Configure 10.1.1.1 as the IP address of the source VTEP of the VXLAN tunnel bound to a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] vxlan vni 1
[*HUAWEI-vpn-instance-vpn1] vtep-src 10.1.1.1

```