Configuration Precautions for NTP
=================================

Configuration Precautions for NTP

#### Licensing Requirements

NTP is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode) |
| CE8800 series | CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The NTP protocol version of the device ranges from V1 to V4. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| For security purposes, you are advised not to use the weak security algorithm provided by this feature. By default, the device provides the weak security algorithm feature package WEAKEA. If the weak security algorithm is required, run the install feature-software WEAKEA command to install the weak security algorithm feature package WEAKEA. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| 1. The existing configuration will not be deleted when the NTP service is disabled.  2. Currently, each device can be configured with a maximum of 256 multicast servers, peers, unicast servers, 1024 NTP authentication keys, and 1024 multicast clients. A maximum of 256 multicast clients can take effect simultaneously.  3. A device running NTP supports a maximum of 256 sessions at the same time, including static and dynamic sessions. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |