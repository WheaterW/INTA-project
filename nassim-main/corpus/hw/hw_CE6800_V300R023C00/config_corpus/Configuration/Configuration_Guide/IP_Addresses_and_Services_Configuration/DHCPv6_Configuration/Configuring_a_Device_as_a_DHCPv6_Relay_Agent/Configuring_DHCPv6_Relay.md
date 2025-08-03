Configuring DHCPv6 Relay
========================

Configuring DHCPv6 Relay

#### Context

You can configure DHCPv6 relay using either of the following methods:

* Method 1: Configure an IPv6 address for a DHCPv6 server or next-hop relay agent on an interface. This method applies to the scenario where the peer end of a DHCPv6 relay agent is connected to a DHCPv6 server or next-hop relay agent.
* Method 2: Bind a DHCPv6 server group to an interface. Specifically, create a DHCPv6 server group in the system view, add the IPv6 addresses of multiple DHCPv6 servers or next-hop relay agents in the DHCPv6 server group, and bind the DHCPv6 server group to the interface. This method is applicable to the scenario where the peer end of the DHCPv6 relay agent is connected to multiple DHCPv6 servers or next-hop relay agents. In this way, the DHCPv6 relay agent can flexibly select and manage DHCPv6 servers or next-hop relay agents.

Multiple DHCPv6 relay agents can be deployed between a DHCPv6 client and server. If a device functions as a DHCPv6 relay agent and is connected to a DHCPv6 server, you must specify the IPv6 address of the DHCPv6 server when enabling DHCPv6 relay. If the device is connected to a next-hop relay agent (for example, relay agent A), you must specify the IPv6 address of relay agent A on the device and specify the IPv6 address of the peer DHCPv6 server or next-hop relay agent connected to relay agent A on relay agent A.

![](public_sys-resources/note_3.0-en-us.png) 

When configuring DHCPv6 relay on a Multichassis Link Aggregation Group (M-LAG), you must configure DHCPv6 relay on the two devices that constitute the M-LAG.

When a VRRP6 device functions as a DHCPv6 relay agent, the DHCPv6 relay interface in the VRRP6 backup state does not forward DHCPv6 request messages.



#### Procedure

