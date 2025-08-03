display interface brief
=======================

display interface brief

Function
--------



The **display interface brief** command displays brief information about all interfaces on a device, including the physical status, IPv4 protocol status, recent bandwidth usage in the sending and receiving directions, and number of received and sent error packets.




Format
------

**display interface brief** [ *ifType* ]

**display interface brief** [ *ifType* ] **main**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ifType* | Displays brief information about the specified main interface. | - |
| **main** | Displays brief information about the main interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Before you monitor interface status or locate an interface fault, run the **display interface brief** command to view the status of and statistics on the interface. The command output helps you diagnose faults.Compared with the **display interface** command, the **display interface brief** command provides briefer interface information, focusing on the most important information.Perform any of following operations based on the interface status and statistics:

* If the interface is Down, check whether the link connection is correct or whether interface negotiation succeeds.
* Interface statistics reflect traffic received and sent. If the interface has a lot of error statistics, check whether the interface is attacked or whether the link quality is stable.

**Follow-up Procedure**



Run the **reset interface counters** command to delete interface statistics displayed using the **display interface brief** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all interfaces on an existing device.
```
<HUAWEI> display interface brief
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
(ms): MACsec down
(ed): error down
InUti/OutUti: input utility rate/output utility rate
Interface                  PHY      Protocol  InUti OutUti   inErrors  outErrors
100GE1/0/1               *down    down         0%     0%          0          0
100GE1/0/2               *down    down         0%     0%          0          0
MEth0/0/0                up       up        0.01%     0%          0          0
NULL0                    up       up(s)        0%     0%          0          0

```

# Display brief information about all main interfaces on the current device.
```
<HUAWEI> display interface brief main
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
(ms): MACsec down
(ed): error down
InUti/OutUti: input utility rate/output utility rate
Interface                  PHY      Protocol  InUti OutUti   inErrors  outErrors
100GE1/0/1               *down    down         0%     0%          0          0
100GE1/0/2               *down    down         0%     0%          0          0
MEth0/0/0                up       up        0.01%     0%          0          0
NULL0                    up       up(s)        0%     0%          0          0

```

**Table 1** Description of the **display interface brief** command output
| Item | Description |
| --- | --- |
| Interface | Name and number of an interface. If an Eth-Trunk interface has member interfaces, the member interfaces are displayed in lexicographic order, and the first character of each line is indented by two spaces. The interface types that can be displayed are the same as those displayed in the display interface brief command output.  The content in the brackets following a 100GE interface can be expressed as follows:   * Actual bandwidth of the interface.For example, for a GE main interface or sub-interface with a bandwidth of 100 Gbit/s, the interface name is followed by a bandwidth identifier "100G". * For a main interface or sub-interface whose bandwidth is limited by a license, a bandwidth identifier is displayed next to the interface name. * For a main interface or sub-interface with adaptive bandwidth, a bandwidth identifier is displayed next to the interface name. |
| PHY | Physical status of the interface. The possible physical states are as follows:   * up: indicates that the physical layer of the interface is Up. * down: indicates that the physical layer of the interface is faulty. * \*down: Administratively DOWN. The administrator runs the shutdown command on the interface. * ^down: standby, indicating that the interface is a standby interface. * (l): loopback, indicating that the loopback function is enabled on the interface. * (E): E-Trunk down, indicating that the Eth-Trunk interface goes Down due to E-Trunk protocol negotiation. * (b): BFD down, indicating that the physical layer of the interface is in BFD Down state. * (p): port alarm down, indicating that the interface alarm is associated with the physical status Down, for example, CRC alarm. * (ed): error down, indicating that the physical layer of the interface is in Error Down state. * (ex): External-detection down, indicating that the interface goes Down when the device detects that the IP address is not allowed. For example, if 1.1.1.1 is configured using the external communication detection command and the device is connected to 1.1.1.1, the interface goes Down. * (lcs): license not activated. The license of the Ethernet interface on the CM board is not activated. * (D): DF backup down, indicating that the interface is Down due to EVPN DF election.   The actually supported physical status depends on the device. |
| Protocol | IPv4 link-layer protocol status of the interface. The possible link protocol states are as follows:   * up: The data link layer of the interface is Up. * down: The link layer protocol of the interface is faulty. * \*down: Administratively DOWN. The administrator has run the shutdown network-layer command on the interface. * (l): loopback, indicating that the loopback function is enabled on the interface. * (s): spoofing, indicating that the spoofing function is enabled on the interface. * (b): BFD down, indicating that the data link layer of the interface is in BFD Down state. * (e): ETHOAM down, indicating that EFM detection at the physical layer of the interface fails. * (p): port alarm down, indicating that the physical layer of the interface is in the port alarm Down state. * (dl): DLDP down, indicating that the link layer of the interface is in DLDP Down state. * (c): CFM down, indicating that CFM is associated with the interface to go Down. * (sd): STP instance discarding, indicating that traffic on the interface is blocked because the loop is disconnected due to STP calculation. * (ms): MACsec down, indicating that the data link layer of the interface is in MACsec Down state. * (ed): error down, indicating that the physical layer of the interface is in Error Down state. * Blank: The interface has no link-layer protocol status.   The actual supported link status depends on the device. |
| InUti | Average inbound bandwidth usage of an interface within the last 300 seconds. Average inbound bandwidth usage within the last 300 seconds = Average inbound traffic rate within the last 300 seconds/Interface bandwidth If the value is smaller than 0.01% and the interface has traffic, 0.01% is displayed. When the interface bandwidth becomes lower, the bandwidth usage may be displayed as 100% because the communication traffic is not adjusted in time. "--" indicates that this type of interface does not support the display of bandwidth usage.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| OutUti | Average outbound bandwidth usage within the last 300 seconds. Average outbound bandwidth usage within the last 300 seconds = Average outbound traffic rate within the last 300 seconds/Interface bandwidth If the value is smaller than 0.01% and the interface has traffic, 0.01% is displayed. When the interface bandwidth becomes lower, the bandwidth usage may be displayed as 100% because the communication traffic is not adjusted in time. "--" indicates that this type of interface does not support the display of bandwidth usage.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| inErrors | Number of error packets received by the interface. After the reset counters interface command is run in the user view, the statistics on the corresponding interface are reset to 0. A maximum of 9999999999 error packets can be displayed. When the number of error packets on an interface exceeds 9999999999, 9999999999 is always displayed. In this case, you can run the display interface command to query the actual number of error packets. |
| outErrors | Number of error packets sent by an interface. After the reset counters interface command is run in the user view, the statistics on the corresponding interface are reset to 0. A maximum of 9999999999 error packets can be displayed. When the number of error packets on an interface exceeds 9999999999, 9999999999 is always displayed. In this case, you can run the display interface command to query the actual number of error packets. |