Overview of Buffer Optimization
===============================

Overview of Buffer Optimization

#### Definition

Buffer optimization provides a series of technologies that can optimize buffer allocation in a device.


#### Purpose

Priority-based Flow Control (PFC) is a flow control technology that effectively prevents packet loss. A PFC-enabled queue is called a lossless queue. When congestion occurs in such a queue on a downstream device, the downstream device sends a PFC notification packet to the upstream device. The upstream device then stops sending packets in the queue, ensuring lossless transmission of packets.

However, as the service scale expands, the communication distance between network devices increases accordingly. For example, in a Data Center Interconnect (DCI) scenario, the communication distance may reach 100 km, and therefore requires a longer amount of time for transmitting a PFC notification packet between network devices. If a device does not have sufficient buffer to store packets that are received between the time when a queue sends a PFC notification packet and the time when the upstream device stops sending packets, packet loss occurs. In addition, for large-scale services, the many-to-one incast traffic model is often used, which may lead to burst traffic. This can also cause packet loss to occur if the device does not have sufficient buffer to store burst traffic.

To overcome these challenges, the intelligent lossless network supports buffer optimization, which optimizes the buffer space based on actual service scenarios to fully ensure lossless packet forwarding of lossless queues.