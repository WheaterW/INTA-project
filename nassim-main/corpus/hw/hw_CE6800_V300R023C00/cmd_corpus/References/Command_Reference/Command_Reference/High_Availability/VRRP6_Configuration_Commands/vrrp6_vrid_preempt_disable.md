vrrp6 vrid preempt disable
==========================

vrrp6 vrid preempt disable

Function
--------



The **vrrp6 vrid preempt disable** command disables a device in a VRRP6 group from preempting the Master state.

The **undo vrrp6 vrid preempt** command restores preemption in a VRRP6 group to the default setting.



By default, a router in a VRRP6 backup group is enabled to immediately preempt the Master state.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *vrid-value* **preempt** **disable**

**undo vrrp6 vrid** *vrid-value* **preempt**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vrid-value* | Specifies the ID of a VRRP6 backup group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A device in a VRRP6 group can work in either of the following modes:

* Non-preemption mode: After a device receives a VRRP6 Advertisement packet from the master device, the device does not preempt the master role even if the priority carried in the packet is lower than the local priority.
* Preemption mode: After a device receives a VRRP6 Advertisement packet from the master device, the device preempts the master role if the priority carried in the packet is lower than the local priority.When a device in a VRRP6 group works in preemption mode, you can run the **vrrp6 vrid preempt timer delay** command to set a preemption delay for the device. If the master device fails, the device preempts the master role after the configured preemption delay elapses. To disable a device in a VRRP6 group from preempting the master role, run this command.

**Prerequisites**

A VRRP6 backup group has been created using the **vrrp6 vrid virtual-ip** command.

**Configuration Impact**

After you run this command to disable a router in a VRRP6 backup group from preempting the Master state, the router works in non-preemption mode. When the master router is working properly, the router does not preempt the Master state even if its priority is higher than the master router's priority.

**Precautions**

Set the preemption delay to 0 on a router to allow it to become a master immediately after its priority changes or set the preemption delay to a non-0 value on the master router so that it can preempt the Master state after a specified delay if a master/backup VRRP switchover is performed. These settings allow a period of time for status synchronization between the user-to-network link and network-to-user link on routers on an unstable network. This prevents the situation in which user devices learn an incorrect master router IP address when two master routers coexist or a master/backup VRRP switchover is performed frequently.


Example
-------

# Disable a router in VRRP6 backup group 1 from preempting the Master state.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 preempt disable

```