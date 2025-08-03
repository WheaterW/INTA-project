Configuring VPN IPv6 FRR
========================

This section describes how to configure private network IPv6 FRR in the networking where multiple CEs at an IPv6 VPN site access the same PE. This feature can quickly switch traffic to a link connected to another CE if the primary route from a PE to a CE becomes unreachable.

#### Usage Scenario

This feature applies to IP services that are sensitive to the packet loss and delay on a VPN. After VPN IPv6 FRR is configured, if the route from a PE to a CE is unreachable, traffic from the PE can be quickly switched to a link connected to another CE. This feature ensures non-stop forwarding of IP services.

The NE40E supports two VPN IPv6 FRR modes:

* IPv6 FRR: applies to the networking where different PE-CE pairs use different routing protocols.
* VPN BGP auto FRR: applies to the networking where BGP runs between the PEs and CE.

#### Pre-configuration Tasks

Before configuring VPN IPv6 FRR, complete the following tasks:

* Configure a BGP/MPLS IPv6 VPN.
* Ensure that the PE learns IPv6 VPN routes with the same prefix from different CEs attached to it.

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
* Configure VPN BGP auto FRR.
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
* (Optional) Enable IP FRR poison reverse.
  1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface or sub-interface view is displayed.
     
     
     
     The Eth-Trunk interface, Eth-Trunk sub-interface, GE interface, or GE sub-interface view can be displayed.
  2. Run [**poison-reverse enable**](cmdqueryname=poison-reverse+enable)
     
     
     
     IP FRR poison reverse is enabled.
     
     
     
     On an IP ring network configured with IP FRR, this command prevents instantaneous traffic storms caused by route convergence.
     
     In the load balancing scenario, poison reverse does not take effect.

#### Verifying the Configuration

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] **verbose** command to check the backup outbound interface and backup next hop of the VPN IPv6 route in the routing table.