vxlan vni
=========

vxlan vni

Function
--------



The **vxlan vni** command creates a VXLAN network identifier (VNI) and binds it to a BD.

The **undo vxlan vni** command unbinds a VNI from a BD.



By default, no VNI is created.

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

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A virtual network (VN) on a VXLAN is a virtual broadcast domain. To allow a BD to function as a VXLAN network entity to transmit VXLAN traffic, run the **vxlan vni** command to map a VNI to a BD.

**Precautions**

* The VNI bound to a VPN instance cannot be bound to a BD.

Example
-------

# Bind VNI 5000 to BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 5000

```