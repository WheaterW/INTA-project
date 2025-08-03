Enabling the DHCPv6 Server Function
===================================

Enabling the DHCPv6 Server Function

#### Context

There are two ways in which you can enable the DHCPv6 server function: specifying an address pool or enabling automatic searching for an address pool.

* Specifying an address pool in the interface view.After you enable the DHCPv6 server function on an interface and bind an IPv6 address pool to it, the device assigns IPv6 addresses or other configuration parameters (such as the DNS server address) to the clients connected to this interface from the bound address pool when the interface receives DHCPv6 request messages from the clients.
  + If a DHCPv6 server and clients reside on the same link (that is, a DHCPv6 relay agent does not exist), the device can assign IPv6 addresses or other configuration parameters (such as the DNS server address) to the clients.
  + If a DHCPv6 server and clients reside on different links (that is, a DHCPv6 relay agent exists), the device can assign IPv6 addresses or other configuration parameters (such as the DNS server address) to the clients in one network segment through the relay agent.

* Enabling automatic searching for an address pool in the interface view.
  
  When a DHCPv6 server and clients reside on different links (that is, a DHCPv6 relay agent exists), only one IPv6 address pool can be specified on an interface. Therefore, configuration parameters such as IPv6 addresses can be assigned to the clients only in one network segment through the relay agent. To use the DHCPv6 relay agent to assign configuration parameters (such as IPv6 addresses) to DHCPv6 clients in multiple network segments, enable automatic searching for an address pool in the interface view. The server matches an appropriate address pool based on the link address in a relay message.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address prefix-length* |*ipv6-address*/*prefix-length* }
   
   
   
   A global unicast address is configured for the interface.
5. Run [**dhcpv6 server**](cmdqueryname=dhcpv6+server) { *pool-name* | **auto-select** } [ **preference** *preference-value* | **rapid-commit** | **unicast** ] \*
   
   
   
   The DHCPv6 server function is enabled on the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can specify the **auto-select** parameter to enable automatic searching for an address pool. If the existing configurations in the IPv6 address pool view cannot identify the link of a DHCPv6 client, you can run the [**link-address**](cmdqueryname=link-address) *ipv6-address*/*prefix-length* command to configure a link prefix, thereby defining the link scope of the client.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

For clients (such as PCs) that automatically obtain IPv6 addresses based on IPv6 RA messages by default, flags in RA messages need to be configured on the client gateway. This is necessary so that the clients can obtain IPv6 addresses using DHCPv6. When the device functions as a client gateway, perform the following operations:

* When no DHCPv6 relay agent exists and the device functions as a client gateway:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run [**undo ipv6 nd ra halt**](cmdqueryname=undo+ipv6+nd+ra+halt)
     
     The device is enabled to send RA messages.
  4. Run [**ipv6 nd autoconfig managed-address-flag**](cmdqueryname=ipv6+nd+autoconfig+managed-address-flag)
     
     The managed address configuration flag of stateful address autoconfiguration in an RA message is configured.
  5. Run [**ipv6 nd autoconfig other-flag**](cmdqueryname=ipv6+nd+autoconfig+other-flag)
     
     The other configuration flag of stateful address autoconfiguration in an RA message is configured.
     
     After the managed address configuration and other configuration flags of stateful address autoconfiguration in an RA message are configured, the clients can obtain IPv6 addresses using DHCPv6.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* When a DHCPv6 relay agent exists and functions as a client gateway, perform the preceding operations on the DHCPv6 relay agent.