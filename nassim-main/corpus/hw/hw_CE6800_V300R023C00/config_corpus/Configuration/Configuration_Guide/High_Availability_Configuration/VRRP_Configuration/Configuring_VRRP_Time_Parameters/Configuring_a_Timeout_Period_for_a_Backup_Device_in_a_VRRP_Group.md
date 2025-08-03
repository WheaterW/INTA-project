Configuring a Timeout Period for a Backup Device in a VRRP Group
================================================================

Configuring a Timeout Period for a Backup Device in a VRRP Group

#### Context

By default, the timeout period after which a backup device in a VRRP group assumes the master role is three times the interval at which VRRP Advertisement packets are sent. You can configure a timeout period by specifying a multiplier of this interval as required. If the backup device does not receive any VRRP Advertisement packet before the timeout period expires, it switches to the Master state.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure a timeout period by specifying a multiplier (*holding-multiplier-value*) of the interval at which VRRP Advertisement packets are sent.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id holding-multiplier holding-multiplier-value
   ```
   
   By default, the timeout period of a backup device in a VRRP group is three times the interval at which VRRP Advertisement packets are sent.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.