filter-list vni
===============

filter-list vni

Function
--------



The **filter-list vni** command creates a VNI list and display the VNI list view.

The **undo filter-list vni** command deletes a VNI list.



By default, no VNI list is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**filter-list vni** *name*

**undo filter-list vni** *name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies a VNI list name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

VNIs, similar to VLAN IDs, differentiate virtual extensible local area network (VXLAN) segments and identify tenants. A VNI represents one tenant, even if multiple terminal users share the same VNI. To create a VNI list, run the **filter-list vni** command. The VNI list can be applied to an if-match clause to filter EVPN routes.

**Follow-up Procedure**

Run the **vni** command in the VNI list view to add VNIs for the list.


Example
-------

# Create a VNI list named vni-list.
```
<HUAWEI> system-view
[~HUAWEI] filter-list vni vni-list

```