Configuring Route Recursion to SR Tunnels
=========================================

To use SR tunnels to transmit service traffic, configure route recursion to SR tunnels.

#### Context

You can configure a tunnel policy or a policy that prioritizes SR-MPLS BE tunnels to recurse routes to SR tunnels.


#### Procedure

* Configure a tunnel policy on PEs, DC GWs, and L2GWs/L3GWs, so that you can recurse routes to SR-MPLS BE or SR-MPLS TE tunnels. For configuration details, see [Configuring and Applying a Tunnel Policy](dc_vrp_tnlm_cfg_0036.html).
* If both LDP and SR-MPLS BE tunnels are deployed and you want to recurse routes to SR-MPLS BE tunnels, configure a policy that prioritizes SR-MPLS BE tunnels on each device.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     The SR view is displayed.
  3. Run [**tunnel-prefer segment-routing**](cmdqueryname=tunnel-prefer+segment-routing)
     
     
     
     SR-MPLS BE tunnels are configured to take precedence over other tunnels.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.