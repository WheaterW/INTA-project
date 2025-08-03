(Optional) Configuring DHCPv6 Relay Options
===========================================

DHCPv6 relay options include the Interface-ID option, Subscriber-ID option, and Remote-ID option. These options carry detailed user information for address assignment and parameter configuration.

#### Context

A DHCPv6 server assigns IPv6 addresses and other configuration parameters to clients based on options carried in DHCPv6 messages. You can determine whether to enable the DHCPv6 relay agent to add these options to DHCPv6 messages based on the server implementation.

* The Interface-ID option carries information about the inbound interface that receives client messages.
* The Remote-ID option carries information about a DHCPv6 relay agent, such as the DUID, port identifier, and VLAN ID.
* The Subscriber-ID option carries the MAC address of a client.

Among these options, the Interface-ID, Subscriber-ID, and Remote-ID options can be configured for Layer 2 or Layer 3 Ethernet interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where DHCPv6 relay options need to be configured is displayed.
3. Run [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id** **mode** { **cn-telecom** | **tr-101** | **cn-telecom-inherit** } | **remote-id** | **subscriber-id** } or [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id** **mode** **self-define** *self-define-value* | **remote-id** **mode** **self-define** *self-define-value* }
   
   
   
   The interface is enabled to add the Interface-ID, Subscriber-ID, and Remote-ID relay options to DHCPv6 messages.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.