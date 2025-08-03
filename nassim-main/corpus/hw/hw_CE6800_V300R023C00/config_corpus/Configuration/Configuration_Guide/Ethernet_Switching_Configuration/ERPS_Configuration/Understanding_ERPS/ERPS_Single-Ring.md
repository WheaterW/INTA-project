ERPS Single-Ring
================

ERPS is a standard ring network protocol used to prevent loops on an ERPS ring at the Ethernet link layer. To prevent loops on an ERPS ring, you can enable the loop prevention mechanism to block the RPL owner port to eliminate loops. If a link on the ring network fails, the device running ERPS immediately unblocks the blocked port and performs link protection switching to restore communication between nodes on the ring network. In an ERPS single-ring scenario, only one ERPS ring is configured on an ERPS network. Both ERPSv1 and ERPSv2 support ERPS single-ring.

This section describes how ERPS is implemented on a single-ring network when links are normal, when a link fails, and when the link recovers (including protection switching operations).

#### Normal Links

In [Figure 1](#EN-US_CONCEPT_0000001141938798__fig_dc_fd_erps_000501), DeviceA through DeviceE constitute a ring and can communicate with each other.

1. To prevent loops, ERPS blocks the RPL owner port and also the RPL neighbour port (if any). Other ports can forward service traffic.
2. The RPL owner port on the ERPS ring sends R-APS NRRB messages to other nodes on the ring at an interval of 5s, indicating that ERPS links are normal.

**Figure 1** ERPS single-ring networking (normal links)  
![](figure/en-us_image_0000001216615190.png)

#### Link Fault

In [Figure 2](#EN-US_CONCEPT_0000001141938798__fig_dc_fd_erps_000502), if the link between DeviceD and DeviceE fails, the ERPS protection switching mechanism is triggered. The ports on both ends of the faulty link are blocked, and the RPL owner port and RPL neighbour port are unblocked to send and receive user traffic, ensuring uninterrupted traffic forwarding. The detailed process is as follows:

1. After DeviceD and DeviceE detect the link fault, they block their ports on the faulty link and update their FDB entries.
2. DeviceD and DeviceE send three consecutive R-APS SF messages carrying local link fault information to the other devices and then send R-APS SF messages at an interval of 5s.
3. After receiving R-APS SF messages, the other devices update their FDB entries. After receiving R-APS SF messages, DeviceC (where the RPL owner port resides) unblocks the RPL owner port and updates its FDB entries. Similarly, after receiving R-APS SF messages, DeviceB (where the RPL neighbour port resides) unblocks the RPL neighbour port and updates its FDB entries.

**Figure 2** ERPS single-ring networking (link fault)  
![](figure/en-us_image_0000001261447981.png)

#### Link Recovery

After the faulty link recovers, if the ERPS ring uses the revertive switching mode, the device where the RPL owner port resides blocks the RPL again, and the link that has recovered is used to forward traffic. If the ERPS ring uses the non-revertive switching mode, the link that has recovered is still blocked, and the RPL is not blocked. The following uses the revertive switching mode as an example to describe the recovery process:

1. After the link between DeviceD and DeviceE recovers, DeviceD and DeviceE start the Guard timer to prevent them from receiving out-of-date R-APS NR messages. They do not receive any R-APS NR messages before the Guard timer expires. At the same time, DeviceD and DeviceE send R-APS NR messages.
2. After receiving R-APS NR messages, DeviceC on which the RPL owner port resides starts the WTR timer. After the WTR timer expires, DeviceC blocks the RPL owner port and sends R-APS NRRB messages.
3. After receiving R-APS NRRB messages from DeviceC, DeviceD and DeviceE unblock their blocked ports, stop sending R-APS NR messages, and update their FDB entries. After receiving R-APS NRRB messages from DeviceC, the other devices update their FDB entries.