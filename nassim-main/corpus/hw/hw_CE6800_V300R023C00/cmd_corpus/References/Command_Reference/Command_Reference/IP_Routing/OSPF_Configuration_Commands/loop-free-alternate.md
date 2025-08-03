loop-free-alternate
===================

loop-free-alternate

Function
--------



The **loop-free-alternate** command enables OSPF/OSPFv3 IP FRR and generates a loop-free backup route.

The **undo loop-free-alternate** command disables OSPF/OSPFv3 IP FRR.



By default, FRR is disabled.


Format
------

**loop-free-alternate**

**undo loop-free-alternate**


Parameters
----------

None

Views
-----

OSPF FRR view,OSPFv3 FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Loop-free alternate (LFA) is a method of implementing IP FRR. With LFA, a device can generate a loop-free backup link to implement basic IP FRR functions. OSPF IP FRR takes effect only after the **loop-free-alternate** command is run.

**Prerequisites**



An OSPF FRR view has been created and the system has entered the OSPF FRR view using the **frr** command.An OSPFv3 FRR view has been created and the system has entered the OSPFv3 FRR view using the **frr** command.



**Precautions**

* If a link that carries important services cannot function as the backup link of other links, run the **ospf frr block** command on the interface connected to the link before configuring OSPF IP FRR. In this way, OSPF IP FRR does not calculate the link connected to the interface as a backup link.
* If a link that carries important services cannot function as a backup link for other links, run the **ospfv3 frr block** command on the interface connected to the link before configuring OSPFv3 IP FRR. In this way, OSPFv3 IP FRR does not calculate the link connected to the interface as a backup link.
* If OSPF IP FRR is configured only for specified routes, run the **frr-policy route route-policy route-policy-name** command to configure a filtering policy for OSPF IP FRR. Only the backup OSPF routes that meet the filtering conditions can be added to the forwarding table. When this route fails, OSPF can quickly switch traffic to the backup route.
* This command takes effect regardless of whether the same route is advertised by multiple nodes.

Example
-------

# Enable OSPFv3 IP FRR through LFA.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3
[*HUAWEI-ospfv3-1] frr
[*HUAWEI-ospfv3-1-frr] loop-free-alternate

```

# Enable OSPF IP FRR through LFA.
```
<HUAWEI> system-view
[~HUAWEI] ospf
[*HUAWEI-ospf-1] frr
[*HUAWEI-ospf-1-frr] loop-free-alternate

```