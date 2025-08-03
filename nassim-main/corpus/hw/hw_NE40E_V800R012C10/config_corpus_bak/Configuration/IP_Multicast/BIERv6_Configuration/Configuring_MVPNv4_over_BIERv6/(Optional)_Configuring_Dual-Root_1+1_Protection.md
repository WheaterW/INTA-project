(Optional) Configuring Dual-Root 1+1 Protection
===============================================

In an MVPNv4 over BIERv6 scenario, if a node or link fails, multicast services can be restored only after BGP peer convergence is complete. However, such convergence takes a long time and therefore cannot meet the high reliability requirements of multicast services. To speed up BGP convergence, which in turn accelerates multicast service convergence, you can configure BFD for BGP. You can also deploy the dual-root 1+1 protection solution, which further improves the performance of multicast service convergence.

#### Context

In [Figure 1](#EN-US_TASK_0283127778__fig2048117501308), the MVPNv4 over BIERv6 dual-root 1+1 protection solution is deployed as follows:

1. Two sender PEs (Root1 and Root2) are deployed. Root1 and Root2 each set up a PMSI tunnel with themselves as the BFIRs. PE1 is a leaf node on the two tunnels.
2. VPN fast reroute (FRR) is configured on PE1 so that PE1 has two routes to the same multicast source. In this example, PE1 selects the route advertised by Root1 as the primary route, and the one advertised by Root2 as the backup route.
3. C-multicast FRR in flow-based detection mode is configured on PE1.

**Figure 1** MVPNv4 over BIERv6 dual-root 1+1 protection networking  
![](figure/en-us_image_0283900046.png "Click to enlarge")
#### Procedure

1. Deploy two sender PEs (Root1 and Root2) and configure them each to set up a PMSI tunnel with themselves as the BFIRs.
   
   
   
   For details, see [Configuring BGP MVPN Peer Relationships](dc_bierv6_cfg_0009.html), [(Optional) Configuring Multicast Traffic Forwarding over a BIERv6 I-PMSI Tunnel](dc_bierv6_cfg_0010.html), and [(Optional) Enabling the BIERv6 S-PMSI Tunnel Function and Configuring Switching Criteria](dc_bierv6_cfg_0011.html).
2. Configure VPN FRR on PE1.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family view is displayed.
   4. Run **[**route-distinguisher**](cmdqueryname=route-distinguisher)** *route-distinguisher*
      
      
      
      An RD is configured for the VPN instance IPv4 address family.
   5. Run [**vpn frr**](cmdqueryname=vpn+frr)
      
      
      
      VPN FRR is enabled.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv4 address family view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. Configure C-multicast FRR in flow-based detection mode on PE1.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number*
      
      
      
      A basic ACL to be associated with C-multicast FRR is created, and the basic ACL view is displayed.
   3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \*
      
      
      
      A rule is configured for the ACL.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the basic ACL view.
   5. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   6. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family view is displayed.
   7. Run [**mvpn**](cmdqueryname=mvpn)
      
      
      
      The VPN instance IPv4 address family MVPN view is displayed.
   8. Run [**c-multicast frr**](cmdqueryname=c-multicast+frr) [ *frrPlyNum* | **acl-name** *acl-name* ]
      
      
      
      C-multicast FRR is enabled.
   9. Run [**c-multicast frr flow-detection-based**](cmdqueryname=c-multicast+frr+flow-detection-based) { *frrPlyNum* | **acl-name** *acl-name* }
      
      
      
      The flow detection mode is configured for C-multicast FRR.
   10. (Optional) Run [**multicast wtr**](cmdqueryname=multicast+wtr) *wtr-time*
       
       
       
       The WTR time is set.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 address family MVPN view.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 address family view.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance view.
   14. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.