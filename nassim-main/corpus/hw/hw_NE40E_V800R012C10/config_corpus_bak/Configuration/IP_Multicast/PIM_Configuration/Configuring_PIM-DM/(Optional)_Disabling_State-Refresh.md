(Optional) Disabling State-Refresh
==================================

This section describes how to disable State-Refresh. State-Refresh can be disabled if all clients receive multicast data. When State-Refresh is disabled on an interface, the interface does not forward State-Refresh messages.

#### Context

The PIM-DM status is refreshed based on the State-Refresh messages periodically sent on the network. A Router in the Prune state resets the Prune status timer upon the receipt of a State-Refresh message. This implementation prevents the downstream interfaces from forwarding data when the timer expires.

When State-Refresh is disabled, interfaces start to forward multicast data after the Prune timer expires. The downstream Router that rejects the data then sends Prune messages. However, this process repeats itself periodically, occupying a lot of network resources. It is advised not to disable State-Refresh, because this allows you to save network resources.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**undo pim state-refresh-capable**](cmdqueryname=undo+pim+state-refresh-capable)
   
   
   
   PIM-DM State-Refresh is disabled. The interface on which this function is disabled does not forward State-Refresh messages.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To re-enable PIM-DM State-Refresh on the interface, run the [**pim state-refresh-capable**](cmdqueryname=pim+state-refresh-capable) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.