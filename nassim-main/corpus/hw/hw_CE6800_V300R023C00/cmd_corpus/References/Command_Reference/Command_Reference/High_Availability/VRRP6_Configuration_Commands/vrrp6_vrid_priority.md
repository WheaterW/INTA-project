vrrp6 vrid priority
===================

vrrp6 vrid priority

Function
--------



The **vrrp6 vrid priority** command sets a priority for a router in a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group.

The **undo vrrp6 vrid priority** command restores the default priority.



The default priority is 100 for a router in a VRRP6 backup group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* **priority** *priority-value*

**undo vrrp6 vrid** *virtual-router-id* **priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP6 group. | The value is an integer ranging from 1 to 255. |
| *priority-value* | Specifies a priority for a router in a VRRP6 backup group. | The value is an integer ranging from 1 to 254. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The priority of a router determines its position in a VRRP6 backup group. After you run the vrrp6 vrid priority command to set priorities for the routers in a VRRP6 backup group, the router with the highest priority becomes the master router.

**Prerequisites**

A VRRP6 backup group has been created using the **vrrp6 vrid virtual-ip** command.

**Precautions**

If the routers in a VRRP6 backup group have the same priority, the router that first switches to the Master state becomes the master router. Other backup routers no longer preempt the Master state.


Example
-------

# Set the priority to 150 for a router in VRRP6 backup group 1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 priority 150

```