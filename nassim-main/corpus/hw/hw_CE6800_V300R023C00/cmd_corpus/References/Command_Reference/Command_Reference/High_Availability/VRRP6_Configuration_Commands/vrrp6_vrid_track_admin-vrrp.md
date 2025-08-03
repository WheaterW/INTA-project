vrrp6 vrid track admin-vrrp
===========================

vrrp6 vrid track admin-vrrp

Function
--------



The **vrrp6 vrid track admin-vrrp** command binds a common Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group to a management Virtual Router Redundancy Protocol for IPv6 (mVRRP6) backup group. After the binding is complete, the common VRRP6 backup group becomes a service VRRP6 backup group.

The **undo vrrp6 vrid track admin-vrrp** vrrp command unbinds a service VRRP6 backup group from an mVRRP6 backup group. After the unbinding is complete, the service VRRP6 backup group restores to a common VRRP6 backup group.



By default, no common VRRP6 backup group is bound to an mVRRP6 backup group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id1* **track** **admin-vrrp** **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id2* [ **unflowdown** ]

**undo vrrp6 vrid** *virtual-router-id1* **track** **admin-vrrp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id1* | Specifies the ID of a common VRRP6 backup group. | The value is an integer ranging from 1 to 255. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of the interface on which an mVRRP6 backup group resides. | - |
| *virtual-router-id2* | Specifies the ID of an mVRRP6 group. | The value is an integer ranging from 1 to 255. |
| **unflowdown** | Binds a common VRRP6 backup group to an mVRRP6 backup group in unflowdown mode. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When multiple VRRP6 backup groups are configured on a router to forward traffic, each VRRP6 backup group maintains its own state machine, which causes a large number of VRRP6 Advertisement packets to be transmitted. To reduce the impact of these packets on network bandwidths and CPU performance, run the vrrp6 vrid track admin-vrrp6 command to bind a common VRRP6 backup group to an mVRRP6 backup group.A common VRRP6 backup group can be bound to an mVRRP6 backup group in either of the following modes:

* Flowdown mode: When an mVRRP6 backup group is in the Backup or Initialize state, the interface on which a service VRRP6 backup group bound to the mVRRP6 backup group goes Down and the service VRRP6 backup group switches to the Initialize state. The flowdown mode applies to networks on which both user-to-network and network-to-user traffic is transmitted over the same path. When a firewall is deployed in VRRP6 networking scenarios, it checks the paths for transmitting user-to-network and network-to-user traffic. Network-to-user traffic cannot pass through the firewall if it travels over a path different from the one used by user-to-network traffic. As a result, a backup router discards network-to-user traffic. To ensure that traffic is forwarded properly, specify the flowdown mode to enable network-to-user traffic to be forwarded over the same path as user-to-network traffic.
* Unflowdown mode: When an mVRRP6 backup group is in the Backup or Initialize state, the interface on which a service VRRP6 backup group bound to the mVRRP6 backup group does not go Down and the service VRRP6 backup group remains in the same state as the mVRRP6 backup group. The unflowdown mode applies to networks on which user-to-network and network-to-user traffic can be transmitted over different paths. User-to-network traffic is forwarded only through the master router, whereas network-to-user traffic can be forwarded through the master or backup router.

**Prerequisites**

Before binding a common VRRP6 backup group to an mVRRP6 backup group, perform the following operations to create them on different interfaces:

* Run the **admin-vrrp6 vrid** command to create an mVRRP6 backup group.
* Run the **vrrp6 vrid virtual-ip** command to create a common VRRP6 backup group.

**Configuration Impact**

After a common VRRP6 backup group is bound to an mVRRP6 backup group, the common VRRP6 backup group becomes a service VRRP6 backup group. The service VRRP6 backup group does not send VRRP6 Advertisement packets to negotiate the master/backup status, and its status is determined by the mVRRP6 backup group. The service VRRP6 backup group only forwards service traffic, which significantly reduces router loads and bandwidth consumption.

**Precautions**

* This command can be run only on the interface on which a common VRRP6 backup group resides.
* Only one common VRRP6 backup group can be bound to an mVRRP6 backup group on an interface or a sub-interface.
* Do not run the **control-flap** command on a network-side interface monitored by a VRRP6 backup group. If this command is run on a network-side interface monitored by a VRRP6 backup group, the interface waits a period when changing from Down to Up. During this period, network-side routing information has not recovered but the VRRP6 backup group directly switches from the Backup state to the Master state. As a result, the master router discards traffic from the user side.

Example
-------

# Bind common VRRP6 backup group 1 on 100GE 1/0/1 to mVRRP6 backup group 2 on 100GE 1/0/7.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/7
[~HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] ipv6 enable
[*HUAWEI-100GE1/0/7] ipv6 address 2001:db8:1:1::200 64
[*HUAWEI-100GE1/0/7] vrrp6 vrid 1 virtual-ip FE80::1 link-local
[*HUAWEI-100GE1/0/7] vrrp6 vrid 1 virtual-ip 2001:db8:1:1::201
[*HUAWEI-100GE1/0/7] vrrp6 vrid 1 admin
[*HUAWEI-100GE1/0/7] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:1::1/64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8:1::2/64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 track admin-vrrp interface 100GE 1/0/7 vrid 1

```