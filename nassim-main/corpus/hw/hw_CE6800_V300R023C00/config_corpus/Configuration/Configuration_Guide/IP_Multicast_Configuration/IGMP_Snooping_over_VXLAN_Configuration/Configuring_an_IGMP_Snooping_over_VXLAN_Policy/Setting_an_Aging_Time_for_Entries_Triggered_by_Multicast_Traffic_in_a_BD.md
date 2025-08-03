Setting an Aging Time for Entries Triggered by Multicast Traffic in a BD
========================================================================

Setting an Aging Time for Entries Triggered by Multicast Traffic in a BD

#### Context

The aging time can be flexibly configured based on the number of multicast entries used on the network. If many multicast entries exist and the configured time is too short, some entries cannot be generated. Conversely, if the time is too long, unused entries cannot be promptly deleted and system resources cannot be released.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Set the aging time of (S, G) or (\*, G) entries triggered by multicast traffic in a BD.
   
   
   ```
   [multicast layer-2 source-lifetime](cmdqueryname=multicast+layer-2+source-lifetime) SrcLifetimeValue
   ```
   
   
   
   If the number of multicast entries in a BD is less than 1000, you are advised to use the default aging time (210s). If the number of multicast entries in a BD is 1000 or larger, you are advised to set the aging time to 1000s.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```