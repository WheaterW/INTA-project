(Optional) Configuring IPv4 and IPv6 Traffic Statistics Collection on a Main Interface
======================================================================================

You can configure IPv4 and IPv6 traffic statistics collection for all main interfaces.

#### Context

Do as follows on the Router that needs to be configured with IPv4 and IPv6 traffic statistics collection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**statistic enable**](cmdqueryname=statistic+enable)
   
   
   
   IPv4 and IPv6 traffic statistics collection is enabled on the main interface.
4. Run [**statistic mode**](cmdqueryname=statistic+mode) **forward**
   
   
   
   IPv4 and IPv6 traffic statistics collection is enabled on the main interface.
5. (Optional) Run [**statistic accelerate enable**](cmdqueryname=statistic+accelerate+enable)
   
   
   
   Statistics acceleration is enabled on the interface.
   
   If dual-stack statistics collection is enabled on a main interface, you can run this command to improve the forwarding performance of the main interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.