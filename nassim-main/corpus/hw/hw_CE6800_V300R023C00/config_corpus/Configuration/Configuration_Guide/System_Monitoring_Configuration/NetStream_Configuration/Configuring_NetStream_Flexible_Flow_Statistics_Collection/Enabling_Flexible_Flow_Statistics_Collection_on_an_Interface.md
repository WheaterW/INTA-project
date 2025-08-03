Enabling Flexible Flow Statistics Collection on an Interface
============================================================

Enabling Flexible Flow Statistics Collection on an Interface

#### Context

Flexible flow statistics can be exported only after the flexible flow statistics collection function is enabled on an interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Switch the NetStream mode.
   
   
   ```
   assign forward enp netstream enable
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command is supported only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.
   
   By default, the NetStream flow table of a small size is supported on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S. After the NetStream mode is switched, the NetStream flow table of a large size is supported and the configuration takes effect after the device restarts.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Perform the following configurations based on your site requirements:
   * Apply a created IPv4 flexible flow statistics template to an interface, and enable IPv4 flexible flow statistics collection on the interface.
     ```
     [netstream record](cmdqueryname=netstream+record) record-name ip
     [netstream](cmdqueryname=netstream) { inbound | outbound } ip
     ```
     
     By default, IPv4 flexible flow statistics collection is disabled on an interface.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Only one IPv4 flexible flow statistics template can be applied to each interface. After an IPv4 flexible flow statistics template is applied to an interface, it cannot be modified or deleted. To change this template on the interface, run the [**undo netstream record**](cmdqueryname=undo+netstream+record) **ip** command to delete it first.
   * Apply a created IPv6 flexible flow statistics template to an interface, and enable IPv6 flexible flow statistics collection on the interface.
     ```
     [netstream record](cmdqueryname=netstream+record) record-name ipv6
     [netstream](cmdqueryname=netstream) { inbound | outbound } ipv6
     ```
     
     By default, IPv6 flexible flow statistics collection is disabled on an interface.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Only one IPv6 flexible flow statistics template can be applied to each interface. After an IPv6 flexible flow statistics template is applied to an interface, it cannot be modified or deleted. To change this template on the interface, run the [**undo netstream record**](cmdqueryname=undo+netstream+record) **ipv6** command to delete it first.
   * Apply a created VXLAN flexible flow statistics template to an interface, and enable VXLAN flexible flow statistics collection on the interface.
     ```
     [netstream record](cmdqueryname=netstream+record) record-name vxlan inner-ip
     [netstream](cmdqueryname=netstream) { inbound | outbound } ip
     ```
     
     By default, VXLAN flexible flow statistics collection is disabled on an interface.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Only one VXLAN flexible flow statistics template can be applied to each interface. After a VXLAN flexible flow statistics template is applied to an interface, it cannot be modified or deleted. To change this template on the interface, run the [**undo netstream record**](cmdqueryname=undo+netstream+record) **vxlan inner-ip** command to delete it first.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```