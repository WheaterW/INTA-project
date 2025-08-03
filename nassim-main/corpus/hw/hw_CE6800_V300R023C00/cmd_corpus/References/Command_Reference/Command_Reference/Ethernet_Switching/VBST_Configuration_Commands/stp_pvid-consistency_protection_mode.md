stp pvid-consistency protection mode
====================================

stp pvid-consistency protection mode

Function
--------



The **stp pvid-consistency protection mode** command configures a protection mode for PVID inconsistency between directly connected ports in VLAN-based Spanning Tree (VBST).

The **undo stp pvid-consistency protection mode** command deletes the protection mode for PVID inconsistency between directly connected ports in VBST.



By default, no protection mode is configured for PVID inconsistency between directly connected ports. That is, the device will be not blocked when the PVIDs of directly connected ports are different.


Format
------

**stp pvid-consistency protection mode block**

**undo stp pvid-consistency protection mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **block** | Block mode. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

VBST checks whether PVIDs of two directly connected ports are the same. If they are different, the processing method varies as follows:

* If the protected mode is block, VBST will block the PVIDs.
* If no protected mode is configured, VBST will not block the PVIDs.

**Precautions**

When the PVID of the interface is inconsistent and the PVID needs to be blocked, the **stp pvid-consistency protection mode block** command must be configured on the two directly connected ports and their link types must be both trunk.


Example
-------

# Set the protection mode for PVID inconsistency between directly connected ports to block.
```
<HUAWEI> system-view
[~HUAWEI] stp pvid-consistency protection mode block

```