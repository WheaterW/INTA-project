Configuring Route Re-origination-based Evolution
================================================

Configure route re-origination-based evolution to gradually switch traffic to SRv6 EVPN routes, so that VPWS accessing L3VPN over MPLS can evolve to VPWS accessing EVPN over SRv6.

#### Procedure

1. Configure route re-origination on RSGs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
      
      
      
      The BGP-VPNv4 or BGP-VPNv6 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+import+reoriginate) *ipv4-address* **import** **reoriginate** or [**peer**](cmdqueryname=peer+import+reoriginate) *group-name* **import** **reoriginate**
      
      
      
      The device is enabled to add a re-origination flag to the routes received from a specified VPNv4 or VPNv6 peer or peer group.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) *peerIpv6Addr* **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** } or [**peer**](cmdqueryname=peer+advertise+route-reoriginated) *peerGroupName* **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The device is enabled to advertise the re-originated EVPN routes in the VPNv4 or VPNv6 address family to an EVPN IPv6 peer or peer group.
      
      After this step is performed, the RSG re-originates VPNv4 or VPNv6 routes accepted from the ASGs and then advertises SRv6 EVPN routes to EVPN IPv6 peers.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   9. (Optional) Disable the function to re-originate EVPN routes in a specified VPN instance.
      
      
      1. Run the [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance) *vpn-instance-name* command to enter the BGP-VPN instance IPv4 or IPv6 address family view.
      2. Run the [**advertise route-reoriginate evpn disable**](cmdqueryname=advertise+route-reoriginate+evpn+disable) command to enable the function to re-originate EVPN routes in the specified VPN instance.
         
         If some services on ASGs are still carried by traditional L3VPNs, the routes corresponding to these L3VPN instances do not need to be re-originated on RSGs.
      3. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure priority-based route selection on each ASG so that the ASGs preferentially select SRv6 EVPN routes.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+high-priority) *peerIpv6Addr* **high-priority** or [**peer**](cmdqueryname=peer+high-priority) *peerGroupName* **high-priority**
      
      
      
      EVPN routes learned from a specified IPv6 peer or peer group are enabled to participate in route selection based on the high priority.
      
      After this step is performed, for routes with the same prefix, the device preferentially selects the SRv6 EVPN routes learned from the IPv6 peer or peer group.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
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