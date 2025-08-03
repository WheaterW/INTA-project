Configuring a DHCPv6 Server Group
=================================

A DHCPv6 server group needs to be configured only when BAS-side users are assigned IPv6 addresses or prefixes from a remote address pool.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6-server group**](cmdqueryname=dhcpv6-server+group) *group-name*
   
   
   
   A DHCPv6 server group is created, and its view is displayed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. Run [**dhcpv6-server**](cmdqueryname=dhcpv6-server) { **destination** *ipv6-address* [ **vpn-instance** *vpn-instance* ] | **interface** *interface-type interface-number* } [ **weight** *weight-value* ]
   
   
   
   An IPv6 address or an outbound interface is configured for the DHCPv6 server. A maximum of eight DHCPv6 servers can be configured in a DHCPv6 server group.
5. (Optional) Run [**dhcpv6-server algorithm**](cmdqueryname=dhcpv6-server+algorithm) { **loading-share** | **master-backup** | **polling** }
   
   
   
   The algorithm for selecting DHCPv6 servers is configured.
   
   
   
   This algorithm takes effect only when the DHCPv6 server group contains multiple servers. The available algorithms are load balancing, active/standby, and polling.
   
   * Load balancing: Traffic is distributed based on the weights of DHCPv6 servers.
   * Active/standby: The first server that you configure is the active server and the others are standby servers.
   * Polling: The device sends Solicit, Request, Rebind, and Confirm messages to all servers in the DHCPv6 server group and selects the server that first responds to the request message for subsequent message exchanges.
6. (Optional) Run [**release-agent**](cmdqueryname=release-agent)
   
   
   
   The DHCPv6 release agent function is enabled.
   
   
   
   When a user wants to go offline and the DHCPv6 release agent function is enabled, the NE40E, instead of the user, sends DHCPv6 Release messages to DHCPv6 servers.
7. (Optional) Run [**dhcpv6-server source**](cmdqueryname=dhcpv6-server+source) { **interface** *interface-type interface-name* | **link-address** }
   
   
   
   The source address or source interface of the messages to be sent to servers in the DHCPv6 server group is configured.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. (Optional) Configure the device to insert Option 18 and Option 37 into the messages to be sent to a DHCPv6 server.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   2. Run the [**dhcpv6 relay option-insert mode type1**](cmdqueryname=dhcpv6+relay+option-insert+mode+type1) [ **remote-id** { **neba** | **vula** } ] command to configure the device to insert the Option 18 and Option 37 attributes in OSP format into the Relay-Forward messages to be sent to the DHCPv6 server. Alternatively, run the [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code2* **mode cn-telecom version2** command to insert the Option 18 attribute into the Relay-Forward messages to be sent to the DHCPv6 server.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The [**dhcpv6 relay option-insert mode type1**](cmdqueryname=dhcpv6+relay+option-insert+mode+type1) [ **remote-id** { **neba** | **vula** } ], [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code*2 **mode cn-telecom version2**, and [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id** **mode** { **cn-telecom** | **tr-101** } | **remote-id** } commands are mutually exclusive.
      * The [**dhcpv6 relay option-insert mode type1**](cmdqueryname=dhcpv6+relay+option-insert+mode+type1) [ **remote-id** { **neba** | **vula** } ] command takes effect in real time. After the command configuration is added, the device enables the function to insert the Option 18 and Option 37 attributes into the messages to be sent to the DHCPv6 server in the OSP format for online users on the current interface. After the command configuration is deleted, the device disables this function for online users on the current interface.
      * The [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code*2 **mode cn-telecom version2** command takes effect in real time. After the command configuration is added, the device enables the function to insert the Option 18 attribute into the Relay-Forward messages to be sent to the DHCPv6 server for online users on the current interface. After the command configuration is deleted, the device disables this function for online users on the current interface.
      * The [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id** **mode** { **cn-telecom** | **tr-101** } | **remote-id** } command takes effect in real time in BAS relay scenarios. After the command configuration is added, the device enables the function to insert the Option 18 and Option 37 attributes into the messages to be sent to the DHCPv6 server in the specified format for online users on the current interface. After the command configuration is deleted, the device disables this function for online users on the current interface.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
10. (Optional) Configure the device to insert Option 79 into the messages to be sent to a DHCPv6 server.
    1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
    2. Run the [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code*1 command to configure the device to insert Option 79 into the Relay-Forward messages to be sent to a DHCPv6 server.
    3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
11. (Optional) Run [**dhcpv6-server**](cmdqueryname=dhcpv6-server) [ *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] ] { **dead-count** *dead-count* | **timeout** *timeout-value* | **dead-time** *dead-time* } \*
    
    
    
    The threshold for the DHCPv6 server to alternate between up and down is configured.
12. (Optional) Configure whitelist session-CAR for DHCPv6.
    1. (Optional) Run the [**undo whitelist session-car dhcpv6-server disable**](cmdqueryname=undo+whitelist+session-car+dhcpv6-server+disable) command to enable Whitelist session-CAR for DHCPv6.
    2. Run the **whitelist session-car dhcpv6-server** { **cir***cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \* command to configure the bandwidth parameters of whitelist session-CAR for DHCPv6.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.