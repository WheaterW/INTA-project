Configuring Association Between VRRP6 and Route Status
======================================================

Configuring Association Between VRRP6 and Route Status

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
4. Configure association between VRRP6 and route status.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-ID track ipv6 route ip-address mask-length [ vpn-instance vpn-name ] [ { reduce reduced-value|increase increased-value } ]
   ```
   
   By default, if the tracked route is withdrawn or becomes inactive, the master device in a VRRP6 group reduces its priority by 10.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP6 group status.