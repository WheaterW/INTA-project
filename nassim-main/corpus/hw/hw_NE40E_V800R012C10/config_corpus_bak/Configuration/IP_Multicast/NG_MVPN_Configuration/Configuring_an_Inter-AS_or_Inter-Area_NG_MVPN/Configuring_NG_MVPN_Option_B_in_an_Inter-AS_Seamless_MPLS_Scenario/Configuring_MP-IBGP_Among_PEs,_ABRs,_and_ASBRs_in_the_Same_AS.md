Configuring MP-IBGP Among PEs, ABRs, and ASBRs in the Same AS
=============================================================

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes among the PEs, ABRs, and ASBRs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *node*
   
   
   
   The routing policy is configured.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   The IBGP peer relationship is set up among the PEs, ABRs, and ASBRs in the same AS.
5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface of the BGP session.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The BGP-IPv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The function to exchange IPv4 routes among the PEs, ABRs, and ASBRs is enabled.
8. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **label-route-capability**
   
   
   
   The PEs, ABRs, and ASBRs can receive and process labeled routes.
9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
   
   
   
   The routing policy used to establish routes to peers is configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.