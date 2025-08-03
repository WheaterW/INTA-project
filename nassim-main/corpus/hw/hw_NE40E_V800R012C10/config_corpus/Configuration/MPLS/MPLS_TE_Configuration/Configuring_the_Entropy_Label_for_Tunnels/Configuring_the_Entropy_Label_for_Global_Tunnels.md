Configuring the Entropy Label for Global Tunnels
================================================

The entropy label can be configured to global tunnels to improve load balancing performance.

#### Context

If severe load imbalance occurs, the entropy label can be configured for global tunnels to help transit nodes properly load-balance traffic. The entropy label capability is enabled on the egress for tunnels. An entropy label is configured in the tunnel interface view to confirm the tunnel entropy label requirement, and the ingress sends the requirement to the forwarding plane for processing.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is globally enabled.
4. Run [**mpls te entropy-label rsvp-te**](cmdqueryname=mpls+te+entropy-label+rsvp-te)
   
   
   
   An entropy label is configured for all RSVP-TE tunnels.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.