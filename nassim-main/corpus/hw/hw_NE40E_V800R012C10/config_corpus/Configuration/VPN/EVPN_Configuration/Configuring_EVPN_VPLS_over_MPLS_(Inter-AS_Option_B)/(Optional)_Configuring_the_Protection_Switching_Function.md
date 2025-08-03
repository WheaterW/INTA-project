(Optional) Configuring the Protection Switching Function
========================================================

A protection switching function, such as link or node protection, can be configured to provide high availability for an inter-AS EVPN Option B network.

#### Context

On the EVPN Option B dual-homing network shown in [Figure 1](#EN-US_TASK_0172370549__fig54606204295), protection switching is configured on ASBR1. If PE1 fails, traffic can be switched to the backup path pointing to PE2, ensuring normal traffic transmission.

**Figure 1** Fault scenario  
![](images/fig_evpn_mpls_optionB_02.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**auto-frr**](cmdqueryname=auto-frr)
   
   
   
   VPN auto FRR is enabled.
5. (Optional) Run [**bestroute nexthop-resolved**](cmdqueryname=bestroute+nexthop-resolved) **tunnel**
   
   
   
   The function to allow BGP EVPN routes with next hops recursing to IP addresses to participate in route selection is enabled. This helps prevent packet loss during traffic switchback.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.