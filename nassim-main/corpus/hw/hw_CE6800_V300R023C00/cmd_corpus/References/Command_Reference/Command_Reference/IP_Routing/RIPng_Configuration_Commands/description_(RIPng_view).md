description (RIPng view)
========================

description (RIPng view)

Function
--------



The **description** command configures a description for a RIPng process.

The **undo description** command deletes the description of a RIPng process.



By default, no description is configured for a RIPng process.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description of a RIPng process. | The description text is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A description of a RIPng process helps you identify the RIPng process and understand the configurations easily.

**Precautions**

If the command is run more than once, only the latest configuration takes effect.


Example
-------

# Configure a description this process configure the poison reverse process for RIPng process 100.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100
[*HUAWEI-ripng-100] description this process configure the poison reverse process

```