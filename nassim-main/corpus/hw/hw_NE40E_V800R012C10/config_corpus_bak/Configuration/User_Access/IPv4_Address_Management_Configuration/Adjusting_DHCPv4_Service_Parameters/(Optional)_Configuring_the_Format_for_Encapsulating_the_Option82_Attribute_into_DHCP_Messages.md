(Optional) Configuring the Format for Encapsulating the Option82 Attribute into DHCP Messages
=============================================================================================

This section describes how to enable a device to insert Sub-option 2 (remote ID) into the Option 82 attribute or replace Sub-option 2 carried in the Option 82 attribute of a message to be sent to the DHCP server based on a fixed format when addresses are assigned to Layer 2 users from a remote address pool.

#### Context

When IP addresses are assigned from a remote address pool to Layer 2 access users, the DHCP server identifies a carrier based on the remote ID carried in the Option 82 attribute of a DHCP message. As such, you need to configure a device to insert Sub-option 2 (remote ID) into the Option 82 attribute or replace Sub-option 2 carried in the Option 82 attribute of a message to be sent to the DHCP server based on a fixed format. In this format, self-defined character strings can be encapsulated into Sub-option 2.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Configure the format for encapsulating the Option 82 attribute into DHCP messages. Perform the following steps as required: The following commands are mutually exclusive:
   
   
   * To encapsulate the Option 82 attribute into the messages to be sent to the DHCP server in a fixed format, which does not support self-defined content, run the [**dhcp option82 rebuild version3 send-to-server**](cmdqueryname=dhcp+option82+rebuild+version3+send-to-server) [ **remote-id** { **neba** | **vula** } ] command.
     
     This command has a higher priority than the [**dhcp option-82 agent-remote-id strip**](cmdqueryname=dhcp+option-82+agent-remote-id+strip) command.
   * To encapsulate the Option 82 attribute into the messages to be sent to the DHCP server in the sysname:interface-name:svlan-cvlan format, run the [**dhcp option82 rebuild version4 send-to-server**](cmdqueryname=dhcp+option82+rebuild+version4+send-to-server) command.
   * To encapsulate the Option 82 attribute into the messages to be sent to the DHCP server in the fixed OSP format, which supports self-defined content, run the [**dhcp option82 rebuild self-define**](cmdqueryname=dhcp+option82+rebuild+self-define) { **circuit-id** *circuit-id-value* [ *add-domain-description* ] | **out-vlan** *out-vlan-value* | **inner-vlan** *inner-vlan-value* | **remote-id** *remote-id-value* } \* **send-to-server** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This configuration takes effect only after DHCP proxy is enabled on the BAS interface.
   * The *add-domain-description* parameter takes effect only after a domain description is configured using the [**description**](cmdqueryname=description) *description-text* command in the domain view. For configuration details, see [(Optional) Configuring DHCP Messages to Carry Domain Description](dc_ne_aaa_cfg_1124.html).
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.