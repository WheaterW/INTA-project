Configuring Active-Route-Advertise
==================================

Configuring Active-Route-Advertise

#### Prerequisites

Before configuring active-route-advertise, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

By default, optimal routes selected in the BGP routing table can be advertised to BGP peers. After the [**active-route-advertise**](cmdqueryname=active-route-advertise) command is configured, only the routes that are selected by BGP and active at the routing management layer can be advertised to peers.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable BGP to advertise only the preferred routes in the IP routing table to peers.
   
   
   ```
   [active-route-advertise](cmdqueryname=active-route-advertise)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**active-route-advertise**](cmdqueryname=active-route-advertise) and [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) commands are mutually exclusive.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```