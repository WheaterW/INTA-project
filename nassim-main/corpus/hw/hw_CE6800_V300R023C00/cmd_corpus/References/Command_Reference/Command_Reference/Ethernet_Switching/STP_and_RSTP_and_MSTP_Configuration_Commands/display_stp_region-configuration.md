display stp region-configuration
================================

display stp region-configuration

Function
--------



The **display stp region-configuration** command displays an MST region's valid configuration, including the region name, revision level, mappings between VLANs and spanning tree instances, and configuration digest.




Format
------

**display stp region-configuration** [ **digest** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **digest** | Displays digest of a valid MST region configuration. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



After an MST region is configured and takes effect on the MSTP network, run the display stp region-configuration command to view the MST region name, revision level, mapping between STP MSTIs and VLANs.



**Precautions**



If you run this command in the MSTP process view without specifying an MSTP process, information about the MSTP process in this view is displayed by default. If you run this command in other views without specifying the ID of an MSTP process, information about MSTP process 0 is displayed by default. If you specify the ID of an MSTP process, information about the MSTP process with the specified ID is displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display digest of a valid MST region configuration.
```
<HUAWEI> display stp region-configuration digest
Operating Configuration:
Format selector    :0
   Region name        :huawei
   Revision level     :0
   Digest             :0xAC36177F50283CD4B83821D8AB26DE62

```

# Display the configuration of an MST region.
```
<HUAWEI> display stp region-configuration
Operating Configuration:
Format selector :0
Region name     :huawei
Revision level  :0
Instance   VLAN
0   21 to 4094
          1   1 to 10
          2   11 to 20

```

**Table 1** Description of the **display stp region-configuration** command output
| Item | Description |
| --- | --- |
| Operating Configuration | Operating Configuration. |
| Format selector | Selection factors defined by MSTP. |
| Region name | Name of the MST region. |
| Revision level | Revision level of the MST region. |
| Digest | Digest of the MST region configuration. |
| Instance VLAN | Mappings between spanning tree MSTIs and VLANs of the MST region. |