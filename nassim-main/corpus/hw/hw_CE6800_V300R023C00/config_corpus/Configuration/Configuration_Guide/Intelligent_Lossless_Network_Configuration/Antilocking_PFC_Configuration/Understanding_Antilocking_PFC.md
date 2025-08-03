Understanding Antilocking PFC
=============================

Understanding Antilocking PFC

#### Traditional PFC

**Stopping the upstream device from sending traffic â traditional PFC procedure**

[Figure 1](#EN-US_CONCEPT_0000001513045306__fig13511427183412) shows how traditional PFC controls the upstream device to stop sending traffic. (BPFC indicates the interface bandwidth, and TPFC indicates the one-way forwarding delay between DeviceA and DeviceB.)

1. When the buffer usage of lossless queues on DeviceA is lower than the threshold for triggering a PFC frame, DeviceB continuously sends traffic to DeviceA. As a result, the buffer usage of lossless queues on DeviceA gradually increases.
2. When the buffer usage of lossless queues on DeviceA exceeds the threshold for triggering a PFC frame, DeviceA sends a PFC frame to instruct DeviceB to stop sending traffic. However, within period TPFC before the PFC frame reaches DeviceB, DeviceB still sends traffic to DeviceA. As a result, the buffer usage of lossless queues on DeviceA keeps increasing.
3. Upon receiving the PFC frame, DeviceB stops sending traffic to DeviceA.
4. Traffic that has been sent from DeviceB is still sent to DeviceA and arrives at DeviceA after period TPFC. The buffer usage of lossless queues on DeviceA keeps increasing during this period.
5. DeviceA stops receiving traffic from DeviceB. The buffer usage of lossless queues on DeviceA reaches the maximum value and then gradually decreases.

To prevent packet loss in DeviceA's lossless queues, the buffer space of these lossless queues still needs to absorb BPFC x 2TPFC traffic received within period 2TPFC after the threshold for triggering a PFC frame is exceeded.

**Figure 1** Stopping the upstream device from sending traffic in PFC  
![](figure/en-us_image_0000001563765645.png)

**Upstream device resuming sending traffic â traditional PFC procedure**

[Figure 2](#EN-US_CONCEPT_0000001513045306__fig13422115314) shows how traditional PFC controls the upstream device to resume sending traffic.

1. When the buffer usage of lossless queues on DeviceA exceeds the threshold for stopping a PFC frame, DeviceB does not send traffic to DeviceA. As a result, the buffer usage of lossless queues on DeviceA gradually decreases.
2. When the buffer usage of lossless queues on DeviceA falls below the threshold for stopping a PFC frame, DeviceA sends a PFC frame to instruct DeviceB to resume sending traffic. However, DeviceB still does not send traffic to DeviceA within period TPFC â until the PFC frame reaches DeviceB. As a result, the buffer usage of lossless queues on DeviceA keeps decreasing.
3. Upon receiving the PFC frame, DeviceB resumes sending traffic to DeviceA.
4. The traffic from DeviceB will reach DeviceA after period TPFC. As a result, the buffer usage of lossless queues on DeviceA continues to decrease within this period.
5. DeviceA starts receiving traffic from DeviceB. The buffer usage of lossless queues on DeviceA reaches the minimum value and then gradually increases.

To ensure that DeviceA's lossless queues have throughput, their buffer usage must be greater than 0 within 2TPFC after the buffer usage falls below the threshold for stopping a PFC frame. Therefore, the threshold for stopping a PFC frame must be at least BPFC x 2TPFC.

During flow control, stop PFC frames after resolving the congestion to ensure reduced buffer usage. This means that the threshold for stopping a PFC frame must be smaller than the threshold for triggering a PFC frame. As such, to ensure zero packet loss and high throughput of lossless queues, the queue buffer size must be at least 2 x (BPFC x 2TPFC).

**Figure 2** Upstream device resuming sending traffic in PFC  
![](figure/en-us_image_0000001513165298.png)

#### Antilocking PFC

Antilocking PFC periodically scans the buffer usage of lossless queues and calculates the duration (tstop) during which the upstream device stops sending traffic in a period of t. When the value of tstop is greater than 0, a PFC frame with a timer is sent to the upstream device, controlling the upstream device to resume sending traffic after tstop expires in the corresponding period. (The duration of a period is t, which is far shorter than the one-way forwarding delay between two devices. The value of tstop is within the range of 0 to t.)

**Figure 3** Working principle of antilocking PFC  
![](figure/en-us_image_0000001563885281.png)

The headroom buffer of a lossless queue is used to store packets received after the queue sends a PFC frame and before the queue stops receiving packets from the upstream device, preventing packets in this period from being discarded. According to the preceding analysis of the traditional PFC mechanism, the threshold for triggering a PFC frame is at least BPFC x 2TPFC, and the headroom buffer size is at least BPFC x 2TPFC. Therefore, the required buffer size is at least 2 x (BPFC x 2TPFC). (BPFC indicates the interface bandwidth, and TPFC indicates the one-way forwarding delay between devices at the two ends.)

Antilocking PFC does not have a threshold for triggering a PFC frame. When the buffer usage exceeds the preset threshold, antilocking PFC starts to take effect. The duration from the time when a PFC frame is sent upon the end of a period to the time when the traffic controlled by the PFC frame is sent to the local device is 2TABS. To ensure that the lossless queues have throughput but no packet loss, the headroom buffer size must be at least BABS x 2TABS; therefore, the required buffer size is at least BABS x 2TABS + threshold. To ensure the maximum distance with the minimum buffer, you are advised to set the threshold to 0. In this case, the buffer occupied by antilocking PFC is about BABS\*2TABS. (BABS indicates the interface bandwidth, and TABS indicates the one-way forwarding delay between devices at the two ends.)

**Figure 4** Comparison between traditional PFC and antilocking PFC in terms of buffer allocation  
![](figure/en-us_image_0000001512845766.png)

Therefore, if the bandwidth and buffer size in traditional PFC are the same as those in antilocking PFC (that is, BPFC = BABS and 2 x (BPFC x 2TPFC) = BABS x 2TABS), TABS is about twice TPFC, meaning that the distance supported by antilocking PFC is about twice that supported in traditional PFC.

Antilocking PFC can continuously control sending and pausing of a small amount of traffic at a high frequency within a short period. Therefore, when the bandwidth and device distance are the same, antilocking PFC occupies much less buffer space than traditional PFC. When the buffer size and bandwidth are the same, antilocking PFC can support longer-distance lossless transmission than traditional PFC.


#### PFC Deadlock Detection for Antilocking PFC

Antilocking PFC uses PFC frames to control traffic, which may cause PFC deadlocks. To detect such deadlocks, antilocking PFC provides the PFC deadlock detection function. After determining that a PFC deadlock occurs, antilocking PFC enters the deadlock recovery process, but it does not support deadlock control. For more details, see "PFC Deadlock Detection" in Configuration Guide > DCN and Network Management Configuration > DCB Configuration.