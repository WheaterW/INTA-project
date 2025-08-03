Configuring MP-EBGP for PEs and ASBRs in Different ASs
======================================================

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. And after an MP-EBGP peer relationship is established between ASBRs in different ASs, an ASBR can advertise the VPNv4 routes of its AS to the other ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The peer ASBR is specified as an EBGP peer.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** **loopback** *interface-number*
   
   
   
   A loopback interface is specified as the outbound interface for BGP sessions.
5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
   
   
   
   The maximum number of hops between PEs for which an EBGP peer relationship is to be configured is specified.
   
   PEs of different ASs are generally not directly connected. To set up the EBGP peer relationship between PEs of different ASs, configure the maximum number of hops between PEs and ensure that PEs are reachable.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The unicast IPv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The function to exchange IPv4 routes is enabled.
8. (On PEs) Run [**quit**](cmdqueryname=quit)
   
   
   
   The BGP view is displayed.
9. (On PEs) Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the device functioning as an ASBR advertises VPNv4 routes to a PE, the device can automatically change the next hop of the routes to its own IP address.
10. (On PEs) Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
    
    
    
    The capability to exchange VPNv4 routes is enabled.
11. (On PEs) Run [**policy vpn-target**](cmdqueryname=policy+vpn-target)
    
    
    
    The VPN-Target filter function is enabled on PEs.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.