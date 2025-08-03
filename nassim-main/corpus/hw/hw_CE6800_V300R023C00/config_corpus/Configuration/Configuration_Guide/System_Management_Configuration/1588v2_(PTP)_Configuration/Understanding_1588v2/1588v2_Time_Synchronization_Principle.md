1588v2 Time Synchronization Principle
=====================================

The principle of 1588v2 time synchronization is the same as that of NTP time synchronization. The master and slave nodes exchange timing packets, and calculate the packet transmission delays in both directions (sending and receiving) according to the receiving and sending timestamps in the exchanged timing packets. If the packet transmission delays in both directions are identical, the unidirectional delay is half the bidirectional delay. On this basis, the time offset between the slave and master nodes can be obtained. The slave node then synchronizes with the master node by correcting its local time according to the time offset. While 1588v2 and NTP have the same principles, they differ in implementation.

* NTP typically runs on main control boards to measure the communication delay, including the link delay and delays caused by various internal processing such as internal congestion queuing, software scheduling, and software processing. These make the packet transmission delay unstable, causing packet transmission delays in two directions to be asymmetric. As a result, the accuracy of NTP-based time synchronization is low.
* Different from NTP, 1588v2 assumes that the link delay is a constant value (or a trivial value that can be ignored between synchronization processes), and that delays in opposite directions on a link are the same. In this case, 1588v2 adds timestamps at the points closest to each end of a link to measure the link delay, achieving the highest possible degree of time synchronization precision.

1588v2 defines two modes for delay measurement and time synchronization:

* Delay mode: measures the end-to-end delay.
* Peer Delay (Pdelay) mode: calculates the transmission time (link delay) between two communication ports that support the Pdelay mechanism. This mechanism is irrelevant to master and slave states of ports.

![](public_sys-resources/note_3.0-en-us.png) 

Currently, the device supports only the Delay mode. The following describes the principles of the Delay mode.


#### Delay Mode

