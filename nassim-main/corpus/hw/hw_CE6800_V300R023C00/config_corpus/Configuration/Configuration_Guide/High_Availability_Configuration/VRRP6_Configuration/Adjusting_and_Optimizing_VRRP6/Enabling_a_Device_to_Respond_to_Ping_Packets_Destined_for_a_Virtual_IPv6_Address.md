Enabling a Device to Respond to Ping Packets Destined for a Virtual IPv6 Address
================================================================================

Enabling a Device to Respond to Ping Packets Destined for a Virtual IPv6 Address

#### Context

To monitor the connectivity of the link between hosts and a VRRP6 device (gateway), enable the device to respond to the ping packets destined for the virtual IPv6 address of the VRRP6 group to which the device belongs.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to respond to ping packets destined for a virtual IPv6 address.
   ```
   [undo vrrp virtual-ip ping disable](cmdqueryname=undo+vrrp+virtual-ip+ping+disable)
   ```
   
   By default, the master device in a VRRP6 group is enabled to respond to ping packets destined for a virtual IPv6 address of the VRRP6 group.
   
   After this function is enabled, hosts can ping a virtual IPv6 address, which may expose the device to ICMPv6 attacks. In this case, run the [**vrrp virtual-ip ping disable**](cmdqueryname=vrrp+virtual-ip+ping+disable) command to disable the ping function.
3. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.