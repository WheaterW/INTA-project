Configuration Precautions for Rosen MVPN
========================================

Configuration_Precautions_for_Rosen_MVPN

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In a ROSEN MVPN scenario, extranet entries support only static RPs. The RPs in the receiver VRF and source VRF must be the same, and the RP must be in the source VRF. The routes to the source and RP are from the same VRF. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In ROSEN MVPN scenarios, unicast routes in the BGP IPv4 Multicast VPN address family cannot be used for RPF route selection. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IPv4 multicast VPN (Rosen) EXTRANET does not support IGMP access to BAS interfaces. As a result, IPv4 multicast VPN (Rosen) EXTRANET forwarding fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IPv4 multicast VPN (Rosen) EXTRANET does not support the access of PIM to BAS interfaces. As a result, IPv4 multicast VPN (Rosen) EXTRANET forwarding fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IP multicast-IPv4 multicast VPN (Rosen) public network packets do not support fragmentation and reassembly. As a result, fragmented IP multicast-IPv4 multicast VPN (Rosen) packets are discarded.  You are advised to properly plan the path MTU to prevent packet fragmentation. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In a remote cross scenario of multicast VPN extranet, receiver VPNs cannot be configured on the PE where the source VPN resides. Therefore, the source VPN cannot be crossed to different VPNs.  You are advised to configure a source VPN instance on the receiver PE to implement remote cross. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In inter-AS Rosen MVPN Option B and Option C scenarios, Ps and ASBRs cannot process PIM Join/Prune messages carrying vector information.  If the preceding problem occurs, multicast traffic cannot be forwarded. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In Rosen MVPN scenarios, BGP does not support the connector attribute. When a receiver PE performs RPF route selection in a VPN instance, the receiver PE cannot use the connector attribute as an RPF peer.  When a remote PE advertises a VPNv4 route carrying the connector attribute, if the next hop of the VPNv4 route is different from the connector attribute, multicast traffic cannot be forwarded. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In a Rosen MVPN extranet scenario, multicast traffic cannot be locally crossed between different VPN instances on a multicast source-side PE. If a receiver VPN has an MTunnel outbound interface, the MTunnel of the receiver VPN cannot be delivered to the source VPN. If local crossing is not performed on the PE at the multicast receiver side, multicast traffic cannot be forwarded.  It is recommended that multicast traffic be locally crossed between different VPN instances on the receiver-side PE. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |