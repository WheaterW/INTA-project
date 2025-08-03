check region-configuration
==========================

check region-configuration

Function
--------



The **check region-configuration** command displays the configuration of an MST region.




Format
------

**check region-configuration**


Parameters
----------

None

Views
-----

MST region view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* The MSTP divides a switching network into multiple regions, each of which has multiple spanning trees that are independent of each other. Each region is called an MST region, and each spanning tree is called a Multiple Spanning Tree Instance (MSTI).
* Two devices belong to the same MST region only when their following configurations are the same:
* MST region name
* MST region revision level
* Mappings between MSTIs and VLANs
* To ensure that MST region configuration on each device is correct, run the **check region-configuration** command to check the MST region configuration.

**Precautions**



By default, the VLANs that are not mapped to non-zero instances using the **instance** command are mapped to instance 0.




Example
-------

# Display the configuration of an MST region.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[~HUAWEI-mst-region] check region-configuration
 Admin configuration
   Format selector    :0
   Region name        :38ba757b9a02
   Revision level     :0

   Instance   VLAN        
      0       2 to 3, 101 to 4094
      1       1
      2       4 to 100

```

**Table 1** Description of the **check region-configuration** command output
| Item | Description |
| --- | --- |
| Format selector | Selection factor defined by MSTP. |
| Region name | Name of the MST region. |
| Revision level | Revision level of the MST region. |
| Instance VLAN | Mappings between spanning tree MSTIs and VLANs of the MST region. |