ECN Fundamentals
================

ECN Fundamentals

#### Context

Explicit Congestion Notification (ECN), also known as the static ECN function, is an extension of WRED. When the number of packets in the forwarding queue exceeds the ECN threshold, the ECN-enabled device sends a packet tagged with the ECN field to the destination server to notify it of congestion on the network. After receiving the packet, the destination server sends a Congestion Notification Packet (CNP) to instruct the source server to reduce the traffic rate.

In [Figure 1](#EN-US_CONCEPT_0000001512675206__fig_dc_cfg_low-latency_000501), when a packet enters a queue, traditional ECN allows the device to determine whether the buffer used by the queue exceeds the ECN threshold. If so, the device tags the packet with the ECN field value of 11. The time that the destination server takes to receive this packet is the packet forwarding time in the device queue (the time from adding the ECN field to the packet to forwarding the tagged packet to the device) plus the time taken to forward the tagged packet on the network. If there is severe network congestion, the traditional mode may exacerbate queue congestion. In extreme cases, the entire network may stop sending packets due to Priority-based Flow Control (PFC).

**Figure 1** Traditional ECN  
![](figure/en-us_image_0000001563994621.png "Click to enlarge")

Fast ECN is developed to overcome these shortcomings. It allows the device to tag a packet with the ECN field when it leaves the queue, as opposed to when the packet enters the queue. This shortens the time from adding the ECN field to the packet to forwarding the tagged packet to the device.


#### Implementation

As mentioned, fast ECN allows a device to tag a packet with the ECN field when it leaves the queue. When a packet leaves a queue, the device determines whether the buffer used by the queue exceeds the ECN threshold. If so, the packet is tagged with the ECN field value of 11. The device tags a packet with the ECN field when forwarding the packet out, shortening the time taken to forward the packet, and ensuring the destination server receives the tagged packet with the least delay possible.

**Figure 2** Fast ECN  
![](figure/en-us_image_0000001513034390.png "Click to enlarge")

Currently, the device supports fast ECN.