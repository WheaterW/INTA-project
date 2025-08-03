(Optional) Adjusting BFD Parameters
===================================

(Optional) Adjusting BFD Parameters

#### Context

You can adjust BFD parameters, including the minimum interval at which BFD control packets are sent, the minimum interval at which BFD control packets are received, and the local detection multiplier, as required.


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
4. Adjust BFD parameters, including the minimum interval at which BFD control packets are sent, the minimum interval at which BFD control packets are received, and the local detection multiplier.
   
   
   ```
   [pim ipv6 bfd](cmdqueryname=pim+ipv6+bfd) { min-tx-interval tx-value | min-rx-interval rx-value | detect-multiplier multiplier-value } 
   ```
   
   
   
   By default, the value of **detect-multiplier** is 3.
   
   If the same BFD parameters are configured for other protocols, the configured BFD parameters may be affected.
   
   The negotiation mechanism of the actual sending interval, receiving interval, and detection period of BFD control packets is as follows:
   * Actual sending and receiving intervals:
     + Actual sending interval = max (local **min-tx-interval**, peer **min-rx-interval**)
     + Actual receiving interval = max (remote **min-tx-interval**, local **min-rx-interval**)
   * Actual detection period = remote **detect-multiplier** x max (remote **min-tx-interval**, local **min-rx-interval**)BFD parameters can be set on both the sending and receiving ends, and both configurations take effect.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```