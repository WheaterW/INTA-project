Setting the Limit on the Rate at Which the First Packet Is Sent to Create a Flow
================================================================================

Limiting the rate at which the first packet is sent to create a session prevents users from occupying a large number of CPU resources through first packet attacks, which would otherwise affect common traffic forwarding.

#### Context

You can flexibly set the limit on the rate at which the first packet is sent to create a session, based on different types of packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat flow-defend reverse-blacklist disable**](cmdqueryname=nat+flow-defend+reverse-blacklist+disable)
   
   
   
   The reverse first-packet blacklist function is disabled on the service board.
3. Run [**nat flow-defend**](cmdqueryname=nat+flow-defend) { **forward** | **fragment** | **reverse** } **rate** *rate-number* **slot** *slot-id* 
   
   
   
   The limit on the rate at which the first packet is sent to create a session on a service board is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.