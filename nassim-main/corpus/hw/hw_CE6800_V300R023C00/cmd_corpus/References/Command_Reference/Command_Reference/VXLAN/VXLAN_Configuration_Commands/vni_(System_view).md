vni (System view)
=================

vni (System view)

Function
--------



The **vni** command creates a VXLAN network identifier (VNI) and displays the VNI view. If a VNI has been created, the VNI view is directly displayed.

The **undo vni** command deletes a configured VNI.



By default, no VNI is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vni** *vni-id*

**undo vni** *vni-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI ID. | The value is an integer ranging from 1 to 16777215. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

VNIs, similar to VLAN IDs, are used to differentiate VXLAN segments and identify tenants. A VNI identifies only one tenant. If multiple terminal users share the same VNI, they are considered one tenant. To create a global VNI and enter the VNI view, run the vni command. Then, global VNI configurations can be performed in the view.

**Follow-up Procedure**

Run the **peer ip-address** command in the VNI view to create and display the VNI peer view.


Example
-------

# Create a VNI with the VNI ID of 4096.
```
<HUAWEI> system-view
[~HUAWEI] vni 4096

```