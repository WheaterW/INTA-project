vrrp vrid preempt disable
=========================

vrrp vrid preempt disable

Function
--------



The **vrrp vrid preempt disable** command configures the non-preemption mode for a device in a VRRP group.

The **undo vrrp vrid preempt** command restores the preemption mode.



By default, a device in a VRRP group adopts the immediate preemption mode.


Format
------

**vrrp vrid** *virtual-router-id* **preempt** **disable**

**undo vrrp vrid** *virtual-router-id* **preempt**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a backup device with a higher priority to automatically become the master device in a VRRP group, you can configure the preemption mode for the backup device.In non-preemption mode, if the master device in a VRRP group works properly, a backup device cannot preempt the master device though the backup device has a higher priority.

* If the non-preemption mode is configured for a backup device in a VRRP group, the backup device does not preempt the master device even when detecting that the priority in a received VRRP Advertisement packet is lower than the local priority.
* If the preemption mode is configured for a backup device in a VRRP group and the backup device detects that the priority in a received VRRP Advertisement packet is lower than the local priority, the backup device preempts the master device after the delay expires.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid virtual-ip** command.

**Configuration Impact**

After the vrrp vrid preempt-mode disable command is run, the device in the specified VRRP group on a specified interface works in non-preemption mode.

**Precautions**

Exercise caution when running the vrrp vrid preempt-mode disable command to configure the non-preemption mode for a device in a VRRP group.


Example
-------

# Configure VRRP group 1 to work in non-preemption mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.1
[*HUAWEI-100GE1/0/1] vrrp vrid 1 preempt disable

```