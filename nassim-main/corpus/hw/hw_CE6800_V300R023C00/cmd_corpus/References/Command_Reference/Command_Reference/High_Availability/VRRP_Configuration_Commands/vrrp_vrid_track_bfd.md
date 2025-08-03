vrrp vrid track bfd
===================

vrrp vrid track bfd

Function
--------



The **vrrp vrid track bfd** command enables a VRRP group to track a BFD session.

The **undo vrrp vrid track bfd** command disables a VRRP group from tracking a BFD session.



By default, a VRRP group does not track a BFD session.


Format
------

**vrrp vrid** *virtual-router-id* **track** **bfd** *bfd-session-id* [ **increase** *value-increased* | **reduce** *value-reduced* ]

**vrrp vrid** *virtual-router-id* **track** **bfd** **session-name** *bfd-configure-name* [ **increase** *value-increased* | **reduce** *value-reduced* ]

**vrrp vrid** *virtual-router-id* **track** **bfd** *bfd-session-id* { **peer** | **link** }

**vrrp vrid** *virtual-router-id* **track** **bfd** **session-name** *bfd-configure-name* { **peer** | **link** }

**undo vrrp vrid** *virtual-router-id* **track** **bfd** [ *bfd-session-id* | **session-name** *bfd-configure-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| *bfd-session-id* | Specifies the local discriminator of a BFD session tracked by a VRRP group. | The value is an integer ranging from 1 to 16384. |
| **increase** | Increases the priority of the VRRP group. | - |
| *value-increased* | Specifies a value by which the priority of the VRRP group specified by virtual-router-id increases when the status of the tracked BFD session changes from up to down. This parameter takes effect regardless of whether the VRRP group is in the master or backup state. | The value is an integer ranging from 1 to 255. As 255 is the priority of an IP address owner, the largest priority can be set to 254. |
| **reduce** | Reduces the priority of the VRRP group. | - |
| *value-reduced* | Specifies the value by which the priority of the VRRP group decreases when the tracked BFD session changes from up to down. This parameter takes effect regardless of whether the VRRP group is in the master or backup state. | The value is an integer ranging from 1 to 255. The smallest priority is 1. By default, the priority reduces by 10 if the tracked BFD session goes Down. |
| **session-name** *bfd-configure-name* | Specifies the name of the BFD session tracked by the VRRP group. | The value is a string of 1 to 15 characters excluding spaces. If spaces are used, the string must start and end with double quotation marks (").   * When you configure the name of a BFD session, the uppercase and lowercase letters in the name must be consistent with the name entered by the user. * BFD session names are case-insensitive. For example, ABC and abc are regarded as the same BFD session. If a BFD session named ABC has been configured and abc is specified, the system directly displays the ABC view. |
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

If a link between devices in a VRRP group fails, the VRRP group performs a master/backup switchover after a period of three times the interval at which VRRP packets are sent. Packet loss may occur during this period. BFD can rapidly monitor links and detect link faults, which helps prevent the preceding problem. The **vrrp vrid track bfd-session** command is used to configure a VRRP group to track BFD sessions. If the tracked BFD session status changes, the BFD module notifies the VRRP module of the change. After receiving the notification, the VRRP module adjusts the priorities of VRRP devices or directly changes VRRP status to rapidly implement a master/backup VRRP switchover.

* The vrrp vrid virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ increase value-increased | reduce value-reduced ] command is used to configure a VRRP group to track a common BFD session. If the BFD session detects a fault and goes Down, it notifies the VRRP module of the status change. After receiving the notification, the VRRP module increases or reduces the VRRP priorities of devices to perform a master/backup VRRP switchover. Backup devices use BFD sessions to monitor the status of the master device.
* The vrrp vrid virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ peer | link ] command is used to configure the VRRP group to track a peer or link BFD session. If the peer or link BFD session detects a fault and goes Down, it notifies the VRRP module of the status change. After receiving the notification, the VRRP module directly performs a master/backup VRRP switchover without changing VRRP priorities of devices. VRRP devices identify a local fault after receiving BFD packets from a peer BFD session and a remote fault after receiving BFD packets from a link BFD session.

