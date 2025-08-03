monitor interface-information
=============================

monitor interface-information

Function
--------



The **monitor interface-information** command enables a device to monitor the running status and traffic statistics of an interface.




Format
------

**monitor interface-information interface** { *interface-name* | *interface-type* *interface-number* } [ [ **interval** *interval-value* ] [ **times** { *times-value* | **infinity** } ] | [ **times** { *times-value* | **infinity** } ] [ **interval** *interval-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | The value is an enumerated type. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 characters, spaces not supported. |
| **interval** *interval-value* | Specifies the interval at which the running status and traffic statistics of an interface are monitored. | The value is an integer ranging from 2 to 600, in seconds. The default value is 10. |
| **times** *times-value* | Specifies the number of times that the running status and traffic statistics of an interface are monitored. | The value is an integer ranging from 1 to 999. The default value is 5. |
| **infinity** | Displays the traffic rate on an interface. If rate is not specified, the number of packets on an interface is displayed.  This parameter is supported only on an interface whose physical status is Up. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To display detailed information about a specified interface for a specified number of times at a specified interval, run the monitor interface-information command. The information includes the running status and traffic statistics.By default, once this command is run, the system displays real-time traffic statistics at an interval of 10s for five times. To stop the statistics display, press Ctrl+C.



**Precautions**



An interface must be specified before you run the monitor interface-information command.




Example
-------

# Set the interval for displaying traffic statistics on 100GE1/0/1 to 10 seconds and set the number of times for displaying traffic statistics on this interface to 2.
```
<HUAWEI> monitor interface-information interface 100GE1/0/1 interval 10 times 2
Display information of the interface at the interval of 10 seconds for up to 2 times. Press Ctrl + C to stop.
  0 seconds left
Times 1
100GE1/0/1 current state : UP (ifindex: 6)
Line protocol current state : UP
Last line protocol up time :  2017-07-29 15:39:29
Description: HUAWEI, 100GE1/0/1 Interface
Route Port,The Maximum Transmit Unit is 1500
Internet Address is 10.1.1.1/1
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Last physical up time   :  2017-07-29 15:39:23
Last physical down time : 2017-07-29 15:38:41
Current system time: 2017-07-30 09:15:33
Statistics last cleared:never

      Last 300 seconds input rate: 23513 bits/sec, 2 packets/sec
      Last 300 seconds output rate: 64319 bits/sec, 3 packets/sec
      Input peak rate 26099 bits/sec, Record time: 2017-07-29 15:40:58
      Output peak rate 64809 bits/sec, Record time: 2017-07-30 03:59:41
      Input: 183126871 bytes, 182525 packets 
      Output: 509287017 bytes, 244628 packets
    Input:
      Unicast: 55 packets, Multicast: 0 packets
      Broadcast: 21708 packets JumboOctets: 31031 packets
      CRC: 0 packets, Symbol: 0 packets
      Overrun: 0 packets, InRangeLength: 0 packets
      LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
      Fragment: 0 packets, Undersized Frame: 0 packets
      RxPause: 0 packets
    Output:
      Unicast: 53 packets, Multicast: 0 packets
      Broadcast: 585 packets JumboOctets: 0 packets
      Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
      System: 0 packets, Overruns: 0 packets
      TxPause: 0 packets

    Last 300 seconds input utility rate:  0.01%
    Last 300 seconds output utility rate: 0.01%

  0 seconds left
Times 2
100GE1/0/1 current state : UP (ifindex: 6)
Line protocol current state : UP
Last line protocol up time :  2017-07-29 15:39:29
Description: HUAWEI, 100GE1/0/1
Route Port,The Maximum Transmit Unit is 1500
Internet Address is 10.1.1.1/1
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-3456
Last physical up time   :  2017-07-29 15:39:23
Last physical down time : 2017-07-29 15:38:41
Current system time: 2017-07-30 09:15:33
Statistics last cleared:never

      Last 300 seconds input rate: 23513 bits/sec, 2 packets/sec
      Last 300 seconds output rate: 64319 bits/sec, 3 packets/sec
      Input peak rate 26099 bits/sec, Record time: 2017-07-29 15:40:58
      Output peak rate 64809 bits/sec, Record time: 2017-07-30 03:59:41
      Input: 183126871 bytes, 182525 packets 
      Output: 509287017 bytes, 244628 packets
    Input:
      Unicast: 55 packets, Multicast: 0 packets
      Broadcast: 21708 packets JumboOctets: 31031 packets
      CRC: 0 packets, Symbol: 0 packets
      Overrun: 0 packets, InRangeLength: 0 packets
      LongPacket: 0 packets, Jabber: 0 packets, Alignment: 0 packets
      Fragment: 0 packets, Undersized Frame: 0 packets
      RxPause: 0 packets
    Output:
      Unicast: 53 packets, Multicast: 0 packets
      Broadcast: 585 packets JumboOctets: 0 packets
      Lost: 0 packets, Overflow: 0 packets, Underrun: 0 packets
      System: 0 packets, Overruns: 0 packets
      TxPause: 0 packets

    Last 300 seconds input utility rate:  0.01%
    Last 300 seconds output utility rate: 0.01%

```

**Table 1** Description of the **monitor interface-information** command output
| Item | Description |
| --- | --- |
| seconds left | Time elapsed since the next display of interface traffic statistics, in seconds. |
| Times | Number of times for the statistics display. This field is displayed each time when the query starts. |
| current state | Physical status of the interface:   * UP. * DOWN.   + AUAIS: Administrative unit-alarm indication signal (AU-AIS), which is a higher-order alarm indication.   + B3TCA fault: B3 threshold-crossing alarm indication.   + LAIS: Line alarm indication signal.   + LOF: Loss of frame.   + LOM: Loss of tributary multiframe.   + LOP: Loss of pointer.   + LOS: Loss of signal.   + LRDI: Line remote defect indication.   + LREI: Multiplex section-remote error indication.   + OOF: Out of frame.   + PAIS: Path alarm indication signal.   + PRDI: Path remote defect indication.   + PREI: Path remote error indication.   + PPLM: Path payload mismatch.   + RDOOL: Receive data out of lock.   + RROOL: Receive reference out of lock.   + SDBERE: Signal degradation.   + SFBERE: Remote signal failure.   + TROOL: Transmit reference out of lock.   + PUNEQ: Path unequipped indication.   + LCD: Loss of code group synchronization.   + WLNK: WAN interface link status alarm indication.   + ODU-AIS: ODU-(optical channel data unit) alarm indication signal.   + ODU-LCK: ODU-(optical channel data unit) locked.   + ODU-OCI: ODU-(optical channel data unit) open connection indication.   + OTU-AIS: OTU-(optical channel transport unit) alarm indication signal.   + OTU-LOM: OTU-(optical channel transport unit) loss of tributary multiframe.   + OTU-SD-BER: OTU-(optical channel transport unit) signal degrade.   + OTU-SF-BER: OTU-(optical channel transport unit) signal fail.   + PM-BDI: ODU-(optical channel data unit) path monitoring (PM) backward defect indication (BDI).   + PM-TIM: ODU-(optical channel data unit) path monitoring (PM) trail trace identifier (TTI) mismatch.   + SM-BDI: OTU-(optical channel transport unit) section monitoring (SM) backward defect indication (BDI).   + SM-IAE: OTU-(optical channel transport unit) section monitoring (SM) incoming alignment error (IAE).   + SM-TIM: OTU-(optical channel transport unit) section monitoring (SM) trail trace identifier (TTI) mismatch.   + OFFLINE: Alarm indicating that the optical module is offline.   + B1TCA: B1 threshold-crossing alarm indication.   + B2TCA: B2 threshold-crossing alarm indication.   + clock fault: Clock fault.   + link fault: Link fault.   + negotiation fail: Auto-negotiation failure.   + PMA fault: Physical medium attachment fault.   + WIS fault: WAN interface sublayer fault.   + PCS fault: Physical coding sublayer fault.   + XGXS fault: XGMII extender sublayer fault.   + local fault: Fault at the local end.   + remote fault: Fault at the remote end.   + high BER: High bit error rate in received packets.   + transceiver fault: Transceiver fault.   + IIC fault: Inter-integrated circuit fault.   + local fault and remote fault: Fault at both the local and remote ends.   + chip fault: Component fault.   + PREFEC TCA: Pre-forward error correction threshold-crossing alarm.   + transceiver offline: Alarm indicating that the transceiver is offline (no optical module is inserted).   + transceiver unmatch: Mismatch between the transceiver type and the port mode.   + group id unmatch: Mismatch between the transceiver type and the port mode.   + bandwidth limit: Bandwidth limit.   + ODU-SD-BER: ODU-(optical channel data unit) signal degrade. * Administratively Down: This state is displayed after the network administrator runs the shutdown command on the interface. * Flow Down: The status of the data flow on the interface is Down. This state is determined by the status of the mVRRP bound to the interface. If the mVRRP status is Backup or Initialized, the status of the data flow on the interface is Down. |
| Line protocol current state | Link layer protocol status of the interface:   * UP: The link layer protocol of this interface is working properly. * DOWN (BFD status down): The bidirectional forwarding detection (BFD) session bound to the interface goes Down. * DOWN (Main BFD status down): The BFD session bound to the main interface goes Down, which changes the BFD session status on the Layer 2 or Layer 3 sub-interface correspondingly. This state is available only for the Layer 2 or Layer 3 sub-interface. * DOWN (Main bit-error-detection down): The status displayed on Layer 2 or Layer 3 sub-interfaces when the bit error ratio of the interface exceeds the alarm threshold. By default, the bit error function on an interface associates with that on Layer 2 or Layer 3 sub-interfaces. * DOWN (Bit-error-detection down): The bit error ratio on the interface exceeds the alarm threshold. * DOWN (dampening suppressed):The interface is being suppressed by the protocol module. * DOWN: The link layer protocol status of the interface is Down or no IP address is assigned to the interface.   For example, if no IP address is assigned to an IP service-capable interface,its protocol status is Down.   * UP (spoofing): The link layer protocol of the interface is always Up with the spoofing feature enabled. |
| Last line protocol up time | Last time the link-layer protocol of the interface went Up. |
| Last physical up time | Last time when the interface went up. - indicates that the interface status did not change in the past.  When the interface goes Up, if the system is configured with a time zone and the daylight saving time begins, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Last physical down time | Last time when the physical status of the interface goes Down.  A hyphen (-) indicates that the physical status of the interface does not change.  When the interface goes Down, if the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Last 300 seconds output rate | Rate of the bit and the output packet that pass through the interface in the last 5 minutes:   * If the interface is in the hybrid mode, that is, it reads about all the packets on the LAN, use the error to test the traffic. * If the interface is not in the hybrid mode, that is, the interface records only the traffic sent and received by itself, the error displays only the traffic sent and received by the interface.   You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. |
| Last 300 seconds input utility rate | Percentage of the rate for receiving packets to the total bandwidth. |
| Last 300 seconds output utility rate | Percentage of the rate for sending packets to the total bandwidth. |
| Route Port | Layer 3 interface. |
| Internet Address is | IP address and mask length for the interface. |
| IP Sending Frames' Format is | Format of Ethernet frames sent by the interface.  PKTFMT\_ETHNT\_2 is the default frame format. When receiving frames, an Ethernet interface can identify the following formats:   * PKTFMT\_ETHNT\_2. * Ethernet\_SNAP. * 802.2. * 802.3. |
| Hardware address is | MAC address of the interface. |
| Current system time | Current system time.  If the system is configured with a time zone and is in the summer time, the time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC±HH:MM DST. |
| Statistics last cleared | Last time statistics on the interface were deleted. |
| Input peak rate | Maximum average rate at which packets were received during all statistical intervals. During each statistical interval, packets are received at a specific rate.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. The value is an integer ranging from 10 to 600, in seconds. It must be an integer multiple of 10.  The default interval is 300 seconds. |
| Input | Total number and total bytes of received packets on an interface. Packets include correct packets (unicast, broadcast, multicast packets and JumboOctets), incorrect packets, and dropped packets.   * XXXX bytes, XXXX packets: number of correctly sent packets and bytes. The number of sent packets is the sum of the sent unicast, broadcast, and multicast packets. * Number of correctly received packets and bytes. The packets include:   + Unicast.   + Multicast.   + Broadcast. * Number of received incorrect packets and dropped packets of the following types:   + CRC: Packets whose length is in the normal range but that contain that CRC error.   + Symbol: Error packets at the physical layer.   + Overrun: Packets that are discarded due to overflow.   + InRangeLength: Packets with lengths ranging from 46 bytes to 1500 bytes, excluding other format errors.   + Alignment: Packets longer than 64 bytes and less than 1518 bytes and that contains the CRC error.   + Fragment: Packets less than the minimum packet length and that contain the CRC error.   + Undersized Frame: Short packets less than the minimum packet length.   + RxPause: Received Pause packets. |
| Output peak rate | Maximum average rate at which packets were sent during all statistical intervals. During each statistical interval, packets are sent at a specific rate.  You can run the set flow-stat interval command to change the interval at which traffic statistics are collected. The value is an integer ranging from 10 to 600, in seconds. It must be an integer multiple of 10.  The default interval is 300 seconds. |
| Output | Total number and total bytes of sent packets on an interface. Packets include correct packets (unicast, broadcast, multicast packets and JumboOctets), incorrect packets, and dropped packets.   * XXXX bytes, XXXX packets: number of correctly sent packets and bytes. The number of sent packets is the sum of the sent unicast, broadcast, and multicast packets. * Number of correctly sent packets of the following types:   + Unicast.   + Multicast.   + Broadcast. * Number of sent incorrect packets and dropped packets of the following types:   + Lost: Lost packets.   + Overflow: Packets that are discarded due to overflow.   + Underrun: Half packets.   + System: Packets when system error occurs.   + Overruns: Packets that are discarded due to overflow.   + TxPause: Sent Pause packets. |
| Description | Description of the interface. A maximum of 242 case-sensitive characters (including spaces) can be entered. The description helps you learn about the interface function.  If no description is configured for the interface using the description command, nothing is displayed by default. |
| ifindex | Index of the interface. |
| The Maximum Transmit Unit is | Maximum transmission unit (MTU) of an interface. |