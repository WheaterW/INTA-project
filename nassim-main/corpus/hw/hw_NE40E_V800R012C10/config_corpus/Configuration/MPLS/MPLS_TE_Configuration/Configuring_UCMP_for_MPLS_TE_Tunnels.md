Configuring UCMP for MPLS TE Tunnels
====================================

When multiple MPLS TE tunnels are destined for a downstream device, you can configure UCMP weights or CT bandwidths to load balance traffic among the MPLS TE tunnels in unequal cost multi path (UCMP) mode.

#### Context

If UCMP is globally enabled for static MPLS TE and P2P RSVP-TE tunnels and UCMP weights are configured for all the tunnels, UCMP load-balancing is preferentially performed based on the weights. If no load balancing weight is configured for some tunnels but UCMP is globally enabled and CT bandwidths are configured for all tunnels, UCMP load-balancing is performed based on the CT bandwidths. If both weights and CT bandwidths are not configured for tunnels, equal-cost load balancing is performed by default.

When UCMP load-balancing is performed based on weights, the actual weight of a tunnel is calculated using the following formula: Actual weight of this tunnel = 100 x (Weight of this tunnel/Sum of weights of all tunnels).

The volume of traffic carried by a single tunnel in load balancing mode (called load balancing traffic volume of the tunnel for short) is calculated using the following formula: Load balancing traffic volume of a tunnel = Total traffic volume x (Actual weight of the tunnel/Sum of weights of all tunnels). Because the sum of load balancing weights of all TE tunnels may not be exactly divided by the weight of a single TE tunnel, the actual load balancing traffic volume of a TE tunnel may be slightly different from the calculated value.


#### Procedure

1. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The MPLS TE tunnel interface view is displayed.
2. Run [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable)
   
   
   
   UCMP load-balancing is enabled globally.
3. Configure UCMP for MPLS TE tunnels. For details, see [Table 1](#EN-US_TASK_0000001989028832__table29861143141218).
   
   
   
   You can perform one or more steps in [Table 1](#EN-US_TASK_0000001989028832__table29861143141218).
   
   
   
   **Table 1** Configuring UCMP for TE tunnels
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a UCMP load-balancing weight for each MPLS TE tunnel. | [**load-balance unequal-cost weight**](cmdqueryname=load-balance+unequal-cost+weight) *weight* | This function takes effect only when UCMP load-balancing weights are configured for all tunnels. |
   | Configure a bandwidth for each MPLS TE tunnel. | **[**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth)** **ctType** **ctValue** | This function takes effect only when bandwidths are configured for all tunnels. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.