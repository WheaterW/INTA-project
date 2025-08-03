vrrp vrid admin
===============

vrrp vrid admin

Function
--------



The **vrrp vrid admin** command creates a management Virtual Router Redundancy Protocol (mVRRP) group or configure a common VRRP group as an mVRRP group.

The **undo vrrp vrid admin** command deletes an mVRRP group or restores an mVRRP group to a common VRRP group.



By default, no mVRRP group is configured.


Format
------

**vrrp vrid** *virtual-router-id* **admin** [ **ignore-if-down** ]

**undo vrrp vrid** *virtual-router-id* **admin**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ignore-if-down** | Indicates that an mVRRP group ignores an interface Down event.  If an interface on which an mVRRP group is configured goes Down, the status of the mVRRP group becomes Master, not Initialize. | - |
| **vrid** *virtual-router-id* | Specifies the ID of an mVRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A large number of VRRP packets are sent by multiple master devices when multiple common VRRP groups are configured. The VRRP packets consume network bandwidth resources and burden the system. The vrrp vrid admin command can be run to configure an mVRRP group. The mVRRP group sends VRRP packets and determines the status of services VRRP groups that are bound to the mVRRP group. Using mVRRP reduces resource consumption.

* An mVRRP group functioning as a gateway processes both protocol and service packets. An mVRRP group that does not function as a gateway processes only protocol packets.
* Before a VRRP group is bound to an mVRRP group, the VRRP group is a common VRRP group and is able to process both protocol and service packets.
* After the VRRP group is bound to the mVRRP group, the VRRP group becomes a service VRRP group and is able to process only service packets.ignore-if-down must be configured in the vrrp vrid admin command in the following scenario:If a user-side device cannot broadcast packets, mVRRP can be enabled on directly connected interfaces on devices in a VRRP group. The master device sends VRRP packets along the direct link. If a device on one end of the direct link fails, the VRRP-enabled interface on the other device also goes down. The mVRRP status on both devices becomes Initialize, causing service packet interruptions. To prevent the preceding problem, specify the ignore-if-down parameter in the admin-vrrp vridvrrp vrid admin command on both the master and devices. The parameter enables the mVRRP group to ignore the event that a directly connected interface goes Down. This setting allows the VRRP-enabled interface on one end of the direct link to continue forwarding service packets if the VRRP-enabled interface on the other end goes down.

**Prerequisites**

A VRRP group has been created using the **vrrp vrid virtual-ip** command in the interface view if an mVRRP group is used as a gateway.

**Follow-up Procedure**

After the admin-vrrp vrid command is run, run the **vrrp vrid track admin-vrrp** command on the interface on which a service VRRP group is configured to bind the service VRRP group to the mVRRP group.

**Precautions**

After the **undo vrrp vrid admin** command is run to delete an mVRRP group, the association between other service VRRP groups and the mVRRP group is automatically deleted.If the status of the mVRRP group configured with the ignore-if-down function is Initialize and does not change, the ignore-if-down function cannot work properly when the mVRRP group receives a message indicating that the interface goes Down.


Example
-------

# Create VRRP group 2 on 100GE 1/0/1, configure it as an mVRRP group, and enable the mVRRP group to ignore interface down events.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.2.1.1 24
[*HUAWEI-100GE1/0/1] vrrp vrid 2 virtual-ip 10.2.1.111
[*HUAWEI-100GE1/0/1] vrrp vrid 2 admin ignore-if-down

```

# Create VRRP group 1 on 100GE 1/0/1 and configure it as an mVRRP group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
[*HUAWEI-100GE1/0/1] vrrp vrid 1 admin

```