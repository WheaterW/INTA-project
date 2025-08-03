Disabling an Interface from Accepting RIPng Update Messages
===========================================================

Disabling an Interface from Accepting RIPng Update Messages

#### Context

Disabling an interface from accepting RIPng update messages is a method used to prevent routing loops. When a device running RIPng is connected to a network running other routing protocols, you can run the [**undo ripng input**](cmdqueryname=undo+ripng+input) command on the interface that connects the RIPng device to the network to prevent the interface from accepting unnecessary update messages from the network.


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
   
   Determine whether to perform this step based on the current interface mode.
4. Disable the interface from accepting RIPng update messages.
   
   
   ```
   [undo ripng input](cmdqueryname=undo+ripng+input)
   ```
   
   
   
   By default, an interface can accept RIPng update messages.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```