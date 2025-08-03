vxlan statistics enable (NVE interface view)
============================================

vxlan statistics enable (NVE interface view)

Function
--------



The **vxlan statistics enable** command enables the function of collecting IPv6 VXLAN packet statistics based on the VNI and IPv6 VXLAN tunnel.

The **undo vxlan statistics enable** command disables the function of collecting IPv6 VXLAN packet statistics based on the VNI and IPv6 VXLAN tunnel.



By default, the function of collecting IPv6 VXLAN packet statistics based on the VNI and IPv6 VXLAN tunnel is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan statistics peer** *destIpv6Addr* **vni** *vni-val* **enable**

**vxlan statistics peer** *destIpv6Addr* **enable**

**vxlan statistics source** *srcIpv6Addr* **peer** *destIpv6Addr* **enable**

**vxlan statistics source** *srcIpv6Addr* **peer** *destIpv6Addr* **vni** *vni-val* **enable**

**undo vxlan statistics peer** *destIpv6Addr* **vni** *vni-val* **enable**

**undo vxlan statistics peer** *destIpv6Addr* **enable**

**undo vxlan statistics source** *srcIpv6Addr* **peer** *destIpv6Addr* **enable**

**undo vxlan statistics source** *srcIpv6Addr* **peer** *destIpv6Addr* **vni** *vni-val* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vni** *vni-val* | Enables IPv6 VXLAN packet statistics collection for a specified VNI. | The value is an integer ranging from 1 to 16777215. |
| **peer** *destIpv6Addr* | Enables IPv6 VXLAN packet statistics collection for a specified remote VTEP IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **source** *srcIpv6Addr* | Enables IPv6 VXLAN packet statistics collection for a specified local VTEP IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, IPv6 VXLAN traffic statistics collection is disabled. To enable the IPv6 VXLAN traffic statistics collection function based on a VNI ID and IPv6 VXLAN tunnel, run the **vxlan statistics enable** command. If the function of collecting IPv6 VXLAN packet statistics is disabled, you cannot obtain the statistics.


Example
-------

# Enable the IPv6 VXLAN packet statistics collection function based on the VNI with the ID of 1 and the IPv6 address of the peer VTEP as 2001:DB8:2::2.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] source 2001:DB8:1::1
[*HUAWEI-Nve1] vxlan statistics peer 2001:DB8:2::2 vni 1 enable

```