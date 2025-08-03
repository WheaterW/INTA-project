(Optional) Configuring BGP Soft Reset
=====================================

(Optional) Configuring BGP Soft Reset

#### Context

If a BGP export routing policy changes, you can configure export BGP soft reset to allow the new policy to immediately take effect. This configuration triggers re-advertisement of BGP routes based on the new policy without terminating any BGP connection.

BGP soft reset requires peers to support the route-refresh capability.


#### Procedure

* (Optional) Enable the route-refresh capability.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enable the route-refresh capability.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [capability-advertise](cmdqueryname=capability-advertise+route-refresh) route-refresh
     ```
     
     By default, the route-refresh capability is enabled.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure BGP soft reset.
  1. Configure export BGP soft reset in the user view.
     
     
     ```
     [refresh bgp](cmdqueryname=refresh+bgp+all+group+external+internal+export) { all | ipv4-address | group group-name | external | internal } export
     ```
     
     **external** softly resets an EBGP connection, and **internal** softly resets an IBGP connection.