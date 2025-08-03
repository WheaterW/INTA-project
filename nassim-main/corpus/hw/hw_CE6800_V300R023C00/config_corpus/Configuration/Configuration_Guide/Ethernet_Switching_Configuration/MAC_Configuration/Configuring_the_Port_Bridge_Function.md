Configuring the Port Bridge Function
====================================

Configuring the Port Bridge Function

#### Context

The port bridge function enables an interface to forward packets whose source and destination MAC addresses are both learned on the interface. By default, an interface discards packets whose source and destination MAC addresses are both learned on itself. When enabled with the port bridge function, the interface forwards such packets if their destination MAC addresses are found in the MAC address table.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 3 to Layer 2. Determine whether to perform this step based on the current interface working mode.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
4. Enable the port bridge function.
   
   
   ```
   [port bridge enable](cmdqueryname=port+bridge+enable)
   ```
   
   By default, the port bridge function is disabled on an interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```