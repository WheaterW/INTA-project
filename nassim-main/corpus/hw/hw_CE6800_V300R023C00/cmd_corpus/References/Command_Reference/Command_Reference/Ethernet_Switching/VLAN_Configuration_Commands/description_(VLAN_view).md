description (VLAN view)
=======================

description (VLAN view)

Function
--------



The **description** command is used to configure the description of a VLAN.

The **undo description** command is used to clear the description of a VLAN.



By default, the description of a VLAN contains the VLAN ID. For example, the description of VLAN 2 is VLAN 0002.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Indicates the description of a VLAN. | The value is a string of 1 to 80 characters, spaces supported. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To facilitate VLAN management and identification, run the **description** command to configure a description for a VLAN.After this command is configured, run the **display vlan vlan-id verbose** command to view information about the VLAN.




Example
-------

# Configure a description for VLAN as huawei.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] description huawei

```