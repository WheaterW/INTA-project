(Optional) Modifying Graft Control Parameters
=============================================

This section describes how to modify graft control parameters. You can configure the interval at which Graft messages are sent according to the actual situation.

#### Context

On a PIM-DM network, if State-Refresh is enabled on pruned interfaces, it is possible that the forwarding function will never be restored. When a new multicast member is added to a pruned interface, PIM-DM uses the graft mechanism to restore the forwarding function on the interface to save time. In other words, a Router sends a Graft message to require an upstream Router to forward multicast data to this network segment. When the upstream Router receives the Graft message, it returns a Graft-Ack message and re-enables the forwarding function on the interface that received the Graft message. If the Router does not receive the Graft-Ack message during the configuration period, it will keep sending the same Graft message before it receives the Graft-Ack message from the upstream device. If there is no special requirement, default values are recommended.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim timer graft-retry**](cmdqueryname=pim+timer+graft-retry) *interval*
   
   
   
   The interval at which Graft messages are retransmitted is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.