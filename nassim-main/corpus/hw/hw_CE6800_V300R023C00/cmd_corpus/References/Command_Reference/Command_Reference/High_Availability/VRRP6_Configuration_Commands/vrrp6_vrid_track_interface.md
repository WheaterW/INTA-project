vrrp6 vrid track interface
==========================

vrrp6 vrid track interface

Function
--------



The **vrrp6 vrid track interface** command enables a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group to monitor a VRRP6-disabled interface.

The **undo vrrp6 vrid track interface** command disables a VRRP6 backup group from monitoring a VRRP6-disabled interface.



By default, a VRRP6 backup group does not monitor a VRRP6-disabled interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* **track** [ **ipv6** ] **interface** { *interface-name* | *interface-type* *interface-number* } [ **increase** *value-increased* | **reduce** *value-reduced* ]

**undo vrrp6 vrid** *virtual-router-id* **track** **interface** [ *interface-name* | *interface-type* *interface-number* ]

**undo vrrp6 vrid** *virtual-router-id* **track** **ipv6** **interface** [ { *interface-name* | *interface-type* *interface-number* } [ **increase** *value-increased* | **reduce** *value-reduced* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP6 group. | The value is an integer ranging from 1 to 255. |
| **ipv6** | Tracks the IPv6 status of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of a monitored VRRP6-disabled interface. | - |
| *interface-name* | Specifies the name of the monitored interface. | - |
| **increase** *value-increased* | Specifies a value by which the priority of a router in a VRRP6 backup group increases when a monitored VRRP6-disabled interface goes Down. | The value is an integer ranging from 1 to 255. As 255 is the priority of an IP address owner, the largest priority can be set to 254. |
| **reduce** *value-reduced* | Specifies a value by which the priority of a router in a VRRP6 backup group decreases when a monitored VRRP6-disabled interface goes Down. | The value is an integer ranging from 1 to 255. The smallest value can be set to 1. By default, the priority decreases by 10 when a monitored VRRP6-disabled interface goes Down. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A VRRP6 backup group cannot detect changes in the status of a VRRP6-disabled interface. If a VRRP-disabled interface connected to a network fails, the VRRP6 backup group is unable to detect the fault and still forwards user packets through the failed interface, which results in service interruptions.To enable a VRRP6 backup group to monitor a VRRP6-disabled interface, run thevrrp6 vrid track interface command. If a router or VRRP6-disabled interface connected to a network fails, a VRRP6 backup group detects the fault and performs a master/backup VRRP switchover.

* If a monitored VRRP6-disabled interface goes Down, the router on which the interface resides increases or decreases its priority by a specified value and performs a master/backup VRRP switchover.
* If a monitored VRRP6-disabled interface goes Up, the router on which the interface resides restores its priority.

**Prerequisites**

A VRRP6 backup group has been created using the **vrrp6 vrid virtual-ip** command.

**Configuration Impact**

When you enable a VRRP6 backup group to monitor a VRRP6-disabled interface, the specified increase value-increased or reduce value-reduced parameter affects the status of the VRRP6 backup group. The specified parameter value only needs to ensure that a master/backup VRRP6 switchover can be performed. For example, if the master router's priority is 120 and a backup router's priority is 110, you need to set the reduce value-reduced parameter to 20 only on the master router.

**Precautions**

After you enable a VRRP6 group to track a VRRP6-disabled interface, an IP address owner's priority does not change because it is fixed at 255.When you configure a VRRP6 group to track the IPv4 status of an interface, the network-layer protocol of the tracked interface must contain IPv4. Otherwise, the VRRP6 group tracks the link status of the interface.When a VRRP6 group monitors the IPv4 status of multiple interfaces, the final priority of the device is determined by the IPv4 priority changes of all the monitored interfaces.Multiple VRRP6 groups can track the IPv4 status of an interface. A common VRRP6 group can track the IPv4 status of a maximum of 16 interfaces.When you configure a VRRP6 group to track the IPv6 protocol status of an interface, the network-layer protocol of the tracked interface must contain IPv6. Otherwise, the VRRP6 group tracks the link status of the interface.When a VRRP6 group monitors the IPv6 status of multiple interfaces, the final priority of the device is determined by the IPv6 priority changes of all the monitored interfaces.Multiple VRRP6 groups can track the IPv6 status of an interface. A common VRRP6 group can track the IPv6 status of a maximum of 16 interfaces.


Example
-------

# Enable VRRP6 backup group 1 to monitor 100GE 1/0/2.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 track interface 100GE 1/0/2 reduce 20

```

# Configure VRRP6 group 1 to track IPv6 on 100GE 1/0/2.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 track  ipv6 interface 100GE 1/0/2 reduce 20

```