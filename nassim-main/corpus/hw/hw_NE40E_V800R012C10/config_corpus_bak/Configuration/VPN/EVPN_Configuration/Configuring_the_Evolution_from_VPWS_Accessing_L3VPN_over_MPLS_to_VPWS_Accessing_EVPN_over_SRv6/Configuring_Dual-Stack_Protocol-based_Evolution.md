Configuring Dual-Stack Protocol-based Evolution
===============================================

Configure dual-stack protocol-based evolution so that VPWS accessing L3VPN over MPLS can evolve to VPWS accessing EVPN over SRv6 when IPv4 and IPv6 networks coexist.

#### Procedure

1. Configure priority-based route selection on ASGs and RSGs so that the ASGs and RSGs preferentially select SRv6 EVPN routes.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+high-priority) *peerIpv6Addr* **high-priority** or [**peer**](cmdqueryname=peer+high-priority) *peerGroupName* **high-priority**
      
      
      
      The EVPN routes learned from an IPv6 peer or peer group are granted the high priority for route selection.
      
      After this step is performed, the device preferentially selects the SRv6 EVPN routes learned from the specified IPv6 peer or peer group among routes with the same prefix.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure route-policies on each RR to filter out VPNv4 or VPNv6 routes.
   
   
   
   After completing the preceding step, configure the import and export route-policies on each RR to filter out received VPNv4 or VPNv6 routes and reflect only EVPN routes, reducing memory consumption.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *RR\_IN* **permit** **node** *node*
      
      
      
      An import route-policy and a permit node are configured to add a specified community attribute (*aa:nn*) to VPNv4 or VPNv6 routes to be accepted by the RR.
   3. Run [**apply community**](cmdqueryname=apply+community) *aa:nn*
      
      
      
      A community attribute (*aa:nn*) is set for routes.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**ip community-filter**](cmdqueryname=ip+community-filter) *cfIndex* **permit** *aa:nn*
      
      
      
      A community filter is created.
      
      The community filter is used to match the VPNv4 or VPNv6 routes against the specified community attribute (*aa:nn*), which is further used to apply an export route-policy.
   6. Run [**route-policy**](cmdqueryname=route-policy) *RR\_OUT* **deny** **node** *node1*
      
      
      
      An export route-policy and a deny node are configured to filter out the VPNv4 or VPNv6 routes with a specified community attribute to be advertised by the RR.
   7. Run [**if-match community-filter**](cmdqueryname=if-match+community-filter) *cfIndex*
      
      
      
      A rule for matching routes against the specified community filter is created.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**route-policy**](cmdqueryname=route-policy) *RR\_OUT* **permit** **node** *node2*
      
      
      
      Another node is configured in the export route-policy to allow unmatched routes to be advertised.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       
       
       The BGP view is displayed.
   12. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
       
       
       
       The BGP-VPNv4 or BGP-VPNv6 address family view is displayed.
   13. Run [**peer**](cmdqueryname=peer+route-policy+import) *ipv4-address* **route-policy** *RR\_IN* **import** or [**peer**](cmdqueryname=peer+route-policy+import) *group-name* **route-policy** *RR\_IN* **import**
       
       
       
       The route-policy RR\_IN is applied to the RR to filter VPNv4 or VPNv6 routes to be accepted from a specified peer or peer group.
   14. Run [**peer**](cmdqueryname=peer+route-policy+export) *ipv4-address* **route-policy** *RR\_OUT* **export** or [**peer**](cmdqueryname=peer+route-policy+export) *group-name* **route-policy** *RR\_OUT* **export**
       
       
       
       The route-policy RR\_OUT is applied to the RR to filter out VPNv4 or VPNv6 routes so that the routes are not advertised to a specified peer or peer group.
   15. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. After the evolution is complete, delete BGP VPNv4 or VPNv6 peer relationships from the RRs, ASGs, and RSGs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      
      
      The BGP-VPNv4 or BGP-VPNv6 address family view is displayed.
   4. Run [**undo peer**](cmdqueryname=peer+enable)*ipv4-address* **enable**
      
      
      
      The specified VPNv4 or VPNv6 peer is deleted.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.