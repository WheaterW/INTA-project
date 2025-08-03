vrrp vrid track interface
=========================

vrrp vrid track interface

Function
--------



The **vrrp vrid track interface** command enables a VRRP group to track an interface.

The **undo vrrp vrid track interface** command disables a VRRP group from tracking an interface.



By default, a VRRP group does not track an interface.


Format
------

**vrrp vrid** *virtual-router-id* **track** **interface** { *interface-name* | *interface-type* *interface-number* } [ **increase** *value-increased* | **reduce** *value-reduced* ]

**undo vrrp vrid** *virtual-router-id* **track** **interface** [ *interface-name* | *interface-type* *interface-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer in the range 1 to 255. The minimum priority value is 1. By default, the priority decreases by 10 when a monitored VRRP6-disabled interface goes Down. |
| **interface** *interface-type* *interface-number* | Specifies the interface whose status is tracked by a VRRP group.  A VRRP group can track Layer 2 and Layer 3 interfaces.   * If the tracked interface is a Layer 2 interface, the VRRP group tracks the physical status of the Layer 2 interface and changes its own priority based on the tracked physical status. * If the tracked interface is a Layer 3 interface, the VRRP group tracks the protocol status of the Layer 3 interface and changes its own priority based on the tracked protocol status. | - |
| *interface-name* | Specifies the name of the monitored interface. | - |
| **increase** | Increases the priority of the VRRP group. | - |
| *value-increased* | Specifies the value by which the VRRP priority increases if the tracked interface becomes down. This parameter takes effect on both the master and backup devices in a VRRP group. | The value is an integer ranging from 1 to 255. As 255 is the priority of an IP address owner, the largest priority can be set to 254. |
| **reduce** | Reduces the priority of the VRRP group. | - |
| *value-reduced* | Specifies the value by which the VRRP priority reduces if the tracked interface becomes down. This parameter takes effect on both the master and backup devices in a VRRP group. | The value is an integer in the range 1 to 255. The minimum priority value is 1. By default, the priority decreases by 10 when a monitored VRRP6-disabled interface goes Down. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The master device cannot detect status changes of interfaces that are not in a VRRP group. If a VRRP-disabled interface connected to a network fails, the master device is unable to detect the fault and still forwards user packets through the failed interface, resulting in service interruptions.The vrrp vrid track interface command can be used to configure a VRRP group to track a VRRP-disabled interface. If the device or the network-side interface fails, a VRRP group can be notified of the fault and perform a master/backup VRRP switchover. If the tracked interface goes Down, devices in the VRRP group increase or decrease VRRP priorities by a specified value and perform a master/backup VRRP switchover. The new master device will take over traffic.If the tracked interface becomes Up, the original priorities of devices in a VRRP group will be restored.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid virtual-ip** command.

**Configuration Impact**

The parameter increase value-increased or reduce value-reduced in the vrrp vrid track interface command affects the change of device status in a VRRP group. The increased or reduced value must ensure that changes in VRRP priorities can trigger a master/backup switchover. Assume that the priorities of the master and backup devices in a VRRP group are 120 and 110, respectively. If the parameter reduced 20 is configured on the master device, the priority of the master device becomes 100, a value less than the priority of the backup device. As a result, a master/backup switchover is triggered.

**Precautions**

If a VRRP device is an IP address owner, the association between the VRRP group and interface does not take effect.Multiple VRRP groups can monitor the same interface, and a common VRRP group can monitor a maximum of 16 interfaces simultaneously.When a VRRP group monitors multiple interfaces, the final priority of the device in the VRRP group is determined by the priority change of all monitored interfaces.If the monitored interface has an IPv4 address and this IPv4 protocol status changes, the VRRP group re-elects a master device. If the monitored interface has an IPv6 address and this IPv6 protocol status changes, the change does not affect the status of the VRRP group.


Example
-------

# Configure VRRP group 1 to track 100GE 1/0/2.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.1
[*HUAWEI-100GE1/0/1] vrrp vrid 1 track interface 100GE 1/0/2 reduce 20

```