(Optional) Configuring an Entropy Label Capability for a Tunnel in the Tunnel Interface View
============================================================================================

The entropy label capability can be configured in the tunnel interface view to improve load balancing performance.

#### Context

If severe load imbalance occurs, the entropy label can be configured in the tunnel interface view to help transit nodes properly load-balance traffic. The entropy label capability is enabled on the egress for tunnels. An entropy label is set on the ingress to confirm the tunnel entropy label requirement, and the ingress sends the requirement to the forwarding plane for processing. If no entropy label is configured in the tunnel interface view, the entropy label capability is determined by the global entropy label capability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled globally.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
5. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view is displayed.
6. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
   
   
   
   MPLS TE is specified as the tunnel protocol.
7. Run [**mpls te entropy-label**](cmdqueryname=mpls+te+entropy-label)
   
   
   
   An entropy label is configured for a tunnel in the tunnel interface view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.