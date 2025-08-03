display this interface
======================

display this interface

Function
--------



The **display this interface** command displays interface information in the current interface view.




Format
------

**display this interface**


Parameters
----------

None

Views
-----

200GE interface view,all-interface view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view the status of the interface and packet statistics on an interface, run the **display this interface** command in the interface view.Information displayed using the **display this interface** command in the current interface view is the same as the information displayed using the display interface interface-type interface-number command (interface-type and interface-number specify an existing interface).




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv6 information on 10GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 10GE 1/0/1
[~HUAWEI-10GE1/0/1] display this interface
10GE1/0/1 current state : UP (ifindex: 6)
Line protocol current state : UP
Description:
Switch Port, PVID :    1, TPID : 8100(Hex), The Maximum Frame Length is 9216
Internet protocol processing : disabled
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Port Mode:     COMMON FIBER,     Port Split/Aggregate:               -
Speed:                10000,     Loopback:                        NONE
Duplex:                FULL,     Negotiation:                        -
Input Flow-control: DISABLE,     Output Flow-control:           ENABLE
Mdi:                      -,     Fec:                                -
Last physical up time   : 2022-03-28 10:44:55
Last physical down time : 2022-03-28 10:43:49
Current system time: 2022-03-28 15:53:50
Statistics last cleared:never
    Last 300 seconds input rate: 79 bits/sec, 0 packets/sec
    Last 300 seconds output rate: 491 bits/sec, 0 packets/sec
    Input peak rate 181 bits/sec, Record time: 2022-03-28 10:45:15
    Output peak rate 494 bits/sec, Record time: 2022-03-28 10:52:49
    Input :             207592 bytes,                616 packets
    Output:            1325324 bytes,               9268 packets
    Input:
      Unicast:                      0,   Multicast:                     616
      Broadcast:                    0,   Jumbo:                           0
      Discard:                      0,   Frames:                         --
      Pause:                        0,   Ignoreds:                        0

      Total Error:                  0
      CRC:                          0,   Giants:                          0
      Jabbers:                     --,   Fragments:                       0
      Runts:                        0,   DropEvents:                      0
      Alignments:                   0,   Symbols:                         0

    Output:
      Unicast:                      0,   Multicast:                    9268
      Broadcast:                    0,   Jumbo:                           0
      Discard:                      0,   Buffers Purged:                  0
      Pause:                        0

    Input bandwidth utilization threshold : 90.00%
    Output bandwidth utilization threshold: 90.00%
    Last 300 seconds input utility rate:  0.01%
    Last 300 seconds output utility rate: 0.01%

```

# Display information about MEth0/0/0.
```
<HUAWEI> system-view
[~HUAWEI] interface MEth0/0/0
[~HUAWEI-MEth0/0/0] display this interface
MEth0/0/0 current state : UP (ifindex: 4)
Line protocol current state : UP
Last line protocol up time : 2022-03-28 10:44:46
Description: NETCONF_API_HDM-Secray fuzzing ongoing
Route Port,The Maximum Transmit Unit is 1500
Internet Address is 10.1.1.1/24
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Media type: COMMON COPPER, Link type: auto negotiation
Loopback: NONE, Maximal BW: 1000M, Current BW: 1000M, Full-duplex mode
Last physical up time   : 2022-03-28 10:44:46
Last physical down time : -
Current system time: 2022-03-28 16:50:56
Statistics last cleared:never
    Last 300 seconds input rate: 946 bits/sec, 1 packets/sec
    Last 300 seconds output rate: 337 bits/sec, 0 packets/sec
    Input peak rate 3132 bits/sec, Record time: 2022-03-28 10:51:04
    Output peak rate 4035 bits/sec, Record time: 2022-03-28 10:50:14
    Input :            2264774 bytes,              22916 packets
    Output:            1020730 bytes,               9631 packets
    Input:
      Unicast:                  10878,   Multicast:                    6131
      Broadcast:                 5907,   Overrun:                         0
      Over-car-pps:                 0

      Total Error:                  0,   CRC:                             0
      Giants:                       0,   Jabbers:                         0
      Runts:                        0,   Fragments:                       0

    Output:
      Unicast:                   9311,   Multicast:                       0
      Broadcast:                  301,   Underrun:                        0
    Last 300 seconds input utility rate:  0.01%
    Last 300 seconds output utility rate: 0.01%

