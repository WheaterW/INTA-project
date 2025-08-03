Configuring MP-IBGP Between a PE and an ASBR in the Same AS
===========================================================

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The IBGP peer relationship is set up between the PE and ASBR in the same AS.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface of the BGP session.
5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The function to exchange VPNv4 routes between the PE and ASBR is enabled.
7. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **label-route-capability**
   
   
   
   The capability to exchange labeled IPv4 routes is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.