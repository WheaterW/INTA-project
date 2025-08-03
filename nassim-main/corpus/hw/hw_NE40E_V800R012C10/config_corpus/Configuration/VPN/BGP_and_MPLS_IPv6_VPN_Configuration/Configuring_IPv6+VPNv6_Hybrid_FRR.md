Configuring IPv6+VPNv6 Hybrid FRR
=================================

This section describes how to configure IPv6+VPNv6 hybrid FRR in the CE dual-homing networking. If the next hop from a PE to a CE is unreachable, IPv6+VPNv6 hybrid FRR can send traffic to the other PE over a tunnel, and the traffic will be routed to the CE through IP forwarding on the private network. This improves network reliability.

#### Usage Scenario

IPv6+VPNv6 hybrid FRR can quickly switch traffic from a PE to another PE that serves as the backup next hop if the primary route to a CE is unreachable.

A PE learns IPv6 VPN routes with the same prefix from a CE and other PEs. In this situation, IPv6+VPNv6 hybrid FRR can be configured on the PE. After IPv6+VPNv6 hybrid FRR is enabled, the PE generates a primary route and a backup route to the VPN prefix. If the link between the PE and CE fails, the traffic can be quickly switched to the backup next hop (another PE).

The NE40E supports two IPv6+VPNv6 hybrid FRR modes:

* IPv6 FRR: applies to the networking where a non-BGP routing protocol runs between the PEs and CE.
* Private network BGP auto FRR: applies to the networking where BGP runs between the PEs and CE.

#### Pre-configuration Tasks

Before configuring hybrid FRR for IPv6 and VPNv6 routes, complete the following tasks:

* Configure a BGP/MPLS IPv6 VPN.
* Ensure that a PE learns IPv6 routes with the same prefix from a CE and other VPNv6 peers.

#### Procedure

* Configure IPv6 FRR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**ipv6 frr**](cmdqueryname=ipv6+frr)
     
     
     
     IPv6 FRR is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure private network BGP auto FRR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**auto-frr**](cmdqueryname=auto-frr)
     
     
     
     BGP auto FRR is enabled.
  5. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
     
     
     
     A delay for selecting a route to the intermediate device on the primary path is configured. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the intermediate device completes refreshing forwarding entries.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Checking the Configurations

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] **verbose** command on the PE to check the backup outbound interface and backup next hop of the IPv6 route in the routing table.