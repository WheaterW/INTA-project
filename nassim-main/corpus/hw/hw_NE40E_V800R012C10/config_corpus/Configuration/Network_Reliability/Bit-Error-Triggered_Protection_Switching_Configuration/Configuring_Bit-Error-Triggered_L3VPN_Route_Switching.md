Configuring Bit-Error-Triggered L3VPN Route Switching
=====================================================

This section describes how to configure bit-error-triggered L3VPN route switching when bit-error-triggered RSVP-TE switching fails to remove bit errors.

#### Context

In an H-VPN scenario in which an RSVP-TE tunnel with TE hot standby protection carries services and VPN FRR is configured, you can configure bit-error-triggered L3VPN route switching in addition to bit-error-triggered RSVP-TE tunnel switching. If the primary and backup constraint-based routed label switched paths (CR-LSPs) of the RSVP-TE tunnel are both in the excessive bit error rate (BER) state or the TE hot standby tunnel fails and bit-error-triggered RSVP-TE tunnel switching cannot protect services against bit errors, bit-error-triggered L3VPN route switching can do so.

[Figure 1](#EN-US_TASK_0172362278__fig_dc_vrp_cfg_error-code_00001301) shows an H-VPN scenario where an RSVP-TE tunnel with TE hot standby protection configured carries L3VPN services. VPN FRR is configured on the user-end provider edge (UPE). If the primary and backup CR-LSPs of the RSVP-TE tunnel are both in the excessive BER state or the TE hot-standby tunnel fails, bit-error-triggered RSVP-TE tunnel switching cannot protect traffic against bit errors. To resolve this problem, configure bit-error-triggered L3VPN route switching on the UPE and SPE1. Bit-error-triggered L3VPN route switching triggers VPN route convergence in the case of a bit error event, diverting traffic from the link that has encountered the bit error event.

**Figure 1** Networking diagram for bit-error-triggered L3VPN route switching  
![](images/fig_dc_vrp_cfg_error-code_00001301.png)

#### Pre-configuration Tasks

Before configuring bit-error-triggered L3VPN route switching, complete the following tasks:

* [Configure VPN FRR.](dc_vrp_mpls-l3vpn-v4_cfg_2017.html)
* [Configure bit-error-triggered RSVP-TE tunnel switching.](dc_vrp_cfg_error-code_000007.html)

#### Procedure

* Configure the UPE to reroute traffic when a bit error event occurs. 
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  4. Run [**bestroute bit-error-detection**](cmdqueryname=bestroute+bit-error-detection)
     
     
     
     The function is enabled to reroute traffic when a bit error event occurs.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure SPE1 to adjust the local preference or Multi-Exit Discriminator (MED) values of the VPN routes that it advertises to the network provider edge (NPE) when a bit error event occurs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4)
     
     
     
     The BGP-VPNv4 address family view is displayed.
  4. Run [**nexthop recursive-lookup bit-error-detection**](cmdqueryname=nexthop+recursive-lookup+bit-error-detection) { **med** + *med-adjust-value* | **local-preference** - *localpref-adjust-value* } \* [ **route-policy** *route-policy-name* ]
     
     
     
     Bit error events are associated with the adjustment of VPN route local preference or MED values.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After you configure the association between bit error events and the adjustment of VPN route local preference or MED values, the local preference or MED value of a route changes if the tunnel to which the route is recursed encounters a bit error event. However, only routes meeting the routing policy can be advertised with adjusted local preference or MED values. Pay special attention to routing policy configuration when configuring the association between bit error events and the adjustment of VPN route local preference or MED values. If the routing policy is not appropriately configured, routes may fail to be advertised after having their local preference or MED values changed. To ignore the command configuration when applying the routing policy, run the [**peer**](cmdqueryname=peer) {*peerIpv4Addr* | **peerGroupName** } **route-filter** *route-filter-name***export****ignore-bit-error** or [**peer**](cmdqueryname=peer) {*peerIpv4Addr* | **peerGroupName** } **route-policy** *route-policy-name***export****ignore-bit-error** command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.