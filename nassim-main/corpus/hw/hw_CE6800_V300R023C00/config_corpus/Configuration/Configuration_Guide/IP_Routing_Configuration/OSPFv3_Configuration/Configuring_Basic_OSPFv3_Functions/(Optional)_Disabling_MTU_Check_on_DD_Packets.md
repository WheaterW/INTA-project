(Optional) Disabling MTU Check on DD Packets
============================================

(Optional) Disabling MTU Check on DD Packets

#### Context

To allow an OSPFv3 device to accept DD packets with the MTU field being 0, you can disable the OSPFv3 interface on the device from checking the DD field in received DD packets.

Perform the following steps on the device that runs OSPFv3.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable MTU check on DD packets.
   
   
   ```
   [ospfv3 mtu-ignore](cmdqueryname=ospfv3+mtu-ignore) [ instance instance-id ]
   ```
   
   After this command is run, the interface no longer checks the MTU field in received DD packets.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```