* **Method 1: Configure an IPv6 address for a DHCPv6 server or next-hop relay agent on an interface.**
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
  5. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  6. Configure a global unicast IPv6 address for the interface.
     
     
     ```
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length |ipv6-address/prefix-length }
     ```
  7. Perform either of the following operations to enable DHCPv6 relay on the interface as required.
     
     
     
     **Table 1** Enabling DHCPv6 relay on the interface
     | Operation | Command | Description |
     | --- | --- | --- |
     | In an intra-VPN scenario, configure the IPv6 address or outbound interface of a DHCPv6 server or next-hop relay agent. | [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) { **destination** *ipv6-address* | **interface** *interface-type interface-number* } | By default, DHCPv6 relay is disabled on an interface.  The configured IPv6 address is a global unicast address or unique local address. The device searches for routes and sends relay messages to the configured IPv6 address.  If a DHCPv6 relay agent is connected to multiple DHCPv6 servers or next-hop relay agents, repeat this step. |
     | In an inter-VPN scenario, configure the IPv6 address and VPN information of a DHCPv6 server or next-hop relay agent. | [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) **destination** *ipv6-address* { **vpn-instance** *vpn-instance-name* | **public-net** } | By default, the IPv6 address and VPN information of a DHCPv6 server or next-hop relay agent are not configured.  The configured IPv6 address is a global unicast address or unique local address. The device searches for routes and sends relay messages to the configured IPv6 address.  If a DHCPv6 relay agent is connected to multiple DHCPv6 servers or next-hop relay agents, repeat this step.  If the DHCPv6 server or next-hop relay agent belongs to the public network, specify the **public-net** parameter.  If the DHCPv6 server or the next-hop relay agent belongs to a VPN, set the **vpn-instance** *vpn-instance-name* parameter to the name of the VPN instance to which the DHCPv6 server or the next-hop relay agent belongs. |
  8. (Optional) Configure a client's gateway address or a source IPv6 address used for forwarding DHCPv6 messages on the DHCPv6 relay agent.
     
     
     
     To meet requirements in some scenarios, you can configure a client's gateway address on the DHCPv6 relay agent and a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards. For example, this configuration is suitable if the source IPv6 address of DHCPv6 messages must remain unchanged and the DHCPv6 server must know the message forwarding path of a client for address allocation and parameter configuration. The device supports the following two configuration methods.
     
     **Table 2** Configuring a client's gateway address on the DHCPv6 relay agent and a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards
     | Operation | Command | Description |
     | --- | --- | --- |
     | **Method 1:** Use the IPv6 address of a specified interface.  + If a global unicast address is configured on a DHCPv6 relay interface, running the [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) command does not change a client's gateway address configured on the DHCPv6 relay agent, but changes only the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards. + If multiple IPv6 addresses are configured on a specified interface, the first configured IPv6 address is used as the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards. If the DHCPv6 relay agent restarts, the smallest IPv6 address is used as the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards. In this case, if service requirements cannot be met, you can use method 2. | [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* | By default, a DHCPv6 relay agent selects the first configured global unicast IPv6 address from an interface with DHCPv6 relay enabled as its gateway address, and uses the gateway IPv6 address as the source address of DHCPv6 messages. |
     | **Method 2:** Configure a gateway address for the DHCPv6 relay agent and a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards. | + Configure a gateway address for the DHCPv6 relay agent. [**dhcpv6 relay link-address**](cmdqueryname=dhcpv6+relay+link-address) *ipv6-address* + Configure a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards. [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) **source-ip-address** *ipv6-address* |
     
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + The [**dhcpv6 relay link-address**](cmdqueryname=dhcpv6+relay+link-address) *ipv6-address* and [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* commands are mutually exclusive on an interface.
     + The [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) **source-ip-address** *ipv6-address* and [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* commands are mutually exclusive on an interface.
     + In inter-VPN scenarios, the [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) **source-ip-address** *ipv6-address* or [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* command must be run, because the destination address of reply messages sent from the DHCPv6 server to the DHCPv6 relay agent is the source address of request messages received by the DHCPv6 server. To ensure that there is a reachable route to the destination address of reply messages in the VPN, you must configure the IPv6 address of the outbound interface on the DHCPv6 relay agent as a source IPv6 address for DHCPv6 request messages that the DHCPv6 relay agent forwards.
  9. (Optional) Enable the DHCPv6 relay agent to forward routing information of DHCPv6 PD clients.
     
     
     ```
     [dhcpv6 relay advertise prefix-delegation route](cmdqueryname=dhcpv6+relay+advertise+prefix-delegation+route)
     ```
     
     By default, a DHCPv6 relay agent is disabled from forwarding routing information of DHCPv6 PD clients.
     
     This command takes effect only for the first-hop DHCPv6 relay agent connected to DHCPv6 PD clients.
  10. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
  11. (Optional) Save routing information forwarded by the DHCPv6 relay agent to a specified file.
      
      
      ```
      [dhcpv6 relay prefix-delegation route](cmdqueryname=dhcpv6+relay+prefix-delegation+route) autosave file-name
      ```
      
      By default, routing information forwarded by a DHCPv6 relay agent is not saved.
  12. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* **Method 2: Bind a DHCPv6 server group to an interface.**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable DHCP.
     
     
     ```
     [dhcp enable](cmdqueryname=dhcp+enable)
     ```
  3. Create a DHCPv6 server group.
     
     
     ```
     [dhcpv6 server group](cmdqueryname=dhcpv6+server+group) group-name
     ```
     
     
     
     By default, no DHCPv6 server group is created.
  4. Add the IPv6 address or outbound interface of the DHCPv6 server or next-hop relay agent in the DHCPv6 server group.
     
     
     ```
     [dhcpv6-server](cmdqueryname=dhcpv6-server) ipv6-address [ interface interface-type interface-number ]
     ```
     
     
     
     By default, no DHCPv6 server or next-hop relay agent is configured in a DHCPv6 server group.
     
     If a DHCPv6 relay agent is connected to multiple DHCPv6 servers or next-hop relay agents, repeat this step. The device supports a maximum of 20 DHCPv6 servers or next-hop relay agents in this scenario.
  5. (Optional) Bind a VPN instance to the DHCPv6 server group.
     
     
     ```
     vpn-instance vpn-instance-name
     ```
     
     By default, no VPN instance is bound to a DHCPv6 server group.
  6. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  7. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  8. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  9. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  10. Configure a global unicast IPv6 address for the interface.
      
      
      ```
      [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length |ipv6-address/prefix-length }
      ```
  11. Configure a DHCPv6 server group for the DHCPv6 relay agent.
      
      
      ```
      [dhcpv6 relay server-select](cmdqueryname=dhcpv6+relay+server-select) group-name
      ```
      
      By default, no DHCPv6 server group is configured for a DHCPv6 relay agent.
  12. (Optional) Configure a client's gateway address or a source IPv6 address used for forwarding DHCPv6 messages on the DHCPv6 relay agent.
      
      
      
      To meet requirements in some scenarios, you can configure a client's gateway address on the DHCPv6 relay agent and a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards. For example, this configuration is suitable if the source IPv6 address of DHCPv6 messages must remain unchanged and the DHCPv6 server must know the message forwarding path of a client for address allocation and parameter configuration. The device supports the following two configuration methods.
      
      **Table 3** Configuring a client's gateway address on the DHCPv6 relay agent and a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards
      | Operation | Command | Description |
      | --- | --- | --- |
      | **Method 1:** Use the IPv6 address of a specified interface.  + If a global unicast address is configured on a DHCPv6 relay interface, running the [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) command does not change a client's gateway address configured on the DHCPv6 relay agent, but changes only the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards. + If multiple IPv6 addresses are configured on a specified interface, the first configured IPv6 address is used as the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards. If the DHCPv6 relay agent restarts, the smallest IPv6 address is used as the source IPv6 address of DHCPv6 messages that the DHCPv6 relay agent forwards. In this case, if service requirements cannot be met, you can use method 2. | [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* | By default, a DHCPv6 relay agent selects the first configured global unicast IPv6 address from an interface with DHCPv6 relay enabled as its gateway address, and uses the gateway IPv6 address as the source address of DHCPv6 messages. |
      | **Method 2:** Configure a gateway address for the DHCPv6 relay agent and a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards. | + Configure a gateway address for the DHCPv6 relay agent. [**dhcpv6 relay link-address**](cmdqueryname=dhcpv6+relay+link-address) *ipv6-address* + Configure a source IPv6 address for DHCPv6 messages that the DHCPv6 relay agent forwards. [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) **source-ip-address** *ipv6-address* |
      
      
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      + The [**dhcpv6 relay link-address**](cmdqueryname=dhcpv6+relay+link-address) *ipv6-address* and [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* commands are mutually exclusive on an interface.
      + The [**dhcpv6 relay**](cmdqueryname=dhcpv6+relay) **source-ip-address** *ipv6-address* and [**dhcpv6 relay source-interface**](cmdqueryname=dhcpv6+relay+source-interface) *interface-type interface-number* commands are mutually exclusive on an interface.
  13. (Optional) Enable the DHCPv6 relay agent to forward routing information of DHCPv6 PD clients.
      
      
      ```
      [dhcpv6 relay advertise prefix-delegation route](cmdqueryname=dhcpv6+relay+advertise+prefix-delegation+route)
      ```
      
      By default, a DHCPv6 relay agent is disabled from forwarding routing information of DHCPv6 PD clients.
      
      This command takes effect only for the first-hop DHCPv6 relay agent connected to DHCPv6 PD clients.
  14. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
  15. (Optional) Save routing information forwarded by the DHCPv6 relay agent to a specified file.
      
      
      ```
      [dhcpv6 relay prefix-delegation route](cmdqueryname=dhcpv6+relay+prefix-delegation+route) autosave file-name
      ```
      
      By default, routing information forwarded by a DHCPv6 relay agent is not saved.
  16. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Follow-up Procedure

If the DHCPv6 relay agent functions as the gateway of clients (such as PCs) that automatically obtain IPv6 addresses based on RA messages by default, configure flags in RA messages on the gateway so that the clients can obtain IPv6 addresses using DHCPv6.

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable the device to send RA messages.
   ```
   [ipv6 nd ra halt disable](cmdqueryname=ipv6+nd+ra+halt+disable)
   ```
   
   By default, a device is disabled from sending RA messages.
5. Configure the managed address configuration flag of stateful address autoconfiguration in an RA message.
   ```
   [ipv6 nd autoconfig managed-address-flag](cmdqueryname=ipv6+nd+autoconfig+managed-address-flag)
   ```
   
   By default, the managed address configuration flag of stateful address autoconfiguration in an RA message is not configured.
6. Configure the other configuration flag of stateful address autoconfiguration in an RA message.
   ```
   [ipv6 nd autoconfig other-flag](cmdqueryname=ipv6+nd+autoconfig+other-flag)
   ```
   
   By default, the other configuration flag of stateful address autoconfiguration in an RA message is not configured.
   
   After the managed address configuration and other configuration flags of stateful address autoconfiguration in an RA message are configured, the clients can obtain IPv6 addresses using DHCPv6.
7. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```