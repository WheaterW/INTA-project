Adjusting Control Parameters for PIM-DM State-Refresh Messages
==============================================================

Adjusting Control Parameters for PIM-DM State-Refresh Messages

#### Prerequisites

Before adjusting PIM-DM State-Refresh control parameters, complete the following task:

[Configuring Basic PIM-DM Functions](vrp_pim_cfg_0007.html)


#### Context

The PIM-DM state is refreshed through State-Refresh messages that are sent periodically on the network. When a device in the pruned state receives a State-Refresh message, it resets the Prune state timer, which prevents the downstream interface from forwarding data when the timer expires.

By default, all devices can forward State-Refresh messages. If you want multicast data to be flooded on the entire network upon each flooding-prune occasion, disable forwarding of State-Refresh messages so that suppression of the pruned interface on the device does not depend on State-Refresh message forwarding.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
3. Configure time control parameters for State-Refresh messages as required.
   
   
   
   **Table 1** Configuring time control parameters for State-Refresh messages
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set an interval at which a PIM device directly connected to a multicast source sends State-Refresh messages. | [**state-refresh-interval**](cmdqueryname=state-refresh-interval) *interval* | The PIM device directly connected to a multicast source sends State-Refresh messages downstream at intervals. |
   | Set a suppression time for State-Refresh messages. | [**state-refresh-rate-limit**](cmdqueryname=state-refresh-rate-limit) *interval* | After a device receives a State-Refresh message corresponding to an (S, G) entry, the device starts a timer and sets the timer value to the suppression time carried in the message. If the device receives the same State-Refresh message within the timer, it drops the received message. |
   | Set a TTL value for State-Refresh messages. | [**state-refresh-ttl**](cmdqueryname=state-refresh-ttl) *ttl-value* | When a device receives a State-Refresh message, it reduces the TTL value of the message by 1 and forwards the message downstream. The State-Refresh message is transmitted on the network until its TTL value reduces to 0.  Because State-Refresh messages originate from the first-hop PIM device connected to a multicast source, the TTL value of State-Refresh messages must be configured on the first-hop device. |
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Disable forwarding of State-Refresh messages.
   
   
   ```
   [undo pim state-refresh-capable](cmdqueryname=undo+pim+state-refresh-capable)
   ```
   
   
   
   By default, forwarding of State-Refresh messages is enabled on the interface. Disabling forwarding of State-Refresh messages is not recommended because the State-Refresh mechanism conserves network resources.
   
   If an interface is disabled from forwarding State-Refresh messages, you can run the [**pim state-refresh-capable**](cmdqueryname=pim+state-refresh-capable) command on the interface to enable it to forward State-Refresh messages again.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```