Configuration Precautions for CLI-based Device Login
====================================================

Configuration Precautions for CLI-based Device Login

#### Licensing Requirements

CLI-based Device Login is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode) |
| CE8800 series | CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature | Feature Requirements | Series | Models |
| --- | --- | --- | --- |
| Telnet | Only the primary IP address can be configured as the Telnet source address. The virtual IP address cannot be configured. If packets need to be restricted based on virtual IP addresses, you can configure a source IP address and an ACL to restrict the packets. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| Telnet | Telnet is not recommended for security purposes.  By default, the device provides the weak security algorithm/protocol feature package WEAKEA. If you need to use the weak security algorithm/protocol feature package WEAKEA, run the install feature-software WEAKEA command to install it. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |