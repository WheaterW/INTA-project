Disabling a Device from Checking TTL Values in VRRP6 Advertisement Packets
==========================================================================

Disabling a Device from Checking TTL Values in VRRP6 Advertisement Packets

#### Context

A VRRP-enabled device checks the TTL value in every received VRRP6 Advertisement packet, and discards packets if their TTL is not 255. On a network where devices of different vendors are deployed, a device with TTL check enabled may incorrectly discard valid packets. In this case, disable TTL check so that devices of different vendors can communicate.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP6 group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable the device from checking TTL values in received VRRP6 Advertisement packets.
   ```
   [vrrp6 hop-limit-check disable](cmdqueryname=vrrp6+hop-limit-check+disable)
   ```
   
   By default, a device checks TTL values in received VRRP6 Advertisement packets.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.