display interface brief panel-order
===================================

display interface brief panel-order

Function
--------



The **display interface brief panel-order** command displays brief information about all interfaces on each board in a specific sequence.




Format
------

**display interface brief panel-order**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view brief information about all interfaces on each interface board in a specific sequence, run the **display interface brief panel-order** command. The command output includes the physical and protocol status of interfaces, latest inbound and outbound bandwidth usage, and the number of sent and received error packets. The command output helps you collect traffic statistics and troubleshoot interface faults.



**Follow-up Procedure**



To re-collect traffic statistics on an interface within a specified period, run the **reset interface counters** command to clear the existing traffic statistics on the interface.



**Precautions**

After the **display interface brief panel-order** command is run, information about interfaces is displayed as follows:

* Physical interfaces are displayed first followed by logical interfaces.
* Physical interfaces in different slots are displayed in ascending order of slot numbers.
* Physical interfaces in the same slot are displayed in ascending order of interface numbers.
* Logical interfaces are displayed in alphabetical order.
* The same type of logical interfaces is displayed in ascending order of interface numbers.If a logical interface, such as an Eth-Trunk interface has member interfaces, these member interfaces are displayed based on preceding rules, and each line is indented by two spaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all interfaces on an existing device.
```
<HUAWEI> display interface brief panel-order
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(e): ETHOAM down
(d): Dampening Suppressed
(p): port alarm down
(dl): DLDP down
(c): CFM down
(sd): STP instance discarding
(ed): error down
InUti/OutUti: input utility rate/output utility rate
Interface                  PHY      Protocol  InUti OutUti   inErrors  outErrors
MEth0/0/0                  up       up           0%     0%          0          0

100GE1/0/1                 down     down         0%     0%          0          0
100GE1/0/2                 down     down         0%     0%          0          0
100GE1/0/3                 up       up        0.01%  0.01%          0          0

Eth-Trunk0                 down     down         0%     0%          0          0
Eth-Trunk1                 down     down         0%     0%          0          0

LoopBack0                  up       up(s)        --     --          0          0
LoopBack1                  up       up(s)        --     --          0          0

NULL0                      up       up(s)        0%     0%          0          0

Nve1                       up       up           --     --          0          0

Tunnel1                    down     down         --     --          0          0

Vbdif1                     down     down         --     --          0          0

Vlanif1                    up       up           --     --          0          0

```

**Table 1** Description of the **display interface brief panel-order** command output
| Item | Description |
| --- | --- |
| (l): loopback | The loopback function is configured on the interface. |
| (s): spoofing | The spoofing feature of the link protocol status of the interface. That is, the link protocol status of the interface is always Up.  This is the build-in attribute of an interface. When this interface is assigned an IP address, (s) is still displayed. |
| (b): BFD down | Indicates that the data link layer of the interface is in BFD Down state. |
| (e): ETHOAM down | Indicates that the data link layer of the interface is in Ethernet OAM Down state. |
| (d): Dampening Suppressed | Protocol of the interface is suppressed. |
| (p): port alarm down | Indicates that the physical layer of the interface is in port alarm Down state. |
| (dl): DLDP down | Indicates that the data link layer of the interface is in DLDP Down state. |
| (c): CFM down | Indicates that the interface is associated with CFM and goes Down. |
| (sd): STP instance discarding | Indicates that traffic on the interface is blocked because the loop is broken due to STP calculation. |
| (ed): error down | The physical layer of the interface is in the Error Down state. |
| Interface | Interface type and number. All interfaces are displayed in the panel sequence. If a logical interface such as an Eth-Trunk has member interfaces, the member interfaces are displayed in the sequence at which they reside on the panel and two indented spaces are required for each row. The interfaces that can be displayed are the same as those that can be displayed through the display interface command, including but not limited to the following interfaces:   * Meth. * Eth-Trunk. * 100GE. * Loopback. * NULL. * Tunnel. * VLANIF.   The supported interface types depend on the device. |
| PHY | Physical status of the interface:   * up: The physical layer of this interface is working properly. * down: The physical layer of this interface becomes faulty. * \*down: Administratively Down, indicating that the administrator has run the shutdown command on this interface. * ^down: standby, indicating that this interface is a backup interface. * (l): loopback, indicating that this interface is enabled with the loopback function. * (b): BFD down, indicating that the physical layer of the interface is in the BFD Down state. * (p): port alarm down, indicating that the physical layer of this interface is in the port alarm down state. * (ed): error down, indicating that the physical layer of the interface is in the Error Down state. |
| Protocol | Link layer protocol status of the interface:   * up: The link layer protocol of this interface is working properly. * down: The link layer protocol of this interface becomes faulty. * (l): loopback, indicating that this interface is enabled with the loopback function. * (s): spoofing, indicating that this interface is enabled with the spoofing function. * (b): BFD Down, indicating that the link layer protocol of the interface is in the BFD Down state. * (e): ETHOAM down, indicating that the data link layer of the interface is in the ETHOAM Down state. * (d): dampening suppressed, indicating that the protocol module of the interface is suppressed. * (dl): DLDP Down, indicating that the data link layer of the interface is in the DLDP Down state. * (c): CFM down, indicating that the interface goes Down due to CFM association with the interface status. * (sd): STP instance discarding, indicating that traffic on the interface is interrupted due to STP calculation. * Blank: The interface is not configured with a link layer protocol. |
| InUti | Average inbound bandwidth usage of this interface in the last 300 seconds.  Average inbound bandwidth usage in the last 300 seconds = Average inbound rate in the last 300 seconds/Interface bandwidth.  When the average inbound bandwidth usage is lower than 0.01% and this interface is receiving traffic, value 0.01% is displayed.  When the interface bandwidth becomes lower (for example, the bandwidth of an Ethernet interface is adjusted using the speed command, or the member interface of an Eth-Trunk goes Down or is unbound), bandwidth usage may become 100% because adjusting the traffic volume is delayed. Hyphens (--) indicate that this type of interface does not support the display of bandwidth usage.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| OutUti | Average outbound bandwidth usage in the last 300 seconds.  Average outbound bandwidth usage in the last 300 seconds = Average outbound rate in the last 300 seconds/Interface bandwidth.  When the average outbound bandwidth usage is lower than 0.01% and this interface is sending traffic, value 0.01% is displayed.  When the interface bandwidth becomes lower (for example, the bandwidth of an Ethernet interface is adjusted using the speed command, or the member interface of an Eth-Trunk goes Down or is unbound), bandwidth usage may become 100% because adjusting the traffic volume is delayed. Hyphens (--) indicate that this type of interface does not support the display of bandwidth usage.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| inErrors | Number of error packets received by an interface.  After the reset interface counters command is run in the user view or the number of received error packets reaches the maximum value 4294967295, the number of received error packets is set to 0. |
| outErrors | Number of error packets sent by an interface. After the reset interface counters command is run in the user view or the number of sent error packets reaches the maximum value 4294967295, the number of sent error packets is set to 0. |
| \*down | Reason that interface is physically Down.  Administratively DOWN: The network administrator runs the shutdown command on the interface. |
| ^down | standby: indicates that the interface is a backup interface. |