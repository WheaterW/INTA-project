display interface
=================

display interface

Function
--------



The **display interface** command displays the running status of and traffic statistics on an interface.




Format
------

**display interface** [ *interface-type* [ *interface-number* ] | **slot** *slot-number* ]

**display interface** *interface-name*

**display interface main**

**display interface** *interface-type* **main**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface.  If no interface type is specified, the description of all interfaces is displayed. | - |
| *interface-number* | Specifies the number of an interface.  If an interface type is specified but no interface number is specified, the description of all interfaces of this type is displayed. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **slot** *slot-number* | Specifies the slot number.  If no slot number is specified, the description of all slots is displayed. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-name* | Displays the description of a specified interface. | - |
| **main** | Displays the running status of and traffic statistics on an interface.   * If an interface has no Layer 2 or Layer 3 sub-interfaces, the status of and traffic statistics on the interface are displayed whether you specify this parameter or not. * If an interface has Layer 2 or Layer 3 sub-interfaces, the status of and traffic statistics on the interface and its Layer 2 or Layer 3 sub-interfaces are displayed if you do not specify this parameter. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Before you monitor the status of an interface or locate an interface fault, use the **display interface** command to collect the running status of and statistics on the interface. You can troubleshoot the interface based on the command output.Perform any of following operations based on the interface status and statistics:

* If the interface is Down, check whether the link connection is correct or whether interface negotiation succeeds.
* Interface statistics reflect traffic received and sent. If the interface has a lot of error statistics, check whether the interface is attacked or whether the link quality is stable.
* If the date and time when the interface last went Up and Down are different from those in the actual situation, contact technical support personnel.Compared with the **display interface brief** command, the **display interface** command provides more interface information to help locate faults.

**Precautions**



Check the physical status and IPv4 link protocol status of the interface. Normally, the link status of the interface in use is Up.Check the values of Last 300 seconds input rate and Last 300 seconds output rate. Compare the current traffic with the interface bandwidth. If the usage exceeds 80% of the interface bandwidth, record and check whether there are error statistics in the inbound and outbound directions of the interface. Pay attention to the increase of error statistics.The queried interface bandwidth rate is calculated as follows: 1 Gbit/s = 10^9 bit/s.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status and statistics information about Layer 2 sub-interface 100GE1/0/1.1.
```
<HUAWEI> display interface 100ge1/0/1.1
100GE1/0/1.1 current state : UP (ifindex: 6)
Line protocol current state : UP
Description:
Route Port,The Maximum Transmit Unit is 1500
Internet protocol current state: disabled
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Current system time: 2013-07-30 09:15:33
Last 10 seconds input rate 8668298072 bits/sec, 8208616 packets/sec
Last 10 seconds output rate 0 bits/sec, 1641915 packets/sec
Input:  2462584682 packets, 325061178024 bytes
Output:  492575036 packets, 0 bytes
    Last 10 seconds input utility rate:  86.68%
    Last 10 seconds output utility rate: 0.00%

```

