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
3. Adjust BFD parameters, including the minimum interval at which BFD control packets are sent, the minimum interval at which BFD control packets are received, and the local detection multiplier.
   
   
   ```
   [pim bfd](cmdqueryname=pim+bfd) { min-tx-interval tx-value | min-rx-interval rx-value | detect-multiplier multiplier-value } 
   ```
   
   
   
   By default, the **min-tx-interval**, **min-rx-interval**, and **detect-multiplier** values are 10 ms, 10 ms, and 3, respectively.
   
   If the same BFD parameters are configured for other protocols, the configured BFD parameters may be affected.
   
   The negotiation mechanism of the actual sending interval, receiving interval, and detection period of BFD control packets is as follows:
   * Actual sending and receiving intervals:
     + Actual sending interval = max (local **min-tx-interval**, remote **min-rx-interval**)
     + Actual receiving interval = max (remote **min-tx-interval**, local **min-rx-interval**)
   * Actual detection period = remote **detect-multiplier** x max (remote **min-tx-interval**, local **min-rx-interval**)BFD parameters can be set on both the sending and receiving ends, and both configurations take effect.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```