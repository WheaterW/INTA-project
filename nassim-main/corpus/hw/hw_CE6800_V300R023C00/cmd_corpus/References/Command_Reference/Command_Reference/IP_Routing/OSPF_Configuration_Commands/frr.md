frr
===

frr

Function
--------



The **frr** command creates an OSPF FRR view and enters the OSPF FRR view.

The **undo frr** command exits from the OSPF FRR view and deletes the OSPF FRR view.



By default, no OSPF FRR view is created.


Format
------

**frr**

**undo frr**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF IP FRR needs to be configured in the OSPF FRR view. To create an OSPF FRR view and enter the OSPF FRR view, run the frr command. To enable OSPF IP FRR, run the **loop-free-alternate** command so that a loop-free backup link can be generated.

**Prerequisites**

OSPF has been enabled using the **ospf** command.

**Precautions**

A link with the cost 65535 cannot participate in FRR path calculation.


Example
-------

# Create an OSPF FRR view and enter the OSPF FRR view.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] frr

```