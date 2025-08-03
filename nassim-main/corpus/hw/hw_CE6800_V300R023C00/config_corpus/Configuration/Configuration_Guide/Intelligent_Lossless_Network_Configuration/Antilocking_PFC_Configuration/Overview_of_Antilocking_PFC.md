Overview of Antilocking PFC
===========================

Overview of Antilocking PFC

#### Definition

Antilocking Priority-based Flow Control (PFC) is a type of PFC technology that enables a device to periodically scan the buffer usage of priority queues on an interface, and then send PFC frames to the upstream device to control the period during which the upstream device stops sending traffic. This allows the device to constantly adjust when traffic is being sent or paused.


#### Purpose

In a long-distance Data Center Interconnect (DCI) scenario, the ingress devices of the two data centers are far away from each other. If buffer congestion occurs on one device, this device must have sufficient buffer space to absorb the traffic sent from the peer device until it stops receiving traffic from the peer device after having sent a PFC frame to the said peer. This ensures lossless transmission over a long distance. Under the same buffer size and bandwidth conditions, antilocking PFC applies to longer-distance lossless transmission than traditional PFC, as antilocking PFC offers a mechanism of continuously adjusting the sending and pausing of a small amount of traffic at a high frequency within a short period.