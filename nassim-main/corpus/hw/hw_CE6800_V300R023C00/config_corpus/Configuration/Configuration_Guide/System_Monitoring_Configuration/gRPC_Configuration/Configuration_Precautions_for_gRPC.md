Configuration Precautions for gRPC
==================================

Configuration Precautions for gRPC

#### Licensing Requirements

gRPC is not under license control.


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
| 1. In dial-in mode, the subscription is automatically canceled after the server is disconnected.  2. The gRPC server supports subscription based on IPv4 and IPv6 addresses, and IPv4 and IPv6 gRPC servers can co-exist.  3. The gRPC client supports subscription based on IPv4 and IPv6 addresses, and IPv4 and IPv6 gRPC clients can co-exist.  4. After the collector is disconnected from the device, the collector reconnects to the device every 30 seconds. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| 1. If the weak security protocol feature package is not installed and no SSL policy is bound to the gRPC server, the gRPC service cannot be enabled on the device.  2. If the weak security protocol feature package is installed and no SSL policy is bound to the gRPC server, the gRPC service function can be enabled on the device.  3. If the gRPC service is enabled on the device but no SSL policy is bound, the weak security protocol feature package cannot be uninstalled.  4. For security purposes, you are not advised to use weak security protocols.  5. By default, the device provides the weak security protocol feature package WEAKEA. If you need to use it, run the install feature-software WEAKEA command to install the weak security protocol feature package WEAKEA. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |