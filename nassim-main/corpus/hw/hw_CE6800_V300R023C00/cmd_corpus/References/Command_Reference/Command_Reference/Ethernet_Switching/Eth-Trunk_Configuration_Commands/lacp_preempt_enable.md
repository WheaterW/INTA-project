lacp preempt enable
===================

lacp preempt enable

Function
--------



The **lacp preempt enable** command enables Link Aggregation Control Protocol (LACP) priority preemption on Eth-Trunk interfaces in static LACP mode.

The **undo lacp preempt enable** command disables LACP priority preemption from Eth-Trunk interfaces in static LACP mode.



By default, Eth-Trunk interfaces in static LACP mode are not enabled with LACP priority preemption.


Format
------

**lacp preempt enable**

**undo lacp preempt enable**


Parameters
----------

None

Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After LACP priority preemption is enabled on Eth-Trunk interfaces in static LACP mode, Eth-Trunk interfaces always use interfaces with high priorities as active interfaces. For example, two devices are connected through three interfaces on each side. After the three interfaces are bundled into an Eth-Trunk interface, the **mode lacp-static** command is used to configure the Eth-Trunk interface to work in static LACP mode. If the maximum number of Up member interfaces is 2, the **lacp priority** command can be used in the interface view to set the LACP priorities of two member interfaces to 9 and 10, and the remaining interface uses the default LACP priority value 32768. Through LACP negotiation, the member interfaces with higher LACP priorities are selected as active interfaces, and the member interfaces with the default LACP priority are backup interfaces.



**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.



**Configuration Impact**



After LACP priority preemption is enabled on an Eth-Trunk interface in static LACP mode, the system re-selects active member interfaces according to LACP system priorities and interface priorities.



**Precautions**

* To ensure that the Eth-Trunk interface works properly, you are advised to enable or disable LACP preemption on both ends of the Eth-Trunk interface.
* When a Huawei device connects to a non-Huawei device, you need to enable the LACP preemption mode on the local device.
* If the LACP preemption mode is disabled and the LACP negotiation parameters of the peer device change, the local device triggers LACP preemption once to select member ports to ensure normal LACP operation. However, the LACP preemption mode is not enabled.


Example
-------

# Enable LACP priority preemption on Eth-Trunk 1 in static LACP mode.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp preempt enable

```