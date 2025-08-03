Configuring an IPv4 Address for a DHCPv4 Server
===============================================

Configuring an IPv4 Address for a DHCPv4 Server

#### Context

To ensure that DHCPv4 messages can be forwarded from a DHCPv4 relay agent to a DHCPv4 server, you must configure the IPv4 address of the server on the interface where DHCPv4 relay is enabled. You can configure the IPv4 address of a DHCPv4 server in either the interface or DHCPv4 server group view. If DHCPv4 relay needs to be configured on only one interface, the interface view is recommended. Otherwise, the DHCPv4 server group view is recommended.

![](public_sys-resources/note_3.0-en-us.png) 

The number of times that DHCPv4 messages are relayed between a DHCPv4 server and client cannot exceed 16. Otherwise, DHCPv4 messages are discarded.

All servers in a DHCPv4 server group must be in the same VPN instance.



#### Procedure

* **Configure an IPv4 address for a DHCPv4 server in the interface view.**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Enable DHCPv4 server polling on the DHCPv4 relay agent.
     
     
     ```
     [ip relay address cycle](cmdqueryname=ip+relay+address+cycle)
     ```
     
     By default, DHCPv4 server polling is disabled on a DHCPv4 relay agent.
  3. (Optional) Set a TTL value for DHCPv4 request messages after they are forwarded by the DHCPv4 relay agent at Layer 3.
     
     
     ```
     [dhcp set ttl](cmdqueryname=dhcp+set+ttl) { unvaried | ttl-value }
     ```
     
     By default, the TTL value of DHCPv4 request messages decreases by 1 after they are forwarded by the DHCPv4 relay agent at Layer 3.
  4. Configure an IPv4 address for a DHCPv4 server.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [undo portswitch](cmdqueryname=undo+portswitch)
     [dhcp relay server-ip](cmdqueryname=dhcp+relay+server-ip) ip-address [ vpn-instance vpn-instance-name | public-net ]
     ```
     
     By default, no IPv4 address is configured for a DHCPv4 server on an interface.
     
     Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
     
     In an inter-VPN scenario, if the DHCPv4 client and server are located in different VPNs, you must specify the **vpn-instance** *vpn-instance-name* parameter when performing this step.
     
     In a non-inter-VPN scenario, you are advised not to specify the **vpn-instance** *vpn-instance-name* parameter because the DHCPv4 server and relay interface belong to the same VPN by default. In this case, you only need to bind the interface to a VPN and use the VPN information of the interface.
  5. (Optional) Enable DHCPv4 relay gateway switching.
     
     
     ```
     [dhcp relay gateway-switch enable](cmdqueryname=dhcp+relay+gateway-switch+enable)
     ```
     
     By default, DHCPv4 relay gateway switching is disabled.
     
     When the primary and secondary IPv4 addresses are configured on an interface, the primary IPv4 address functions as the gateway of clients in normal cases. If clients cannot obtain IPv4 addresses from the gateway with the primary IPv4 address, enable DHCPv4 relay gateway switching to allow them to do so with a secondary IPv4 address. After DHCPv4 relay gateway switching is enabled, configure the address pool on the same network segment as the secondary IPv4 address on the remote DHCPv4 server.
     + The gateway address switches from the primary to a secondary IPv4 address only when a user has failed to obtain an IPv4 address using the primary IPv4 address at least three times and the interval between the first and last failures exceeds 24 seconds.
     + When a primary IPv4 address and multiple secondary IPv4 addresses are configured on an interface, the primary and secondary IPv4 addresses are traversed in turn until users successfully obtain IPv4 addresses (the secondary IPv4 addresses are traversed based on the configuration sequence).
* **Configure an IPv4 address for a DHCPv4 server in the DHCPv4 server group view.**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Enable DHCPv4 server polling on the DHCPv4 relay agent.
     
     
     ```
     [ip relay address cycle](cmdqueryname=ip+relay+address+cycle)
     ```
     
     By default, DHCPv4 server polling is disabled on a DHCPv4 relay agent.
  3. (Optional) Set a TTL value for DHCPv4 request messages after they are forwarded by the DHCPv4 relay agent at Layer 3.
     
     
     ```
     [dhcp set ttl](cmdqueryname=dhcp+set+ttl) { unvaried | ttl-value }
     ```
     
     By default, the TTL value of DHCPv4 request messages decreases by 1 after they are forwarded by the DHCPv4 relay agent at Layer 3.
  4. Create a DHCPv4 server group and enter its view.
     
     
     ```
     [dhcp relay server group](cmdqueryname=dhcp+relay+server+group) group-name
     ```
     
     By default, no DHCPv4 server group is created.
  5. Configure a DHCPv4 server in the DHCPv4 server group.
     
     
     ```
     [server](cmdqueryname=server) ip-address [ ip-address-index ]
     ```
     
     By default, no DHCPv4 server is configured in a DHCPv4 server group.
     
     A maximum of 20 DHCPv4 servers can be configured in a DHCPv4 server group.
  6. (Optional) Configure a gateway address for the DHCPv4 server.
     
     
     ```
     [gateway](cmdqueryname=gateway) ip-address
     ```
     
     
     
     By default, no gateway address is configured for a DHCPv4 server.
     
     If the IPv4 address of the interface that connects the DHCPv4 relay agent to clients functions as the gateway address, skip this step. The gateway address configured in this step must be the same as the egress gateway address of clients configured on the DHCPv4 server.
  7. (Optional) Bind the DHCPv4 server group to a specified VPN instance.
     
     
     ```
     [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name
     ```
     
     By default, no DHCPv4 server group is bound to a VPN instance.
     
     If the DHCPv4 relay agent is deployed on a VPN, you must bind the DHCPv4 server group to the VPN instance that has been bound to the address pool of the DHCPv4 server. Otherwise, DHCPv4 clients cannot obtain IPv4 addresses.
  8. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  9. Configure a DHCPv4 server group on an interface.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [undo portswitch](cmdqueryname=undo+portswitch)
     [dhcp relay server-group](cmdqueryname=dhcp+relay+server-group) group-name
     ```
     
     By default, no DHCPv4 server group is configured on an interface.
     
     Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
  10. (Optional) Enable DHCPv4 relay gateway switching.
      
      
      ```
      [dhcp relay gateway-switch enable](cmdqueryname=dhcp+relay+gateway-switch+enable)
      ```
      
      By default, DHCPv4 relay gateway switching is disabled.
      
      When the primary and secondary IPv4 addresses are configured on an interface, the primary IPv4 address functions as the gateway of clients in normal cases. If clients cannot obtain IPv4 addresses from the gateway with the primary IPv4 address, enable DHCPv4 relay gateway switching to allow them to do so with a secondary IPv4 address. After DHCPv4 relay gateway switching is enabled, configure the address pool on the same network segment as the secondary IPv4 address on the remote DHCPv4 server.
      + The gateway address switches from the primary to a secondary IPv4 address only when a user has failed to obtain an IPv4 address using the primary IPv4 address at least three times and the interval between the first and last failures exceeds 24 seconds.
      + When a primary IPv4 address and multiple secondary IPv4 addresses are configured on an interface, the primary and secondary IPv4 addresses are traversed in turn until users successfully obtain IPv4 addresses (the secondary IPv4 addresses are traversed based on the configuration sequence).
  11. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```