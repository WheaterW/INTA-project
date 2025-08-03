(Optional) Adjusting Unicast Negotiation Parameters
===================================================

Time synchronization is the basis for normal network operations. 1588 ATR packets should have a higher priority than other service packets so that they can reach the destination in case of network congestion.

#### Context

This section describes the configuration of unicast negotiation parameters on a 1588 ATR server only. For details about how to configure unicast negotiation parameters on a 1588 ATR client, see the configuration manual.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ptp-adaptive dscp**](cmdqueryname=ptp-adaptive+dscp) *dscp-value*
   
   
   
   The DSCP priority value is configured for 1588 ATR packets.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.