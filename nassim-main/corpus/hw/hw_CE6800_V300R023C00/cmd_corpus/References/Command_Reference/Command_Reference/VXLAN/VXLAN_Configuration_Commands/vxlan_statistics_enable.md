vxlan statistics enable
=======================

vxlan statistics enable

Function
--------



The **vxlan statistics enable** command enables the function of collecting VXLAN packet statistics based on the VNI and VXLAN tunnel.

The **undo vxlan statistics enable** command disables the function of collecting VXLAN packet statistics based on the VNI and VXLAN tunnel.



By default, the function of collecting VXLAN packet statistics based on the VNI and VXLAN tunnel is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan statistics peer** *peer-ip* **vni** *vni-id* **enable**

**vxlan statistics peer** *peer-ip* **enable**

**vxlan statistics source** *srcAddr* **peer** *peer-ip* **enable**

**vxlan statistics source** *srcAddr* **peer** *peer-ip* **vni** *vni-id* **enable**

**undo vxlan statistics peer** *peer-ip* **vni** *vni-id* **enable**

**undo vxlan statistics peer** *peer-ip* **enable**

**undo vxlan statistics source** *srcAddr* **peer** *peer-ip* **enable**

**undo vxlan statistics source** *srcAddr* **peer** *peer-ip* **vni** *vni-id* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vni** *vni-id* | Enables VXLAN packets statistics collection based on a specified VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **peer** *peer-ip* | Enables VXLAN packet statistics collection based on the IP address of the peer VTEP. | The value is in dotted decimal notation. |
| **source** *srcAddr* | Enable VXLAN packet statistics collection with a specified local VTEP IP address. | The value is in dotted decimal notation. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, VXLAN traffic statistics collection is disabled. To enable the VXLAN traffic statistics collection function based on a VNI ID and VXLAN tunnel, run the **vxlan statistics enable** command. If the function of collecting VXLAN packet statistics is disabled, you cannot obtain the statistics.


Example
-------

# Enable the VXLAN packet statistics collection function based on the VNI with the ID of 1 and the IP address of the peer VTEP as 1.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] source 1.1.1.1
[*HUAWEI-Nve1] vni 1 head-end peer-list 1.1.1.2
[*HUAWEI-Nve1] vxlan statistics peer 1.1.1.2 vni 1 enable

```