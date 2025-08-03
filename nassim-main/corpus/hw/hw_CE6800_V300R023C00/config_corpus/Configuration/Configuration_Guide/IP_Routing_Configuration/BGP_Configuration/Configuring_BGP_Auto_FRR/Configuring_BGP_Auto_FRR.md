Configuring BGP Auto FRR
========================

Configuring BGP Auto FRR

#### Prerequisites

Before configuring BGP Auto FRR, you have completed the following tasks:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)
* [Configure BFD for BGP.](vrp_bgp_cfg_0111.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Enable BGP Auto FRR for unicast routes.
   
   
   ```
   [auto-frr](cmdqueryname=auto-frr)
   ```
   
   By default, BGP Auto FRR is disabled.
5. (Optional) Configure delayed route selection.
   
   
   ```
   [route-select delay](cmdqueryname=route-select+delay) delay-value
   ```
   
   By default, the delay is 0 seconds. That is, route selection is not delayed.
   
   After the primary path recovers, delayed route selection ensures that the device on the primary path performs route selection only after the corresponding forwarding entries on the device are stable. This prevents traffic loss during traffic switchback.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring BGP Auto FRR, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* [ { *mask* | *mask-length* } [ **longer-prefixes** ] ] ] command to check information about routes in the BGP routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) [ *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] ] **verbose** command to check backup forwarding information about routes in the routing table.