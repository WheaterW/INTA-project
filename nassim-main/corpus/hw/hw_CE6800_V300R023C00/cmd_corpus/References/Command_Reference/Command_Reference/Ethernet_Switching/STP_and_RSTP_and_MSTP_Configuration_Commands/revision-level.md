revision-level
==============

revision-level

Function
--------



The **revision-level** command configures a revision level for an MST region.

The **undo revision-level** command restores the default level.



By default, the revision level is 0.


Format
------

**revision-level** *level*

**undo revision-level**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *level* | Specifies an MST region revision level. | The value is an integer ranging from 0 to 65535. |



Views
-----

MST region view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MSTP divides a switching network into multiple regions, each of which has independent Multiple Spanning Trees. Each region is called an MST region, and each spanning tree is called an MSTI.Two devices belong to the same MST region only when their following configurations are the same:

* MST region name
* Mappings between MSTIs and VLANs
* MST region revision levelIf two devices have the same region name and VLAN mapping table, run the **revision-level** command twice to configure different revision levels for the two devices. After this configuration, the devices belong to different MST regions.


Example
-------

# Configure the revision level of an MST region to 5.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[~HUAWEI-mst-region] revision-level 5

```