[Figure 1](#EN-US_CONCEPT_0000001563999209__fig_dc_cfg_ptp_000701) shows how 1588v2 calculates the average link delay and time offset between the master and slave devices in Delay mode.

**Figure 1** Delay mode  
![](figure/en-us_image_0000001564119065.png)  

![](public_sys-resources/note_3.0-en-us.png) 

* When a packet arrives at or leaves a device, the device adds a timestamp to the packet based on its system clock.
* In one-step mode, a Sync message in Delay mode carries the timestamp indicating when the message was sent.
* In two-step mode, a Sync message in Delay mode does not carry the timestamp indicating when the message was sent. The device records the time when the Sync message is sent, and sends a subsequent Follow\_Up message that carries the timestamp indicating when the Sync message was sent.

1. The master device sends a Sync message at t1. If the master device works in one-step mode, t1 is sent to the slave device through the Sync message. If the master device works in two-step mode, t1 is sent to the slave device through the subsequent Follow\_Up message.
2. In one-step mode, the slave device receives the Sync message at t2 and obtains t1 from the Sync message. In two-step mode, the slave device receives the Sync message at t2 and obtains t1 from the Follow\_Up message.
3. The slave device sends a Delay\_Req message to the master device at t3.
4. The master device receives the Delay\_Req message at t4.
5. The master device then sends a Delay\_Resp message carrying t4 to the slave device.

According to the four timestamps t1, t2, t3, and t4 , the slave device can calculate the average link delay and time offset between itself and the master device to synchronize its time with the master device. The calculation process is as follows:

1. Assume that the time delay for sending packets from the master device to the slave device is Delayms, the time delay for sending packets from the slave device to the master device is Delaysm, and the time offset between the slave and master devices is Offset. The formula for the average link delay between the master and slave devices is: Delay = (Delayms + Delaysm)/2.
2. Because t2 â t1 = Delayms + Offset and t4 â t3 = Delaysm â Offset, (t2 â t1) â (t4 â t3) = (Delayms + Offset) â (Delaysm â Offset).
3. According to the preceding formula:
   * Delayms + Delaysm = (t2 â t1) + (t4 â t3)
   * Offset = [(t2 â t1) â (t4 â t3) â (Delayms â Delaysm)]/2
4. If bidirectional link delays between the master and slave devices are symmetric or Delayms equals Delaysm, the following formulas can be used to calculate the average link delay and time offset between the two devices:
   * Delay = [(t2 â t1) + (t4 â t3)]/2
   * Offset = [(t2 â t1) â (t4 â t3)]/2

In [Figure 2](#EN-US_CONCEPT_0000001563999209__fig_dc_cfg_ptp_000702), the time offset between the local clock and current time is calculated using 1588v2, and then the local clock is adjusted based on the time offset. This synchronization process is performed repeatedly to ensure time synchronization between the slave and master devices.

**Figure 2** Time correction  
![](figure/en-us_image_0000001563878957.png)  

1588v2 time synchronization requires symmetric bidirectional path delays between the master and slave devices. If bidirectional path delays are asymmetric, a synchronization offset is introduced. The offset is half of the difference between bidirectional path delays. 1588v2 high-precision time synchronization requires that the delay between the two nodes be stable and no jitter occur. Generally, the link delay can achieve the required results, but the forwarding delay and jitter of the device can be large. Therefore, in IEEE 1588v2, the correctionField field indicating delay correction must be introduced to calculations in Delay mode in order to obtain the correct average link delay (Delay) and time offset (Offset).

**Figure 3** Forwarding delay correction process  
![](figure/en-us_image_0000001512679826.png)

As shown in [Figure 3](#EN-US_CONCEPT_0000001563999209__fig8507135013461), the device modifies the correctionField field of a 1588v2 message on the inbound and outbound interfaces. Specifically, the device subtracts the timestamp indicating when the 1588v2 message was received on the inbound interface and adds the timestamp indicating when the 1588v2 message was sent from the outbound interface. As such, the forwarding delays of the 1588v2 message on the device are added to the correctionField field. In IEEE 1588v2, the process of calculating the average link delay by using the Delay mechanism that uses forwarding delay correction is as follows:

1. The master node sends a Sync message to the slave node. The message carries the correctionField CF1 containing the forwarding delay generated when the message passes through the master node. When the slave node receives the Sync message and performs time synchronization calculation, it subtracts the CF1. There is only the link delay.![](public_sys-resources/note_3.0-en-us.png) 
   
   In two-step mode, the slave node also needs to deduct the value of the correctionField field from the Follow\_Up message during time synchronization calculation.
2. The slave node sends a Delay\_Req message to the master node. The message carries the correctionField field containing the forwarding delay of the slave node.
3. After receiving the Delay\_Req message, the master node calculates a new correctionField and adds the correctionField value in the Delay\_Req message to the new correctionField field to form CF2.
4. The master node sends a Delay\_Resp message carrying CF2 to the slave node.
5. After receiving the Delay\_Resp message, the slave node performs time synchronization calculation and subtracts the correctionField value containing the forwarding delay. The correct Delay and Offset values can then be obtained as follows:
   * Delay = [(t2 â t1 â CF1) + (t4 â t3 â CF2)]/2 = [(t2 â t1) + (t4 â t3) â (CF1+CF2)]/2
   * Offset = [(t2 â t1 â CF1) â (t4 â t3 â CF2)]/2 = [(t2 â t1) â (t4 â t3) â (CF1â CF2)]/2

In this way, high-precision time synchronization can be implemented.


#### Asymmetrical Delay Correction

1588v2 requires bidirectional delays of a link to be symmetric. In real-world scenarios, however, bidirectional delays of a link may be asymmetric. Asymmetric delays may be caused by link attributes or device attributes, for example, bidirectional link delays are different on the link segment from the location of a timestamp to the link. To address this issue, 1588v2 provides the asymmetric delay correction mechanism. [Figure 4](#EN-US_CONCEPT_0000001563999209__fig_dc_cfg_ptp_000704) shows this mechanism.

**Figure 4** Asymmetric delay correction mechanism  
![](figure/en-us_image_0000001512679814.png)

Generally, tms equals tsm. If tms does not equal tsm, you can configure their time difference as the asymmetric delay correction value as long as the delay difference is fixed and can be obtained in advance. During time synchronization, 1588v2 also calculates the asymmetrical delay correction value, improving time synchronization accuracy on links with asymmetric delays.