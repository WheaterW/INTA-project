Configuration Precautions for 1588 ACR
======================================

Configuration Precautions for 1588 ACR

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| 1588 ACR is not supported in the port extension scenario. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1588v2 ACR has the following requirements for the intermediate network:  1. The PDV of the intermediate network cannot exceed 16 ms.  2. When the intermediate network is a packet switched network (PSN), the scenarios defined in G.8261 are supported. The packet loss rate is less than 0.5%, the highest QoS priority is used, the number of hops is less than 10 (10 NEs), and the long-term traffic is less than 80% of the total traffic.  3. If the intermediate network is an SDH network, the SDH network must support VC-4 encapsulation but not VC-12 or VC-3 encapsulation. ACR packets can only be sent and received across the SDH network once.  4. If the intermediate network is a microwave network, the microwave is Packet microwave. TDM microwave is the same as SDH microwave. The highest QoS priority is used. The microwave bandwidth must be greater than 100 Mbit/s, the number of hops must be less than or equal to two (three NEs), and the long-term traffic must be less than 80% of the total traffic.  The 1588 ACR frequency synchronization performance is affected. Therefore, you are advised to plan a 1588 ACR clock synchronization network. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The 1588ACR server and 1588v2 Layer 3 unicast encapsulation mode cannot be used together. If the local IP address of 1588 ACR is the same as the destination IP address of 1588v2, 1588 ACR packets are processed as 1588v2 packets. As a result, 1588 ACR negotiation fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |