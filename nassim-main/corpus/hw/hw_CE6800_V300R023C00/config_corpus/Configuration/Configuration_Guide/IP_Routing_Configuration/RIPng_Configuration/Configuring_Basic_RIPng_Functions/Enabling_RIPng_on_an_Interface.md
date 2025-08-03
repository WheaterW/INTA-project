Enabling RIPng on an Interface
==============================

Enabling RIPng on an Interface

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   
   
   The interface is the network-side interface connecting one routing device to another. To enable the routing device to learn routes on the network segment where the interface resides, ensure that the link status of the interface is up.
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface mode.
4. Enable RIPng on the interface.
   
   
   ```
   [ripng](cmdqueryname=ripng) process-id enable
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If IPv6 is not enabled on the interface, this command cannot be executed.
   * If multiple interfaces on a routing device are connected to other devices, repeat Step 2 and Step 3.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```