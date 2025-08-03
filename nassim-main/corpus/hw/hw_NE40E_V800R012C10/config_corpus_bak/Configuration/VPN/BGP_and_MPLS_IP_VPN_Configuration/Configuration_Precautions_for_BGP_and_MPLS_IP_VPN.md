Configuration Precautions for BGP/MPLS IP VPN
=============================================

Configuration_Precautions_for_BGP_and_MPLS_IP_VPN

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| BGP VPNv4 IPv4 peers cannot receive routes with IPv6 next hops. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| BGP can use IPv4 and IPv6 addresses to establish VPNv4 peer relationships. BGP may receive BGP VPNv4 routes with the same prefix from two types of peers but the next hops are IPv4 and IPv6 addresses respectively, routes recurse to both MPLS (including SR-MPLS) tunnels and SRv6 paths in this case. Currently, load balancing or FRR cannot be implemented among BGP VPNv4 routes with the same prefix. BGP selects only one type of route based on route selection rules to guide data forwarding. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Limitations on L3VPN statistics collection:  1. Traffic statistics collection is supported on L3VPN AC interfaces, but not on tunnel interfaces (such as VXLAN, GRE, and LSP tunnel interfaces).  2. L3VPN statistics include the total traffic volume on all AC interfaces bound to VPN instances. If no AC interfaces are bound to VPN instances, the traffic statistics result is 0. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| BGP ingress LSP load balancing and ingress LSP FRR are mutually exclusive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The POPGO mode does not support load balancing and selects a route to forward packets based on the incoming label.  The one-label-per-next-hop POPGO mode and VPN route load balancing are mutually exclusive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In the unicast address family view, configuration of the peer label capability and configuration of the labeled address family are mutually exclusive. The ipv4-family labeled-unicast and peer label-route-capability (BGP) commands are mutually exclusive.  The peer label capability and labeled address family capability cannot be both enabled in the unicast address family view. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |