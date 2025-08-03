Disabling a GMPLS UNI Tunnel
============================

Before you release bandwidth resources of an existing GMPLS UNI tunnel or modify tunnel parameters, disable the GMPLS UNI tunnel on the ingress EN.

#### Context

To shut down an existing GMPLS UNI tunnel, run the [**shutdown**](cmdqueryname=shutdown) command on the ingress EN to release label and bandwidth resources assigned to the tunnel. GMPLS UNI tunnel configurations, however, are kept.

To start this tunnel again, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to re-establish the tunnel based on the original configuration file. The path of the re-established UNI LSP within a transport network may be different from the original one because topology or bandwidth within a transport network may change.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**gmpls-tunnel**](cmdqueryname=gmpls-tunnel) *gmpls-tunnel-name*
   
   
   
   The view of the established GMPLS UNI tunnel is displayed.
3. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   A GMPLS UNI tunnel is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.