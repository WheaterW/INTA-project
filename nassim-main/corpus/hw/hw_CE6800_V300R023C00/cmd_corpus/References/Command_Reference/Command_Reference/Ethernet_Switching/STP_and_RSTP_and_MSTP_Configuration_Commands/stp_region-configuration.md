stp region-configuration
========================

stp region-configuration

Function
--------



The **stp region-configuration** command displays a Multiple Spanning Tree (MST) region view.

The **undo stp region-configuration** command restores the default MST region configuration.



By default, the MSTP region name is the MAC address of the device, the MSTP revision level is 0, and all VLANs are mapped to the Common and Internal Spanning Tree (CIST).


Format
------

**stp region-configuration**

**undo stp region-configuration**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MSTP divides a switching network into multiple regions. Each region is a Multiple Spanning Tree (MST) region and has independent Multiple Spanning Trees. Each spanning tree is called a Multiple Spanning Tree instance (MSTI).Two devices belong to the same MST region if their following configurations are the same:

* MST region name
* Mappings between VLANs and MSTIs
* Revision level of the MST regionBefore setting the preceding parameters on a device , run the **stp region-configuration** command to enter the MST region view.

**Follow-up Procedure**

* Run the **region-name** command to set the MST region name.
* Run the **instance** command to set mappings between VLANs and MSTIs.
* Run the revision-level name command to set a revision level for the MST region.


Example
-------

# Enter the MST region view.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration

```