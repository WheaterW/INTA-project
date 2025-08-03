vxlan vni (VPN instance view)
=============================

vxlan vni (VPN instance view)

Function
--------



The **vxlan vni** command binds a VXLAN network identifier (VNI) to a virtual private network (VPN) instance.

The **undo vxlan vni** command unbinds a VNI from a VPN instance.



By default, a VNI is not bound to any VPN instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan vni** *vni-id*

**undo vxlan vni** *vni-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI ID. | The value is an integer ranging from 1 to 16777215. |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To isolate tenants at Layer 3, VPN is generally used. In a distributed VXLAN gateway scenario, to implement Layer 3 communication through a Layer 3 gateway, the Layer 3 gateway must be bound to a VPN instance.The Layer 3 gateway assigns a Layer 2 VNI to each tenants and a Layer 3 VNI to each tenant identified by a VPN instance. To bind a VNI to a VPN instance, run the vxlan vni command. During Layer 3 communication through the Layer 3 gateway, the VNI ID bound to the VPN instance is transmitted to the remote Layer 3 gateway through the VXLAN tunnel. The remote Layer 3 gateway identifies VPNs based on tenants' VNI IDs to determine whether tenants belong to the same VPN for communication or isolation purposes.

**Precautions**

A VNI can be bound only to one VPN instance.The VNI bound to a VPN instance cannot be bound to a BD.


Example
-------

# Bind VNI 5000 to a VPN instance named huawei.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] vxlan vni 5000

```