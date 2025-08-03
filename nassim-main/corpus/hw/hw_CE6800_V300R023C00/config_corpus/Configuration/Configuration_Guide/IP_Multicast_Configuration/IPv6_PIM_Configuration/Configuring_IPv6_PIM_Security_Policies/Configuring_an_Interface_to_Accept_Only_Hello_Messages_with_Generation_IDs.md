Configuring an Interface to Accept Only Hello Messages with Generation IDs
==========================================================================

Configuring an Interface to Accept Only Hello Messages with Generation IDs

#### Context

After IPv6 PIM-SM is enabled on an interface, the device generates a random number as the generation ID of a Hello message. When the device status changes, a new generation ID is generated. If the device finds that a Hello message received from the same IPv6 PIM neighbor carries a different generation ID, the device determines that the status of the IPv6 PIM neighbor has changed.


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
4. Configure the device to accept only Hello messages with generation IDs and reject Hello messages without any generation IDs.
   
   
   ```
   [pim ipv6 require-genid](cmdqueryname=pim+ipv6+require-genid)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```