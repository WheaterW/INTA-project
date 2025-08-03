(Optional) Configuring Outbound BGP Soft Reset
==============================================

After a BGP export policy changes, you can configure outbound BGP soft reset to enable BGP to immediately apply the new export policy without tearing down BGP connections.

#### Context

BGP soft reset requires that peers support the route-refresh function.


#### Procedure

* (Optional) Enable the route-refresh function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**capability-advertise**](cmdqueryname=capability-advertise+route-refresh) **route-refresh**
     
     
     
     The route-refresh function is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP soft reset.
  1. Run the [**refresh bgp**](cmdqueryname=refresh+bgp+vpn-instance+ipv4-family+vpnv4+all+group+external) [ **vpn-instance** *vpn-instance-name* **ipv4-family** | **vpnv4** ] { **all** | *ipv4-address* | **group** *group-name* | **external** | **internal** } **export** command in the user view to trigger outbound BGP soft reset immediately.
     
     
     
     The **external** and **internal** parameters indicate soft resets of EBGP and IBGP connections, respectively.