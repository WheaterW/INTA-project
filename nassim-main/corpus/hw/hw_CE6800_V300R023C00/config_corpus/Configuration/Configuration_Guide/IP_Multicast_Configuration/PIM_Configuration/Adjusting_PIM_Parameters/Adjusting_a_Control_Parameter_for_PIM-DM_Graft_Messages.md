Adjusting a Control Parameter for PIM-DM Graft Messages
=======================================================

Adjusting a Control Parameter for PIM-DM Graft Messages

#### Prerequisites

Before configuring graft control parameters, you have completed the following task:

[Configuring Basic PIM-DM Functions](vrp_pim_cfg_0007.html)


#### Context

To quickly resume multicast forwarding to a pruned device on a network segment, the device sends a Graft message upstream and starts a timer on the interface that sends the message. If the device does not receive multicast data within the timer, it sends another Graft message upstream.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set a Graft message retransmission interval.
   
   
   ```
   [pim timer graft-retry](cmdqueryname=pim+timer+graft-retry) interval
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```