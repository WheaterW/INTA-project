Configuring MP-IBGP Between a PE and an ASBR in the Same AS
===========================================================

By importing extended community attributes to BGP, MP-IBGP can advertise VPNv6 routes between the PE and the ASBR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
   
   
   
   An IBGP peer relationship is set up between the PE and ASBR in the same AS.
4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface of the BGP session.
5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** [ **unicast** ]
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
   
   
   
   The capability of VPNv6 route exchange between the PE and ASBR is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.