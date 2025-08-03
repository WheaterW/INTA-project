(Optional) Configuring Option 82 Field Insertion
================================================

After Option 82 field insertion is enabled on a device, the device can record the location information of a DHCP client or create binding entries with accurate interface information based on the Option 82 information.

#### Context

The Option 82 field contains the location information of Dynamic Host Configuration Protocol (DHCP) hosts, such as information about the login interface, virtual local area network (VLAN), and address. After DHCP snooping is configured, the device can create binding entries with accurate interface information based on the Option 82 field. In addition, the DHCP server that supports the Option 82 field can allocate different IP policies to different clients based on the Option 82 information. This provides more flexible address allocation modes.


#### Procedure

* Configure Option 82 field insertion in the VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     The VLAN view is displayed.
  3. Run [**dhcp option82 insert enable**](cmdqueryname=dhcp+option82+insert+enable) [ **interface** { *interface-type* *interface-number* | *interface-name* } ] or [**dhcp option82 rebuild enable**](cmdqueryname=dhcp+option82+rebuild+enable) [ **interface** *interface-type* *interface-number* ]
     
     Option 82 field insertion is enabled.
     
     + After the [**dhcp option82 insert enable**](cmdqueryname=dhcp+option82+insert+enable) command is run: If no Option 82 field exists in a received DHCP packet, the device inserts the Option 82 field into the packet; if the Option 82 field exists in a received DHCP packet, the device checks whether the Option 82 field contains sub-options. If the Option 82 field contains sub-options, the device does not change the sub-options. If the Option 82 field does not contain sub-options and the sub-option format is configured, the device inserts sub-options into the Option 82 field.
     + After the [**dhcp option82 rebuild enable**](cmdqueryname=dhcp+option82+rebuild+enable) command is run: If no Option 82 field exists in a received DHCP packet, the device inserts the Option 82 field into the packet; if the Option 82 field exists in a DHCP packet, the device deletes the Option 82 field and inserts a new Option 82 field into the packet.
  4. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  5. (Optional) Run [**dhcp option82 inner-vlan insert enable**](cmdqueryname=dhcp+option82+inner-vlan+insert+enable)
     
     Option 82 information is encapsulated into the inner and outer VLAN IDs of a double-tagged user packet.
     
     In scenarios where users go online through Layer 2 interfaces or VLANIF interfaces and device interworking and version upgrade are involved, you can determine whether to run this command as required.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure Option 82 field insertion in the BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  3. Run [**dhcp option82 insert enable**](cmdqueryname=dhcp+option82+insert+enable)
     
     Option 82 field insertion is enabled.
     
     + After the [**dhcp option82 insert enable**](cmdqueryname=dhcp+option82+insert+enable) command is run: If no Option 82 field exists in a received DHCP packet, the device inserts the Option 82 field into the packet; if the Option 82 field exists in a received DHCP packet, the device checks whether the Option 82 field contains sub-options. If the Option 82 field contains sub-options, the device does not change the sub-options. If the Option 82 field does not contain sub-options and the sub-option format is configured, the device inserts sub-options into the Option 82 field.
     + After the [**dhcp option82 rebuild enable**](cmdqueryname=dhcp+option82+rebuild+enable) command is run: If no Option 82 field exists in a received DHCP packet, the device inserts the Option 82 field into the packet; if the Option 82 field exists in a DHCP packet, the device deletes the Option 82 field and inserts a new Option 82 field into the packet.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure Option 82 field insertion on an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run [**dhcp option82 insert enable**](cmdqueryname=dhcp+option82+insert+enable) or [**dhcp option82 rebuild enable**](cmdqueryname=dhcp+option82+rebuild+enable)
     
     Option 82 field insertion is enabled.
     
     + After the [**dhcp option82 insert enable**](cmdqueryname=dhcp+option82+insert+enable) command is run: If no Option 82 field exists in a received DHCP packet, the device inserts the Option 82 field into the packet; if the Option 82 field exists in a received DHCP packet, the device checks whether the Option 82 field contains sub-options. If the Option 82 field contains sub-options, the device does not change the sub-options. If the Option 82 field does not contain sub-options and the sub-option format is configured, the device inserts sub-options into the Option 82 field.
     + After the [**dhcp option82 rebuild enable**](cmdqueryname=dhcp+option82+rebuild+enable) command is run: If no Option 82 field exists in a received DHCP packet, the device inserts the Option 82 field into the packet; if the Option 82 field exists in a DHCP packet, the device deletes the Option 82 field and inserts a new Option 82 field into the packet.
  4. (Optional) Run [**dhcp option82 link-selection insert enable**](cmdqueryname=dhcp+option82+link-selection+insert+enable)
     
     The function of inserting sub-option 5 into Option 82 is enabled.
  5. (Optional) Run [**dhcp option82 link-selection subnet-ip-address**](cmdqueryname=dhcp+option82+link-selection+subnet-ip-address) *ip-address*
     
     An IP address corresponding to sub-option 5 in Option 82 is configured.
  6. (Optional) Run [**dhcp option82 vendor-specific insert enable**](cmdqueryname=dhcp+option82+vendor-specific+insert+enable)
     
     The device is enabled to insert Option 82's sub-option 9 into a DHCP packet.
  7. (Optional) Run [**dhcp option82 vendor-specific format**](cmdqueryname=dhcp+option82+vendor-specific+format)
     
     A format is configured for Option 82's sub-option 9 carried in a DHCP packet.
  8. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  9. (Optional) Run [**dhcp option82 inner-vlan insert enable**](cmdqueryname=dhcp+option82+inner-vlan+insert+enable)
     
     Option 82 information is encapsulated into the inner and outer VLAN IDs of a double-tagged user packet.
     
     In scenarios where users go online through Layer 2 interfaces or VLANIF interfaces and device interworking and version upgrade are involved, you can determine whether to run this command as required.
  10. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Follow-up Procedure

After Option 82 field insertion is enabled, you can configure the format of the Option 82 field as required.

* Configure the format of the Option 82 field in the VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     The VLAN view is displayed.
  3. Run [**dhcp option82 format**](cmdqueryname=dhcp+option82+format) { **user-defined** *text* | **type1** | **type2** | **self-define** *self-define* | **cn-telecom** | **cn-telecom-inherit**} **interface** { *interface-type* *interface-number* | *interface-name*}
     
     The format of the Option 82 field is configured for the VLAN.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure the format of the Option 82 field on an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run [**dhcp option82 format**](cmdqueryname=dhcp+option82+format) { **self-define** *extendtext* | **type1** | **type2** | **cn-telecom** | **cn-telecom-inherit** } or [**dhcp option82**](cmdqueryname=dhcp+option82) { **circuit-id** | **remote-id** } **format** **self-define** *extendtext* or [**dhcp option82**](cmdqueryname=dhcp+option82) [ **circuit-id** | **remote-id** ] **format** **user-defined** *text*
     
     The format of the Option 82 field is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.