display interface brief main
============================

display interface brief main

Function
--------



The **display interface brief** command displays brief information about all Ethernet interfaces on a device.




Format
------

**display interface** *interface-type1* **brief**

**display interface** *interface-type1* **brief** **main**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type1* | Displays brief information about the specified main interface. | - |
| **main** | Displays brief information about the main interface.  If you do not specify main in the command, the command displays brief information about all Ethernet interfaces and sub-interfaces. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To monitor Ethernet interface status or locate an Ethernet interface fault, run the display interface brief command to view the status and statistics of all Ethernet interfaces.



**Follow-up Procedure**



To clear the displayed statistics of Ethernet interfaces, run the **reset interface counters** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all Ethernet main interfaces on the device.
```
<HUAWEI> display interface ethernet brief main
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(b): BFD down
(p): port alarm down
Auto-Neg: Auto Negotiation
BW: BandWidth
InUti/OutUti: input utility rate/output utility rate
Interface            PHY   Auto-Neg Duplex    BW  InUti OutUti Trunk Description
100GE1/0/1           *down enable   full    100M     0%     0%    --
100GE1/0/1           *down enable   full    100M     0%     0%    --
100GE1/0/2           *down enable   full    100M     0%     0%    --
100GE1/0/3           *down enable   full    100M     0%     0%    --
MEth0/0/0            up    enable   full    100M  0.01%     0%    --

```

# Display brief information about all Ethernet interfaces on the device.
```
<HUAWEI> display interface ethernet brief
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(b): BFD down
(p): port alarm down
Auto-Neg: Auto Negotiation
BW: BandWidth
InUti/OutUti: input utility rate/output utility rate
Interface            PHY   Auto-Neg Duplex    BW  InUti OutUti Trunk Description
100GE1/0/1           *down enable   full    100M     0%     0%    --
100GE1/0/1           *down enable   full    100M     0%     0%    --
100GE1/0/2           *down enable   full    100M     0%     0%    --
100GE1/0/3           *down enable   full    100M     0%     0%    --
MEth0/0/0            up    enable   full    100M  0.01%     0%    --

```

**Table 1** Description of the **display interface brief main** command output
| Item | Description |
| --- | --- |
| Interface | Interface type and interface number. All interfaces are displayed in alphabetic order. |
| PHY | Physical status of the interface.   * up: indicates that the physical layer of the interface is Up. * down: indicates that the physical layer of the interface is faulty. * \*down: Administratively DOWN. The administrator runs the shutdown command on the interface. * ^down: standby, indicating that the interface is a standby interface. * (l): loopback, indicating that the loopback function is enabled on the interface. * (b): BFD down, indicating that the physical layer of the interface is in BFD Down state. * (d): Dampening Suppressed, indicating that the interface enters the flapping suppression state. * (p): port alarm down, indicating that the interface alarm is associated with the physical status Down, for example, CRC alarm. |
| Auto-Neg | Whether auto-negotiation is enabled on an interface:   * enable: indicates that auto-negotiation is enabled on the interface. * disable: indicates that auto-negotiation is disabled on the interface. * -: indicates that the current interface cannot obtain the attribute. |
| Duplex | Duplex mode of the interface:   * full. * half. |
| InUti | Average inbound bandwidth usage of this interface in the last 300 seconds.  Average inbound bandwidth usage in the last 300 seconds = Average inbound rate in the last 300 seconds/Interface bandwidth.  When the average inbound bandwidth usage is lower than 0.01% and this interface is receiving traffic, value 0.01% is displayed.  When the interface bandwidth becomes lower, bandwidth usage may become 100% because adjusting the traffic volume is delayed. |
| OutUti | Average outbound bandwidth usage in the last 300 seconds.  Average outbound bandwidth usage in the last 300 seconds = Average outbound rate in the last 300 seconds/Interface bandwidth.  When the average outbound bandwidth usage is lower than 0.01% and this interface is sending traffic, value 0.01% is displayed.  When the interface bandwidth becomes lower, bandwidth usage may become 100% because adjusting the traffic volume is delayed. |
| Trunk | Trunk ID of the interface.  -- indicates that the interface is not added to any trunk. |
| BW | Interface bandwidth. |
| Description | Description of the interface. |