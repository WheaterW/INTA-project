(Optional) Configuring Dual-Root 1+1 Protection
===============================================

In an MVPNv6 over BIERv6 scenario, if a node or link fails, multicast services can be restored only after BGP peer convergence is complete. However, such convergence takes a long time and therefore cannot meet the high reliability requirements of multicast services. To speed up BGP convergence, which in turn accelerates multicast service convergence, you can configure BFD for BGP. You can also deploy the dual-root 1+1 protection solution, which further improves the performance of multicast service convergence.

#### Context

In [Figure 1](#EN-US_TASK_0312693159__fig2048117501308), the MVPNv6 over BIERv6 dual-root 1+1 protection solution is deployed as follows:

1. Two sender PEs (Root1 and Root2) are deployed. Root1 and Root2 each set up a PMSI tunnel with themselves as the BFIRs. PE1 is a leaf node on the two tunnels.
2. VPN fast reroute (FRR) is configured on PE1 so that PE1 has two routes to the same multicast source. In this example, PE1 selects the route advertised by Root1 as the primary route, and the one advertised by Root2 as the backup route.
3. Traffic detection-based C-multicast FRR is configured on PE1.

**Figure 1** MVPNv6 over BIERv6 dual-root 1+1 protection networking  
![](figure/en-us_image_0312695483.png "Click to enlarge")
#### Procedure

1. Deploy two sender PEs (Root1 and Root2) and configure them each to set up a PMSI tunnel with themselves as the BFIRs.
   
   
   
   For details, see [Configuring BGP MVPN Peer Relationships](dc_bierv6_cfg_0017.html), [(Optional) Configuring Multicast Traffic Forwarding over a BIERv6 I-PMSI Tunnel](dc_bierv6_cfg_0018.html), and [(Optional) Enabling the BIERv6 S-PMSI Tunnel Function and Configuring Switching Criteria](dc_bierv6_cfg_0019.html).
2. Configure VPN FRR on PE1.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
   3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
   4. Run the **[**route-distinguisher**](cmdqueryname=route-distinguisher)** *route-distinguisher* command to configure an RD for the VPN instance IPv6 address family.
   5. Run the [**vpn frr**](cmdqueryname=vpn+frr) command to enable VPN FRR.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv6 address family view.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Configure traffic detection-based C-multicast FRR on PE1.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* command to create a basic ACL6 to be associated with C-multicast FRR and enter the basic ACL6 view.
   3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \* command to configure a rule for the ACL6.
   4. Run the [**quit**](cmdqueryname=quit) command to exit the basic ACL6 view.
   5. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
   6. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
   7. Run the **[**route-distinguisher**](cmdqueryname=route-distinguisher)** *route-distinguisher* command to configure an RD for the VPN instance IPv6 address family.
   8. Run the [**mvpn**](cmdqueryname=mvpn) command to enter the VPN instance IPv6 address family MVPN view.
   9. Run the [**c-multicast frr**](cmdqueryname=c-multicast+frr) [ *frrPlyNum* | **acl6-name** *frrPlyName* ] command to enable C-multicast FRR.
   10. Run the [**c-multicast frr flow-detection-based**](cmdqueryname=c-multicast+frr+flow-detection-based) { *frrPlyNum* | **acl6-name** *acl-name* } command to set the traffic detection mode for C-multicast FRR.
   11. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv6 address family MVPN view.
   12. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv6 address family view.
   13. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
   14. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.