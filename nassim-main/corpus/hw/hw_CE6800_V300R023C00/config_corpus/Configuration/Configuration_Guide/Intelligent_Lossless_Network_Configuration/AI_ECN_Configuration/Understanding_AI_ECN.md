Understanding AI ECN
====================

Understanding AI ECN

#### Context

The device measures the buffer usage of queues based on the buffer threshold. To implement traffic control and reduce buffer congestion for lossless queues, you can configure two types of buffer thresholds â PFC and ECN â for lossless queues. PFC thresholds are buffer thresholds for a queue in the inbound direction, while ECN thresholds are those for a queue in the outbound direction. In most cases, if congestion does not occur in the outbound direction, it rarely occurs in the inbound direction. As packets are forwarded immediately once they arrive, ECN thresholds can be triggered first to instruct the sender to reduce the packet sending rate when congestion occurs. In this way, congestion is relieved and PFC is not triggered too many times.

The following uses [Figure 1](#EN-US_CONCEPT_0000001512832674__fig81981321163711) as an example to describe the functions of PFC and ECN thresholds.

**Figure 1** Relieving congestion using PFC and ECN thresholds  
![](figure/en-us_image_0000001563752569.png)

1. When congestion occurs in a lossless queue of the device and the used buffer size of the queue exceeds an ECN threshold, the device performs ECN marking for forwarded packets (setting the ECN field to 11).
2. After receiving the ECN-marked packets, the server sends CNPs to the client. Upon receipt of the CNPs, the client reduces the packet sending rate.
3. If the lossless queue on the device is further congested and the used buffer size of the queue exceeds the threshold for triggering PFC frames, the device sends PFC notification packets to the client. After receiving the PFC notification packets, the client stops sending packets in the corresponding priority queue.
4. When the congestion in the lossless queue on the device is relieved and the used buffer size of the queue is lower than the threshold for stopping PFC frames, the device sends PFC stop packets to the client. After receiving the PFC stop packets, the client continues to send packets in the corresponding priority queue.

![](public_sys-resources/note_3.0-en-us.png) 

The PFC threshold described in this section refers to the threshold for triggering PFC frames (PFC-XOFF). The threshold for stopping PFC frames (PFC-XON) is not discussed in this section. The value of PFC-XON must be lower than that of PFC-XOFF to ensure that PFC is stopped after the occupied buffer space is reduced (congestion is relieved).

The preceding process shows that after the device has detected congestion in the queue and performed ECN marking, a certain amount of time is required for the client to become aware of network congestion and reduce the packet sending rate. During this period, the client still sends traffic to the device at the original packet sending rate. As a result, congestion in the queue buffer of the device deteriorates, and the client stops sending traffic when PFC is triggered. To prevent PFC from being triggered, proper ECN thresholds need to be set so that the buffer gap between ECN and PFC thresholds can accommodate the traffic sent by the client during the period between ECN marking on the device and rate decrease of the client.

In addition, there are both delay-sensitive mice flows and throughput-sensitive elephant flows on the network. When setting ECN thresholds, pay attention to the following points:

* When high ECN thresholds are set, ECN marking can be delayed. This ensures the traffic sending rate and the buffer space for storing burst traffic in a queue, meeting the bandwidth requirement of throughput-sensitive elephant flows. However, when congestion occurs in a queue, packets are queued in the buffer space, leading to a long queue delay which is not beneficial to delay-sensitive mice flows.
* When low ECN thresholds are set, ECN marking is triggered as soon as possible to instruct the client to reduce the packet sending rate. This ensures a low buffer depth, reduces packet queuing, and lowers the queue delay, which is beneficial to delay-sensitive mice flows. However, a low ECN threshold affects throughput-sensitive elephant flows by limiting their bandwidth and cannot ensure high throughput for elephant flows.

ECN thresholds in the static ECN function are configured manually. For lossless services that require lossless transmission, fixed ECN thresholds cannot adapt to the changing buffer space in a queue. As such, the static ECN function cannot prevent PFC from being triggered while meeting bandwidth requirements of both delay-sensitive mice flows and throughput-sensitive elephant flows.

The AI ECN function can solve the preceding problems. Using intelligent algorithms, the AI ECN function for lossless queues enables the device to perform AI training based on the traffic model on the live network, predict network traffic changes, and adjust ECN thresholds based on traffic characteristics such as the queue length. In this way, the lossless queue buffer is accurately managed and controlled, ensuring the optimal performance across the entire network.


#### Implementation

As shown in [Figure 2](#EN-US_CONCEPT_0000001512832674__fig_dc_cfg_low-latency_000701), the device collects traffic characteristics on the live network and sends them to the AI ECN component. The AI ECN component intelligently sets the optimal ECN thresholds for lossless queues based on the inference result of the Embedded Artificial Intelligence (EAI) system to ensure low delay and high throughput of lossless queues. In this way, the optimal performance of lossless services can be achieved in different traffic scenarios.

**Figure 2** Implementation of the AI ECN function for lossless queues  
![](figure/en-us_image_0000001512673074.png)

1. The forwarding component on the device collects traffic characteristics such as the queue buffer usage, bandwidth throughput, and current ECN thresholds, and uses telemetry to push the real-time network traffic status to the AI ECN component.
2. After the AI ECN function is enabled, the AI ECN component automatically subscribes to services of the EAI system. After receiving the pushed network traffic status information, the AI ECN component intelligently determines the current traffic model and identifies whether the current network traffic scenario is a known scenario based on the EAI system.
   * If the traffic model is a trained model in the EAI system, the AI ECN component determines that the current network traffic scenario is a known scenario. The AI ECN component then calculates the ECN thresholds that match the current network status based on the optimal inference result of the EAI system. This mode is called the model inference mode. Because this mode uses the Neural Network (NN) algorithm, it is also called the NN mode.
   * If the traffic model is not a trained model in the EAI system, the AI ECN component determines that the current network traffic scenario is an unknown scenario. The AI ECN component then uses the heuristic search algorithm to continuously correct the current ECN thresholds in real time based on the live network status, ensuring high bandwidth and low delay. Finally, the optimal ECN thresholds are obtained. This mode is called the heuristic inference mode. Because this mode uses Bottleneck Bandwidth and Round-trip propagation time (BBR) algorithm, it is also called the BBR mode.
3. The AI ECN component delivers the optimal ECN threshold configuration to the device, and the device adjusts the ECN thresholds of lossless queues accordingly.
4. The device performs the preceding operations for new traffic status to ensure optimal performance of lossless services.