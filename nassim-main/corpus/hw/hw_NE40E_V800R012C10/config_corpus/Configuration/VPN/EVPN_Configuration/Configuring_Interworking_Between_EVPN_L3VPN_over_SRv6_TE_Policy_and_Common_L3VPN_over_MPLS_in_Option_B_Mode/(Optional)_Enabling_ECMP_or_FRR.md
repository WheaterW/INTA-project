(Optional) Enabling ECMP or FRR
===============================

(Optional) Enabling ECMP or FRR

#### Procedure

1. To enable ECMP or FRR for BGP VPNv4, perform the following steps.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   3. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4)
      
      The VPNv4 address family is enabled, and its view is displayed.
   4. Run [**maximum load-balancing import-rib**](cmdqueryname=maximum+load-balancing+import-rib) *number*
      
      The maximum number of imported routes allowed for load balancing when the optimal routes are imported routes is configured.
   5. Run [**auto-frr**](cmdqueryname=auto-frr)
      
      Auto FRR is enabled.
   6. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPNv4 address family view.
   7. Run [**quit**](cmdqueryname=quit)
      
      Exit the BGP instance view.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
2. To enable ECMP or FRR for BGP VPNv6, perform the following steps.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   3. Run [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      The VPNv6 address family is enabled, and its view is displayed.
   4. Run [**maximum load-balancing import-rib**](cmdqueryname=maximum+load-balancing+import-rib) *number*
      
      The maximum number of imported routes allowed for load balancing when the optimal routes are imported routes is configured.
   5. Run [**auto-frr**](cmdqueryname=auto-frr)
      
      Auto FRR is enabled.
   6. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPNv6 address family view.
   7. Run [**quit**](cmdqueryname=quit)
      
      Exit the BGP instance view.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
3. To enable ECMP or FRR for BGP EVPN, perform the following steps.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      The EVPN address family is enabled, and its view is displayed.
   4. Run [**maximum load-balancing import-rib**](cmdqueryname=maximum+load-balancing+import-rib) *number*
      
      The maximum number of imported routes allowed for load balancing when the optimal routes are imported routes is configured.
   5. Run [**auto-frr**](cmdqueryname=auto-frr)
      
      Auto FRR is enabled.
   6. Run [**quit**](cmdqueryname=quit)
      
      Exit the EVPN address family view.
   7. Run [**quit**](cmdqueryname=quit)
      
      Exit the BGP instance view.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.