Configuring Association Between VRRP and Route Status
=====================================================

Configuring Association Between VRRP and Route Status

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
4. Associate the VRRP group with a route.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id track ip route ip-address { mask-address | mask-length } [ vpn-instance vpn-instance-name ] [ { reduce value-reduced | increase increased-value } ]
   ```
   
   By default, if the tracked route is withdrawn or becomes inactive, the master device in the VRRP group reduces its priority by 10.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.