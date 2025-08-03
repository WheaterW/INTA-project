Overview of Differentiated Flow Scheduling
==========================================

Overview of Differentiated Flow Scheduling

#### Definition

Differentiated flow scheduling is a technology that schedules elephant and mice flows with the same 5-tuple.


#### Purpose

A flow on the network is a sequence of packets from a source host to a destination host. Each flow is uniquely identified by canonical 5-tuple: source IP address, destination IP address, source port, destination port, and protocol. Traffic flows on most networks are bimodal, consisting of both elephant flows and mice flows.

* Mice flows are flows with a small number of protocol packets (such as packets used to establish connections) transmitted at a low rate. They are sensitive to both latency and packet loss.
* Elephant flows carry a large number of data packets transmitted at a high rate. Such flows aim to achieve high throughput performance and are highly tolerant to packet loss.

Clearly, elephant and mice flows have different requirements for forwarding performance. However, packets from flows with the same 5-tuple are put in the same queue, and as such are subject to the same first-in-first-out (FIFO) scheduling. This means that when congestion occurs in a queue, mice flows are hindered by elephant flows in the buffer space of the queue, leading to significantly longer forwarding latency. In extreme cases, elephant flows may even consume the entire buffer space of the queue, resulting in packets being dropped from mice flows that are unable to enter the queue.

To address this issue, the intelligent lossless network provides differentiated flow scheduling. With this function enabled, a device can identify elephant and mice flows with the same 5-tuple, put them in different queues, and preferentially schedule packets in mice flows to ensure the forwarding performance of such flows. The following figure illustrates how differentiated flow scheduling works.

1. On the inbound interface, the device groups the packets with the same 5-tuple forwarded by a differentiated flow scheduling-enabled queue in the same flow. In differentiated flow scheduling, for the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855, the first N packets in a flow are identified as a mice flow, and the remaining packets are identified as an elephant flow. This is because protocol packets are mostly sent before data packets; for the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, small packets transmitted at a low rate are identified as a mice flow, and large packets transmitted at a high rate are identified as an elephant flow.
2. On the outbound interface, the device automatically schedules the identified mice flow to a high-priority queue for forwarding. The elephant flow is still forwarded in the queue with the original priority.

**Figure 1** Implementation of differentiated flow scheduling (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855)  
![](figure/en-us_image_0000001512840378.png)
**Figure 2** Implementation of differentiated flow scheduling (CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S)  
![](figure/en-us_image_0000001513159930.png)