description (OSPF view)
=======================

description (OSPF view)

Function
--------



The **description** command configures a description for an OSPF process.

The **undo description** command deletes the configured description.



By default, no description is configured for an OSPF process.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies a description for an OSPF process. | The description text is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The description of an OSPF process helps identify special processes, facilitating network maintenance.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.


Example
-------

# Configure a description for the OSPF process.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] description this process contains 3 areas

```