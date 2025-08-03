vrrp vrid track admin-vrrp
==========================

vrrp vrid track admin-vrrp

Function
--------



The **vrrp vrid track admin-vrrp** command binds a common VRRP group to a management VRRP (mVRRP) backup group. After the binding is configured, the common VRRP group becomes a service VRRP group.

The **undo vrrp vrid track admin-vrrp** command removes the binding between a service VRRP group and an mVRRP group. After the binding is removed, the service VRRP group changes to a common VRRP group.



By default, no VRRP group is bound to an mVRRP group.


Format
------

**vrrp vrid** *virtual-router-id1* **track** **admin-vrrp** **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id2* [ **unflowdown** ]

**undo vrrp vrid** *virtual-router-id1* **track** **admin-vrrp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id1* | Specifies the ID of a common VRRP group. | The value is an integer ranging from 1 to 255.  Each card supports a maximum of eight VRIDs.  The VRID on an interface must be unique, but different interfaces can be bound to VRRP groups with the same VRID. If the number of VRIDs is insufficient, bind different interfaces to VRRP groups with the same VRID.  The total number of virtual MAC addresses on VLANIF, Eth-Trunk, VBDIF, and NVE interfaces of the device cannot exceed the maximum number of VRIDs. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface on which an mVRRP group is configured. | - |
| **vrid** *virtual-router-id2* | Specifies the ID of an mVRRP group. | The value is an integer ranging from 1 to 255.  Each card supports a maximum of eight VRIDs.  The VRID on an interface must be unique, but different interfaces can be bound to VRRP groups with the same VRID. If the number of VRIDs is insufficient, bind different interfaces to VRRP groups with the same VRID.  The total number of virtual MAC addresses on VLANIF, Eth-Trunk, VBDIF, and NVE interfaces of the device cannot exceed the maximum number of VRIDs. |
| **unflowdown** | Disables the flowdown function of the interface. A common VRRP group is bound to an mVRRP group in unflowdown mode.  After the unflowdown function is configured for the mVRRP group that is in the Backup or Initialize state, the interface on which the bound service VRRP group is established will retain the Up state and the service VRRP group will enter the Backup or Initialize state.  By default, the flowdown mode is used.  After the flowdown function is configured for the mVRRP group that is in the Backup or Initialize state, the interface on which the bound service VRRP group is established will go Down and the service VRRP group will enter the Initialize state. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When multiple VRRP groups are configured on a single device to forward traffic, each VRRP group maintains its own state machine. This means that a large number of VRRP Advertisement packets are transmitted, consuming a lot of bandwidth and CPU resources. To reduce resource consumption, run the vrrp vrid track admin-vrrp command to bind a common VRRP group to an mVRRP group.VRRP groups can be bound to the mVRRP group in flowdown or unflowdown mode.

* flowdown: This mode is used on a network where the upstream and downstream traffic forwarding paths must be the same. On a network configured with a firewall and a VRRP group, upstream traffic flows through the master device and the downstream traffic flows through either the master or backup device. If downstream traffic flows through the backup device and the firewall detects inconsistency between the upstream and downstream traffic paths, the backup device has to discard downstream traffic. The default flowdown mode is used to allow the downstream traffic to be forwarded through the master device so that the firewall allows the packets to pass through.
* unflowdown: This mode is used on a network where the upstream and downstream traffic forwarding paths do not need to be the same. unflowdown can be configured to allow the mVRRP group to determine the states of its bound VRRP group. This means that upstream traffic travels through the master device and then reaches the upper-layer network and downstream traffic travels through either the master or backup device and reaches the user.

**Prerequisites**

* An mVRRP group has been created using the **admin-vrrp vrid** command.
* A common VRRP group has been created using the **vrrp vrid virtual-ip** command.

**Configuration Impact**

After a common VRRP group is bound to an mVRRP group, the common VRRP group becomes a service VRRP group. The mVRRP group sends VRRP Advertisement packets to determine the master/backup status of the service VRRP group. The service VRRP group only forwards service traffic, which significantly reduces device loads and bandwidth consumption.

**Precautions**

* The vrrp vrid track admin-vrrp command can be run only on the interface on which a common VRRP group resides.
* A common VRRP4 backup group and a common VRRP6 group can be configured on the same interface. However, when both a common VRRP4 backup group and a common VRRP6 backup group are configured on an interface, there are several restrictions:
* The common VRRP4 backup group must be bound to the mVRRP4 backup group, whereas the common VRRP6 backup group must be bound to the mVRRP6 backup group.
* A maximum of one common VRRP4 group and one common VRRP6 group can be configured on an interface. The common VRRP groups must be configured on the interface using the unflowdown parameter.

Example
-------

# Bind the service VRRP group 1 on 100GE 1/0/1 to the mVRRP group 2 on 100GE 1/0/7.1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 track admin-vrrp interface 100GE 1/0/7.1 vrid 2

```