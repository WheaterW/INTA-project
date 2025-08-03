Disabling an Interface from Sending RIPng Update Messages
=========================================================

Disabling an Interface from Sending RIPng Update Messages

#### Context

Disabling an interface from sending RIPng update messages is a method used to prevent routing loops. When a device running RIPng is connected to a network running other routing protocols, you can run the [**undo ripng output**](cmdqueryname=undo+ripng+output) command on the interface that connects the RIPng device to the network to prevent the interface from sending unnecessary update messages to the network.


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
4. Disable the interface from sending RIPng update messages.
   
   
   ```
   [undo ripng output](cmdqueryname=undo+ripng+output)
   ```
   
   
   
   By default, an interface can send RIPng update messages.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```