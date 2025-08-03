vlan vlan-name (system view)
============================

vlan vlan-name (system view)

Function
--------



The **vlan vlan-name** command is used to enter the VLAN view through the name of the vlan.

The **undo vlan vlan-name** command is used to delete VLAN by its name.




Format
------

**vlan vlan-name** *vlan-name*

**undo vlan vlan-name** *vlan-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-name* | The name of VLAN. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Users can intuitively operate and manage VLAN through the name of vlan.




Example
-------

# Enter the corresponding VLAN view by name user1.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] name user1
[*HUAWEI-vlan2] quit
[*HUAWEI] vlan vlan-name user1

```