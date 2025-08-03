Configuring the NAT Server Function
===================================

The NAT Server function can be configured on a private network so that external users can access the server through a NAT device.

#### Usage Scenario

NAT can be configured to allow users on a private network to access public network services, while hiding the structure of the private network and devices on the private network. In this case, a user on an external network cannot communicate with a private network user.

To address this problem, the internal NAT Server can be configured to implement reverse translation from a public IP address to a private IP address by statically configuring the mapping between "a private IP address and a port number" and "a public IP address and a port number" or between a private IP address and a public IP address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. (Optional) Create a NAT address pool. For details, see [Creating a NAT Address Pool](dc_ne_nat_cfg_0013.html).
   
   
   
   When a user accesses the internal NAT Server, a user entry needs to be created. If the [**nat server-mode enable**](cmdqueryname=nat+server-mode+enable) command is not run to enable the address-level NAT Server mode, the public IP address in the user entry is obtained from the NAT address pool. In this case, a NAT address pool needs to be configured.
4. (Optional) Run [**nat server-mode enable**](cmdqueryname=nat+server-mode+enable)
   
   
   
   The address-level NAT Server mode is enabled.
   
   
   
   When a user accesses the internal NAT Server, a user entry needs to be created. After the address-level NAT Server mode is enabled, the public IP address in the user entry used for NAT Server access is not obtained from a NAT address pool. Instead, the public IP address is obtained through the [**nat server global inside**](cmdqueryname=nat+server+global) command.
5. (Optional) Run [**nat server session enhance enable**](cmdqueryname=nat+server+session+enhance+enable)
   
   
   
   The device is enabled to create a session after the device receives the first TCP packet that matches the NAT Server mapping.
6. Run any of the following commands to configure a NAT Server:
   
   
   * If multiple internal servers are assigned the same public IP address, run the [**nat server protocol**](cmdqueryname=nat+server+protocol+tcp+udp+global+vpn-instance+inside) { **tcp** | **udp** | *protocol-number* } **global** *global-address* [ *global-protocol* ] [ **vpn-instance** *global-vpn-instance-name* ] **inside** *inside-address* [ *inside-protocol* ] [ **vpn-instance** *inside-vpn-instance-name* ] [ **outbound** ] command to configure internal NAT Servers for different types of packets.
     
     To configure one-to-many relationships between public IP addresses and internal servers in batches, run the [**nat server protocol**](cmdqueryname=nat+server+protocol+tcp+udp+global+mask+vpn-instance+inside+mask) { **tcp** | **udp** | *protocol-number* } **global** *global-start-address* { *global-end-address* | **mask** { *global-address-mask-length* | *global-address-mask* } } [ *global-protocol* ] [ **vpn-instance** *vpn-instance-name* ] **inside** *host-start-address* { *host-end-address* | **mask** { *host-address-mask-length* | *host-address-mask* } } [ *host-protocol* ] [ **vpn-instance** *vpn-instance-name* ] command.
   * If each internal server is assigned a specific public IP address, run the [**nat server global**](cmdqueryname=nat+server+global+vpn-instance+inside+vpn-instance) *global-address* [ **vpn-instance** *vpn-instance-name* ] **inside** *inside-address* [ **vpn-instance** *vpn-instance-name* ] command to configure an internal NAT server.
     
     To configure one-to-one relationships between public IP addresses and internal servers in batches, run the [**nat server global**](cmdqueryname=nat+server+global+mask+vpn-instance+inside+mask+vpn-instance) *global-start-address* { *global-end-address* | **mask** { *global-address-mask-length* | *global-address-mask* } } [ **vpn-instance** *vpn-instance-name* ] **inside** *host-start-address* { *host-end-address* | **mask** { *host-address-mask-length* | *host-address-mask* } } [ **vpn-instance** *vpn-instance-name* ] command.
   * To conserve public IP addresses and allow an internal NAT Server to reuse interface addresses, run the [**nat server protocol**](cmdqueryname=nat+server+protocol+tcp+udp+global+unnumbered+interface+inside) { **tcp** | **udp** | *protocol-number* } **global** **unnumbered** **interface** { *interface-name* | *interface-type* *interface-number* } *global-protocol* **inside** *host-address* *host-protocol* [ **vpn-instance** *vpn-instance-name* ] command to create a reusing relationship between the internal NAT Server and interface address for different types of packets.
   * If an internal server is assigned multiple public IP addresses, run the [**nat server global**](cmdqueryname=nat+server+global+vpn-instance+inside+vpn-instance+extendable) *global-address* [ **vpn-instance** *vpn-instance-name* ] **inside** *inside-address* [ **vpn-instance** *vpn-instance-name* ] [ **extendable** ], [**nat server protocol**](cmdqueryname=nat+server+protocol+tcp+udp+global+vpn-instance+inside) { **tcp** | **udp** | *protocol-number* } **global** *global-address* [ *global-protocol* ] [ **vpn-instance** *global-vpn-instance-name* ] **inside** *inside-address* [ *inside-protocol* ] [ **vpn-instance** *inside-vpn-instance-name* ] [ **extendable** ], or [**nat server protocol**](cmdqueryname=nat+server+protocol+tcp+udp+global+unnumbered+interface+inside) { **tcp** | **udp** | *protocol-number* } **global** **unnumbered** **interface** { *interface-name* | *interface-type* *interface-number* } *global-protocol* **inside** *host-address* *host-protocol* [ **vpn-instance** *vpn-instance-name* ] [ **extendable** ] command to configure an internal NAT Server.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The IP address of the NAT Server cannot be the same as the IP address of a DHCP server. Otherwise, a message indicating a conflict is displayed.
   * If the [**nat server-mode enable**](cmdqueryname=nat+server-mode+enable) command is not run, the public IP address of the address-level NAT Server must differ from an assigned public IP address in the NAT address pool.
   * If no NAT address pool is configured in a NAT instance, you must run the [**nat server-mode enable**](cmdqueryname=nat+server-mode+enable%E3%80%82) command to enable the address-level NAT Server function.
   * The port-level NAT Server mode uses the [**nat server protocol global inside**](cmdqueryname=nat+server+protocol) command to implement address and port translation between public and private addresses for internal servers. A user entry needs to be created when a user accesses a NAT server. To create this entry, a public IP address must be obtained from a NAT address pool, which therefore must be configured in a NAT instance.
   * If the [**nat server-mode enable**](cmdqueryname=nat+server-mode+enable) command is not run, the [**nat outbound**](cmdqueryname=nat+outbound) command must be run to bind an address-level NAT Server to a NAT address pool.
   * A port-level NAT Server must be bound to a NAT address pool using the [**nat outbound**](cmdqueryname=nat+outbound) command.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.