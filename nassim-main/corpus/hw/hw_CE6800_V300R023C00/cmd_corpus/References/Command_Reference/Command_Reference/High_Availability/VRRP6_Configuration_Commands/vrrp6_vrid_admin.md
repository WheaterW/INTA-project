vrrp6 vrid admin
================

vrrp6 vrid admin

Function
--------



The **vrrp6 vrid admin** command creates a management Virtual Router Redundancy Protocol for IPv6 (mVRRP6) backup group or specifies an existing common VRRP6 backup group as an mVRRP6 backup group.

The **undo vrrp6 vrid admin** command deletes an mVRRP6 backup group or restores an mVRRP6 backup group with a virtual IPv6 address configured to a common VRRP6 backup group.



By default, no mVRRP6 backup group exists on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* **admin** [ **ignore-if-down** ]

**undo vrrp6 vrid** *virtual-router-id* **admin**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ignore-if-down** | Configures an mVRRP6 backup group to ignore an interface Down event.  If you specify this parameter and the interface on which an mVRRP6 backup group resides goes Down, the VRRP6 backup groups bound to the mVRRP6 backup group directly switch to the Master state. | - |
| **vrid** *virtual-router-id* | Specifies the ID of an mVRRP6 group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you configure multiple common VRRP6 backup groups, the master router generates a large number of VRRP packets, which consume bandwidth resources and increase system loads. To resolve this issue, run the admin-vrrp6 vrid command to create an mVRRP6 backup group or specifies an existing common VRRP6 backup group as an mVRRP6 backup group. The mVRRP6 backup group processes VRRP packets and determines the status of the common VRRP6 backup groups bound to it.Configuration parameters are required in the following scenario:

* If user-side devices do not provide broadcast functions, create an mVRRP6 backup group on the directly connected interfaces on two routers with a VRRP6 backup group configured so that VRRP packets sent by the master router are transmitted on the directly connected link. If a router fails, the other router's interface that is directly connected to the router goes Down. As a result, the mVRRP6 backup group on the two routers both switches to the Initialize state and service traffic forwarding fails. To resolve this issue, specify the ignore-if-down parameter for both routers to enable the mVRRP6 backup group to ignore an interface Down event. After a router receives an interface Down event from the other router, this router does not respond to the event and service traffic is forwarded properly.

**Prerequisites**

A VRRP6 backup group has been created using the **vrrp6 vrid virtual-ip** command in the interface view if an mVRRP6 backup group functions as a gateway.An mVRRP6 backup group that functions as a gateway processes both VRRP and service packets, whereas an mVRRP6 backup group that does not function as a gateway processes only VRRP packets.

**Follow-up Procedure**

Run the **vrrp6 vrid track admin-vrrp** command on the interface on which a common VRRP6 backup group resides to bind the common VRRP6 backup group to the mVRRP6 backup group.

**Precautions**

If the status of an mVRRP6 backup group configured with the ignore-if-down function is Initialize and remains unchanged, the ignore-if-down function cannot work properly after the mVRRP6 backup group receives a message indicating that an interface goes Down.


Example
-------

# Create VRRP6 backup group 2 on 100GE 1/0/1, configure it as an mVRRP6 backup group, and configure the mVRRP6 backup group to ignore an interface Down event.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:1::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 2 virtual-ip FE80::200:1FF:FE04:5D01 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 2 admin ignore-if-down

```

# Create VRRP6 backup group 1 on 100GE 1/0/1 and configure it as an mVRRP6 backup group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::1 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 admin

```