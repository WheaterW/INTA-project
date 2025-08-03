Configuration Precautions for Congestion Avoidance
==================================================

Configuration Precautions for Congestion Avoidance

#### Licensing Requirements

Congestion avoidance is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In addition to the common upper threshold, lower threshold, and mark probability, the ECN waterline also includes the drop waterline. When the buffer exceeds the waterline, packets are directly discarded to avoid excessive buffer consumption.After the ECN function is enabled, the device automatically sets the drop threshold to ensure that ECN flows are not discarded. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| If ECN, WRED and tail drop (that is, queue length) are configured for a queue, ECN takes effect first, then tail drop, and finally WRED.  The device compares the static threshold configured for WRED or tail drop with the static threshold converted from the global dynamic threshold in the current buffer mode. If the configured static threshold is greater than the static threshold converted from the global dynamic threshold, the global dynamic threshold takes effect. Otherwise, the configured static threshold takes effect.  When a display command is run to query the current buffer, the actual value that takes effect is displayed. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| The global ECN configuration takes precedence over the queue ECN configuration. After the global ECN function is enabled, the ECN policy is applied to all packets whose ECN field is 01/10 (regardless of whether the queue ECN function is enabled).  If ECN is disabled for a queue, the default ECN configuration is used for global ECN marking. If ECN is enabled for a queue, the user-defined ECN profile bound to the queue is used for ECN marking.  After ECN is enabled globally, you need to enable ECN in queues to view ECN flag statistics.  After ECN is enabled globally, WRED-, ECN-, and AI ECN-disabled queues can buffer ECN packets of only 0.5 MB and will discard the excess ECN packets when congestion occurs in these queues.  It is recommended that this feature be used only in lossless scenarios. To use this function in lossless and lossy scenarios, disable the ECN marking function for lossy traffic (set the ECN field of packets to 00). | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| When the ECN threshold is greater than or equal to the tail drop threshold, the ECN field of packets is not marked and some packets are discarded.  When the ECN function is used, the ECN threshold needs to be set to a value less than the tail drop threshold. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| The ECN function cannot be configured for queues 6 and 7 on an interface using the qos queue <queue-index> ecn command. That is, the ECN function can be configured for queues 0 to 5. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| After ECN is enabled globally, WRED cannot be configured for queue 6 and queue 7. After WRED is configured for queue 6 or queue 7, ECN cannot be enabled globally. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Congestion avoidance takes effect only for known unicast packets. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| When multiple interfaces send traffic to one interface, if the burst traffic exceeds the maximum buffer, the device discards the excess packets. If a large amount of burst traffic exists and multiple interfaces need to send traffic to one interface, run the qos burst-mode command to set the burst traffic buffering mode to non-standard mode. This configuration improves the device's capability to forward burst traffic. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| In the following scenarios, ECN may not be triggered and does not take effect when a queue is congested:  1. The ECN threshold is too high.  2. The queue buffer threshold is too low. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |