display interface brief main non-unicast
========================================

display interface brief main non-unicast

Function
--------



The **display interface brief main non-unicast** command displays brief information about all interfaces on a device, including the physical status and protocol status of the interfaces, latest inbound and outbound bandwidth usage, and the number of sent and received error packets.




Format
------

**display interface** *interface-type* **brief** **main** **non-unicast**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays brief information about a specified interface. | Displays brief information about broadcast packets on an interface. Currently, only Ethernet interfaces are supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Before you monitor interface status or locate an interface fault, run the **display interface brief main non-unicast** command to view the status of and statistics on the interface. The command output helps you diagnose faults.Compared with the **display interface** command, the **display interface brief main non-unicast** command provides briefer interface information, focusing on the most important information.Perform any of following operations based on the interface status and statistics:

* If the interface is Down, check whether the link connection is correct or whether interface negotiation succeeds.
* Interface statistics reflect traffic received and sent. If the interface has a lot of error statistics, check whether the interface is attacked or whether the link quality is stable.

**Follow-up Procedure**



Run the **reset interface counters** command to delete interface statistics displayed using the display interface brief command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about broadcast and multicast packets on all main interface on a device.
```
<HUAWEI> display interface ethernet brief main non-unicast
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(B): Bit-error-detection down
(e): ETHOAM down
(d): Dampening Suppressed
(p): port alarm down
(dl): DLDP down
(c): CFM down
(ms): MACsec down
InUti/OutUti: input utility/output utility
Interface                   PHY   Protocol  InBroad OutBroad   InMulti  OutMulti
100GE1/0/1                  *down down            0        0         0         0
100GE1/0/1                  up    down            0        0         0         0
MEth0/0/0                   up    down         3726        0     18609         0

```

**Table 1** Description of the **display interface brief main non-unicast** command output
| Item | Description |
| --- | --- |
| \*down: administratively down | If the network administrator runs the shutdown command on the interface, the interface status is displayed as administratively down. |
| ^down: standby | standby: indicates that the interface is a backup interface. |
| (l): loopback | The loopback function is configured on the interface. |
| (b): BFD down | Indicates that the data link layer of the interface is in BFD Down state. |
| (B): Bit-error-detection down | Indicates that the data link layer of the interface is in the bit error Down state. |
| (e): ETHOAM down | Indicates that the data link layer of the interface is in Ethernet OAM Down state. |
| (d): Dampening Suppressed | Indicates that the protocol module of the interface is suppressed. |
| (p): port alarm down | Indicates that the physical layer of the interface is in port alarm Down state. |
| (s): spoofing | The spoofing feature of the link protocol status of the interface. That is, the link protocol status of the interface is always Up.  This is the build-in attribute of an interface. When this interface is assigned an IP address, (s) is still displayed. |
| (c): CFM down | Indicates that the interface is associated with CFM and goes Down. |
| Interface | Name and number of an interface.  If logical interfaces have member interfaces, these member interfaces are displayed in alphabetical order. The first character of each line in the output is indented by two spaces. Interface types are the same as those displayed in the display interface brief command output. |
| PHY | Physical status of an interface. |
| Protocol | Link layer protocol status of the interface. |
| InBroad | Number of broadcast packets received by an interface. |
| OutBroad | Number of broadcast packets sent by an interface. |
| InMulti | Number of multicast packets received by an interface. |
| OutMulti | Number of multicast packets sent by an interface. |
| (ms): MACsec down | Indicates that the data link layer of the interface is in MACsec down state. |
| InUti | Average inbound bandwidth usage of this interface in the last 300 seconds.  Average inbound bandwidth usage in the last 300 seconds = Average inbound rate in the last 300 seconds/Interface bandwidth.  When the average inbound bandwidth usage is lower than 0.01% and this interface is receiving traffic, value 0.01% is displayed.  When the interface bandwidth becomes lower, bandwidth usage may become 100% because adjusting the traffic volume is delayed. Hyphens (--) indicate that this type of interface does not support the display of bandwidth usage.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| OutUti | Average outbound bandwidth usage in the last 300 seconds.  Average outbound bandwidth usage in the last 300 seconds = Average outbound rate in the last 300 seconds/Interface bandwidth.  When the average outbound bandwidth usage is lower than 0.01% and this interface is sending traffic, value 0.01% is displayed.  When the interface bandwidth becomes lower, bandwidth usage may become 100% because adjusting the traffic volume is delayed. Hyphens (--) indicate that this type of interface does not support the display of bandwidth usage.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |