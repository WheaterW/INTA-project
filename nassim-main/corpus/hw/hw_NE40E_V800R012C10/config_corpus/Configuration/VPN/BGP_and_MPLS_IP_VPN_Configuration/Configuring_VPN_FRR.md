Configuring VPN FRR
===================

If a CE is multi-homed to two PEs, you can configure VPN FRR to ensure that VPN services are switched to a standby link if the active link between PEs fails.

#### Usage Scenario

VPN FRR applies to services that are sensitive to packet loss and delay on VPN networks. As shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_2017.html#EN-US_TASK_0172369417__fig_dc_vrp_mpls-l3vpn-v4_cfg_201701), CE1 is dual-homed to PE2 and PE3. VPN FRR is configured on PE1. If the link between PE1 and PE2 fails, VPN traffic needs to be rapidly switched to the link between PE1 and PE3.

**Figure 1** VPN FRR  
![](figure/en-us_image_0258271906.png)

#### Prerequisites

Before configuring VPN FRR, complete the following tasks:

* Configure a routing protocol on the Routers to implement network connectivity.
* Configure PE1 to ensure that two unequal-cost routes destined for the CE are available.
* Set up a VPN network.

#### Background

You can enable VPN FRR in either the VPN instance IPv4 address family view or the BGP-VPN instance IPv4 address family view as needed. For example, if only BGP VPNv4 peers are configured on a device but no BGP-VPN instance is configured, you need to enable VPN FRR in the VPN instance IPv4 address family view.


#### Procedure

* Enable VPN FRR in the VPN instance IPv4 address family view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  4. Run [**vpn frr**](cmdqueryname=vpn+frr)
     
     
     
     VPN FRR is enabled.
  5. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the VPN instance view.
  6. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. (Optional) Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  9. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
     
     
     
     A route selection delay is set. After the active path recovers, an appropriate delay ensures that traffic switches back to the active path after the intermediate devices refresh forwarding entries and the entries become stable, preventing packet loss during a traffic switchback.
     
     The *delay-value* value is an integer ranging from 0 to 3600, in seconds.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Enable VPN FRR in the BGP-VPN instance IPv4 address family view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  4. Run [**auto-frr**](cmdqueryname=auto-frr)
     
     
     
     VPN FRR is enabled.
  5. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
     
     
     
     A route selection delay is set. After the active path recovers, an appropriate delay ensures that traffic switches back to the active path after the intermediate devices refresh forwarding entries and the entries become stable, preventing packet loss during a traffic switchback.
     
     
     
     The *delay-value* value is an integer ranging from 0 to 3600, in seconds.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring VPN FRR, you can run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] **verbose** command to check the backup next hop (PE), backup tunnel, and backup label in the routing table of the VPN instance IPv4 address family.