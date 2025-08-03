(Optional) Configuring BGP-EVPN Route Reflection on an ASBR
===========================================================

When multiple PEs exist in the ASs, you can configure an ASBR as an RR to lower configuration complexity.

#### Context

In the inter-AS EVPN Option B scenario shown in [Figure 1](#EN-US_TASK_0172370552__fig157308815308), if multiple PEs exist in an AS, you can configure an ASBR as an RR to reduce the number of MP-IBGP connections needed between PEs. Configuring an ASBR as an RR will burden the ASBR. Therefore, it is recommended that a high-performance device be used as the ASBR. On the network shown in the figure, ASBR1 is configured as an RR so that PE1 and PE2 do not need to set up an MP-IBGP peer relationship.

**Figure 1** Inter-AS EVPN Option B solution  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_004701.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The ASBR1's system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+reflect-client) *peerIpv4Addr* **reflect-client**
   
   
   
   ASBR1 is configured as an RR, and a PE is configured as its client. To configure both PE1 and PE2 as clients, run this command once again.
5. Run [**peer**](cmdqueryname=peer+next-hop-local) *peerIpv4Addr* **next-hop-local**
   
   
   
   The ASBR is configured to change the next hop address of a route to the device's own IP address before the device advertises the route to IBGP peers PE1 and PE2.
6. (Optional) If the clients are fully meshed, run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
   
   
   
   Route reflection between the clients through RRs is disabled.
7. (Optional) Run [**rr-filter**](cmdqueryname=rr-filter) *extended-list-number*
   
   
   
   A reflection policy is configured for the RR.
8. (Optional) Run [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute)
   
   
   
   The RR is enabled to modify the path attributes of BGP routes using an export policy.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on the RR:
   
   * In the BGP-EVPN address family view, the [**peer route-policy**](cmdqueryname=peer+route-policy) **export** command takes precedence over the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command.
   * In the BGP-EVPN address family view, the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command takes precedence over the [**peer route-policy**](cmdqueryname=peer+route-policy) **export** command.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.