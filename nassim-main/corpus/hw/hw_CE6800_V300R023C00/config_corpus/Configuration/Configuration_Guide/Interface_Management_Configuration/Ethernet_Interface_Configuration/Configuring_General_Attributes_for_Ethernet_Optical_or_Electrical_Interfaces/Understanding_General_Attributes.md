Understanding General Attributes
================================

Understanding General Attributes

#### Interface Rate

In auto-negotiation mode, interfaces at both ends of a link negotiate an interface rate. If the automatically negotiated interface rate does not meet requirements or the peer device does not support auto-negotiation, you need to manually set an interface rate in non-auto-negotiation mode. The interface rates set on both ends of a link must be the same.


#### Interface IFG

The inter-frame gap (IFG) is used to differentiate two Ethernet frames, as shown in [Figure 1](#Ethernet_Interface_other1__fig_dc_cfg_int_003401). It can affect the packet forwarding capability on an interface.

The packet forwarding capability, also called interface throughput, refers to the data forwarding capability on an interface, which is expressed in packets per second (pps). The packet forwarding capability is calculated based on the number of 64-byte data packets (smallest packets) sent in a certain period. During calculation, the lengths of the preamble and IFG must be taken into account.

It is recommended that the default IFG of 12 bytes is used. If you set the IFG to a smaller value, after receiving one data frame, a device may not be well prepared to receive the next one. This could result in frame loss. If the length of a data frame to be sent is too large, it is recommended that you change the IFG to 16 bytes.

**Figure 1** IFG  
![](figure/en-us_image_0000001513041014.png "Click to enlarge")

#### Traffic Statistics Collection

You can check the running status and traffic statistics of an interface by running the **display interface** command. The **Last 300 seconds input rate** and **Last 300 seconds output rate** fields in the command output indicate the inbound and outbound traffic rates on the interface in the last 300 seconds.

* To obtain the total number of bytes (including the number of packet bytes and the fixed lengths of the IFG and preamble) passing through an interface per second, configure collection of traffic statistics that include the IFG and preamble. The interface's traffic rate is then calculated as follows: Interface's traffic rate = (Original packet length + IFG length + Preamble length) x Number of packets passing through the interface per second
* To obtain only the number of packet bytes (excluding the fixed lengths of the IFG and preamble) passing through an interface per second, configure collection of traffic statistics that exclude the IFG and preamble. The interface's traffic rate is then calculated as follows: Interface's traffic rate = Original packet length x Number of packets passing through the interface per second

#### Jumbo Frame Length Allowed on an Interface

Ethernet frames longer than 1518 bytes and VLAN frames longer than 1522 bytes are called jumbo frames.

When exchanging a large amount of data (for example, when transmitting files), Ethernet interfaces may receive jumbo frames whose length exceeds that of common packets. However, if the length of the received Jumbo frame exceeds the default data frame length, it is directly discarded by the device. To address this issue, you can adjust the jumbo frame length allowed on an interface.

After adjustment, the common Ethernet frame length no longer restricts the allowed packet length limit. In this way, flexible packet forwarding can be achieved. Jumbo frames also improve bandwidth utilization. When transmitting data packets, common Ethernet frames introduce a lot of overheads such as IFGs and headers. In contrast, jumbo frames reduce this number and therefore improve bandwidth utilization.

The jumbo frame lengths allowed on interfaces cannot be set to the maximum value, as extra packet encapsulation must be considered. After an interface receives protocol packets such as VLAN packets, it encapsulates packet headers containing certain bytes to the packets. The length of the outgoing packets then exceeds that of the incoming packets, which may cause packet loss. To prevent this, the packet header length must be considered when you configure the maximum frame length on an interface.


#### Alarm Threshold for Outbound/Inbound Bandwidth Usage

You can configure a threshold for outbound/inbound bandwidth usage. When this threshold is exceeded, an alarm is generated. This helps you to expand bandwidth in advance and prevent service interruptions. For best effect, the threshold must be set to an appropriate value. If it is too high, for example, 95%, you may not have enough time to expand the bandwidth after the alarm is generated, which may cause service interruptions.


#### Alarms for Sudden Traffic Rate Changes on Interfaces

To notify users that the incoming or outgoing traffic rate on an interface suddenly increases or decreases, the device supports hwInputRateChangeOverThresholdNotice or hwOutputRateChangeOverThresholdNotice alarm.


#### Control-Flap

The flapping of routing protocols and other protocols caused by frequent changes of the interface status affects the stability of the whole network. To resolve this problem, you can configure the control-flap function.

![](public_sys-resources/note_3.0-en-us.png) 

Only Layer 3 interfaces support the control-flap function.



#### Fast Detection of Interfaces' Physical Status Changes

An Ethernet interface can be physically up or down. When a local device is connected to a transmission device or deployed on a network requiring high reliability, enable this device to rapidly detect interfaces' physical status changes, so that services can run properly.


#### Fault Detection on an Interface

Fault detection enables a device to set its local interface to down when detecting that the peer interface is down or the involved link signal is weak, or restores its local interface to up when detecting that the peer interface is up or the involved link signal is strong.

If the interface status changes multiple times due to fault detection, the device reports the hwLocalFaultAlarm alarm.


#### Delay to Report an Interface Up Event

An Ethernet interface can be physically up or down. When the physical status of an interface changes, the device where the interface resides notifies upper-layer protocol modules, such as the routing and forwarding modules, of the change to guide packet receiving and forwarding. In addition, the device automatically generates traps and logs to remind users to perform the corresponding operations on physical links. If the interface's physical status changes to up, but the upper-layer protocol modules are not ready for forwarding after the device restarts or a subcard resets, the upper-layer protocol modules cannot properly process the packets sent from the interface. As a result, the negotiation mechanism used in the upper-layer protocols cannot take effect. To address this issue, you can set a delay to report a downstream interface up event only after the upper-layer protocol modules are ready for forwarding.


#### Delay to Report Interfaces' Physical Status Changes

An Ethernet interface can be physically up or down. When the physical status of an interface changes, the device where the interface resides notifies upper-layer protocol modules, such as the routing and forwarding modules, of the change to guide packet receiving and forwarding. In addition, the device automatically generates traps and logs to remind users to perform the corresponding operations on physical links.

After you configure a delay in reporting changes in interfaces' physical status, the device will not detect physical status changes during that delay. After the delay, if the physical status has not resumed its original status, the physical status changes are reported to the device.


#### Link Flapping Causing Interfaces to Enter the Error-Down State

A device sets the status of an interface to error-down when it detects a fault on the interface. An interface in error-down state cannot send or receive packets, and the interface indicator is off. Link flapping is one possible cause of an interface entering the error-down state. To address this issue, link flapping protection shuts down the interfaces whose physical status frequently alternates between up and down, thereby preventing network topologies from frequently changing and affecting user communication. For example, if the physical status of the active link's interface frequently alternates between up and down, services are frequently switched between the active and standby links. This increases the load on the device and may cause service data loss. To prevent this issue, configure link flapping protection on the active link's interface. If this function is configured and the device detects that the physical status of the active link's interface frequently changes, the device shuts down this interface to trigger an active/standby link switchover. The standby link then takes over to steadily transmit services. The link flapping protection function involves the following parameters:

* Number of link flaps: One interface up/down transition is recorded as one link flap.
* Link flapping detection interval: a period during which a device counts the number of link flaps.

If the number of link flaps on an interface reaches a preset threshold within a link flapping interval, a device disables the interface and records its status as **ERROR DOWN(link-flap)**.


#### Threshold for the Number of Received CRC Error Packets that Cause an Interface to Enter the Error-Down State

A device sets the status of an interface to error-down when it detects a fault on the interface. An interface in error-down state cannot send or receive packets, and the interface indicator is off. Receiving excessive CRC error packets is one of the possible causes of an interface entering the Error-Down state. If this function is not enabled, an interface that encounters a fault may be still up, preventing traffic from being switched to a configured backup link. To avoid impact on services, you can configure the interface to enter the error-down state when it receives excessive CRC error packets. When the number of received error packets on the interface exceeds the upper alarm threshold, the device disables the interface and records its status as error-down. Services are then switched to the backup link immediately.