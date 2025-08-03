stp (MSTP process view)
=======================

stp (MSTP process view)

Function
--------



The **stp enable** command enables STP/Rapid Spanning Tree Protocol (RSTP)/Multiple Spanning Tree Protocol (MSTP) on an MST region.

The **stp disable** command disables STP/RSTP/MSTP on an MST region.

The **undo stp enable** command cancels the stp enable command configuration.

The **undo stp disable** command cancels the stp disable command configuration.



By default, STP/RSTP/MSTP is disabled on an MST region.


Format
------

**stp** { **enable** | **disable** }

**undo stp** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables STP/RSTP/MSTP. | - |
| **disable** | Disables STP/RSTP/MSTP. | - |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a complex Layer 2 network, STP/RSTP/MSTP can be configured on devices to prevent or break loops.To enable STP/RSTP/MSTP, run the **stp enable** command. The devices running STP/RSTP/MSTP exchange information to discover loops on the network and block some interfaces to trim the ring topology into a loop-free tree topology. This prevents packet replication and circular propagation and device performance deterioration.Spanning tree calculation consumes system resources. Therefore, run the **stp disable** command to disable STP/RSTP/MSTP on devices or interfaces that do not need to participate in spanning tree calculation.



**Precautions**

* STP/RSTP/MSTP must be enabled on all interfaces that participate in spanning tree calculation. Otherwise, a loop may occur.
* If the **undo stp enable** or **stp disable** command is run in the system view, the global STP/RSTP/MSTP function is disabled, which may cause a loop.
* If the **undo stp enable** or **stp disable** command is run in the MSTP process view, the STP/RSTP/MSTP function in the MSTP process is disabled, which may cause a loop in the MSTP process.


Example
-------

# Enable STP/RSTP/MSTP on MST region.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp enable

```