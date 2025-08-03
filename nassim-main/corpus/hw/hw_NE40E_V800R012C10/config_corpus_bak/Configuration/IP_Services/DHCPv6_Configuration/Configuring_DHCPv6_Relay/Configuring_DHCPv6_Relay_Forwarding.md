Configuring DHCPv6 Relay Forwarding
===================================

DHCPv6 relay forwarding functions are configured on the user-side inbound interface of DHCPv6 messages. You can specify the outbound interface, destination DHCPv6 server address, or next-hop DHCPv6 relay agent address.

#### Context

To relay messages sent from DHCPv6 clients on a network segment, configure DHCPv6 relay forwarding on the DHCPv6 relay agent's interface that connects to the network segment. If multiple outbound interfaces or destination IPv6 addresses are specified, the DHCPv6 relay agent forwards one copy of messages to each outbound interface or destination IPv6 address. The destination IPv6 address can be an interface address on the next-hop DHCPv6 relay agent or the DHCPv6 server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**dhcpv6 relay server group**](cmdqueryname=dhcpv6+relay+server+group) *group-name*. A DHCPv6 relay server group is configured, and the server group view is displayed.
   
   
   
   If you want to enable DHCPv6 relay on multiple interfaces and specify the same DHCPv6 relay servers for these interfaces, configure a DHCPv6 relay server group to simplify the configuration.
3. (Optional) Run [**server**](cmdqueryname=server) *server-addr*
   
   
   
   A server is added to the DHCPv6 relay server group.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where DHCPv6 relay needs to be enabled is displayed.
6. Perform either of the following operations as required:
   
   
   * To specify an outbound interface or destination IPv6 address for DHCPv6 messages on the interface, run the [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) { **interface** *interface-type* *interface-number* | **destination** *ipv6-address* } command.
   * To bind the interface to a DHCPv6 relay server group, run the [**dhcpv6 relay binding server group**](cmdqueryname=dhcpv6+relay+binding+server+group) *group-name* command.
7. (Optional) Run [**dhcpv6 relay link-address**](cmdqueryname=dhcpv6+relay+link-address) *ipv6-address*
   
   
   
   A DHCPv6 relay gateway address is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When a DHCPv6 relay agent is connected to a host, it needs to periodically send RA messages to the host. An RA message carries both the IPv6 address prefix and stateful address autoconfiguration flag. You can run the **undo ipv6 nd ra halt** command to enable the agent to send RA messages.
8. (Optional) For the DHCPv6 server that replies with messages based on the source IP address, the DHCPv6 relay agent uses the IP address of the relay interface as the source IP address when forwarding a DHCP request message from a DHCPv6 client. If the source IP address needs to be specified, perform either of the following operations:
   
   
   * Run [**dhcpv6 relay source-ip-address**](cmdqueryname=dhcpv6+relay+source-ip-address) *ipv6-address*
     
     The source IPv6 address is specified for DHCPv6 messages on the interface.
   * Run [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) { *interface-name* | *interface-type* *interface-num* }
     
     The IPv6 address of a specified interface is configured as the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards.
   
   
   
   Both the [**dhcpv6 relay source-ip-address**](cmdqueryname=dhcpv6+relay+source-ip-address) and [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) commands can specify the source IP address used by a DHCP relay agent to forward messages. These two commands are mutually exclusive. If both of the two commands are run on a DHCP relay interface, the latest configuration overrides the previous one.
9. (Optional) Run [**dhcpv6 relay gateway-switch enable**](cmdqueryname=dhcpv6+relay+gateway-switch+enable)
   
   
   
   Automatic DHCPv6 relay gateway switching is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If the [**dhcpv6 relay link-address**](cmdqueryname=dhcpv6+relay+link-address) command has been run on an interface to configure a gateway address, the **dhcpv6 relay gateway-switch enable** command does not take effect.
   * The gateway switching function supports only global unicast addresses.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
11. (Optional) Run [**dhcpv6 rate-limit**](cmdqueryname=dhcpv6+rate-limit) { **disable** | *rate-limit* }
    
    
    
    Global rate limiting is disabled for DHCPv6 messages or a global rate limit is configured for DHCPv6 messages.
12. (Optional) Run [**dhcpv6 source-ip-address format adaptive enable**](cmdqueryname=dhcpv6+source-ip-address+format+adaptive+enable)
    
    
    
    The source IPv6 address type of the response messages sent by the DHCPv6 relay agent to the DHCPv6 client is configured as link-local.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.