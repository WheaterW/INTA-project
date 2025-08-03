Configuring RADIUS Attribute Translation
========================================

Configuring_RADIUS_Attribute_Translation

#### Context

Different vendors define some RADIUS attributes differently and provide RADIUS servers that support different RADIUS attribute sets. To communicate with different RADIUS servers, the device provides the RADIUS attribute translation function.

After this function is configured, the device can encapsulate or parse *src-attribute* by using the format of *dest-attribute* when sending or receiving RADIUS packets, enabling the device to communicate with different types of RADIUS servers.

This function is applied when one attribute has multiple formats. For example, the **nas-port-id** attribute has a new format and an old format. If the device uses the new format but the RADIUS server uses the old format, you can run the [**radius-attribute translate nas-port-id nas-port-identify-old receive send**](cmdqueryname=radius-attribute+translate+nas-port-id+nas-port-identify-old+receive+send) command on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
3. Run [**radius-server attribute translate**](cmdqueryname=radius-server+attribute+translate)
   
   
   
   RADIUS attribute translation is enabled.
4. Perform any of the following operations to configure RADIUS attribute translation:
   
   
   
   **Table 1** Attribute translation modes
   | Operation | Command |
   | --- | --- |
   | Configure attribute translation for response or request packets. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) *src-attr-description* *dest-attr-description* { { **receive** | **send** } \* } |
   | Configure attribute translation for any combination of Access-Accept, Access-Request, or accounting packets. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) *src-attr-description* *dest-attr-description* { **access-accept** | { **access-request** | **account** }\* } |
   | Configure extended attribute translation for any combination of Access-Accept, Access-Request, or accounting packets. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** *src-attr-description* *dest-attr-description* { **access-accept** | { **access-request** | **account**} \* } |
   | Configure extended attribute translation for Access-Request packets, accounting packets, or both. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** *src-attr-description* **vendor-specific** *src-vendor-id* *src-sub-attr-id* { **access-request** | **account** } \* |
   | Configure extended attribute translation for Access-Accept packets. | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** **vendor-specific** *src-vendor-id* *src-sub-attr-id* *dest-attr-description* **access-accept** |
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.