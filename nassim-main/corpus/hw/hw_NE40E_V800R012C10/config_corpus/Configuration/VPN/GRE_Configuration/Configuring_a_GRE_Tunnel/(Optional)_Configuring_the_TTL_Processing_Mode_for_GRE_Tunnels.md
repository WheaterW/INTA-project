(Optional) Configuring the TTL Processing Mode for GRE Tunnels
==============================================================

This section describes how to configure GRE tunnels to process TTL in pipe or uniform mode.

#### Context

Perform the following steps on the endpoint Routers of a tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**gre ttl-mode**](cmdqueryname=gre+ttl-mode) { **pipe** | **uniform** }
   
   
   
   The TTL processing mode is configured for GRE tunnels.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.