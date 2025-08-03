PFC
===

PFC

#### Context

The Ethernet Pause mechanism ensures lossless transmission. When a downstream device detects that its receive capability is lower than the transmit capability of its upstream device, it sends Pause frames to the upstream device, requesting the upstream device to stop sending traffic for a period of time. The drawback, however, is that it stops all traffic on a link (for the entire interface). This in turn affects link sharing, which is critical to actual services. Link sharing requires:

* Burst traffic of one type cannot affect forwarding of other types of traffic.
* A large amount of one type of traffic in a queue cannot occupy buffer resources of other types.

PFC addresses the conflict between Ethernet Pause and link sharing.


#### Fundamentals

PFC, also called Per Priority Pause or Class Based Flow Control (CBFC), enhances Ethernet Pause. PFC is a kind of priority-based flow control mechanism. As shown in [Figure 1](#EN-US_CONCEPT_0000001564008733__en-us_concept_0000001563749997_fig_dc_fd_dcb_000401), eight priority queues on the transmit interface of DeviceA correspond to eight receive buffers on the receive interface of DeviceB. When a receive buffer on DeviceB is congested, DeviceB sends a backpressure signal "STOP" to DeviceA, requesting DeviceA to stop sending packets in the corresponding priority queue.

**Figure 1** PFC working mechanism  
![](figure/en-us_image_0000001512830130.png)
A backpressure signal is an Ethernet frame, and its format is shown in [Figure 2](#EN-US_CONCEPT_0000001564008733__en-us_concept_0000001563749997_fig_dc_fd_dcb_000402).**Figure 2** PFC frame format  
![](figure/en-us_image_0000001563869657.png)

**Table 1** Fields in a PFC frame
| Field | Description |
| --- | --- |
| Destination address | Destination MAC address, which has a fixed value of 01-80-c2-00-00-01. |
| Source address | Source MAC address. |
| Ethertype | Ethernet frame type. The value is 88-08. |
| Control opcode | Control code. The value is 01-01. |
| Priority enable vector | Priority-enable vector.  E(*n*) corresponds to queue *n* and determines whether backpressure is enabled for queue *n*. When E(*n*) is 1, backpressure is enabled for queue *n* and the backpressure time is Time(*n*). When E(*n*) is 0, backpressure is disabled for queue *n*. |
| Time(0) to Time(7) | Backpressure timer.  If Time(*n*) is 0, backpressure is canceled. |
| Pad(transmit as zero) | Reserved.  The value is 0 during PFC frame transmission. |
| CRC | Cyclic Redundancy Check. |


When receiving backpressure signals, a device stops only traffic in one or several priority queues, but not on the entire interface. What's more, PFC can pause or restart any queue, without interrupting traffic in other queues. This feature enables traffic of various types to share one link. For priority queues with PFC disabled, the system does not apply the backpressure mechanism. Instead, it directly discards packets in these queues when congestion occurs.