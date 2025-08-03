stp (Layer 2 interface view)
============================

stp (Layer 2 interface view)

Function
--------



The **stp enable** command enables STP/Rapid Spanning Tree Protocol (RSTP)/Multiple Spanning Tree Protocol (MSTP) on a device or an interface.

The **undo stp enable** command cancels the stp enable command configuration.

The **stp disable** command disables STP/RSTP/MSTP on a device or an interface.

The **undo stp disable** command cancels the stp disable command configuration.



By default, STP/RSTP/MSTP is enabled on a Layer 2 interface.


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

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* On a complex Layer 2 network, STP/RSTP/MSTP can be configured on devices to prevent or break loops.
* To enable STP/RSTP/MSTP, run the **stp enable** command. The devices running STP/RSTP/MSTP exchange information to discover loops on the network and block some interfaces to trim the ring topology into a loop-free tree topology. This prevents packet replication and circular propagation and device performance deterioration.
* Spanning tree calculation consumes system resources. Therefore, run the **stp disable** command to disable STP/RSTP/MSTP on devices or interfaces that do not need to participate in spanning tree calculation.

**Configuration Impact**



If STP/RSTP/MSTP is enabled on an interface, the interface participates in spanning tree calculation, and its forwarding state is determined based the calculation result.If STP/RSTP/MSTP is disabled on an interface, the interface does not participate in spanning tree calculation and is always in the forwarding state.



**Precautions**

* If the **undo stp enable** or **stp disable** command is run in the system view, the global STP/RSTP/MSTP function is disabled, which may cause a loop.
* STP/RSTP/MSTP must be enabled on all interfaces that participate in spanning tree calculation. Otherwise, a loop may occur.


Example
-------

# Disable STP/RSTP/MSTP on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp disable

```