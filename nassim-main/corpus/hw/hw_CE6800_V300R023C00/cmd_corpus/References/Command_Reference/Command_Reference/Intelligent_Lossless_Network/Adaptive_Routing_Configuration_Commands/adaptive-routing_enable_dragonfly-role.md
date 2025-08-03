adaptive-routing enable dragonfly-role
======================================

adaptive-routing enable dragonfly-role

Function
--------



The **adaptive-routing enable dragonfly-role** command enables the adaptive routing function on an interface and configures the role of the interface on a direct network.

The **undo adaptive-routing enable dragonfly-role** command disables the adaptive routing function on an interface and cancels the role configuration of the interface on a direct network.



By default, the adaptive routing function is disabled on an interface, and no role is configured for the interface on a direct network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**adaptive-routing enable dragonfly-role** { **global** | **local** }

**undo adaptive-routing enable dragonfly-role** { **global** | **local** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Global role. | - |
| **local** | Local role. | - |



Views
-----

100GE interface view,200GE interface view,400GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a role is configured for an interface on a direct network, when congestion occurs on the direct network, the interface performs corresponding operations based on the role to quickly adjust network paths and prevent services from being blocked.

**Precautions**

* Before running this command to configure the role of an interface in a direct topology, you must run the **adaptive-routing enable** command in the system view to enable the global adaptive routing function.
* Before running this command to configure the role of an interface in a direct topology, you must run the **undo portswitch** command to switch the interface to Layer 3 mode.
* If adaptive routing is enabled globally on a device, an interface is added to a direct topology and participates in adaptive routing calculation only if the role of the interface is configured in the direct topology.
* If PFC or antilocking PFC has been enabled on an interface, PFC resources on the interface are occupied. To release PFC resources on the interface, disable PFC or antilocking PFC on the interface and restart the device.
* This command can be delivered only to physical interfaces. It cannot be delivered to split interfaces or logical interfaces such as sub-interfaces, Eth-Trunk interfaces, VLANIF interfaces, and VBDIF interfaces.

For the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

* PFC and dragonfly antilocking PFC cannot be both enabled on an interface.
* Antilocking PFC and dragonfly antilocking PFC cannot be both enabled on an interface.
* Currently, PFC or antilocking PFC can be enabled on a maximum of 127 interfaces. If the accumulated number of interfaces where PFC or antilocking PFC has been enabled has reached 127, disable the delivered configurations to reduce the number of such interfaces and restart the device. Then you can enable PFC or antilocking PFC on more interfaces.

For the CE8855 and CE8851-32CQ4BQ:

* If dragonfly deadlock prevention has been enabled, you must enable PFC for the priority queue corresponding to the deadlock prevention function on the interface before running this command to configure the role of the interface in the direct topology.

Example
-------

# Configure the global role for an interface on a direct network.
```
<HUAWEI> system-view
[~HUAWEI] adaptive-routing enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] adaptive-routing enable dragonfly-role global

```