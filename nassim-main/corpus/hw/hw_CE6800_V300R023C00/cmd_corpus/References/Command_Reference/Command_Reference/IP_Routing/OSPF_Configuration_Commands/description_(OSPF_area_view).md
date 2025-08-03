description (OSPF area view)
============================

description (OSPF area view)

Function
--------



The **description** command configures a description for an OSPF area.

The **undo description** command deletes the description.



By default, no description is configured for an OSPF area.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description of an OSPF area. | The value is a string of 1 to 80 characters. |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The description of an OSPF area helps identify special areas, facilitating network maintenance.


Example
-------

# Configure a description for OSPF area 1.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 1
[*HUAWEI-ospf-100-area-0.0.0.1] description this is a stub area

```