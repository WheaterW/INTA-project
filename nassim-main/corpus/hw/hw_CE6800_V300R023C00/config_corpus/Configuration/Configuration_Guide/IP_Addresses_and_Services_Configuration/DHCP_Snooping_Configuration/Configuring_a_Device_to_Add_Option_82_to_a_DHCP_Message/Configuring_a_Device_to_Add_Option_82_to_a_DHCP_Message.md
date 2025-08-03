Configuring a Device to Add Option 82 to a DHCP Message
=======================================================

Configuring a Device to Add Option 82 to a DHCP Message

#### Context

Option 82 records the location of a DHCP client. A device adds Option 82 to a DHCP request message to send the location of a DHCP client to the DHCP server. This enables the DHCP server to allocate a proper IP address and other configurations to the client based on the content of Option 82, implementing security control on the client.

![](../public_sys-resources/note_3.0-en-us.png) 

DHCP Option 82 must be configured on the user side of a device; otherwise, the DHCP messages sent by the device to the DHCP server do not carry Option 82.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the function of adding Option 82 to DHCP messages in different views.
   
   
   * Configure the device to add Option 82 to DHCP messages in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp option82](cmdqueryname=dhcp+option82) { insert | rebuild } enable
     [quit](cmdqueryname=quit)
     ```
   * Configure the device to add Option 82 to DHCP messages in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [dhcp option82](cmdqueryname=dhcp+option82) { insert | rebuild } enable
     [quit](cmdqueryname=quit)
     ```
   * Configure the device to add Option 82 to DHCP messages in the BD view.
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     [dhcp option82](cmdqueryname=dhcp+option82) { insert | rebuild } enable
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, Option 82 is not added to DHCP messages.
3. (Optional) Enable the function of inserting Option 82's suboptions 1, 2, 6, and 9 into DHCPv4 messages. The configuration can be performed in the system, BD, VLAN, or interface view. If the configuration is performed in the system view, it takes effect for all interfaces of the device. If the configuration is performed in the VLAN or BD view, it takes effect for DHCPv4 messages that are received by all interfaces and belong to the VLAN or BD. If the configuration is performed in the interface view, it takes effect only for the specified interface.
   
   
   * Perform the configuration in the system view.
     ```
     [dhcp option82 encapsulation](cmdqueryname=dhcp+option82+encapsulation) { circuit-id | remote-id | subscriber-id | vendor-specific-id } *
     ```
   * Perform the configuration in the BD view.
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     [dhcp option82 encapsulation](cmdqueryname=dhcp+option82+encapsulation) { circuit-id | remote-id | subscriber-id | vendor-specific-id } *
     [quit](cmdqueryname=quit)
     ```
   * Perform the configuration in the VLAN view.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp option82 encapsulation](cmdqueryname=dhcp+option82+encapsulation) { circuit-id | remote-id | subscriber-id | vendor-specific-id } *
     [quit](cmdqueryname=quit)
     ```
   * Perform the configuration in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [dhcp option82 encapsulation](cmdqueryname=dhcp+option82+encapsulation) { circuit-id | remote-id | subscriber-id | vendor-specific-id } *
     [quit](cmdqueryname=quit)
     ```
     
     Determine whether to run the [**portswitch**](cmdqueryname=portswitch) command to switch the interface working mode to Layer 2 based on the current interface working mode.
   
   By default, suboption 1 circuit-id (CID), suboption 2 remote-id (RID), suboption 6 subscriber-id (SID), and suboption 9 vendor-specific information are inserted into Option 82.
4. (Optional) Configure user-defined formats for Option 82's suboptions 1 and 2.
   
   
   
   You can perform the configuration in the system or interface view. If the configuration is performed in the system view, it takes effect for all interfaces of the device. If the configuration is performed in the interface view, it takes effect only for the specified interface.
   
   ![](../public_sys-resources/notice_3.0-en-us.png) 
   * All Option 82 information configured in the system view or in the same interface view shares a length of 1 to 255 bytes. If their total length exceeds 255 bytes, some Option 82 information is lost.
   * There is no limit on the amount of Option 82 information configured on a device. However, configuring a large amount of Option 82 information consumes memory resources and prolongs the device's processing time. To ensure device performance, you are advised to configure Option 82 information based on service requirements and device memory size.
   * Configure the format of Option 82 in the system view.
     ```
     [dhcp option82](cmdqueryname=dhcp+option82) [ vlan vlanid ] [ ce-vlan ce-vlanid ] [ circuit-id | remote-id ] format { default | common | extend | user-defined text }
     ```
   * Configure the format of Option 82 in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [dhcp option82](cmdqueryname=dhcp+option82) [ vlan vlanid ] [ ce-vlan ce-vlanid ] [ circuit-id | remote-id ] format { default | common | extend | user-defined text }
     ```
     
     Determine whether to run the [**portswitch**](cmdqueryname=portswitch) command to switch the interface working mode to Layer 2 based on the current interface working mode.
   
   By default, the format of Option 82 in DHCPv4 messages is **default**.
