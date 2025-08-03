Configuring a Fallback Cost for an Eth-Trunk Multi-Area Adjacency Interface
===========================================================================

Configuring a fallback cost for an Eth-Trunk multi-area adjacency interface helps control route selection.

#### Context

After an Eth-trunk member interface goes down, the OSPF cost value is automatically adjusted. When an Eth-trunk member interface becomes invalid, the remaining bandwidth may fail to meet user requirements, causing service loss. In this fault scenario, the cost of the Eth-Trunk can be dynamically adjusted to a larger value so that traffic is transmitted through other paths. When the interface bandwidth is less than the fallback bandwidth threshold, the device changes the interface cost to the configured fallback cost in time so that a better transmission path is selected. When the bandwidth of an Eth-Trunk interface is greater than or equal to the configured fallback bandwidth threshold, cost-fallback does not take effect.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   The Eth-Trunk interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
5. Run [**ospf cost-fallback**](cmdqueryname=ospf+cost-fallback) *fallbackcost* **threshold** *fallbackbw* **multi-area** *area-id*
   
   
   
   A fallback cost is configured for an Eth-Trunk multi-area adjacency interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.