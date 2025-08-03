(Optional) Configuring UCMP for SR-MPLS TE Tunnels
==================================================

When multiple SR-MPLS TE tunnels are destined for a downstream device, you can configure weights to load balance traffic among the SR-MPLS TE tunnels in unequal cost multipath (UCMP) mode.

#### Context

If load balancing weights are configured for all SR-MPLS TE tunnels, traffic is distributed based on these weights. If no such weight is configured for a tunnel, equal-cost load balancing is performed by default.

The weight of a tunnel is calculated using the following formula: Weight of a tunnel = 100 Ã (Configured weight of the tunnel/Sum of the configured weights of all tunnels).

The volume of traffic carried by a tunnel in load balancing mode (called load balancing traffic volume of a tunnel for short) is calculated using the following formula: Load balancing traffic volume of a tunnel = Total traffic volume Ã (Weight of the tunnel/Sum of the weights of all tunnels). Because the sum of load balancing weights configured for SR-MPLS TE tunnels may not be exactly divided by the weight of a single tunnel, the actual load balancing traffic volume of a tunnel may be slightly different from the calculated value.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For SR-MPLS TE tunnels, UCMP is implemented among multiple tunnels. By contrast, for SR-MPLS TE Policies, UCMP is implemented among multiple segment lists of the same SR-MPLS TE Policy.

SR-MPLS TE tunnels do not support UCMP based on the CT bandwidth configured for the tunnels. To implement UCMP for a transit P node of a tunnel (such as an SR-MPLS TE tunnel), run the [**load-balance mpls unequal-cost enable**](cmdqueryname=load-balance+mpls+unequal-cost+enable) command.

To implement UCMP for the headend of an SR-MPLS TE Policy, you only need to configure weights for the segment lists of the policy. To implement UCMP for a transit P node of an SR-MPLS TE Policy, run the [**load-balance mpls unequal-cost enable**](cmdqueryname=load-balance+mpls+unequal-cost+enable) command.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable)
   
   
   
   UCMP is enabled globally.
3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The SR-MPLS TE tunnel interface view is displayed.
4. Run [**load-balance unequal-cost weight**](cmdqueryname=load-balance+unequal-cost+weight) *weight*
   
   
   
   A UCMP weight is configured for traffic forwarding over the SR-MPLS TE tunnel.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.