```

**Table 1** Description of the **display this interface** command output
| Item | Description |
| --- | --- |
| current state | Current status of the interface:   * UP: indicates that the physical status of the interface is Up. * DOWN: indicates that the physical layer of the interface is faulty. * Administratively DOWN: The administrator has run the shutdown command on the interface. * Flow Down: The traffic status of the interface is Down. This status is determined by the status of the management Virtual Router Redundancy Protocol (mVRRP) bound to the interface. If the mVRRP status is Backup or Initialize, the status of the data flow on the interface is Down. * OFFLINE: The board where the interface resides is not properly installed. * ERROR DOWN (monitor-link): The downlink interface is in Error-Down state because the uplink interface link is faulty. |
| Line protocol current state | Link layer protocol status of the interface:   * UP: The link layer protocol of this interface is working properly. * (mf): mac-flapping blocked. Traffic on the interface is interrupted due to a network loop. * DOWN (BFD status down): The bidirectional forwarding detection (BFD) session bound to the interface goes Down. * DOWN (Main BFD status down): The BFD session bound to the main interface goes Down, which changes the BFD session status on the Layer 2 or Layer 3 sub-interface correspondingly. This state is available only for the Layer 2 or Layer 3 sub-interface. * DOWN (Main bit-error-detection down): The status displayed on Layer 2 or Layer 3 sub-interfaces when the bit error ratio of the interface exceeds the alarm threshold. By default, the bit error function on an interface associates with that on Layer 2 or Layer 3 sub-interfaces. * DOWN (Bit-error-detection down): The bit error ratio on the interface exceeds the alarm threshold. * DOWN (dampening suppressed):The interface is being suppressed by the protocol module. * DOWN: The link layer protocol status of the interface is Down or no IP address is assigned to the interface.   For example, if no IP address is assigned to an IP service-capable interface,its protocol status is Down.   * UP (spoofing): The link layer protocol of the interface is always Up with the spoofing feature enabled. |
| Switch Port | A Layer 2 interface is displayed.  If the interface is a Layer 3 interface, such as a VLANIF interface, Route Port is displayed here. |
| PVID | Default VLAN ID of the interface. |
| TPID | Type of frames that are supported on the interface.  By default, this field displays 0x8100, indicating an 802.1Q frame. |
| The Maximum Transmit Unit is | Maximum transmission unit (MTU) of an interface. |
| The Maximum Frame Length | Maximum frame length allowed by the interface. You can run the jumboframe enable command to set this parameter. |
| Internet Address is | IP address and mask length for the interface. |
| Internet protocol processing | If the interface is a Layer 3 interface and has an IP address configured, this field displays the IP address. If the interface is a Layer 2 interface or has no IP address configured, this field displays disabled. |
| IP Sending Frames' Format is | Format of Ethernet frames sent by the interface.  PKTFMT\_ETHNT\_2 is the default frame format. When receiving frames, an Ethernet interface can identify the following formats:   * PKTFMT\_ETHNT\_2. * Ethernet\_SNAP. * 802.2. * 802.3. |
| Hardware address is | MAC address of the interface. |
| Port Mode | Working mode of an interface:  ·COMMON COPPER: The interface works in electrical signal mode. For example, the interface is an electrical interface or an optical interface that has a copper module or high-speed cable installed.  ·COMMON FIBER: The interface works in optical signal mode. For example, an optical module or AOC cable is installed on an optical interface.  ·AUTO: The interface working mode is not identified. For example, no medium is installed on the optical interface. |
| Port Split | Split status of an electrical interface.  "-" indicates that the item is not involved.  disable: indicates that the interface is not split. The field is displayed only in interfaces that can be split.  enable: indicates that the interface is split. This field is displayed only after interface split takes effect.  Enable after board reset: The interface split configuration takes effect only after the board restarts. If an interface is split using the port split command but the board is not restarted, this status is displayed.  Disable after board reset: The interface merge takes effect only after the board is restarted. After the undo port split command is run to merge interfaces and before the board is restarted, this status is displayed. |
| Port Split/Aggregate | Split or merge status of an optical interface.  "-" indicates that the item is not involved.  disable: indicates that the interface is not split. The field is displayed only in interfaces that can be split.  enable: indicates that the interface is split. This field is displayed only after interface split takes effect.  Enable after board reset: The interface split configuration takes effect only after the board restarts. If an interface is split using the port split command but the board is not restarted, this status is displayed.  Disable after board reset: The interface merge takes effect only after the board is restarted. After the undo port split command is run to merge interfaces and before the board is restarted, this status is displayed. |
| Input peak rate | Maximum average rate at which packets were received during all statistical intervals. During each statistical interval, packets are received at a specific rate.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. The value is an integer ranging from 10 to 600, in seconds. It must be an integer multiple of 10.  The default interval is 300 seconds. |
| Input Flow-control | Whether flow control is enabled in the inbound direction:  ·ENABLE: Flow control is enabled in the inbound direction of the interface.  ·DISABLE: Flow control is disabled in the inbound direction of the interface. |
| Input | Total numbers of packets and bytes received on an interface. Packets include correct packets (unicast, broadcast, and multicast packets), incorrect packets, and discarded packets.  ·840968 bytes, 3899 packets: numbers of correct packets and bytes.  Total numbers of correct packets and bytes received by the interface. The packet types include:  Unicast: Number of unicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.  Multicast: Number of multicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.  Broadcast: Number of broadcast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.  Jumbo: Number of packets with correct FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length.  Discard: Number of packets discarded by the interface during physical layer detection. The value is always 0.  Frames: Number of packets with incorrect 802.3 length received by the interface.  Pause: Number of pause frames.  Overrun: Number of discarded packets received by the management interface.  Over-car-pps: Number of packets discarded due to rate limit configured using the qos lr pps command on a management interface.  Ignoreds: Number of received MAC control frames with OpCode not being PAUSE.  ·Total Error: total number of error packets received by the interface. The packet types include:  CRC: Number of packets with CRC errors and with lengths greater than or equal to 64 bytes and less than or equal to the maximum jumbo frame size supported by the interface.  Giants: Number of received packets with length exceeding the maximum jumbo frame size and correct FCS values.  Jabbers: Number of received packets with incorrect FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length. The value is always 0.  Fragments: Number of fragments received by the interface. A fragmented packet is a packet shorter than 64 bytes and with incorrect CRC values.  Runts: Number of undersized frames with the correct FCS received by the interface. An undersized frame is a frame that is shorter than 64 bytes, in correct format, and contains a valid CRC field.  DropEvents: Number of received packets that are discarded due to GBP full or back pressure.  Alignment: Number of received packets with frame alignment errors.  Symbols: Number of received packets with coding errors. |
| Input bandwidth utilization threshold | Threshold for inbound bandwidth usage. |
| Output peak rate | Maximum average rate at which packets were sent during all statistical intervals. During each statistical interval, packets are sent at a specific rate.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. The value is an integer ranging from 10 to 600, in seconds. It must be an integer multiple of 10.  The default interval is 300 seconds. |
| Output Flow-control | Whether flow control is enabled in the outbound direction:  ·ENABLE: Flow control is enabled in the outbound direction of the interface.  ·DISABLE: Flow control is disabled in the outbound direction of the interface. |
| Output | Total number of sent packets and bytes on an interface. Packets include correct packets (unicast, broadcast, and multicast packets), incorrect packets, and discarded packets.  · 4652516 bytes, 34247 packets: Number of correct packets and bytes.  · Number of correct packets sent by the interface. The packets include:  Unicast: number of unicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.  Multicast: number of multicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.  Broadcast: number of broadcast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.  Jumbo: number of packets with correct FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length.  · Number of incorrect packets and discarded packets sent by the interface. The packets include:  Underrun: number of discarded packets sent by the management interface.  Discard: number of packets discarded by the interface during physical layer detection. Run the reset qos queue statistics interface command to clear the number of discarded packets in the outbound direction.  Buffers Purged: number of packets aged out because they have been stored in the queue buffer for a long time when the interface sends packets.  Pause: number of pause frames. |
| Output bandwidth utilization threshold | Threshold for outbound bandwidth usage. |
| Last line protocol up time | Last time the link-layer protocol of the interface went Up. |
| Last physical up time | Last time when the interface went up. - indicates that the interface status did not change in the past.  When the interface goes Up, if the system is configured with a time zone and the daylight saving time begins, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Last physical down time | Last time when the physical status of the interface goes Down.  A hyphen (-) indicates that the physical status of the interface does not change.  When the interface goes Down, if the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Last 300 seconds output rate | Rate of the bit and the output packet that pass through the interface in the last 5 minutes:   * If the interface is in the hybrid mode, that is, it reads about all the packets on the LAN, use the error to test the traffic. * If the interface is not in the hybrid mode, that is, the interface records only the traffic sent and received by itself, the error displays only the traffic sent and received by the interface.   You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| Last 300 seconds input utility rate | Percentage of the rate for receiving packets to the total bandwidth. |
| Last 300 seconds output utility rate | Percentage of the rate for sending packets to the total bandwidth. |
| Last 300 seconds input rate | Rate of the bit and the input packet that pass through the interface in the last 5 minutes:   * If the interface is in the hybrid mode, that is, it reads about all the packets on the LAN, use the error to test the traffic. * If the interface is not in the hybrid mode, that is, the interface records only the traffic sent and received by itself, the error displays only the traffic sent and received by the interface.   You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| Current system time | Current system time.  If the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Current BW | Current bandwidth. |
| Statistics last cleared | Last time statistics on the interface were deleted. |
| Route Port | Layer 3 interface. |
| Maximal BW | Maximum bandwidth. |
| Description | Description of the interface. A maximum of 242 case-sensitive characters (including spaces) can be entered. The description helps you learn about the interface function.  If no description is configured for the interface using the description command, nothing is displayed by default. |
| ifindex | Index of the interface. |
| Speed | Current interface bandwidth.  · In auto-negotiation mode, you can run the speed auto command to set this parameter.  · In non-auto-negotiation mode, you can run the speed command to set this parameter. |
| Loopback | Loopback configuration of the interface. To configure loopback on an interface, run the loopback command. |
| Duplex | Duplex mode of the interface. If this field displays FULL, the interface works in full-duplex mode. If this field displays HALF, the interface works in half-duplex mode. |
| Negotiation | Auto-negotiation mode of the interface.  ·ENABLE: Auto-negotiation is enabled on the interface.  ·DISABLE: Auto-negotiation is disabled on the interface. |
| Mdi | Network cable type of the interface.  The network cable type is displayed as auto for an electrical interface, and displayed as a hyphen (-) for an optical interface. |
| Fec | FEC mode of an optical interface.  RS-FEC: The RS-FEC function is enabled.  BASE-FEC: The BASE-R FEC function is enabled.  ·NONE: The FEC function is not configured or the FEC mode is not supported.  When the physical status of an optical interface is DOWN, "-" is displayed. |