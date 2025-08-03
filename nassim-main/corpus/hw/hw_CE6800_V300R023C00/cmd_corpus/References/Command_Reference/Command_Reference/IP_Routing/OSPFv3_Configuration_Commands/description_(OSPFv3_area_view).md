description (OSPFv3 area view)
==============================

description (OSPFv3 area view)

Function
--------



The **description** command configures a description for an OSPFv3 area.

The **undo description** command deletes the configured description.



By default, no description is configured for an OSPFv3 area.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies a description for an OSPFv3 area. | The description text is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The description of an OSPFv3 area helps identify special areas, facilitating network maintenance.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.


Example
-------

# Configure a description for OSPFv3 area 0.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 0
[*HUAWEI-ospfv3-1-area-0.0.0.0] description main process

```