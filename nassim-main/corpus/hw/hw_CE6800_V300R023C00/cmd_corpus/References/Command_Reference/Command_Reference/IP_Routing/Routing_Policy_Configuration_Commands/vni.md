vni
===

vni

Function
--------



The **vni** command adds a VNI to a VNI list.

The **undo vni** command deletes a VNI from a VNI list.



By default, no VNI is added to a VNI list.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-value*

**undo vni** *vni-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-value* | Specifies a VNI. | The value is an integer ranging from 1 to 16777215. |



Views
-----

VNI set view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

VNIs, similar to VLAN IDs, differentiate virtual extensible local area network (VXLAN) segments and identify tenants. A VNI represents only one tenant, even if multiple terminal users sharing the VNI. To add a VNI to a VNI list, run the **vni** command.


Example
-------

# Add the VNI 10 to a VNI list.
```
<HUAWEI> system-view
[~HUAWEI] filter-list vni abc
[~HUAWEI-vni-list-abc] vni 10

```