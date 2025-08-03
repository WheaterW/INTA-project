vrrp6 vrid track bfd
====================

vrrp6 vrid track bfd

Function
--------



The **vrrp6 vrid track bfd** command enables a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group to monitor a BFD session.

The **undo vrrp6 vrid track bfd** command disables a VRRP6 backup group from monitoring a BFD session.



By default, a VRRP6 backup group does not monitor a BFD session.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* **track** **bfd** *bfd-session-id* [ **increase** *value-increased* | **reduce** *value-reduced* ]

**vrrp6 vrid** *virtual-router-id* **track** **bfd** **session-name** *bfd-configure-name* [ **increase** *value-increased* | **reduce** *value-reduced* ]

**vrrp6 vrid** *virtual-router-id* **track** **bfd** *bfd-session-id* { **peer** | **link** }

**vrrp6 vrid** *virtual-router-id* **track** **bfd** **session-name** *bfd-configure-name* { **peer** | **link** }

**undo vrrp6 vrid** *virtual-router-id* **track** **bfd** [ *bfd-session-id* | **session-name** *bfd-configure-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP6 group. | The value is an integer ranging from 1 to 255. |
| *bfd-session-id* | Specifies the local discriminator of a monitored BFD session. | The value is an integer ranging from 1 to 16384. |
| **increase** *value-increased* | Specifies a value by which the priority of a VRRP6 group increases when the tracked BFD session changes from up to down. | The value is an integer ranging from 1 to 255. As 255 is the priority of an IP address owner, the largest priority can be set to 254. |
| **reduce** *value-reduced* | Specifies a value by which the priority of a VRRP6 group decreases when the tracked BFD session changes from up to down. | The value is an integer ranging from 1 to 255. The smallest value can be set to 1. By default, the priority decreases by 10 when a monitored BFD session goes Down. |
| **session-name** *bfd-configure-name* | Specifies the name of a monitored BFD session. | The value is a string of 1 to 64 characters, spaces not supported. If spaces are used, the string must start and end with double quotation marks (").   * When configuring a BFD session name, ensure that the uppercase and lowercase letters in the name are the same as those entered by the user. * The system does not distinguish between uppercase and lowercase letters when checking the name of a BFD session. For example, ABC and abc are considered as a BFD session name. If ABC has been configured, the BFD session view of ABC is directly displayed when abc is configured. |
| **peer** | Indicates that a monitored BFD session is a peer BFD session. | - |
| **link** | Indicates that a monitored BFD session is a link BFD session. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the link between routers in a VRRP6 backup group fails, the VRRP6 backup group performs a master/backup VRRP switchover only after a period of three times the interval at which VRRP6 Advertisement packets are sent. During this period, service data may be lost. BFD can rapidly detect link faults. You can run the vrrp6 vrid track bfd-session command to enable a VRRP6 backup group to monitor a BFD session. When the status of the monitored BFD session changes, the BFD module notifies the VRRP6 module of the change. The VRRP6 module changes the priority or status based on configurations to implement a rapid master/backup VRRP switchover.

* To enable a VRRP6 backup group to monitor a common BFD session, run the **vrrp6 vrid track bfd** command. When the BFD module notifies the VRRP6 module of a BFD session status change, the VRRP6 module increases or decreases the priority to implement a master/backup VRRP switchover. Usually, backup routers use BFD sessions to monitor the master router.
* To enable a VRRP6 backup group to monitor a peer or link BFD session, run the **vrrp6 vrid track bfd** command. If peer or link BFD detects a fault and the peer or link BFD session goes Down, the BFD module notifies the VRRP6 module of the status change. After receiving the notification, the VRRP6 module directly performs a master/backup VRRP switchover without changing the priority. A VRRP6 router can determine a local or remote link fault based on the status of the peer or link BFD session.

**Prerequisites**

* A VRRP6 backup group has been created using the **vrrp6 vrid virtual-ip** command.
* BFD has been enabled using the **bfd** command.
* A static BFD session has been created using the **bfd bind peer-ip** command, and a local discriminator has been configured for the static BFD session using the **discriminator** command. Or a static BFD session with automatically negotiated discriminators has been created using the **bfd bind peer-ip source-ip auto** command.

**Configuration Impact**

When you run the vrrp6 vrid virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ increased value-increased | reduce value-reduced ] command to enable a VRRP6 backup group to monitor a BFD session, the specified increased value-increased or reduced value-reduced parameter value affects the status of the VRRP6 backup group. The specified parameter value only needs to ensure that a master/backup VRRP switchover can be performed. For example, if the master router's priority is 120 (which can be viewed using the **display vrrp6 brief** command) and a backup router's priority is 110, you need to set the increased value-increased parameter to 20 only on the backup router.After you enable a VRRP6 backup group to monitor a link BFD session, you cannot change the BFD session type. To change the BFD session type, you must first disable the VRRP6 backup group from monitoring the link BFD session.

**Precautions**

After you enable a VRRP6 backup group to monitor a BFD session, an IP address owner's priority does not change because it is fixed at 255.The VRRP6 considers that the BFD session detects a Down event in the following situations:

* No BFD session is configured on a peer device.
* The peer BFD session is shut down.
* The peer BFD session is deleted.
* BFD session negotiation fails.
* The BFD session is Down.The VRRP6 considers that the BFD session detects an Up event in the following situations:
* BFD session negotiation is successful.
* The BFD session changes from Down to Up.

Example
-------

# Enable VRRP6 backup group 1 to monitor a BFD session with the local discriminator set to 1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd 1 bind peer-ipv6 2001:db8::1 source-ipv6 2001:db8::2 auto
[*HUAWEI-bfd-session-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::2 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 track bfd 1 reduce 20

```

# Enable VRRP6 backup group 3 to monitor a peer BFD session on 100GE 1/0/3.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd peer1 bind peer-ipv6 2001:db8::1 source-ipv6 2001:db8::2 auto
[*HUAWEI-bfd-session-peer1] quit
[*HUAWEI] interface 100GE 1/0/3
[*HUAWEI-100GE1/0/3] undo portswitch
[*HUAWEI-100GE1/0/3] ipv6 enable
[*HUAWEI-100GE1/0/3] ipv6 address 2001:db8::2 64
[*HUAWEI-100GE1/0/3] vrrp6 vrid 3 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/3] vrrp6 vrid 3 track bfd session-name peer1 peer

```

# Enable VRRP6 backup group 2 to monitor a static BFD session named atob with automatically negotiated discriminators.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd atob bind peer-ipv6 2001:db8::1 source-ipv6 2001:db8::2 auto
[*HUAWEI-bfd-session-atob] quit
[*HUAWEI] interface 100GE 1/0/2
[*HUAWEI-100GE1/0/2] undo portswitch
[*HUAWEI-100GE1/0/2] ipv6 enable
[*HUAWEI-100GE1/0/2] ipv6 address 2001:db8::2 64
[*HUAWEI-100GE1/0/2] vrrp6 vrid 2 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/2] vrrp6 vrid 2 track bfd session-name atob reduce 20

```