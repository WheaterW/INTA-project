Configuration Precautions for sFlow
===================================

Configuration Precautions for sFlow

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| IPv4 private network routes and IPv6 private network routes support multi-PE load balancing. Route information is missing in the data sampled. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| sFlow sampling and NetStream sampling are mutually exclusive. Avoid this scenario during service planning. Otherwise, no sampling result is obtained. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| sFlow applies only to physical Ethernet interfaces and their sub-interfaces, and Eth-Trunk interfaces and their sub-interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| SR-MPLS TE does not support downstream sampling on the ingress PE. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |