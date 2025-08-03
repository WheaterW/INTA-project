Controlling the Learning and Advertising of VPN Routes on ASBR
==============================================================

An ASBR can either save partial VPNv6 routes by filtering VPN targets through a routing policy or save all VPNv6 routes.

#### Context

By default, an ASBR filters received VPNv6 routes based on VPN targets. The matching routes are imported into the routing table; otherwise, they are discarded. Therefore, if no VPN instance is configured on the ASBR or no VPN target is configured for the VPN instance, the ASBR discards all the received VPNv6 routes.

Either of the following methods can be used:

* An ASBR can be disabled from filtering routes based on VPN targets. After this configuration, the ASBR saves all VPNv6 routes.
* An ASBR can be enabled to filter routes based on VPN targets. A route-policy can be configured so that only BGP VPNv6 routes matching the policy are accepted.

Perform either of the following methods on the ASBR as needed.


#### Procedure

* Enable the ASBR to accept VPN routes without filtering them based on VPN targets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view of the ASBR is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** [ **unicast** ]
     
     
     
     The BGP-VPN IPv6 address family view is displayed.
  4. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
     
     
     
     Filtering VPN targets of VPNv6 routes is disabled.
     
     In inter-AS VPN Option B mode, the ASBR does not need to store VPN instance information but must store information about all VPNv6 routing information and advertise the routing information to the peer ASBR. In this case, the ASBR needs to import all received VPNv6 routing information without filtering them based on VPN targets.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a route-policy to filter VPN routes based on VPN targets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed on the ASBR.
  2. Perform either of the following operations as required to configure an extcommunity filter.
     
     
     + To configure a basic extcommunity filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *basic-extcomm-filter-num* | **basic** *basic-extcomm-filter-name* } { **deny** | **permit** } { **rt** { *as-number:nn* | *4as-number:nn* | *ipv4-address*:*nn* } } &<1-16> command.
     + To configure an advanced extcommunity filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *advanced-extcomm-filter-num* | **advanced** *advanced-extcomm-filter-name* } { **deny** | **permit** } *regular-expression* command.
  3. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *node*
     
     
     
     A route-policy is configured.
  4. Run [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { { *basic-extcomm-filter-num* [ **matches-all** | **whole-match** ] | *adv-extcomm-filter-num* } &<1-16> | *basic-extcomm-filter-name* [ **matches-all** | **whole-match** ] | *advanced-extcomm-filter-name* }
     
     
     
     A matching rule based on the extcommunity filter is configured for the route-policy.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** [ **unicast** ]
     
     
     
     The BGP-VPN IPv6 address family view is displayed.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* { **export** | **import** }
     
     
     
     The route-policy is used to controlling the importing or exporting of VPNv6 routes.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.