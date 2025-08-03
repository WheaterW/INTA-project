Enabling a Device to Respond to Ping Packets Destined for a Virtual IP Address
==============================================================================

Enabling a Device to Respond to Ping Packets Destined for a Virtual IP Address

#### Context

To monitor the connectivity of the link between hosts and a VRRP device (gateway), enable the device to respond to the ping packets destined for the virtual IP address of the VRRP group to which the device belongs.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to respond to ping packets destined for a virtual IP address.
   ```
   [undo vrrp virtual-ip ping disable](cmdqueryname=undo+vrrp+virtual-ip+ping+disable)
   ```
   
   By default, the master device in a VRRP group is enabled to respond to ping packets destined for a virtual IP address of the VRRP group.
   
   After this function is enabled, hosts can ping a virtual IP address, which may expose the device to ICMP attacks. In this case, run the [**vrrp virtual-ip ping disable**](cmdqueryname=vrrp+virtual-ip+ping+disable) command to disable the ping function.
3. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.