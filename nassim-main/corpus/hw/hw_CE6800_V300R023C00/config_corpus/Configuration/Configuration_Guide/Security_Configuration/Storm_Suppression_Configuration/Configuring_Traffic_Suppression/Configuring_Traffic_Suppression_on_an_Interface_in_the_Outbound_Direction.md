Configuring Traffic Suppression on an Interface in the Outbound Direction
=========================================================================

Configuring Traffic Suppression on an Interface in the Outbound Direction

#### Context

If some interfaces do not need to receive any broadcast packets, unknown multicast packets, or unknown unicast packets (for example, the interfaces are connected to fixed user hosts and demand high security), configure traffic suppression on the interfaces in the outbound direction to block those packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure traffic suppression on an interface in the outbound direction.
   
   
   ```
   [storm suppression](cmdqueryname=storm+suppression) { broadcast | multicast | unknown-unicast } block outbound
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```