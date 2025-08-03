description (RIP view)
======================

description (RIP view)

Function
--------



The **description** command configures a meaningful description for a RIP process.

The **undo description** command deletes the description associated with the RIP process.



By default, no description is associated with the RIP process.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description for a RIP process. | The description text is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A description of a RIP process helps you identify the RIPng process and understand the configurations easily.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.


Example
-------

# Configure a description for RIP process 100.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] description this process configure the poison reverse process

```