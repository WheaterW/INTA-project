(Optional) Configuring a Policy to Prioritize SR-MPLS BE Tunnels
================================================================

You can configure a policy to prioritize SR-MPLS BE tunnels so that they can be preferentially selected.

#### Context

In a tunnel recursion scenario, an LDP tunnel is preferentially selected to forward traffic by default. To enable a device to preferentially select an SR-MPLS BE tunnel, improve the SR-MPLS BE tunnel priority so that the SR-MPLS BE tunnel takes preference over the LDP tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   The SR view is displayed.
3. Run [**tunnel-prefer segment-routing**](cmdqueryname=tunnel-prefer+segment-routing)
   
   
   
   SR-MPLS BE tunnels are configured to take precedence over LDP tunnels.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.