(Optional) Configuring the Load Balancing Mode for an IP-Trunk Interface
========================================================================

You can configure the load balancing mode for an IP-Trunk
interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
   
   
   
   The IP-Trunk interface
   view is displayed.
3. Run [**load-balance**](cmdqueryname=load-balance) { **src-dst-ip** |**packet-all** }
   
   
   
   A load balancing mode is configured for the IP-Trunk
   interface.
   
   * IP-based load balancing ensures packet sequence but not bandwidth
     use efficiency.
   * Packet-based load balancing ensures bandwidth usage efficiency
     but not packet sequence.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.