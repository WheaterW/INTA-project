Enabling IPv6 FRR
=================

Before configuring IPv6 FRR, you need to enable IPv6 FRR globally.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 frr**](cmdqueryname=ipv6+frr)
   
   
   
   IPv6 FRR is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If IPv6 FRR is configured both in the system view and a routing protocol view, the IPv6 FRR that is configured in the routing protocol view preferentially takes effect.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.