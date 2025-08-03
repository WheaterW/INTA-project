vrrp vrid fast-resume
=====================

vrrp vrid fast-resume

Function
--------



The **vrrp vrid fast-resume** command enables rapid VRRP switchback.

The **undo vrrp vrid fast-resume** command disables rapid VRRP switchback.



By default, rapid VRRP switchback is disabled.


Format
------

**vrrp vrid** *virtual-router-id* **fast-resume**

**undo vrrp vrid** *virtual-router-id* **fast-resume**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When downstream links of devices in a VRRP group work in active/standby mode, upstream traffic is transmitted to the external network through the active link and the master device. If a device interface or link fails, the master device lowers the VRRP priority and switches to the Backup state. After the fault is rectified, the priority of the original master device exceeds that of the master device. However, the original master device still needs to receive protocol packets before reclaiming the master state. If the active/standby link switchover speed is faster than that of the master/backup VRRP switchover, the upstream traffic is lost. To solve the problem, run the vrrp vrid fast-resume command to configure the VRRP fast switchback function.With the VRRP fast switchback function enabled, after the original master recovers, the priority of the VRRP group becomes higher than that of the existing master. In this case, the original device does not wait for VRRP protocol packets and directly preempts to be the master.The VRRP fast switchback function takes effect only for mVRRP groups. In addition, the mVRRP groups must monitor the status of interfaces or other features in reduced mode.

**Prerequisites**

The following steps have been performed:

* Run the **vrrp vrid admin** command in the interface view to create an mVRRP group.
* Run the **vrrp vrid preempt timer delay 0** command in the interface view to set the preemption delay to 0 seconds if you have set the preemption delay to a non-zero value.

**Configuration Impact**

If the original master device recovers, it immediately preempts the Master state without waiting for VRRP Advertisement packets from the current master device. However, the current master device switches to the backup state only after it receives a protocol packet with a higher priority. As a result, two master devices coexist during a short period of time.

**Precautions**

The vrrp vrid fast-resume command takes precedence over the vrrp recover-delay command when they take effect. For example, if you enable rapid VRRP switchback for VRRP group 1 and globally set the recovery delay to a non-zero value, the configured recovery delay does not take effect.After you run the vrrp vrid fast-resume command to enable rapid VRRP switchback, this function is disabled if any of the following conditions is true:

* The **vrrp vrid preempt timer delay** command is run to set the preemption delay to a non-zero value.
* The **vrrp vrid preempt disable** command is run to disable VRRP devices from preempting the Master state.
* The **undo vrrp vrid admin** command is run to delete the mVRRP group.

Example
-------

# Create VRRP group 1 on 100GE 1/0/7, configure it as an mVRRP group, and enable rapid VRRP switchback.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/7
[~HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] vrrp vrid 1 admin
[*HUAWEI-100GE1/0/7] vrrp vrid 1 preempt timer delay 0
[*HUAWEI-100GE1/0/7] vrrp vrid 1 fast-resume

```