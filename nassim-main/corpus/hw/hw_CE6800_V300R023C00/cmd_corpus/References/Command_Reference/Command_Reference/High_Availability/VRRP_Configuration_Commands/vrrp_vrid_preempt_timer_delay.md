vrrp vrid preempt timer delay
=============================

vrrp vrid preempt timer delay

Function
--------



The **vrrp vrid preempt timer delay** command sets a preemption delay for a device in a VRRP group.

The **undo vrrp vrid preempt timer delay** command restores the default preemption delay.



The default preemption delay is 5 seconds for a preemption caused by an interface Up event or 0 seconds (indicating immediate preemption) for a preemption caused by other reasons.


Format
------

**vrrp vrid** *virtual-router-id* **preempt** **timer** **delay** *delay-time*

**undo vrrp vrid** *virtual-router-id* **preempt** **timer** **delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay** *delay-time* | Specifies the preempt delay. | The value is an integer ranging from 0 to 3600, in seconds. |
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

Set the preemption delay to 0 on the backup device to allow it to become a master device immediately after its priority changes; set the preemption delay to a non-0 value on the master device so that it can preempt the Master state after a specified delay if a master/backup VRRP switchover is performed. After the faulty master device in the VRRP group recovers, receives protocol packets, and has a lot of service configurations, the master device slowly delivers the VRRP forwarding table. An immediate traffic switchback leads to packet loss on the master device. To prevent packet loss, properly set a delay time in this situation.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid virtual-ip** command.

**Configuration Impact**

After the vrrp vrid preempt-mode timer delay command is run, the device in the specified VRRP group on a specified interface preempts the master device after the preemption delay expires.

**Precautions**

* When the IP address owner (the VRRP device uses the virtual IP address of the VRRP group as the real interface address) recovers from a fault, it immediately switches to the master device without waiting for the preemption delay to expire. The preemption delay is a period during which a backup device is waiting to preempt the master role. Therefore, the preemption delay does not take effect on the IP address owner. For the VRRP group that needs to support the preemption delay, the master device cannot be configured as the IP address owner.
* To enable rapid VRRP switchback in mVRRP scenarios, run the vrrp vrid fast-resume command to set the preemption delay to 0. Otherwise, rapid VRRP switchback is automatically disabled.
* If the VRRP group is associated with a BFD session or an interface in increase mode and the new VRRP priority is higher than the VRRP priority of the master, the VRRP group immediately preempts the master role without waiting for the preemption delay to expire.
* When a device or board is restarted and a large number of services are configured, the backup device may fail to receive protocol packets from the master device immediately after the restart. As a result, the backup device becomes the master device due to a timeout and the configured preemption delay does not take effect. Therefore, you are advised to set a proper status recovery delay by using the vrrp recover-delay command.

Example
-------

# Set the preemption delay in VRRP group 1 to 5 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
[*HUAWEI-100GE1/0/1] vrrp vrid 1 preempt timer delay 5

```