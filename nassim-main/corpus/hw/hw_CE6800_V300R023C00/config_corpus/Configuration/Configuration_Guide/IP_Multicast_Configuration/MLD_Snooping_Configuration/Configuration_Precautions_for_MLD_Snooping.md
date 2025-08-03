Configuration Precautions for MLD Snooping
==========================================

Configuration Precautions for MLD Snooping

#### Licensing Requirements

MLD snooping is a basic function included in the basic software function license. The basic software function license has been installed and activated before delivery. You do not need to manually activate it.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K |
| CE8800 series | CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| MLDv1 Join messages are reported as traffic. The protocol considers that the source is active and marks the ACT flag in multicast routing entries.  MLDv1 Done messages are also reported as traffic. After receiving an MLDv1 Done message, the device deletes only the multicast outbound interface entry. The device deletes the multicast group entry only after the multicast aging time expires. | CE6800 series  CE8800 series | CE6855-48XS8CQ/CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-LL-56F (standard forwarding mode)/CE6885-48YS8CQ-T/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8855-32CQ4BQ/CE8851-32CQ4BQ |