Configuring a Layer 3 Ethernet Sub-interface
============================================

Configuring a Layer 3 Ethernet Sub-interface

#### Context

When a device connects to a Layer 3 network, you can configure Layer 3 Ethernet sub-interfaces to implement Layer 3 communication between users in different VLANs and on different network segments.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet main interface view and switch the interface working mode to Layer 3.
   
   
   ```
   interface interface-type interface-number
   undo portswitch
   ```
3. Create a Layer 3 Ethernet sub-interface and enter its view.
   
   
   ```
   interface interface-type interface-number.subnumber
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```