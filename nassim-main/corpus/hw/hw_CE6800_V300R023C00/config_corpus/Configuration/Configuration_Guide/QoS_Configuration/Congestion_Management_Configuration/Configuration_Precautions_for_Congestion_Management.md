Configuration Precautions for Congestion Management
===================================================

Configuration Precautions for Congestion Management

#### Licensing Requirements

Congestion management is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature | Feature Requirements | Series | Models |
| --- | --- | --- | --- |
| Queue scheduling | If the N:1 incast traffic model is used, congestion may occur on the outbound interface. If SP scheduling is used, the forwarding delays of multiple non-congested queues may vary, and the delays of some queues increase. If this occurs, adjust the shaper or PBS to solve the problem. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Queue scheduling | The HPC mode is usually used together with PFC. After the HPC mode is enabled:  1. Only SP scheduling can be used for queues 6 and 7 on the interface.  2. When a single queue among queues 0 to 5 receives PFC frames for a long time, head-of-line (HOL) blocking occurs in queues 0 to 5. As a result, packet loss occurs in these queues because the buffer capability is exceeded.  3. A larger token bucket depth (including multiple thresholds) indicates a longer PFC deadlock detection period and a higher probability of HOL blocking in queues 0 to 5 on the interface. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Buffer Management | In standard and enhanced burst traffic buffering modes, the total buffer sizes are the same but the queue buffer sizes are different in the display qos buffer-usage interface command output. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Buffer Management | In the shared burst traffic buffering mode, low-priority packets may be scheduled before high-priority packets on an interface. For example, in a LAG scenario, if high-priority LACP packets are discarded, the negotiation fails and the LAG goes down. Therefore, the shared burst traffic buffering mode is not recommended. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Buffer Management | For the CE6800 Series:  When the total bandwidth of uplink and horizontal traffic exceeds 600 Gbit/s, undifferentiated packet loss may occur on the uplink interface, affecting protocol and service traffic. | CE6800 series | CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |
| Cut-through | In the following scenario, the device automatically uses the store-and-forward mode, even if the cut-through mode is enabled: Traffic flows in through a low-bandwidth port and out through a high-bandwidth port, and the bandwidth of the high-bandwidth port is two or more times that of the low-bandwidth port (for example, traffic flows in through a 25GE port and out through a 100GE port, or traffic flows in through a 100GE port and out through a 400GE port). | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Cut-through | Queue shaping does not take effect in cut-through mode. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |