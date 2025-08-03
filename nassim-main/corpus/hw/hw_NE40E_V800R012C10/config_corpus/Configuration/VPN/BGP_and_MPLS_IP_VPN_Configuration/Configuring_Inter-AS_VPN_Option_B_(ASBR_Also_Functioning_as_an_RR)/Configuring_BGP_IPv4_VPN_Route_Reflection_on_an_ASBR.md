Configuring BGP IPv4 VPN Route Reflection on an ASBR
====================================================

Route reflection on an ASBR is used to reflect the VPNv4 routes advertised by the PE in the same AS to other PEs. As a result, PEs do not need to set up BGP peer relationships, which simplifies configurations.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) *peer-ipv4-address* **reflect-client**
   
   
   
   The ASBR is configured as an RR, and the PE is configured as a client. If you need to configure multiple PEs as clients, repeatedly run this command.
5. (Optional) Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
   
   
   
   Route reflection between clients through the RR is disabled. You need to run this command if the clients are fully connected.
6. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
   
   
   
   The function to filter VPNv4 routes based on VPN targets is disabled.
7. (Optional) Run [**rr-filter**](cmdqueryname=rr-filter) *extcomm-filter-name*
   
   
   
   A reflection policy is configured for the RR.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.