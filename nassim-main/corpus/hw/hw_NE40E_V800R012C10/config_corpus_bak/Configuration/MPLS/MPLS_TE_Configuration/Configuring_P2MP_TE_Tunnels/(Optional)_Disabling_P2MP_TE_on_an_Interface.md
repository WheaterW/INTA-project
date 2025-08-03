(Optional) Disabling P2MP TE on an Interface
============================================

You can disable P2MP TE on a specific interface during the network planning.

#### Context

After P2MP TE is globally enabled, P2MP TE is automatically enabled on each MPLS TE-enabled interface on a local node. To disable P2MP TE on a specific interface during network planning or there is no need to have P2MP TE enabled on a specific interface because it does not support P2MP forwarding, disable P2MP TE on the specific interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mpls te p2mp-te disable**](cmdqueryname=mpls+te+p2mp-te+disable)
   
   
   
   P2MP TE is disabled on the interface.
   
   
   
   After the [**mpls te p2mp-te disable**](cmdqueryname=mpls+te+p2mp-te+disable) command is run, P2MP TE LSPs established on the interface are torn down, and newly configured P2MP TE LSPs on the interface fail to be established.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.