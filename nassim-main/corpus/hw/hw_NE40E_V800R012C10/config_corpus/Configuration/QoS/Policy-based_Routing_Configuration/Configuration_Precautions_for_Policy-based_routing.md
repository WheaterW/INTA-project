Configuration Precautions for Policy-based routing
==================================================

Configuration Precautions for Policy-based routing

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| When the redirect ip-nexthop command is run on an interface bound to an L3VPN to redirect traffic to the next hop of a forward PBR policy (public network route), traffic is redirected in the L3VPN bound to the interface, but not to the next hop of the public network route. In this case, you are advised to specify the keyword public-network in the command. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| MF classification applied to a VSI does not support policy-based routing actions. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| MF classification in VXLAN mode does not support PBR actions. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Policy-based routing (PBR) does not support redirection for Layer 2 traffic. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Policy-based routing (PBR) supports redirection only for incoming traffic and does not take effect when MF classification is configured in the outbound direction of an interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| The discard policy for redirection based on policy-based routing supports only direct routes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| The interface specified as the outbound interface of a discard PBR policy is mutually exclusive with the Layer 2 interface configuration. An interface cannot be configured as a Layer 2 interface after being specified as the outbound interface of a discard PBR policy. An interface cannot be specified as the outbound interface of a discard PBR policy after being specified as a Layer 2 interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| Only a VLAN-type Layer 3 sub-interface can be specified as the outbound interface of a discard PBR policy. After a VLAN-type Layer 3 sub-interface is bound to redirection, the VLAN-type configuration cannot be deleted. A sub-interface can be specified as the outbound interface of a discard PBR policy only when it is configured as a Layer 3 sub-interface. After a Layer 3 sub-interface is specified as the outbound interface of a discard PBR policy, the VLAN-type configuration of the sub-interface cannot be deleted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |
| A redirection action (except for IPv4 single-next hop and IPv4 multi-next hop) is configured in a traffic behavior. If the behavior is not bound to a traffic policy or it is bound to a traffic policy but the policy is not applied, after the redirection configuration in the behavior is deleted, the applied RE, NST, NHP, and VPN-Group resources are not released. After data smoothing or verification is performed, residual resources are released. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H |