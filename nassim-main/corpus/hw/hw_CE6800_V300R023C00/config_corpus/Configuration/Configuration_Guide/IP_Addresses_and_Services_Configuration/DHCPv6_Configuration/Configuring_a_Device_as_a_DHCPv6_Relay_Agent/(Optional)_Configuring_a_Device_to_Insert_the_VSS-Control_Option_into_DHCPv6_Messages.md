(Optional) Configuring a Device to Insert the VSS-Control Option into DHCPv6 Messages
=====================================================================================

(Optional) Configuring a Device to Insert the VSS-Control Option into DHCPv6 Messages

#### Context

In inter-VPN address allocation scenarios, a DHCPv6 client and server are not in the same VPN. To enable the DHCPv6 server to search for an address pool based on the VPN to which the client belongs and allocate an address to the client, configure the device functioning as a DHCPv6 relay agent to insert the VSS-Control option into DHCPv6 messages.

After this function is configured, the device inserts the VSS-Control option into a Request message received from a client, constructs a Relay-forward message, and forwards the message to the DHCPv6 server. The server then parses the VSS-Control option to obtain the VPN information of the client.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DHCP.
   
   
   ```
   [dhcp enable](cmdqueryname=dhcp+enable)
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Configure the device to insert the VSS-Control option into DHCPv6 messages.
   
   
   ```
   [dhcpv6 relay vss-control insert enable](cmdqueryname=dhcpv6+relay+vss-control+insert+enable)
   ```
   
   By default, a device is disabled from inserting the VSS-Control option into DHCPv6 messages.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```