Configuring VPNv6 FRR
=====================

This section describes how to configure VPNv6 FRR to protect PEs.

#### Usage Scenario

VPNv6 FRR applies to IPv6 services that are sensitive to the packet loss and delay. The requirements for VPNs transmitting IPv6 services are high. If VPNv6 FRR is enabled, IPv6 VPN services can be quickly switched to another link when a fault occurs on the VPN. As a result, IPv6 VPN services are not interrupted.

The NE40E supports VPNv6 auto FRR. This function automatically selects the next hop (a PE) for VPN routes, and there are no fixed backup next hops.


#### Pre-configuration Tasks

Before configuring VPNv6 FRR, complete the following tasks:

* Configure a BGP/MPLS IPv6 VPN.
* Ensure that the PE receives IPv6 VPN routes with the same prefix from different VPNv6 peers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
   
   
   
   The BGP-VPN instance IPv6 address family view is displayed.
4. Run [**auto-frr**](cmdqueryname=auto-frr)
   
   
   
   VPNv6 auto FRR is enabled.
5. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
   
   
   
   A delay for selecting a route to the intermediate device on the primary path is configured. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the intermediate device completes refreshing forwarding entries.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] **verbose** command on the PE where VPNv6 FRR is enabled. The command output shows the backup next hop (a PE), backup tunnel, and backup label of routes.