Configuring a DHCP Client
=========================

With the DHCP client function configured, a device uses DHCP to dynamically request an IP address from the DHCP server. This achieves appropriate assignment and centralized management of IP addresses.

#### Background

The Dynamic Host Configuration Protocol (DHCP) dynamically assigns IP addresses to hosts and centrally manages host configurations. DHCP uses the client/server model. A client applies to the server for configuration parameters (such as an IP address), and the server replies with the requested configuration parameters.

Some DHCP clients use a fixed IP address for a long time, and some DHCP clients use a temporary IP address. After a DHCP client's lease time is expired, the DHCP server reclaims the IP address of the DHCP client and allocates this IP address to another DHCP client. You can configure an expected lease time for a DHCP client as required. In this case, while assigning an address lease time, the DHCP server compares the expected lease time with the address lease time of the current address pool and provides the DHCP client an appropriate lease time based on address assignment rules.


#### Pre-configuration Tasks

Before configuring the DHCP client function, complete the following tasks:

Configure another device on the network as a DHCP server. For details, see [Configuring a DHCP Server](dc_vrp_dhcp_server_cfg_0011.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. (Optional) Run [**dhcpc option60 redefined**](cmdqueryname=dhcpc+option60+redefined) *option60Value*
   
   Option 60 to be carried in DHCP messages is configured.
3. (Optional) Run [**dhcpc unicast-flag enable**](cmdqueryname=dhcpc+unicast-flag+enable)
   
   The Bootp flags field value in a DHCP request message is set to 0x0000 (Unicast).
   
   By default, DHCP request and response messages are broadcast ones. If the client requires the server to respond in unicast mode for security, run the [**dhcpc unicast-flag enable**](cmdqueryname=dhcpc+unicast-flag+enable) command to set the Bootp flags field value in a DHCP request message to 0x0000 (Unicast) before enabling the DHCP client function.
4. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   The view of the interface to be enabled with the DHCP client function is displayed.
5. Run [**ip address dhcp-alloc**](cmdqueryname=ip+address+dhcp-alloc)
   
   The DHCP client function is enabled on the interface.
   
   After the DHCP client function is enabled, pay attention to the following points:
   
   * If multiple logical interfaces are planned to apply for addresses from the same DHCP server, you are advised to configure different MAC addresses for the logical interfaces. Otherwise, address application may fail.
   * When the DHCP client function is enabled on an interface, the DHCP client cannot process FORCERENEW messages.
   * When the DHCP client function is enabled on an interface, the dynamic IP address obtained by the DHCP client may conflict with the MAP public address segment. As such, ensure that IP addresses do not conflict or overlap during network planning.
6. (Optional) Run [**dhcp client expected-lease**](cmdqueryname=dhcp+client+expected-lease) *lease-time*
   
   The expected IP address lease time for the DHCP client is configured.
7. (Optional) Run [**dhcpc option60 redefined**](cmdqueryname=dhcpc+option60+redefined) *option60Value*
   
   Option 60 to be carried in DHCP messages is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If Option 60 is configured in both the system view and interface view, the configuration in the interface view takes effect.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Follow-up Procedure

When a DHCP client no longer uses the assigned IP address, run the [**dhcp release**](cmdqueryname=dhcp+release) command so that the DHCP client proactively sends a DHCP Release message to the DHCP server to notify the DHCP server of releasing IP address. If this command is run in the system view, the IP addresses requested by all interfaces from the DHCP server are released. If this command is run in the interface view, only the IP address requested by the specific interface is released from the DHCP server.


#### Verifying the Configuration

* Run the [**display dhcp client-info**](cmdqueryname=display+dhcp+client-info) [ **interface** *interface-type* *interface-number* ] command to view status information of a DHCP client.