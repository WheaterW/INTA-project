region-name
===========

region-name

Function
--------



The **region-name** command configures an MST region name.

The **undo region-name** command restores the default name.



By default, the MST region name is the MAC address of the management network interface on a device.


Format
------

**region-name** *name*

**undo region-name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies an MST region name. | The value is a case-sensitive string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

MST region view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MSTP divides a switching network into multiple regions, each of which has independent Multiple Spanning Trees. Each spanning tree is called an MSTI and each region is called an MST region.Two devices belong to the same MST region only when their following configurations are the same:

* MST region name
* Mappings between MSTIs and VLANs
* MST region revision levelTo configure an MST region name, run the region-name command.


Example
-------

# Set an MST region name to huawei.
```
<HUAWEI> system-view
[~HUAWEI] stp region-configuration
[*HUAWEI-mst-region] region-name huawei

```