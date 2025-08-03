vrrp vrid priority
==================

vrrp vrid priority

Function
--------



The **vrrp vrid priority** command configures a priority for a device in a VRRP group.

The **undo vrrp vrid priority** command restores the default priority.



By default, the priority of a device in a VRRP group is 100.


Format
------

**vrrp vrid** *virtual-router-id* **priority** *priority-value*

**undo vrrp vrid** *virtual-router-id* **priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| *priority-value* | Specifies the priority of a device in a VRRP group. | The value is an integer ranging from 1 to 254. A larger value indicates a higher priority. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A priority determines the status of a device in a VRRP group. To configure a priority for a device in a VRRP group, run the vrrp vrid priority command. The device with the highest priority is the master device.A VRRP group works in either master/backup or load balancing mode.

* A single VRRP group can work only in master/backup mode. Devices in the VRRP group have different priorities. The device with the highest VRRP priority is in the Master state and the others are in the Backup state.
* Two or more VRRP groups can work in load balancing mode. Each device has different priorities in different VRRP groups. Repeatedly configuring VRRP priorities allows different devices to function as master devices in different VRRP groups.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid virtual-ip** command.

**Precautions**

Priority 255 is reserved for an IP address owner. The priority of an IP address owner is unconfigurable and fixed at 255.If devices have the same VRRP priority, the device that enters the Master state earlier than the others is the master device. Other devices are backup devices and stop preempting the Master state.


Example
-------

# Set the priority of a device in VRRP group 1 to 150.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
[*HUAWEI-100GE1/0/1] vrrp vrid 1 priority 150

```