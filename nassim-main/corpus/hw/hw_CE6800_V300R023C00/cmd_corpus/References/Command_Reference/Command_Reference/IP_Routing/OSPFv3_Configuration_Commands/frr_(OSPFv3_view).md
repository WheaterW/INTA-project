frr (OSPFv3 view)
=================

frr (OSPFv3 view)

Function
--------



The **frr** command creates an OSPFv3 FRR view and enters the OSPFv3 FRR view.

The **undo frr** command exits from the OSPFv3 FRR view and deletes the OSPFv3 FRR view.



By default, no OSPFv3 FRR view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**frr**

**undo frr**


Parameters
----------

None

Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPFv3 IP FRR needs to be configured in the OSPFv3 FRR view. To create an OSPFv3 FRR view and enter the OSPFv3 FRR view, run the frr command. To enable OSPFv3 IP FRR, run the **loop-free-alternate** command in the OSPFv3 FRR view so that a loop-free backup link can be generated.

**Prerequisites**

OSPFv3 has been enabled using the **ospfv3** command.


Example
-------

# Create an OSPFv3 FRR view and enter the OSPFv3 FRR view.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] frr
[*HUAWEI-ospfv3-1-frr]

```