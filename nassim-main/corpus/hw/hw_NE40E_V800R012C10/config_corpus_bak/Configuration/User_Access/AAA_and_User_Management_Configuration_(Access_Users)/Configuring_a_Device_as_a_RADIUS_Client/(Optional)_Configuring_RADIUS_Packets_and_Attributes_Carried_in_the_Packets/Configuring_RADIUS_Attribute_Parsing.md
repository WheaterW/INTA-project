Configuring RADIUS Attribute Parsing
====================================

Configuring_RADIUS_Attribute_Parsing

#### Context

To ensure compatibility with different vendors' RADIUS attributes if the device interconnects with non-Huawei RADIUS servers, you can configure the RADIUS parsing function to parse specific attributes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 option-17 decode version1**](cmdqueryname=dhcpv6+option-17+decode+version1)
   
   
   
   The device is enabled to parse the Option 17 field based on the format defined by the DSL Forum and send the obtained sub-attributes to a RADIUS server.
3. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
4. Run [**radius-attribute support vendor**](cmdqueryname=radius-attribute+support+vendor) *vendorid* *subattrid* *attributename*
   
   
   
   The attribute allowed to be parsed is configured.
5. Run [**radius-attribute vendor**](cmdqueryname=radius-attribute+vendor) *vendor-id* **enable**
   
   
   
   The ID of a vendor whose proprietary RADIUS attributes can be parsed by the device is configured.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.