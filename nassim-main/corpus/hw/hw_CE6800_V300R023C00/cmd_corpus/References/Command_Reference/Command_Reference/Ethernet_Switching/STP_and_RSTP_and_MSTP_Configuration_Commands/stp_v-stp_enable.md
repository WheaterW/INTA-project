stp v-stp enable
================

stp v-stp enable

Function
--------



The **stp v-stp enable** command enables V-STP on an M-LAG device.

The **undo stp v-stp enable** command disables V-STP on an M-LAG device.



By default, V-STP is disabled.


Format
------

**stp v-stp enable**

**undo stp v-stp enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

V-STP is a Layer 2 topology management feature in the M-LAG solution. V-STP allows two devices that both have STP enabled to be virtualized into one device to perform STP calculation.STP can detect the M-LAG master/backup negotiation status. After the negotiation is complete and V-STP is enabled on the master and backup devices, the two devices are virtualized into one device to calculate roles and rapid convergence. To ensure correct STP calculation, the M-LAG backup device synchronizes the bridge MAC address and instance priority from the master device.

**Precautions**

In V-STP mode, to correctly calculate a network-wide Layer 2 topology, the M-LAG interfaces on the master and backup devices must meet the following requirements: Have the same STP configurations. Generate the same calculation result. Send the same STP packets to the connected aggregation or access device.The V-STP mode conflicts with the global and multi-process MSTP modes.In V-STP mode, the following STP configurations are not allowed to be modified: port priority, port path cost, and port point-to-point link type.


Example
-------

# Enable V-STP on an M-LAG device.
```
<HUAWEI> system-view
[~HUAWEI] stp v-stp enable

```