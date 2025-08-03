Configuration Precautions for Traffic Shaping
=============================================

Configuration Precautions for Traffic Shaping

#### Licensing Requirements

Traffic shaping is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| When two buckets are configured for a queue, the error is as follows:  If the packet size is greater than or equal to 256 bytes and the CIR/PIR ratio is greater than 10%, the maximum error is 5%. If the CIR/PIR ratio is less than 10%, the maximum error is 20%.  If the packet size is smaller than 256 bytes and the CIR/PIR ratio is greater than 41%, the maximum error is 5%. If the CIR/PIR ratio is smaller than 41%, the maximum error is 50%.  Note: The CIR/PIR ratio is the configured ratio of the CIR to the PIR. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| In addition to forwarded packets, the following packets are also counted in port queue statistics:  1. Packets discarded during PFC deadlock recovery  2. Packets pruned or discarded by the egress NP  3. Packets marked with the discard flag by EOP in cut-through mode | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| The CBS value cannot be specified for interface-based rate limiting. The device automatically configures the recommended CBS value of the chip based on the rate limit.  If the rate limit is less than 50 Gbit/s, the CBS is 4 KBytes.  If the rate limit is greater than 50 Gbit/s and less than 100 Gbit/s, the CBS is 8 KBytes.  If the rate limit is greater than 100 Gbit/s and less than 200 Gbit/s, the CBS is 16 KBytes.  If the rate limit is greater than 200 Gbit/s and less than 400 Gbit/s, the CBS is 32 KBytes.  If the rate limit is greater than 400 Gbit/s and less than 800 Gbit/s, the CBS is 64 KBytes.  If the rate limit is greater than 800 Gbit/s and less than 1000 Gbit/s, the CBS is 80 KBytes. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-LL-56F (low latency mode)/CE6885-SAN-56F  CE8855-32CQ4BQ/CE8851-32CQ4BQ |