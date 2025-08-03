(Optional) Enabling the IP Address Blocking Function for Telnet Connections
===========================================================================

The IP address blocking function for Telnet connections prevents IP addresses that fail to be authenticated from logging in to a device through Telnet. If this function is disabled, the device is vulnerable to network attacks.

#### Context

When a device functions as a Telnet server, you can configure the IP address blocking function to protect the device against network attacks, thereby enhancing security.

Perform the following steps on a device that functions as a Telnet server.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**undo telnet server ip-block disable**](cmdqueryname=undo+telnet+server+ip-block+disable) command to enable the IP address blocking function for Telnet connections.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP addresses that fail to be authenticated are blocked only when the IP address blocking function is enabled. This enhances device security.
4. The IP addresses that fail to be authenticated will be locked for 5 minutes. To unlock a locked IP address in advance, perform the following steps:
   1. Run the [**quit**](cmdqueryname=quit) command to exit the system view and enter the user view.
   2. Run the [**activate vty ip-block ip-address**](cmdqueryname=activate+vty+ip-block+ip-address) *ip-address* [ **vpnname** *vpn-name* ] command to unblock the IP address that fails to be authenticated for Telnet connections.