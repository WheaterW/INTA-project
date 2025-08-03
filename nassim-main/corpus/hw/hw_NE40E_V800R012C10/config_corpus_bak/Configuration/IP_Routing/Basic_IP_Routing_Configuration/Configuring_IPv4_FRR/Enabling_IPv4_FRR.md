Enabling IPv4 FRR
=================

Before configuring IPv4 FRR, you need to enable IPv4 FRR globally.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip frr**](cmdqueryname=ip+frr)
   
   
   
   IPv4 FRR is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If IPv4 FRR is configured both in the system view and a routing protocol view, the IPv4 FRR that is configured in the routing protocol view preferentially takes effect.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.