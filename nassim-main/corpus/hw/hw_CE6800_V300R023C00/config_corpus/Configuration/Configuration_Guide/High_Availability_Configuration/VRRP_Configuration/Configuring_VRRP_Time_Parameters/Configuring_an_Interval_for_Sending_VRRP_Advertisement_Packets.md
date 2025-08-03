Configuring an Interval for Sending VRRP Advertisement Packets
==============================================================

Configuring an Interval for Sending VRRP Advertisement Packets

#### Context

A backup device may fail to receive VRRP Advertisement packets before the configured timeout period expires, leading to incorrect preemption of the master role due to heavy network traffic or timer differences between devices. To resolve this problem, set the interval for sending VRRP Advertisement packets on the master device to a larger value.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to learn the interval at which VRRP Advertisement packets are sent.
   ```
   [undo vrrp timer advertise learning disable](cmdqueryname=undo+vrrp+timer+advertise+learning+disable)
   ```
   
   By default, this function is enabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   During a master/backup VRRP switchover, do not disable the device from learning the interval. Otherwise, dual master devices may coexist.
3. Enter the view of the interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Configure an interval for sending VRRP Advertisement packets.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id timer advertise advertise-interval
   ```
   
   The default interval is 1 second.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The interval at which a device sends VRRP Advertisement packets cannot be less than the time required to perform a master/backup VRRP switchover, as this may lead to protocol flapping during the switchover. It is recommended that the interval be set to a value greater than 1s.
6. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.