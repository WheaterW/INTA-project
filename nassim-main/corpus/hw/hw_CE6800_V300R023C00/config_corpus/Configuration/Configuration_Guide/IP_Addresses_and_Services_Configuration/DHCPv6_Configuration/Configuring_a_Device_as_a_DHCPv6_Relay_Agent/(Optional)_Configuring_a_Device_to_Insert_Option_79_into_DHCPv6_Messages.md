(Optional) Configuring a Device to Insert Option 79 into DHCPv6 Messages
========================================================================

(Optional) Configuring a Device to Insert Option 79 into DHCPv6 Messages

#### Context

A MAC address is used to identify a DHCPv4 client on an IPv4 network, whereas a DUID is used to identify a DHCPv6 client on an IPv6 network. In IPv4/IPv6 dual-stack scenarios, an administrator wants to use the MAC address of a client to establish a connection with the IPv4/IPv6 addresses obtained by the client and manage the dual-stack client in a unified manner based on the MAC address. However, the MAC address of a DHCPv6 client cannot be identified using a DUID currently.

As defined in the RFC, a DHCPv6 relay agent can fill the link address and type of a client in Option 79. When a device functions as a DHCPv6 relay agent, you can configure the device to insert Option 79 into DHCPv6 messages so that a DHCPv6 server can obtain clients' MAC addresses. After this function is configured, the device inserts Option 79 into a Request message received from a client, constructs a Relay-forward message, and forwards the message to the DHCPv6 server. The server then parses Option 79 to obtain the MAC address of the client.

![](public_sys-resources/note_3.0-en-us.png) 

* Only the first-hop DHCPv6 relay agent supports this function.
* This function takes effect for all interfaces if it is configured in the system view, and takes effect for a specified interface if it is configured in the view of the interface. If this function is configured in both the interface and system views, the configuration in the interface view takes effect.


#### Procedure

* Configure a device to insert Option 79 into DHCPv6 messages in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable DHCP.
     
     
     ```
     [dhcp enable](cmdqueryname=dhcp+enable)
     ```
  3. Configure the device to insert Option 79 into DHCPv6 messages.
     
     
     ```
     [dhcpv6 relay option79 insert enable](cmdqueryname=dhcpv6+relay+option79+insert+enable)
     ```
     
     
     
     By default, a device is disabled from inserting Option 79 into DHCPv6 messages.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a device to insert Option 79 into DHCPv6 messages in the interface view.
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
  5. Configure the device to insert Option 79 into DHCPv6 messages on the interface.
     
     
     ```
     [dhcpv6 relay option79 insert enable](cmdqueryname=dhcpv6+relay+option79+insert+enable)
     ```
     
     By default, a device is disabled from inserting Option 79 into DHCPv6 messages.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```