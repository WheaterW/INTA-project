vlan-mapping modulo (MST region view)
=====================================

vlan-mapping modulo (MST region view)

Function
--------



The **vlan-mapping modulo** command configures VLAN-to-instance mapping based on a default algorithm.

The **undo vlan-mapping modulo** command restores the default mapping.



By default, all VLANs are mapped to Common and Internal Spanning Tree (CIST), namely, instance 0.


Format
------

**vlan-mapping modulo** *modulo*

**undo vlan-mapping modulo**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *modulo* | Specifies a module value. | The value is an integer ranging from 1 to 63. |



Views
-----

MST region view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Multiple Spanning Tree Protocol (MSTP) divides a switching network into multiple regions, each of which has independent Multiple Spanning Trees. Each spanning tree is called a Multiple Spanning Tree instance (MSTI), and each region is called a Multiple Spanning Tree (MST) region. Two devices belong to the same MST region only when their following configurations are the same:

* MST region name
* Mappings between MSTIs and VLANs
* MST region revision levelTo configure VLAN-to-instance mapping based on a default algorithm, run the vlan-mapping modulo command.

**Precautions**



The instance instance-id vlan command is recommended because VLAN-to-instance mapping based on the algorithm cannot meet actual mapping requirements.In the vlan-mapping modulo command, a VLAN is mapped to an instance based on this formula: Instance ID = MOD (VLAN ID-1)/Modulo value + 1. In the formula, MOD (VLAN ID-1)/Modulo value means the remainder of (VLAN ID-1) divided by the modulo value. For example, if the modulo is 16, VLAN 1 is mapped to MSTI 1, VLAN 2 to MSTI 2, VLAN 16 to MSTI 16, and VLAN 17 to MSTI 1.




Example
-------

# Map all VLANs to spanning tree instances modulo 16.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[~HUAWEI-mst-region] vlan-mapping modulo 16

```