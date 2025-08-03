Configuring MAC Address Flapping Prevention
===========================================

Configuring MAC Address Flapping Prevention

#### Context

You can use either of the following methods to configure MAC address flapping prevention:

* Increase the MAC address learning priority of an interface.
* Prevent MAC address entries from being overridden on interfaces with the same priority.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support MAC address flapping prevention.



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
4. Configure the MAC address learning priority for the interface.
   
   
   ```
   [mac-address learning priority](cmdqueryname=mac-address+learning+priority) priority-id
   ```
   
   
   
   By default, the MAC address learning priority of an interface is 0. The value is in the range from 0 to 3, with a larger value indicating a higher priority.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit) 
   ```
6. Configure the function for preventing MAC address entries from being overridden on interfaces with the same priority.
   
   
   ```
   [undo mac-address learning priority](cmdqueryname=undo+mac-address+learning+priority) priority-id allow-flapping
   ```
   
   
   
   By default, MAC address flapping between interfaces with the same priority is allowed.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```