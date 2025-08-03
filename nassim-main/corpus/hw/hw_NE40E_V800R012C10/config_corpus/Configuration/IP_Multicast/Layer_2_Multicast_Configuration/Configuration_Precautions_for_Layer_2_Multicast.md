Configuration Precautions for Layer 2 Multicast
===============================================

Configuration Precautions for Layer 2 Multicast

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| 1. Layer 2 multicast instances support only VLANs and VSIs, but not BDs. VSIs support only LDP and BGP-AD types (other types need to be shielded). VSIs in BD mode are not supported.  2. In a VPLS over P2MP scenario, only leaf and BUD nodes are supported, and the ingress is not supported. This configuration is mutually exclusive with IGMP snooping. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support BDs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support BGP VPLS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support multicast VLANs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support BGP-AD VPLS over P2MP-TE or MLDP scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support PBB VPLS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support VPLS PW redundancy.  After MLD snooping is deployed, VPLS PW redundancy does not take effect and fast switching is not supported. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support Layer 2 multicast instances. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support Layer 2 multicast CAC. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MLD snooping does not support multicast HQoS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Layer 2 multicast supports bandwidth limit for trunk member interfaces only on the AC side of an L2MC over VPLS network, not on the PW side.  (Eth-Trunk sub-interface view: l2-multicast per-trunk-member limit bandwidth) | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The lossy mode of VSI Layer 2 multicast CAC applies only to trunk dot1q VLAN tag termination sub-interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Layer 2 multicast instances, user instances, and trunk load balancing for multicast are mutually exclusive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| eMDI detection is enabled for upstream traffic in Layer 2 multicast services. A Layer 2 multicast instance has a router interface, and traffic enters the interface. When all users in the multicast group leave and then join the group again within a short period of time, packet loss may be incorrectly reported in the eMDI detection result. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| PIM snooping and IGMP snooping cannot run on the same BAS interface at the same time. In addition, PIM over PPPoE cannot run on the BAS interface that functions as an upstream interface, and IGMP over PPPoE/IPoE cannot run on the BAS interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. In dual-homing scenarios, unicast and multicast traffic are assigned different EVPN instances. A multicast EVPN instance is bound only to one BD. Each access interface in a BD supports only one VLAN or a pair of VLANs. The VLAN configurations must be explicit, and the default VLAN cannot be used. The ESIs of different access interfaces in a BD must be different.  2. S-PMSI tunnels are not supported.  3. Static entries are not backed up through IGMP synchronous routes. The configurations on the dual-homed PEs are the same. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. Only the BD EVPN mode is supported. The non-BD mode and PBB EVPN mode are not supported.  2. Only the VLAN-based EVPN mode is supported. The EVPN in VLAN-bundle or VLAN-aware mode is not supported.  3. A BD cannot be simultaneously bound to an EVPN and a VPLS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The private MIB of the multicast feature can report traps only in the public network instance, but not in the VPN instance. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. In dual-homing scenarios, the sender CE does not support receiver.  2. IGMP snooping can be run on an EVPN only within a BD, not across BDs for communication with global PIM and MVPN.  3. Only EVC untagged and dot1q/QinQ termination sub-interfaces can access a BD and bound to an EVPN. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Bearer tunnels are established using MPLS P2MP mLDP, not IR or VXLAN. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |