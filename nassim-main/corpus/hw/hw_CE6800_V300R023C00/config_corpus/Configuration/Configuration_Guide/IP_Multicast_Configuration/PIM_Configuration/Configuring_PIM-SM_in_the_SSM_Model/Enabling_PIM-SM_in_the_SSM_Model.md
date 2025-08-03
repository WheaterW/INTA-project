Enabling PIM-SM in the SSM Model
================================

Enabling PIM-SM in the SSM Model

#### Prerequisites

After PIM-SM is enabled on the interface connected to another device, the interface can set up PIM neighbor relationships with the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IP multicast routing in the public network instance.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable PIM-SM.
   
   
   ```
   [pim sm](cmdqueryname=pim+sm)
   ```
   
   If you run the [**undo pim sm**](cmdqueryname=undo+pim+sm) command, PIM neighbor and protocol status information on the interface will be deleted. If multicast services are running on the interface, the multicast services will be affected in this case.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```