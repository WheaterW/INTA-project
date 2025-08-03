(Optional) Configuring Route Re-origination
===========================================

On an HVPN, UPEs can communicate through SPEs and NPEs. You can configure route re-origination on SPEs to reduce the number of VPN labels assigned to VPNv4 routes received by the UPEs.

#### Context

On the HVPN shown in [Figure 1](#EN-US_TASK_0172369405__fig_1), UPEs communicate through the SPEs and NPE. If there are a large number of UPEs, the one-label-per-instance mode is configured for VPN instances, and the one-label-per-next-hop mode is configured for the VPNv4 address families of the SPEs, the UPEs receive a large number of labels. If a UPE has a low resource capacity, a traffic forwarding error may occur.

To solve this problem, configure route re-origination on the SPEs so that the VPNv4 routes received by the SPEs are first imported into the VPN instances, which re-originate these routes before advertising them to the VPNv4 address family. Because the one-label-per-instance mode is configured for the VPN instances, only one label is allocated per VPN instance when the re-originated routes are advertised to the UPEs. This helps reduce the number of VPN labels assigned to VPNv4 routes.

**Figure 1** HVPN networking  
![](images/fig_feature_image_0003994499.png)  

Perform the following steps on each SPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
   
   
   
   The BGP-VPN instance IPv4 address family view is displayed.
4. Run [**advertise**](cmdqueryname=advertise) { **best-route** | **valid-routes** } **route-reoriginate** [ **original-attributes** ]
   
   
   
   The VPN instance is configured to advertise re-originated routes to the VPNv4 address family.
   
   
   
   If **original-attributes** is specified, the VPN instance advertises re-originated routes with original attributes to the VPNv4 address family.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
8. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
9. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **enable**
   
   
   
   The device is configured to exchange BGP VPNv4 route information with its peer.
10. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **vpnv4**
    
    
    
    The device is configured to advertise routes re-originated by the VPNv4 address family to its BGP VPNv4 peer.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    To reduce the number of VPN routes assigned to the VPNv4 routes received by a UPE and use a routing policy to prevent an SPE from advertising received original routes to a peer, perform configurations according to [Configuring BGP Routing Policies](dc_vrp_bgp_cfg_3112.html).

#### Verifying the Configuration

Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** *network* command to check VPNv4 route information. Each re-originated VPNv4 route is marked with **reoriginated** in the command output.