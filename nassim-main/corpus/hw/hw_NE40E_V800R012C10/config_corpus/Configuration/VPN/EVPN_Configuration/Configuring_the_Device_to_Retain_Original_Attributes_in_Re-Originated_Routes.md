Configuring the Device to Retain Original Attributes in Re-Originated Routes
============================================================================

EVPN and L3VPN may interwork during EVPN evolution. If route re-origination used for interworking, you can configure the device to retain original attributes in re-originated routes so that traffic can be directly transmitted between UPEs (without taking a detour to the SPE).

#### Context

In EVPN and L3VPN interworking scenario shown in [Figure 1](#EN-US_TASK_0000001343235557__fig_1), UPEs communicate through the SPE and NPE. Traffic between UPEs needs to take a detour to the SPE.

To allow traffic to be directly transmitted between UPEs (without taking a detour to the SPE), configure the SPE to retain original attributes in re-originated routes. The SPE then advertises a received route to the EVPN address family without changing its next hop or original attributes. UPE1 can learn the route whose next hop is UPE2 from a route re-originated by the SPE (the re-originated route retains original attributes). Traffic can then be directly exchanged between the UPEs.

**Figure 1** Interworking between EVPN and L3VPN  
![](figure/en-us_image_0000001290795910.png)

EVPN is deployed on UPE1 and UPE2, and L3VPN is deployed on UPE3. Route re-origination is configured on the SPE for network interworking.

Perform the following configurations on the SPE.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This function takes effect only when tunnels of the same type are used.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit node** *node*
   
   
   
   A route-policy is created, and its view is displayed.
3. Run [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) ****original****
   
   
   
   The device is configured not to change the next hop of a route when advertising the route to a peer.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
   
   
   
   The BGP-VPN instance IPv4 address family view is displayed.
7. Run [**advertise route-reoriginate evpn original-attributes**](cmdqueryname=advertise+route-reoriginate+evpn+original-attributes)
   
   
   
   The VPN instance is configured to advertise re-originated routes with original attributes to the EVPN address family.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
10. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
    
    
    
    The EVPN address family view is displayed.
11. Run [**peer**](cmdqueryname=peer+route-policy+export) *peerIpv4Addr* **[**route-policy**](cmdqueryname=route-policy)** *route-policy-name***[**export**](cmdqueryname=export)**
    
    
    
    A route-policy is specified for the routes to be advertised to a peer.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** command to check EVPN route information. In the command output, re-originated EVPN routes are marked **reoriginated**, and their next hops remain unchanged.