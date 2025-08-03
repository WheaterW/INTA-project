erps self-heal disable
======================

erps self-heal disable

Function
--------



The **erps self-heal disable** command disables ERPS self-healing.

The **undo erps self-heal disable** command enables ERPS self-healing.



By default, ERPS self-healing is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**erps self-heal disable**

**undo erps self-heal disable**


Parameters
----------

None

Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an ERPS ring is stable and no fault occurs, if a non-owner node unexpectedly sends an R-APS PDU carrying the signal failure (SF) field, the RPL owner node on the ERPS ring may be unblocked, causing a loop. To eliminate the loop through status detection, enable ERPS self-healing.

**Prerequisites**

Before enabling this function, you must configure an ERPS ring.


Example
-------

# Disable ERPS self-healing.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1
[*HUAWEI-erps-ring1] erps self-heal disable

```