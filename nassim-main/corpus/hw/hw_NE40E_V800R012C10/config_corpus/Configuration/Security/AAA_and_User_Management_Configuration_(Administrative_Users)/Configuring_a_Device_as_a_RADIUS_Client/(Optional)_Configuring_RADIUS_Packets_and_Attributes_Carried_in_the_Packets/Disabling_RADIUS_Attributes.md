Disabling RADIUS Attributes
===========================

Disabling RADIUS Attributes

#### Prerequisites

You must enable RADIUS attribute translation before disabling RADIUS attributes.


#### Context

RADIUS attributes need to be disabled in the following scenarios:

* The RADIUS server cannot identify or does not expect some RADIUS attributes. In this scenario, you can disable the device from encapsulating some attributes into the packets it sends to the RADIUS server.
* You want the device to ignore some attributes sent by the RADIUS server. In this scenario, you can disable the device from processing the attributes.

This function takes effect for only the RADIUS servers in the RADIUS server group in which it is configured. A maximum of 64 attributes can be disabled in a RADIUS server group.

You can disable RADIUS attributes of both the sent and received packets on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
3. Run [**radius-server attribute translate**](cmdqueryname=radius-server+attribute+translate)
   
   
   
   RADIUS attribute translation is enabled.
4. Run any of the following commands to disable RADIUS attributes:
   
   
   
   **Table 1** Attribute disabling modes
   | Operation | Command |
   | --- | --- |
   | Disable attributes for response packets, request packets, or both. | [**radius-attribute disable**](cmdqueryname=radius-attribute+disable) { *attr-description* | **hw-acct-update-address** } { **receive** | **send** } \* |
   | Disable attributes for any combination of Access-Accept, Access-Request, or accounting packets. | [**radius-attribute disable**](cmdqueryname=radius-attribute+disable) { *attr-description* | **hw-acct-update-address** } { **access-request** | **access-accept** | **account** [ **start** ] } \* |
   | Disable extended attributes for any combination of Access-Accept, Access-Request, or accounting packets. | [**radius-attribute disable extend**](cmdqueryname=radius-attribute+disable+extend) *attr-description* { **access-request** | **access-accept** | **account** } \* |
   | Disable extended attributes for Access-Accept packets. | [**radius-attribute disable extend vendor-specific**](cmdqueryname=radius-attribute+disable+extend+vendor-specific) *src-vendor-id* *src-sub-attr-id* **access-accept** |
   | Disable RADIUS attributes with specified data types and carried in response packets. | [**radius-attribute disable**](cmdqueryname=radius-attribute+disable) { *attr-description* | **hw-acct-update-address** } { **ip** *forbid-ip* | **string** *forbid-string* | **bin** *forbid-bin-value* | **integer** *vendor-id* } **receive** |
   | Disable RADIUS attributes with specified integral values and carried in accounting packets. | [**radius-attribute disable**](cmdqueryname=radius-attribute+disable) { **hw-acct-update-address** | **flow-attributes** } **integer** *integer* **account** |
   | Disable RADIUS attributes in CoA-Request or Disconnect-Request packets. | [**radius-attribute disable**](cmdqueryname=radius-attribute+disable) *attr-description* { **coa-request** | **dm-request** } |
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.