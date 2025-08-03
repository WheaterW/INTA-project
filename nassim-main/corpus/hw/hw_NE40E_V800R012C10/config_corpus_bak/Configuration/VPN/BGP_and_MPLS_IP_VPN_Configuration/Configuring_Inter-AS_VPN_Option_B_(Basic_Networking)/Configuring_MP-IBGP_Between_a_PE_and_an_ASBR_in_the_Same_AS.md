Configuring MP-IBGP Between a PE and an ASBR in the Same AS
===========================================================

By introducing extended community attributes into BGP,
MP-IBGP can advertise VPNv4 routes between the PE and ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The IBGP peer relationship is set
   up between the PE and ASBR in the same AS.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface
   of the BGP session.
5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The function to exchange VPNv4 routes between the PE and ASBR
   is enabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the NE40E, an ASBR can change the next-hop address of a VPNv4 route
   to the ASBR's address before advertising the route to a PE.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.