# Display running status and traffic statistics about an interface on the device.
```
<HUAWEI> display interface main
2020-06-03 10:17:27.684 
100GE1/0/1 current state : DOWN (ifindex: 87)
Line protocol current state : DOWN 
Description: 
Route Port,The Maximum Transmit Unit is 1500,The Maximum Frame Length is 9216
Internet protocol processing : disabled
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Port Mode:             AUTO,     Port Split/Aggregate:         DISABLE
Speed:                 AUTO,     Loopback:                        NONE
Duplex:                FULL,     Negotiation:                        -
Input Flow-control: DISABLE,     Output Flow-control:          DISABLE
Mdi:                      -,     Fec:                                -
Last physical up time   : -
Last physical down time : 2020-06-02 21:16:20
Current system time: 2020-06-03 10:17:27
Statistics last cleared:2020-06-02 22:10:10
    Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
    Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
    Input peak rate 0 bits/sec, Record time: -
    Output peak rate 0 bits/sec, Record time: -
    Input :                  0 bytes,                  0 packets
    Output:                  0 bytes,                  0 packets
    Input: 
      Unicast:                      0,   Multicast:                       0
      Broadcast:                    0,   Jumbo:                           0
      Discard:                      0,   Frames:                          0
      Pause:                        0
      
      Total Error:                  0
      CRC:                          0,   Giants:                          0
      Jabbers:                      0,   Fragments:                       0
      Runts:                        0,   DropEvents:                      0
      Alignments:                   0,   Symbols:                         0
      Ignoreds:                     0
   
    Output:
      Unicast:                      0,   Multicast:                       0
      Broadcast:                    0,   Jumbo:                           0
      Discard:                      0,   Buffers Purged:                  0
      Pause:                        0
    Input bandwidth utilization threshold : 90.00%
    Output bandwidth utilization threshold: 90.00%
    Last 300 seconds input utility rate:  0.00%
    Last 300 seconds output utility rate: 0.00%
100GE1/0/1 current state : DOWN (ifindex: 88)
Line protocol current state : DOWN 
Description: 
Route Port,The Maximum Transmit Unit is 1500,The Maximum Frame Length is 9216
Internet protocol processing : disabled
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Port Mode:             AUTO,     Port Split/Aggregate:         DISABLE
Speed:                 AUTO,     Loopback:                        NONE
Duplex:                FULL,     Negotiation:                        -
Input Flow-control: DISABLE,     Output Flow-control:          DISABLE
Mdi:                      -,     Fec:                                -
Last physical up time   : -
Last physical down time : 2020-06-02 21:16:20
Current system time: 2020-06-03 10:17:29
Statistics last cleared:2020-06-02 22:10:10
    Last 300 seconds input rate: 0 bits/sec, 0 packets/sec
    Last 300 seconds output rate: 0 bits/sec, 0 packets/sec
    Input peak rate 0 bits/sec, Record time: -
    Output peak rate 0 bits/sec, Record time: -
    Input :                  0 bytes,                  0 packets
    Output:                  0 bytes,                  0 packets
    Input: 
      Unicast:                      0,   Multicast:                       0
      Broadcast:                    0,   Jumbo:                           0
      Discard:                      0,   Frames:                          0
      Pause:                        0
      
      Total Error:                  0
      CRC:                          0,   Giants:                          0
      Jabbers:                      0,   Fragments:                       0
      Runts:                        0,   DropEvents:                      0
      Alignments:                   0,   Symbols:                         0
      Ignoreds:                     0
   
    Output:
      Unicast:                      0,   Multicast:                       0
      Broadcast:                    0,   Jumbo:                           0
      Discard:                      0,   Buffers Purged:                  0
      Pause:                        0
    Input bandwidth utilization threshold : 90.00%
    Output bandwidth utilization threshold: 90.00%
    Last 300 seconds input utility rate:  0.00%
    Last 300 seconds output utility rate: 0.00%

```

# Display the status and traffic statistics on 10GE1/0/1.
```
<HUAWEI> display interface 10GE 1/0/1
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

# Display the status and traffic statistics of Eth-Trunk 11.
```
<HUAWEI> display  interface Eth-Trunk 11
2022-09-09 11:06:05.385 +08:00
Eth-Trunk11 current state : DOWN (ifindex: 2010)
Line protocol current state : DOWN
Link quality grade : --
Description:
Switch Port, TPID : 8100(Hex), Hash arithmetic : According to flow, Maximal BW: 400Gbps, Current BW: 0Mbps, The Maximum Transmit Unit is 1500
Internet protocol processing : disabled
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fcf1-f60b
Current system time: 2022-09-09 11:06:05+08:00
Physical is ETH_TRUNK
    Last 300 seconds input rate 0 bits/sec, 0 packets/sec
    Last 300 seconds output rate 0 bits/sec, 0 packets/sec
    Input: 0 packets,0 bytes
           0 unicast,0 broadcast,0 multicast
           0 errors,0 drops
    Output:0 packets,0 bytes
           0 unicast,0 broadcast,0 multicast
           0 errors,0 drops
    Last 300 seconds input utility rate:  0.00%
    Last 300 seconds output utility rate: 0.00%
----------------------------------------------------------
PortName                      Status              Weight
----------------------------------------------------------
10GE1/0/1                 DOWN                1
10GE1/0/2                 DOWN                1
----------------------------------------------------------
The Number of Ports in Trunk : 2
The Number of UP Ports in Trunk : 0

