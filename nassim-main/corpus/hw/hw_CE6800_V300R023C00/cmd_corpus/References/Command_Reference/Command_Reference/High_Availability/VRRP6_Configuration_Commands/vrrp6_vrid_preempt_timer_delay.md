vrrp6 vrid preempt timer delay
==============================

vrrp6 vrid preempt timer delay

Function
--------



The **vrrp6 vrid preempt timer delay** command sets a preemption delay for a router in a Virtual Router Redundancy Protocol for IPv6 (VRRP6) group.

The **undo vrrp6 vrid preempt timer delay** command restores the default preemption delay.



The default preemption delay is 5 seconds for a preemption caused by an interface up event or 0 seconds (indicating immediate preemption) for a preemption caused by any other reason.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* **preempt** **timer** **delay** *delay-time*

**undo vrrp6 vrid** *virtual-router-id* **preempt** **timer** **delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay** *delay-time* | Specifies a preemption delay for the device in a VRRP6 group. | The value is an integer that ranges from 0 to 3600. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP6 group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an unstable network, if backup routers in a VRRP6 backup group fail to receive VRRP packets from the master router within a specified timeout period, a backup router with the highest priority preempts the Master state. If network congestion occurs, backup routers also may not receive VRRP packets from the master router. To prevent frequent master/backup VRRP6 switchovers, run the vrrp6 vrid preempt-mode timer delay command to set a preemption delay for a backup router in a VRRP6 backup group. The backup router preempts the Master state only after the configured preemption delay elapses.

**Prerequisites**

A VRRP6 backup group has been created using the **vrrp6 vrid virtual-ip** command.

**Precautions**

You are advised to set the preemption delay to 0 on a backup device to allow it to preempt the master role immediately after the master device fails or set the preemption delay to a non-0 value on the master device so that it can preempt the master role after a specified delay if a master/backup VRRP6 switchover is performed. If the master device in a VRRP6 group recovers from a fault and receives protocol packets, it delivers the VRRP forwarding table slowly if a large number of service configurations are configured. In this case, an immediate traffic switchback leads to packet loss on the master device. To prevent packet loss, set a proper preemption delay for the master device with a large number of services configured.When an IP address owner recovers from a fault, it immediately preempts the Master state. The preemption delay is a period during which a backup device is waiting to preempt the master role. Therefore, the preemption delay does not take effect on the IP address owner. If a preemption delay needs to be configured for a VRRP6 group, do not configure the master router in the group as an IP address owner.If the VRRP group is associated with a BFD session or an interface in increase mode and the new VRRP priority is higher than the VRRP priority of the master, the VRRP group immediately preempts the Master state without waiting for the preemption delay.When a device or board is restarted and a large number of services are configured, the backup device may fail to receive protocol packets from the master device immediately after the restart. As a result, the backup device becomes the master device due to a timeout and the configured preemption delay does not take effect. Therefore, it is recommended that you set a proper VRRP6 recover-delay when setting the preemption delay.


Example
-------

# Set the preemption delay to 5 seconds for a router in VRRP6 backup group 1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 preempt timer delay 5

```