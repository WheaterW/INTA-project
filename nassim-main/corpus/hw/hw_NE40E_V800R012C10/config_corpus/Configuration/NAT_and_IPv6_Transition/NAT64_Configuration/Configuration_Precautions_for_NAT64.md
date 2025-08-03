Configuration Precautions for NAT64
===================================

Configuration Precautions for NAT64

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| A NAT64 device cannot be connected to a DNS64 server with a non-zero suffix. IPv4-embedded IPv6 addresses are composed of a variable-length prefix, the embedded IPv4 address, and a variable-length suffix. It is recommended that the suffix of a DNS IPv6 server be set to 0. Properly plan the NAT64 prefix and suffix for the DNS64 server. The NAT64 prefix must be the same as that on the CGN device, and the suffix must be 0. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| The device does not support NAT64. | NE40E-M2 | NE40E-M2E |
| NAT64 support the NAT server function. Therefore, DNS and HTTP are not supported in NAT64 server scenario. DNS and HTTP servers cannot be deployed on the private network. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |