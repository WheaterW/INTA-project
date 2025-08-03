Configuration Precautions for APN6
==================================

Configuration Precautions for APN6

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Value-added service boards do not support the APN feature, APN ID-based traffic steering, or APN ID-based traffic isolation. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| If an endpoint runs an early version that does not support APN, a packet carrying an APN ID is not processed, causing one of the following issues:  If the packet is a data packet, the service is interrupted.  If the packet is a ping/trace packet, the ping/trace operation fails.  If the packet is a detection packet, such as a BFD packet, the detection fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If a midpoint runs an early version that does not support APN, TE FRR across IPv6 headers is not supported for an SRv6 packet carrying an APN ID. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When TWAMP is used to detect services, interface ACL matching is not performed, and APN IDs are not encapsulated. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In NetStream sampling, if routes recurse to SRv6 tunnels and traffic is steered based on APN IDs, the collected outbound interface information is inaccurate. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Traffic isolation based on APN IDs is not supported in direct route scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In L3VPN local access scenarios, the received packets cannot carry APN IDs. When a traffic isolation policy is implemented based on the APN ID, the APN ID needs to be configured locally. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In SRv6 HoVPN scenarios, an APN ID is generated on a CPE and carried in a packet to a network PE. When a traffic isolation policy is implemented based on the APN ID, the source APN ID is obtained from a packet. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In SRv6 HoVPN scenarios, if the CPE cannot generate an APN ID and the network PE needs to perform traffic isolation based on the APN ID, you can configure an ACL in the VPN instance of the network PE to generate an APN ID, while ensuring that the VPN isolation policies of different CPEs are the same and allocated with the same group ID or CPE 5-tuple information does not conflict. Configure ACL matching on the network PE. This means that the ACLs configured on different CPEs are uniformly configured on the network PE. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In Layer 2 and Layer 3 interworking scenarios in VE mode, if different CPEs have different VPN isolation policies or are allocated different group IDs, ensure that one L3VE sub-interface corresponds to one CPE. In Option A scenarios, if different CPEs have different VPN isolation policies or are allocated different group IDs, ensure that a VLAN sub-interface is planned for each CPE. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In a scenario where the CPE does not support APN but the network PE supports APN, when an APN ID-based traffic isolation policy is configured on the network PE, only blocked traffic should match the ACL. If permitted traffic also matches the ACL, the traffic is tagged with the APN ID and forwarded. As a result, packet loss occurs as the CPE does not support APN processing. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Similar to data packets, RFC 2544 and Y.1564 detection packets are matched against interface ACL rules. If they match a specific rule, APN IDs are encapsulated. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |