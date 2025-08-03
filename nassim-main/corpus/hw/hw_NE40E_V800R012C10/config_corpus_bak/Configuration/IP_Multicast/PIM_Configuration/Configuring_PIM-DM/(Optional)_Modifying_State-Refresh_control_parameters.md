(Optional) Modifying State-Refresh control parameters
=====================================================

This section describes how to modify State-Refresh control parameters. You can configure the interval at which State-Refresh messages are sent, the timeout period for receiving the next State-Refresh message, and the TTL of State-Refresh messages.

#### Context

On a PIM-DM network, the periodic flooding-pruning wastes lots of network resources. To avoid that the pruned interface is restored to forward packets because the Prune timer expires, you can enable the NE40E to send State-Refresh messages periodically, refresh the Prune state of the interfaces, and maintain the SPT. The NE40E allows you to modify the State-Refresh parameters according to the network environment. If there is no special requirement, the default value is recommended.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim**](cmdqueryname=pim)
   
   
   
   The PIM view is displayed.
3. Run [**state-refresh-interval**](cmdqueryname=state-refresh-interval) *interval*
   
   
   
   The interval at which the Router sends State-Refresh messages is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This command applies to the first hop Router closest to the multicast source.
   * The interval at which State-Refresh messages are sent must be shorter than the expiration time of the Prune state. You can run the [**holdtime join-prune**](cmdqueryname=holdtime+join-prune) command to configure the expiration time of the Prune state.
4. Run [**state-refresh-rate-limit**](cmdqueryname=state-refresh-rate-limit) *interval*
   
   
   
   The timeout period for receiving the next State-Refresh message is configured.
   
   
   
   On a PIM-DM network, it is possible for a Router to receive State-Refresh messages from more than one Router. Some of these messages are duplicate. When a Router with the [**state-refresh-rate-limit**](cmdqueryname=state-refresh-rate-limit) command configuration receives the first State-Refresh message, it immediately resets the Prune timer and starts the State-Refresh timer. The lifetime of the State-Refresh timer is equal to the timeout period for receiving the next State-Refresh message.
   * Before the timer expires, the router discards the repeated State-Refresh messages it receives.
   * After the State-Refresh timer times out, the router is allowed to receive the next State-Refresh message.
5. Run [**state-refresh-ttl**](cmdqueryname=state-refresh-ttl) *ttl-value*
   
   
   
   The TTL of State-Refresh messages to be sent is configured.
   
   
   
   On a PIM-DM network, the Router deducts 1 from the TTL of a received State-Refresh message, and then sends the message to the downstream device. When the TTL is decreased to 0, the message is not forwarded. On a small-scale network, State-Refresh messages are transmitted circularly on the network. You can modify the TTL according to the network scale by running the [**state-refresh-ttl**](cmdqueryname=state-refresh-ttl) command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command takes effect only on the Router directly connected to the multicast source.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.