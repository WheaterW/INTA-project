version
=======

version

Function
--------



The **version** command configures an ERPS version.

The **undo version** command restores the default ERPS version.



By default, ERPSv1 is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**version** { **v1** | **v2** }

**undo version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **v1** | Specifies ERPSv1. | - |
| **v2** | Specifies ERPSv2. | - |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

ERPSv1 and ERPSv2 are currently available. v1 was released by ITU-T in June 2008, and v2 was released by ITU-T in August 2010. ERPSv2, fully compatible with ERPSv1, provides the following enhanced functions:

* Supports multi-ring topologies, such as intersecting rings.
* Supports ring auto protection switching protocol data unit (R-APS PDU) transmission modes on sub-rings.
* Supports two manual port blocking modes: forced switch (FS) and manual switch (MS).
* Supports both revertive and non-revertive switching.To configure an ERPS version, run the **version** command.

Example
-------

# Specify ERPSv1 for ERPS ring 5.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v1

```

# Specify ERPSv2 for ERPS ring 5.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v2

```