**Prerequisites**

* A VRRP group has been configured using the **vrrp vrid virtual-ip** command.
* BFD has been enabled using the **bfd** command.
* A static BFD session has been created using the **bfd bind peer-ip** command, and a local discriminator has been configured using the **discriminator** command on each end of the BFD session. Or a static BFD session with automatically negotiated discriminators has been created using the **bfd bind peer-ip source-ip auto** command.

**Configuration Impact**

When configuring a VRRP group to track a link BFD session, use either of the following parameters as needed:

* session-name bfd-configuration: allows a static BFD session or a static BFD session with automatically negotiated discriminators to be bound to the VRRP group.
* session-id: allows only a static BFD session to be bound to the VRRP group.After the VRRP group is configured to track a link BFD session, the type of the BFD session cannot be changed. To change the BFD session type, delete existing BFD configurations and reconfigure a BFD session of a desired type.

**Precautions**

If a VRRP device is an IP address owner, the association between the VRRP group and BFD does not take effect.The increase value-increased or reduce value-reduced parameter in the **vrrp vrid track bfd-session** command affects the change in device status in a VRRP group. The increased or reduced value must ensure that changes in VRRP priorities can trigger a master/backup switchover. For example, the priorities of the master and backup devices in a VRRP group are 120 and 110 (displayed using the **display vrrp** command), respectively. If the increased 20 parameter is configured on the backup device, the priority of the backup device becomes 130, a value greater than the priority of the master device. As a result, a master/backup switchover is triggered.The VRRP considers that the BFD session detects a Down event in the following situations:

* No BFD session is configured on a peer device.
* The peer BFD session is shut down.
* The peer BFD session is deleted.
* BFD session negotiation fails.
* The BFD session is Down.The VRRP considers that the BFD session detects an Up event in the following situations:
* BFD session negotiation is successful.
* The BFD session changes from Down to Up.

Example
-------

# Configure VRRP group 3 to track a peer BFD session on 100GE 1/0/2.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.1.20.1 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd peer1 bind peer-ip 10.1.20.2 interface 100GE1/0/1 source-ip 10.1.20.1 auto
[*HUAWEI-session-peer1] quit
[*HUAWEI] interface 100GE 1/0/2
[*HUAWEI-100GE1/0/2] vrrp vrid 3 virtual-ip 10.1.20.11
[*HUAWEI-100GE1/0/2] vrrp vrid 3 track bfd session-name peer1 peer

```

# Configure VRRP group 1 to track a BFD session with the local discriminator set to 1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/2
[*HUAWEI-100GE1/0/2] ip address 10.1.10.1 24
[*HUAWEI-100GE1/0/2] quit
[*HUAWEI] bfd test bind peer-ip 10.1.1.1 interface 100GE 1/0/2
[*HUAWEI-session-test] discriminator local 1
[*HUAWEI-session-test] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.11
[*HUAWEI-100GE1/0/1] vrrp vrid 1 track bfd 1 reduce 20

```

# Configure VRRP group 2 to track a static BFD session named atob with automatically negotiated discriminators.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/3
[*HUAWEI-100GE1/0/3] ip address 10.1.10.1 24
[*HUAWEI-100GE1/0/3] quit
[*HUAWEI] bfd atob bind peer-ip 10.1.10.2 interface 100GE1/0/3 source-ip 10.1.10.1 auto
[*HUAWEI-session-atob] quit
[*HUAWEI] interface 100GE 1/0/4
[*HUAWEI-100GE1/0/4] vrrp vrid 2 virtual-ip 10.1.10.11
[*HUAWEI-100GE1/0/4] vrrp vrid 2 track bfd session-name atob reduce 20

```