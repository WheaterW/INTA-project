Understanding DHCP Snooping
===========================

After DHCP snooping is enabled on a device, the device forwards a DHCP request message from a DHCP client to a valid DHCP server through a trusted interface. The device then generates DHCP snooping binding entries based on the DHCPACK message received from the server. After receiving a DHCP message from a DHCP client through a DHCP snooping-enabled interface, the device checks whether the message's information matches the DHCP snooping binding entries. In this way, the device is able to defend against DHCP attacks.

#### DHCP Snooping Trust Function

The DHCP snooping trust function ensures that clients obtain IP addresses from a valid DHCP server.

If a bogus DHCP server exists on the network shown in [Figure 1](#EN-US_CONCEPT_0000001564120377__fig431243175213), DHCP clients may obtain incorrect IP addresses and network configuration parameters from the bogus server, which will lead to communication failures. The DHCP snooping trust function can control the source of DHCP reply messages to prevent bogus DHCP servers from allocating IP addresses and other configurations to DHCP clients.

The DHCP snooping trust function involves two interface roles: trusted interface and untrusted interface.

* A trusted interface accepts DHCPACK, DHCPNAK, and DHCPOFFER messages from the DHCP server.
* An untrusted interface discards DHCPACK, DHCPNAK, and DHCPOFFER messages sent by the DHCP server.

When DHCP snooping is enabled on a Layer 2 access device, the interface directly or indirectly connected to a valid DHCP server is typically configured as a trusted interface (for example, interface 3 in [Figure 1](#EN-US_CONCEPT_0000001564120377__fig431243175213)), and other interfaces are configured as untrusted interfaces (for example, interface 4 in [Figure 1](#EN-US_CONCEPT_0000001564120377__fig431243175213)). As such, DHCP request messages from DHCP clients are forwarded only through the trusted interface. In this way, the clients can obtain IP addresses only from the valid DHCP server, thereby preventing a bogus DHCP server from assigning IP addresses.

**Figure 1** Network diagram of the DHCP snooping trust function  
![](../images/en-us_image_0000001512681230.png)

#### DHCP Snooping Binding Table

In the DHCP scenario shown in [Figure 2](#EN-US_CONCEPT_0000001564120377__fig98881428174319), the clients connected to the Layer 2 access device are configured to automatically obtain IP addresses. A DHCP client broadcasts a DHCP request message, and the DHCP snooping-enabled Layer 2 access device forwards the message to the DHCP server through the trusted interface. The DHCP server then unicasts a DHCPACK message carrying IP address information to the client. During this process, the Layer 2 access device obtains key information (including the client's MAC address, IP address, and address lease) from the received DHCPACK message, learns information (including the interface number and the ID of the VLAN to which the interface belongs) about the DHCP snooping-enabled interface connected to the client, and generates a DHCP snooping binding table based on the information. For example, in [Figure 2](#EN-US_CONCEPT_0000001564120377__fig98881428174319), after receiving a DHCPACK message for Client1, the Layer 2 access device obtains information about IP address 10.0.0.2, MAC address MACA, and the interface (interface 2) connected to the client from the message, and then generates a DHCP snooping binding entry based on the information.

**Figure 2** Network diagram of the DHCP snooping binding table  
![](../images/en-us_image_0000001564000645.png)

The DHCP snooping binding table ages out when the DHCP lease expires, or the corresponding entries are automatically deleted when users send DHCPRELEASE messages to release IP addresses.

The DHCP snooping binding table records parameters such as mappings between the IP and MAC addresses of DHCP clients. A device can check DHCP messages against the table to prevent attacks initiated by unauthorized users.

To ensure that a device can obtain parameters such as a user's MAC address when generating DHCP snooping binding entries, DHCP snooping needs to be applied to the access device on the Layer 2 network or the first DHCP relay agent.