(Optional) Configuring a Device to Insert the Option 18 and Option 37 Attributes into the Messages to Be Sent to the DHCPv6 Server
==================================================================================================================================

(Optional)_Configuring_a_Device_to_Insert_the_Option_18_and_Option_37_Attributes_into_the_Messages_to_Be_Sent_to_the_DHCPv6_Server

#### Context

When addresses are assigned from a remote IPv6 address pool, you can configure a device to insert the user-defined Option 18 and Option 37 attributes into the Relay-Forward messages to be sent to the DHCPv6 server.

Option 18 identifies the interface on which client messages are received on a relay agent, facilitating the forwarding of Relay-Reply messages. A server can also use Option 18 to assign addresses or prefixes. The function of Option 18 is equivalent to that of the circuit ID in DHCPv4 Option 82.

Option 37 carries information about a remote user. This attribute is added by a relay agent to a Relay-Forward message. The function of Option 37 is equivalent to that of the remote ID in DHCPv4 Option 82.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Insert the user-defined Option 18 and Option 37 attributes into the Relay-Forward messages to be sent to the DHCPv6 server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This configuration can be performed in either the interface or BAS interface view. If the configuration is performed in both the interface view and BAS interface view, the configuration in the BAS interface view takes effect.
   
   
   
   * In the interface view, perform the following operations:
     + Run the [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id mode** { **cn-telecom** | **tr-101** } | **remote-id** | **subscriber-id** } command to enable the function to insert relay options into DHCPv6 messages.
     + Run the [**dhcpv6 relay option-insert mode type1**](cmdqueryname=dhcpv6+relay+option-insert+mode+type1) command to insert the Option 18 and Option 37 attributes into the Relay-Forward messages to be sent to the DHCPv6 server in the OSP format in a BAS relay scenario. Alternatively, run the [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code*2 **mode cn-telecom version2** command to insert the Option 18 attribute into the Relay-Forward messages to be sent to the DHCPv6 server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The [**dhcpv6 relay option-insert mode type1**](cmdqueryname=dhcpv6+relay+option-insert+mode+type1) [ **remote-id** { **neba** | **vula** } ], [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code*2 **mode cn-telecom version2**,  and [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id** **mode** { **cn-telecom** | **tr-101** } | **remote-id** } commands are mutually exclusive.
     + The [**dhcpv6 relay option-insert mode type1**](cmdqueryname=dhcpv6+relay+option-insert+mode+type1) [ **remote-id** { **neba** | **vula** } ] command takes effect in real time. After the command configuration is added, the device enables the function to insert the Option 18 and Option 37 attributes into the messages to be sent to the DHCPv6 server in the OSP format for online users on the current interface. After the command configuration is deleted, the device disables this function for online users on the current interface.
     + The [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) *option-code*2 **mode cn-telecom version2** command takes effect in real time. After the command configuration is added, the device enables the function to insert the Option 18 attribute into the Relay-Forward messages to be sent to the DHCPv6 server for online users on the current interface. After the command configuration is deleted, the device disables this function for online users on the current interface.
     + The [**dhcpv6 relay option-insert**](cmdqueryname=dhcpv6+relay+option-insert) { **interface-id** **mode** { **cn-telecom** | **tr-101** } | **remote-id** } command takes effect in real time in BAS relay scenarios. After the command configuration is added, the device enables the function to insert the Option 18 and Option 37 attributes into the messages to be sent to the DHCPv6 server in the specified format for online users on the current interface. After the command configuration is deleted, the device disables this function for online users on the current interface.
   * In the BAS interface view, perform the following operations:
     1. Run the [**bas**](cmdqueryname=bas) command to enter the BAS interface view.
     2. Run the [**access-type**](cmdqueryname=access-type) command to set the access type to Layer 2 common user access, Layer 2 leased line user access, Layer 3 common user access, Layer 3 leased line user access, or Layer 2 VPN leased line user access.
     3. Run the [**dhcpv6 option-18 rebuild self-define**](cmdqueryname=dhcpv6+option-18+rebuild+self-define) *self-define-value* [ *add-domain-description* ] **send-to-server** command to enable the device to insert the user-defined Option 18 attribute into the Relay-Forward messages to be sent to the DHCPv6 server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + The *add-domain-description* parameter takes effect only after a domain description has been configured using the [**description**](cmdqueryname=description) *description-text* command in the domain view. For configuration details, see [(Optional) Configuring DHCP Messages to Carry Domain Description](dc_ne_aaa_cfg_1124.html).
     4. Run the [**dhcpv6 option-37 rebuild self-define**](cmdqueryname=dhcpv6+option-37+rebuild+self-define) *self-define-value* **send-to-server** command to enable the device to insert the user-defined Option 37 attribute into the Relay-Forward messages to be sent to the DHCPv6 server.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.