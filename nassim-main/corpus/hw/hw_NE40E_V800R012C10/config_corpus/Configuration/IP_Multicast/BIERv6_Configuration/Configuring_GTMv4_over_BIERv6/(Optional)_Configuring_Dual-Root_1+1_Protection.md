(Optional) Configuring Dual-Root 1+1 Protection
===============================================

In a GTMv4 over BIERv6 scenario, if a node or link fails, multicast services can be restored only after BGP peer convergence is complete. However, such convergence takes a long time and therefore cannot meet the high reliability requirements of multicast services. To speed up BGP convergence, which in turn accelerates multicast service convergence, you can configure BFD for BGP. You can also deploy the dual-root 1+1 protection solution, which further improves the performance of multicast service convergence.

#### Context

In [Figure 1](#EN-US_TASK_0000001188582639__fig2048117501308), the GTMv4 over BIERv6 dual-root 1+1 protection solution is deployed as follows:

1. Two sender PEs (Root1 and Root2) are deployed. Root1 and Root2 each set up a PMSI tunnel with themselves as the BFIRs. PE1 is a leaf node on the two tunnels.
2. Flow detection-based multicast FRR is configured on PE1.

**Figure 1** GTMv4 over BIERv6 dual-root 1+1 protection networking  
![](figure/en-us_image_0000001188582655.png "Click to enlarge")
![](../../../../public_sys-resources/note_3.0-en-us.png) 

When leaf nodes establish dual-plane BGP peer relationships with the same root node, public network unicast supports FRR between IPv4 and IPv6 peers. As a result, the primary and backup multicast routes may pass through the same root node, and dual-root protection cannot be implemented. To address this problem, configure BGP preferences or use a route-policy so that primary and backup BGP public network unicast routes are formed on the two root nodes.



#### Procedure

1. Two sender PEs (Root1 and Root2) are deployed. Root1 and Root2 each set up a PMSI tunnel with themselves as the BFIRs.
   
   
   
   For details, see [Configuring BGP MVPN Peer Relationships](dc_bierv6_cfg_0009.html), [(Optional) Configuring Multicast Traffic Forwarding over a BIERv6 I-PMSI Tunnel](dc_bierv6_cfg_0010.html), and [(Optional) Enabling the BIERv6 S-PMSI Tunnel Function and Configuring Switching Criteria](dc_bierv6_cfg_0011.html).
2. Configure flow detection-based multicast FRR on PE1.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number*
      
      
      
      A basic ACL to be associated with C-multicast FRR is created, and the basic ACL view is displayed.
   3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \*
      
      
      
      A rule is configured for the ACL.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the basic ACL view.
   5. Run [**multicast mvpn ipv6-underlay**](cmdqueryname=multicast+mvpn+ipv6-underlay) *mvpnid*
      
      
      
      An MVPN IPv6 ID is configured.
   6. Run [**multicast vpn-public**](cmdqueryname=multicast+vpn-public)
      
      
      
      The public network IPv4 address family MVPN view is displayed.
   7. Run [**c-multicast frr**](cmdqueryname=c-multicast+frr) [ *frrPlyNum* | **acl-name** *acl-name* ]
      
      
      
      C-multicast FRR is enabled.
   8. Run [**c-multicast frr flow-detection-based**](cmdqueryname=c-multicast+frr+flow-detection-based) { *frrPlyNum* | **acl-name** *acl-name* }
      
      
      
      The flow detection mode is configured for C-multicast FRR.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the public network IPv4 address family MVPN view.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.