(Optional) Enabling ECMP or FRR
===============================

(Optional)_Enabling_ECMP_or_FRR

#### Procedure

1. To enable ECMP or FRR for BGP VPNv4, perform the following steps.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) command to enable the VPNv4 address family and enter its view.
   4. Run the [**maximum load-balancing import-rib**](cmdqueryname=maximum+load-balancing+import-rib) *number* command to configure the maximum number of imported routes allowed for load balancing when the optimal routes are imported routes.
   5. Run the [**auto-frr**](cmdqueryname=auto-frr) command to enable auto FRR.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the VPNv4 address family view.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP instance view.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. To enable ECMP or FRR for BGP VPNv6, perform the following steps.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6) command to enable the VPNv6 address family and enter its view.
   4. Run the [**maximum load-balancing import-rib**](cmdqueryname=maximum+load-balancing+import-rib) *number* command to configure the maximum number of imported routes allowed for load balancing when the optimal routes are imported routes.
   5. Run the [**auto-frr**](cmdqueryname=auto-frr) command to enable auto FRR.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the VPNv6 address family view.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP instance view.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. To enable ECMP or FRR for BGP EVPN, perform the following steps.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enable the EVPN address family and enter its view.
   4. Run the [**maximum load-balancing import-rib**](cmdqueryname=maximum+load-balancing+import-rib) *number* command to configure the maximum number of imported routes allowed for load balancing when the optimal routes are imported routes.
   5. Run the [**auto-frr**](cmdqueryname=auto-frr) command to enable auto FRR.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN address family view.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP instance view.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.