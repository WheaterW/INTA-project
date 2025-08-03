Configuring the Internal Server Function
========================================

The internal server function can be configured on a private network so that external users can access the server through a NAT device.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run one of the following commands to configure an internal server:
   
   
   * If multiple internal servers are assigned the same public IP address, run the [**nat server protocol**](cmdqueryname=nat+server+protocol) { **tcp** | **udp** | *protocol-number* } **global** *global-address* [ *global-protocol* ] [ **vpn-instance** *global-vpn-instance-name* ] **inside** *inside-address* [ *inside-protocol* ] [ **vpn-instance** *inside-vpn-instance-name* ] [ **redirect** *redirect-ip-address* { **inbound** | **outbound** } ] command to configure the internal servers that each runs a specific protocol.
   * If each internal server is assigned a specific IP address, run the [**nat server global**](cmdqueryname=nat+server+global) *global-address* [ **vpn-instance** *global-vpn-instance-name* ] **inside** *inside-address* [ **vpn-instance** *inside-vpn-instance-name* ] [ **redirect** *redirect-ip-address* { **inbound** | **outbound** } ] command to configure an internal server.
   * To conserve public IP addresses by borrowing an interface address for an internal server, run the [**nat server protocol**](cmdqueryname=nat+server+protocol) { **tcp** | **udp** | *protocol-number* } **global** **unnumbered** **interface** *interface-type* *interface-number* *global-protocol* **inside** *host-address* *host-protocol* [ **vpn-instance** *vpn-instance-name* ] [ **redirect** *redirect-ip-address* { **inbound** | **outbound** } ] command to configure the multiplexing relationship between an internal server running a specific protocol and an interface in a simplified NAT instance.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address of the NAT internal server must be different from the IP address of a DHCP server. Otherwise, a message indicating a conflict is displayed.
   
   The public IP address of the address-level internal server must differ from an assigned public IP address in the NAT address pool.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.