Configuring Distributed VXLAN Gateways to Function as DHCPv4 Relay Agents
=========================================================================

Configuring Distributed VXLAN Gateways to Function as DHCPv4 Relay Agents

#### Prerequisites

Before configuring distributed VXLAN gateways to function as DHCPv4 relay agents, you have completed the following tasks:

1. Configure a device as a DHCPv4 relay agent. For details, see [Configuring a Device to Function as a DHCPv4 Relay Agent](galaxy_dhcpv4_cfg_0022.html).
2. Configure a device as a distributed VXLAN gateway. For details, see VXLAN Configuration.


#### Context

In a distributed VXLAN gateway scenario, DHCPv4 relay is configured on VBDIF interfaces of distributed gateways. The giaddr field carried in a request message sent from a DHCPv4 relay agent to a DHCPv4 server is the IPv4 address of a VBDIF interface. When the server returns a reply message, it determines the network segment of the client based on the giaddr field. However, the reply message from the DHCPv4 server may be forwarded to other distributed gateways (rather than the device that sends the request message), because the IPv4 addresses of VBDIF interfaces on distributed gateways are the same. As a result, users cannot obtain IPv4 addresses.

The preceding issue can be resolved using the following methods:

* Method 1: Configure Option 82 to carry the return address.
  
  The DHCPv4 relay agent still uses the IPv4 address of the VBDIF interface to communicate with the DHCPv4 server. When sending a request message, the relay agent uses the local VTEP IPv4 address as the return address in Option 82. This address is also carried in a reply message sent by the server. When processing a reply message from the DHCPv4 server, the DHCPv4 relay agent checks whether the reply message corresponds to the request message it sent based on the return address carried in the message. If it does, the relay agent forwards the message to the client. Otherwise, the relay agent performs rerouting based on the VTEP IPv4 address to forward the reply message to the corresponding distributed gateway through a VXLAN tunnel.
* Method 2: Configure the functions to modify the giaddr field in DHCPv4 messages and to insert suboption 5 into Option 82.
  
  Suboption 5: corresponds to the **link-selection** parameter, indicating the gateway IPv4 address of a DHCPv4 relay interface. In an inter-VPN scenario, the [**dhcp relay giaddr source-interface**](cmdqueryname=dhcp+relay+giaddr+source-interface) *interface-type* *interface-num* or [**dhcp relay giaddr outgoing-interface-address**](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address) command generally needs to be run to modify the giaddr field in DHCPv4 messages. This ensures that reply messages from a DHCPv4 server can be successfully forwarded to a DHCPv4 relay agent. In this case, suboption 5 must be used to transmit the giaddr field to the DHCPv4 server. The server selects an address pool based on suboption 5 and then allocates an IPv4 address to a client.

The following table compares the two methods.

| Category | IPv4 Address Used by the DHCPv4 Relay Agent to Communicate with the DHCPv4 Server | Advantage and Disadvantage |
| --- | --- | --- |
| Method 1 | IPv4 address of the VBDIF interface | * The DHCPv4 server does not need to parse suboption 5. * Rerouting: A distributed gateway that does not send request messages may also receive reply messages. |
| Method 2 | Primary IPv4 address of the source interface or outbound interface | * The DHCPv4 server must be able to parse suboption 5. * Precise return: Reply messages can be sent to a correct distributed gateway. |




#### Procedure

* **Method 1: Configure Option 82 to carry the return address.**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure Option 82's suboption 2 (vendor-specific suboption) to carry the device's VTEP IPv4 address.
     
     
     ```
     [dhcp option82 vendor-specific format](cmdqueryname=dhcp+option82+vendor-specific+format) vendor-sub-option 2 ip-address ip-address
     ```
     
     By default, Option 82's suboption 2 (vendor-specific suboption) does not carry a device's VTEP IPv4 address.
  3. Enter the VBDIF interface view.
     
     
     ```
     [interface vbdif](cmdqueryname=interface+vbdif) bd-id
     ```
     
     The number of the VBDIF interface must match an existing BD ID.
  4. Enable the DHCPv4 relay agent to support Option 82.
     
     
     ```
     [dhcp relay information enable](cmdqueryname=dhcp+relay+information+enable)
     ```
     
     By default, a DHCPv4 relay agent does not support Option 82.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* **Method 2: Configure the source interface of DHCPv4 relay messages and the function to insert suboption 5 into Option 82.**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VBDIF interface view.
     
     
     ```
     [interface vbdif](cmdqueryname=interface+vbdif) bd-id
     ```
     
     The number of the VBDIF interface must match an existing BD ID.
  3. Modify the information of the giaddr field.
     
     
     
     Configure the source interface of DHCPv4 relay messages, and use the primary IPv4 address of the interface to fill in the giaddr field. The source interface must be able to communicate with a DHCPv4 server.
     
     ```
     [dhcp relay giaddr source-interface](cmdqueryname=dhcp+relay+giaddr+source-interface) interface-type interface-num
     ```
     
     Or configure the device to use the primary IPv4 address of the outbound interface to fill in the giaddr field.
     
     ```
     [dhcp relay giaddr outgoing-interface-address](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address)
     ```
     
     By default, a device uses the IPv4 address of a DHCPv4 relay agent to fill in the giaddr field.
     
     The [**dhcp relay source-ip-address**](cmdqueryname=dhcp+relay+source-ip-address) and [**dhcp relay gateway**](cmdqueryname=dhcp+relay+gateway) commands are mutually exclusive with the [**dhcp relay giaddr source-interface**](cmdqueryname=dhcp+relay+giaddr+source-interface) and [**dhcp relay giaddr outgoing-interface-address**](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address) commands.
     
     The [**dhcp relay giaddr source-interface**](cmdqueryname=dhcp+relay+giaddr+source-interface) *interface-type* *interface-num* command takes precedence over the [**dhcp relay giaddr outgoing-interface-address**](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address) command.
  4. Enable the DHCPv4 relay interface to insert Option 82's suboption 5 into DHCPv4 messages.
     
     
     ```
     [dhcp option82](cmdqueryname=dhcp+option82) link-selection insert enable
     ```
     
     
     
     By default, a DHCPv4 relay interface does not insert Option 82's suboption 5 into DHCPv4 messages.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```