5. (Optional) Configure a user-defined format for Option 82's suboption 6.
   
   
   * Configure a user-defined format for Option 82's suboption 6 in the system view.
     ```
     [dhcp option82 subscriber-id format](cmdqueryname=dhcp+option82+subscriber-id+format) { ascii ascii-text | hex hex-text }
     ```
   * Configure a user-defined format for Option 82's suboption 6 in the interface view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [dhcp option82 subscriber-id format](cmdqueryname=dhcp+option82+subscriber-id+format) { ascii ascii-text | hex hex-text }
     ```
     
     Determine whether to run the [**portswitch**](cmdqueryname=portswitch) command to switch the interface working mode to Layer 2 based on the current interface working mode.
   
   
   
   By default, no user-defined format is configured for Option 82's suboption 6 in DHCPv4 messages.
6. (Optional) Configure the DHCPv4 relay agent to insert suboption 9 into Option 82.
   
   
   
   Option 82's suboption 9 can use either the old or new format. Suboption 9 in the old format carries the hwid or the ID of another company, whereas suboption 9 in the new format does not. If suboption 9 is configured in both the system and interface views, the configuration in the interface view preferentially takes effect. Before configuring the DHCPv4 relay agent to insert suboption 9 into Option 82, you must run the [**dhcp relay information enable**](cmdqueryname=dhcp+relay+information+enable) command to enable the relay agent to support Option 82. Otherwise, the function does not take effect.
   
   * Configure a user-defined format for Option 82's suboption 9 in the old format.
     + Perform the configuration in the system view.
       ```
       [dhcp option82 vendor-specific format](cmdqueryname=dhcp+option82+vendor-specific+format) vendor-sub-option sub-option-num { ascii ascii-text | hex hex-text | ip-address ip-address &<1-8> | sysname }
       ```
     + Perform the configuration in the interface view.
       ```
       [interface](cmdqueryname=interface) interface-type interface-number
       [undo portswitch](cmdqueryname=undo+portswitch)
       [dhcp relay information enable](cmdqueryname=dhcp+relay+information+enable)
       [dhcp option82 vendor-specific format](cmdqueryname=dhcp+option82+vendor-specific+format) vendor-sub-option sub-option-num source-ip-address ip-address
       ```
       
       Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
   * Configure the DHCPv4 relay agent to insert suboption 9 in the new format into Option 82.
     + Perform the configuration in the VLAN view.
       ```
       [vlan](cmdqueryname=vlan) vlan-id
       [dhcp option82 append vendor-specific](cmdqueryname=dhcp+option82+append+vendor-specific)
       [quit](cmdqueryname=quit)
       ```
     + Perform the configuration in the interface view.
       ```
       [interface](cmdqueryname=interface) interface-type interface-number
       [undo portswitch](cmdqueryname=undo+portswitch)
       [dhcp relay information enable](cmdqueryname=dhcp+relay+information+enable)
       [dhcp option82 append vendor-specific](cmdqueryname=dhcp+option82+append+vendor-specific)
       [quit](cmdqueryname=quit)
       ```
       
       Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
   
   By default, suboption 9 is not inserted into Option 82 of DHCPv4 messages.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * If both the [**dhcp option82 append vendor-specific**](cmdqueryname=dhcp+option82+append+vendor-specific) and [**dhcp option82 vendor-specific format**](cmdqueryname=dhcp+option82+vendor-specific+format) commands are run, the [**dhcp option82 append vendor-specific**](cmdqueryname=dhcp+option82+append+vendor-specific) command takes effect.
   * Suboption 9 can be inserted into Option 82 only when the format of suboption 9 configured on a device is the same as that in a received DHCPv4 message. If the formats are different:
     + When the [**dhcp option82 vendor-specific format**](cmdqueryname=dhcp+option82+vendor-specific+format) command is run, suboption 9 in the new format cannot be inserted into Option 82.
     + When the [**dhcp option82 append vendor-specific**](cmdqueryname=dhcp+option82+append+vendor-specific) command is run, whether suboption 9 in the old format can be inserted into Option 82 depends on the mode in which Option 82 is added (configured using the [**dhcp option82 enable**](cmdqueryname=dhcp+option82+enable) command). In Insert mode, suboption 9 is not inserted into Option 82. In Rebuild mode, suboption 9 in the old format is rebuilt and then inserted into Option 82.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display dhcp option82 configuration**](cmdqueryname=display+dhcp+option82+configuration) [ **vlan** *vlan-id* | **interface** *interface-type* *interface-number* ] command to check the Option 82 configuration.