```

**Table 1** Description of the **display interface** command output
| Item | Description |
| --- | --- |
| current state | Physical status of the interface.   * UP: The physical layer of the interface is Up. * DOWN: The physical layer of the interface is faulty. * Transceiver type mismatch: The media type does not match. * The optical power is too low: The optical power of the optical module is too low. * Port unavailable: The port is unavailable due to configurations such as port splitting and high-performance mode. * Cable for stack or peer-link interface only: Only stack ports or peer-link ports support this cable. * Transceiver type for stack only: The medium type is supported only by stack ports. * RTU license down: License resources are insufficient. * Serdes-Mode mismatch: The port cannot go Up due to insufficient frequency modes. * SerDes P/N mismatch: The mapping mode of the optical module does not match that of the port data channel. * Single forward state: The PHY of the copper transceiver module is faulty. * Configuration conflicts with transceiver: The configuration conflicts with the medium type. * Device hardware verification failed: The device hardware verification fails. * Transceiver loose: The medium is not securely installed. * Administratively DOWN: If the administrator runs the shutdown command on the interface, the interface status is Administratively DOWN. * Flow Down: The traffic status of the interface is Down. This status is consistent with the status of the bound mVRRP. If the status of the bound mVRRP group is Backup or Initialize, the traffic status of the service interface is Down. * OFFLINE: The board where the interface resides is not in position. * ERROR DOWN(monitor-link): The downlink interface goes Down due to a link fault on the uplink interface. |
| Line protocol current state | IPv4 link-layer protocol status of the interface.   * UP: The link layer protocol of the interface is Up. * Mac-flapping blocked (UP): Traffic on the interface is blocked due to a loop on the network. * DOWN (BFD status down): The BFD session bound to the interface goes Down. * DOWN (Main BFD status down): The BFD session associated with the main interface goes Down, and the Layer 2 or Layer 3 sub-interface status is associated.This status is displayed only on Layer 2 or Layer 3 sub-interfaces. * DOWN (Bit-error-detection down): The bit error rate on an interface exceeds the bit error alarm threshold. * DOWN (Main bit-error-detection down): The BER of the main interface corresponding to a Layer 2 or Layer 3 sub-interface exceeds the bit error alarm threshold. This state is displayed only on the Layer 2 or Layer 3 sub-interface. By default, bit error detection is associated with Layer 2 or Layer 3 sub-interfaces on a main interface. * DOWN (dampening suppressed): The protocol module of the interface is suppressed. * DOWN: The link-layer protocol status of the interface is Down or no IP address is assigned to the interface.   For example, if no IP address is assigned to an interface that supports IP services, the protocol status of the interface is Down.   * UP (spoofing): The link-layer protocol status of the interface is spoofing. That is, the link-layer protocol status of the interface is always Up. |
| Switch Port | The interface is a Layer 2 interface.  If the interface is a Layer 3 interface, Route Port is displayed. |
| PVID | Default VLAN ID of the interface. |
| TPID | Type of frames that are supported on the interface.  By default, this field displays 0x8100, indicating an 802.1Q frame. |
| The Maximum Transmit Unit | MTU of the interface.  For example, the default MTU of an Ethernet interface is 1500 bytes. The packet whose size is greater than the MTU is fragmented before being transmitted. If fragmentation is not allowed, the packets are discarded. |
| The Maximum Frame Length | Maximum frame length allowed by the interface. You can run the jumboframe enable command to set this parameter. |
| Internet protocol current state | If the interface is a Layer 3 interface and has an IP address configured, this field displays the IP address. If the interface is a Layer 2 interface or has no IP address configured, this field displays disabled. |
| Internet protocol processing | If the interface is a Layer 3 interface and has an IP address configured, this field displays the IP address. If the interface is a Layer 2 interface or has no IP address configured, this field displays disabled. |
| IP Sending Frames' Format | Format of Ethernet frames sent by the interface.  PKTFMT\_ETHNT\_2 is the default frame format. When receiving frames, an Ethernet interface can identify the following formats:   * PKTFMT\_ETHNT\_2. * Ethernet\_SNAP. * 802.2. * 802.3. |
| Hardware address | MAC address of an interface. |
| Last physical up time | Last time when the physical status of the interface went Up.  A hyphen (-) indicates that the physical status of the interface does not change.  When the interface goes Up, if the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Last physical down time | Last time when the physical status of the interface goes Down.  A hyphen (-) indicates that the physical status of the interface does not change.  When the interface goes Down, if the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Last 300 seconds input rate | Rate of the bit and the input packet that pass through the interface in the last 5 minutes:   * If the interface is in the hybrid mode, that is, it reads about all the packets on the LAN, use the error to test the traffic. * If the interface is not in the hybrid mode, that is, the interface records only the traffic sent and received by itself, the error displays only the traffic sent and received by the interface.   You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| Last 300 seconds output rate | Rate of the bit and the output packet that pass through the interface in the last 5 minutes:   * If the interface is in the hybrid mode, that is, it reads about all the packets on the LAN, use the error to test the traffic. * If the interface is not in the hybrid mode, that is, the interface records only the traffic sent and received by itself, the error displays only the traffic sent and received by the interface.   You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| Last 300 seconds output utility rate | Percentage of the rate for sending packets to the total bandwidth. |
| Current system time | Current system time.  If the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Statistics last cleared | Last time when statistics on the interface were deleted. |
| Input peak rate | Maximum average rate at which packets were received during all statistical intervals. During each statistical interval, packets are received at a specific rate.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. The value is an integer ranging from 10 to 600, in seconds. It must be an integer multiple of 10.  The default interval is 300 seconds. |
| Input bandwidth utilization threshold | Utilization of the bandwidth about IPv4/IPv6 packets received by the interface. |
| Input Flow-control | Whether flow control is enabled in the inbound direction:  ·ENABLE: Flow control is enabled in the inbound direction of the interface.  ·DISABLE: Flow control is disabled in the inbound direction of the interface. |
| Input | Total numbers of packets and bytes received on an interface. Packets include correct packets (unicast, broadcast, and multicast packets), incorrect packets, and discarded packets.   * 840968 bytes, 3899 packets: numbers of correct packets and bytes. * Total numbers of correct packets and bytes received by the interface. The packet types include: * Unicast: Number of unicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length. * Multicast: Number of multicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length. * Broadcast: Number of broadcast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length. * Jumbo: Number of packets with correct FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length. * Discard: Number of packets discarded by the interface during physical layer detection. The value is always 0. * Frames: Number of packets with incorrect 802.3 length received by the interface. * Pause: Number of pause frames. * Overrun: Number of discarded packets received by the management interface. * Over-car-pps: Number of packets discarded due to rate limit configured using the qos lr pps command on a management interface. * Ignoreds: Number of received MAC control frames with OpCode not being PAUSE. * Total Error: total number of error packets received by the interface. The packet types include: * CRC: Number of packets with CRC errors and with lengths greater than or equal to 64 bytes and less than or equal to the maximum jumbo frame size supported by the interface. * Giants: Number of received packets with length exceeding the maximum jumbo frame size and correct FCS values. * Jabbers: Number of received packets with incorrect FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length. The value is always 0. * Fragments: Number of fragments received by the interface. A fragmented packet is a packet shorter than 64 bytes and with incorrect CRC values. * Runts: Number of undersized frames with the correct FCS received by the interface. An undersized frame is a frame that is shorter than 64 bytes, in correct format, and contains a valid CRC field. * DropEvents: Number of received packets that are discarded due to GBP full or back pressure. * Alignment: Number of received packets with frame alignment errors. * Symbols: Number of received packets with coding errors. |
| Output peak rate | Maximum average rate at which packets were sent during all statistical intervals. During each statistical interval, packets are sent at a specific rate.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. The value is an integer ranging from 10 to 600, in seconds. It must be an integer multiple of 10.  The default interval is 300 seconds. |
| Output bandwidth utilization threshold | Utilization of the bandwidth about IPv4/IPv6 packets sent by the interface. |
| Output Flow-control | Whether flow control is enabled in the outbound direction:  ·ENABLE: Flow control is enabled in the outbound direction of the interface.  ·DISABLE: Flow control is disabled in the outbound direction of the interface. |
| Output | Total numbers of packets and bytes sent by an interface. Packets include correct packets (unicast, broadcast, and multicast packets), incorrect packets, and discarded packets.   * 840968 bytes, 3899 packets: numbers of correct packets and bytes. * Total numbers of correct packets and bytes sent by the interface. The packet types include:   + Unicast: Number of unicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.   + Multicast: Number of multicast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.   + Broadcast: Number of broadcast packets with lengths greater than or equal to 64 bytes and less than or equal to the maximum non-jumbo frame length.   + Jumbo: Number of packets with correct FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length.   + Discard: Number of packets discarded by the interface during physical layer detection. Run the reset qos queue statistics interface command to clear the number of discarded packets in the outbound direction.   + Frames: Number of packets with incorrect 802.3 length sent by the interface.   + Pause: Number of pause frames.   + Overrun: Number of discarded packets sent by the management interface.   + Over-car-pps: Number of packets discarded due to rate limit configured using the qos lr pps command on a management interface.   + Ignoreds: Number of sent MAC control frames with OpCode not being PAUSE. * Total Error: total number of error packets sent by the interface. The packet types include:   + CRC: Number of packets with CRC errors and with lengths greater than or equal to 64 bytes and less than or equal to the maximum jumbo frame size supported by the interface.   + Giants: Number of sent packets with length exceeding the maximum jumbo frame size and correct FCS values.   + Jabbers: Number of sent packets with incorrect FCS values and with lengths greater than the maximum non-jumbo frame length and less than or equal to the maximum jumbo frame length. The value is always 0.   + Fragments: Number of fragments sent by the interface. A fragmented packet is a packet shorter than 64 bytes and with incorrect CRC values.   + Runts: Number of undersized frames with the correct FCS sent by the interface. An undersized frame is a frame that is shorter than 64 bytes, in correct format, and contains a valid CRC field.   + DropEvents: Number of sent packets that are discarded due to GBP full or back pressure.   + Alignment: Number of sent packets with frame alignment errors.   + Symbols: Number of sent packets with coding errors. |
| Route Port | Layer 3 interface. |
| Port Mode | Working mode of an interface:  ·COMMON COPPER: The interface works in electrical signal mode. For example, the interface is an electrical interface or an optical interface that has a copper module or high-speed cable installed.  ·COMMON FIBER: The interface works in optical signal mode. For example, an optical module or AOC cable is installed on an optical interface.  ·AUTO: The interface working mode is not identified. For example, no medium is installed on the optical interface. |
| Port Split | Split status of an electrical interface.  "-" indicates that the item is not involved.  disable: indicates that the interface is not split. The field is displayed only in interfaces that can be split.  enable: indicates that the interface is split. This field is displayed only after interface split takes effect.  Enable after board reset: The interface split configuration takes effect only after the board restarts. If an interface is split using the port split command but the board is not restarted, this status is displayed.  Disable after board reset: The interface merge takes effect only after the board is restarted. After the undo port split command is run to merge interfaces and before the board is restarted, this status is displayed. |
| Port Split/Aggregate | Split or merge status of an optical interface.  "-" indicates that the item is not involved.  disable: indicates that the interface is not split. The field is displayed only in interfaces that can be split.  enable: indicates that the interface is split. This field is displayed only after interface split takes effect.  Enable after board reset: The interface split configuration takes effect only after the board restarts. If an interface is split using the port split command but the board is not restarted, this status is displayed.  Disable after board reset: The interface merge takes effect only after the board is restarted. After the undo port split command is run to merge interfaces and before the board is restarted, this status is displayed. |
| drops | Indicates the number of discarded packets. |
| Status | Status of the interface.   * UP: The physical status of the interface is Up. For a trunk interface in LACP negotiation mode, LACP negotiation must be successful. * DOWN: The physical status of the interface is Down. For a trunk interface in LACP negotiation mode, if LACP negotiation fails, DOWN is displayed regardless of whether the physical status of the interface is Up. |
| Description | Description of the interface. A maximum of 242 case-sensitive characters (including spaces) can be entered. The description helps you learn about the interface function.  If no description is configured for the interface using the description command, nothing is displayed by default. |
| ifindex | Interface index. |
| errors | Error count. |
| Speed | Current interface bandwidth.  · In auto-negotiation mode, you can run the speed auto command to set this parameter.  · In non-auto-negotiation mode, you can run the speed command to set this parameter. |
| Loopback | Loopback configuration of the interface. To configure loopback on an interface, run the loopback command. |
| Duplex | Duplex mode of the interface. If this field displays FULL, the interface works in full-duplex mode. If this field displays HALF, the interface works in half-duplex mode. |
| Negotiation | Auto-negotiation status of the interface.  ·ENABLE: Auto-negotiation is enabled on the interface.  ·DISABLE: Auto-negotiation is disabled on the interface.  ·-: Auto-negotiation is not supported. By default, the interface works in non-auto-negotiation mode. |
| Mdi | Network cable type of the interface.  The network cable type is displayed as auto for an electrical interface, and displayed as a hyphen (-) for an optical interface. |
| Fec | FEC mode of an optical interface.  RS-FEC: The RS-FEC function is enabled.  BASE-FEC: The BASE-R FEC function is enabled.  ·NONE: The FEC function is not configured or the FEC mode is not supported.  When the physical status of an optical interface is DOWN, "-" is displayed. |