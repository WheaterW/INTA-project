Configuring Bit-Error-Triggered EVPN L3VPN Route Switching
==========================================================

This section describes how to configure bit-error-triggered EVPN L3VPN route switching when bit-error-triggered RSVP-TE switching fails to remove bit errors.

#### Context

In an EVPN L3VPN scenario in which an RSVP-TE tunnel with TE hot standby protection carries services and VPN FRR is configured, you can configure bit-error-triggered EVPN L3VPN route switching in addition to bit-error-triggered RSVP-TE tunnel switching. If the primary and backup constraint-based routed label switched paths (CR-LSPs) of the RSVP-TE tunnel are both in the excessive bit error rate (BER) state or the TE hot standby tunnel fails and bit-error-triggered RSVP-TE tunnel switching cannot protect services against bit errors, bit-error-triggered EVPN L3VPN route switching can do so.

On the EVPN L3VPN H-VPN shown in [Figure 1](#EN-US_TASK_0172362281__fig_dc_vrp_cfg_error-code_evpn_000101), RSVP-TE tunnels are established between the UPE and SPEs to carry services, and the tunnels work in hot-standby mode. VPN FRR is configured on the UPE. If the primary and backup CR-LSPs of the RSVP-TE tunnel are both in the excessive BER state or the TE hot-standby tunnel fails, bit-error-triggered RSVP-TE tunnel switching cannot protect traffic against bit errors. To resolve this problem, configure bit-error-triggered EVPN L3VPN route switching on the UPE and SPE1. This function triggers EVPN route convergence if a bit error event occurs, diverting traffic from the link that has encountered the bit error event.

**Figure 1** Application scenario for bit-error-triggered EVPN L3VPN route switching  
![](images/fig_dc_vrp_cfg_error-code_evpn_000101.png)

#### Pre-configuration Tasks

Before configuring bit-error-triggered EVPN L3VPN route switching, complete the following tasks:

* [Configure VPN FRR.](dc_vrp_mpls-l3vpn-v4_cfg_2017.html)
* [Configure bit-error-triggered RSVP-TE tunnel switching.](dc_vrp_cfg_error-code_000007.html)
* [Configure an EVPN route-policy](dc_vrp_evpn_cfg_0150.html).

#### Procedure

* Configure the UPE to reroute traffic when a bit error event occurs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  4. Run [**bestroute bit-error-detection**](cmdqueryname=bestroute+bit-error-detection)
     
     
     
     The function is enabled to reroute traffic when a bit error event occurs.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure SPE1 to adjust the local preference or MED values of the EVPN routes that it advertises to the NPE when a bit error event occurs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  4. Run [**nexthop recursive-lookup bit-error-detection**](cmdqueryname=nexthop+recursive-lookup+bit-error-detection) { **med** + *med-adjust-value* | **local-preference** - *localpref-adjust-value* } \* [ **route-policy** *route-policy-name* ]
     
     
     
     The function is configured to associate bit error events with the adjustment of EVPN route local preference or MED values.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.