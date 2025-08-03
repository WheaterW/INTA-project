Configuring MP-IBGP Between ASBRs in the Same AS
================================================

After the MP-IBGP peer relationship is established between the ASBRs in the same AS, ASBRs can exchange VPNv4 routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The IBGP peer relationship is
   set up between the ASBRs in the same AS.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** **loopback** *interface-number*
   
   
   
   The loopback interface is specified as the outbound interface of the BGP session.
5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP-VPNv4 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The function to exchange VPNv4 routes between the ASBRs in the
   same AS is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.