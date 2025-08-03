control-flap
============

control-flap

Function
--------



The **control-flap** command enables flapping control on an interface.

The **undo control-flap** command disables flapping control.



By default, flapping control is disabled on an interface.


Format
------

**control-flap** [ *suppress* *reuse* *ceiling* *decay-ok* *decay-ng* ]

**undo control-flap**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *suppress* | Input device actually suppress threshold value is 1000 times the actual value of the device.  If the penalty value exceeds the interface suppressing threshold, the interface is suppressed. When the interface is suppressed, the outputs of the display interface, display interface brief, and display ip interface brief commands show that the protocol status of the interface remains DOWN(dampening suppressed) and does not change with the physical status. | The value ranges from 1 to 20000. The default value is 2000. This value must be greater than the reuse threshold and less than the ceiling threshold. |
| *reuse* | The value of the interface reuse threshold actually entered by the device is 1000 times the actual value of the device.  If the penalty value falls below the interface reuse threshold, the interface is freed from suppression. When the interface is freed from suppression, the protocol status of the interface is in compliance with the actual status and does not remain Down (dampening suppressed). | The value ranges from 1 to 20000. The default value is 750. This value must be smaller than the suppress threshold of the interface. |
| *ceiling* | The maximum value of the interface suppression penalty value actually entered by the device is 1000 times the actual value of the device. The suppress penalty value stops increasing when it exceeds this value. | The value ranges from 1001 to 20000. The default value is 6000. This value must be greater than the suppress threshold of the interface. |
| *decay-ok* | Specifies the half life of the penalty value for an interface in the Up state.  When an interface is Up, if the period since the end of the previous half life reaches the current half life, the penalty value decreases by half. | The value ranges from 1 to 900, in seconds. The default value is 54s. |
| *decay-ng* | Specifies the half life of the penalty value for an interface in the Down state.  When the interface is Down, if the period since the end of the previous half life reaches the current half life, the penalty value decreases by half. | The value ranges from 1 to 900, in seconds. The default value is 54s. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,Sub-interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Physical signal interference and incorrect link layer configuration may cause a device interface to alternate between Up and Down frequently, causing routing protocols to flap constantly. This greatly affects the device and network, and may cause a specific device to collapse and the network to be unavailable.Flapping control applies to reduce the adverse impact on the network stability caused by interface status changes.By default, the penalty value for interface suppression increases by 400 each time the interface goes Down, this value is 1000 times the actual value of the device.For concepts and principles of interface flapping control, see interface flapping control.decay-ok and decay-ng can be configured separately:

* If an interface remains Up for a long period and the interface must be soon available when it is Up, decreasing decay-ok is recommended.
* If an interface remains Down for a long period and the interface must be long suppressed when it is Down, increasing decay-ng is recommended.

**Precautions**

* This command can be run only on Layer 3 interfaces.
* You can run the **display control-flap** command to view the running status and statistics of control-flap on an interface.
* NULL and loopback interfaces do not support control-flap.
* For directly connected interfaces that have static routes configured, if control-flap has to be configured, you are advised to configure it on both ends. If control-flap is configured only on one end, the interface waits for a period of time before changing from Down to Up when the interface recovers from a fault. This causes the states of the directly connected interfaces on both ends to be different within a period of time. As a result, packet loss occurs.
* After control-flap is configured on a sub-interface, if the IP address of the sub-interface is deleted when the sub-interface is in the suppressed state, the sub-interface remains in the suppressed state.
* Do not run the **control-flap** command on the interface tracked by a VRRP group. If control-flapping is enabled on the network-side interface tracked by a VRRP group, the interface waits for a period of time before changing from Down to Up after the fault is rectified. In this situation, the network-side routing information has not been restored, but the VRRP group directly switches from the backup state to the master state. As a result, user-side traffic is discarded by the master device.


Example
-------

# Enable flapping control on 100GE 1/0/1. Set the values of the suppress, reuse, ceiling, decay-ok, and decay-ng parameters to 2000, 750, 16000, 15, and 15, respectively.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] control-flap 2000 750 16000 15 15

```