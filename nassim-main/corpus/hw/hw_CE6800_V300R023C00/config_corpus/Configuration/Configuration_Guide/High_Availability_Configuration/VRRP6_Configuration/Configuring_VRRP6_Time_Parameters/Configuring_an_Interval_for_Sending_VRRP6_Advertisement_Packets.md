Configuring an Interval for Sending VRRP6 Advertisement Packets
===============================================================

Configuring an Interval for Sending VRRP6 Advertisement Packets

#### Context

A backup device may fail to receive VRRP6 Advertisement packets before the configured timeout period expires, leading to incorrect preemption of the master role due to heavy network traffic or timer differences between devices. To resolve this problem, set the interval for sending VRRP6 Advertisement packets on the master device to a larger value.


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
4. Configure an interval for the master device in the VRRP6 group to send VRRP6 Advertisement packets.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id timer advertise advertise-interval
   ```
   The default interval is 1 second.![](public_sys-resources/note_3.0-en-us.png) 
   
   The interval at which a device sends VRRP6 Advertisement packets cannot be less than the time required to perform a master/backup VRRP switchover, as this may lead to protocol flapping during the switchover. It is recommended that the interval be set to a value greater than 1s.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.