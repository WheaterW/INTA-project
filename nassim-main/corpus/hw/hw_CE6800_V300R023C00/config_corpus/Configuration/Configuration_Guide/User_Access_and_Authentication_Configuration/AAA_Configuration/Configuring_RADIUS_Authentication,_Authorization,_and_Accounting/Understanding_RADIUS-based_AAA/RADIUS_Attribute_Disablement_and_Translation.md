RADIUS Attribute Disablement and Translation
============================================

Different vendors support different collections of RADIUS attributes and each vendor may have their private attributes. As a result, RADIUS attributes of different vendors may be incompatible and RADIUS attributes sent between devices from different vendors cannot be parsed. To resolve this issue, the RADIUS attribute disablement and translation functions are often used in device interconnection and replacement scenarios.

#### RADIUS Attribute Disablement

The RADIUS server may have RADIUS attributes with the same attribute IDs and names as but different encapsulation formats or contents from those on the device. In this case, you can configure the RADIUS attribute disablement function to disable such attributes. The device then does not parse these attributes after receiving them from the RADIUS server, and does not encapsulate these attributes into RADIUS packets to be sent to the server.

Currently, Huawei-supported RADIUS attributes (with Huawei-supported attribute names and IDs) in a sent or received packet can be disabled on a device.


#### RADIUS Attribute Translation

RADIUS attribute translation is used to achieve compatibility between RADIUS attributes defined by different vendors. For example, a Huawei device delivers the administrator priority using the Huawei proprietary attribute Exec-Privilege (26-29), whereas another vendor's access device and the RADIUS server deliver this priority using the Login-service(15) attribute. When the Huawei device and another vendor's access device share one RADIUS server, the Huawei device needs to be compatible with the Login-service(15) attribute. After RADIUS attribute translation is configured on the Huawei device, the device automatically processes the Login-service(15) attribute in a received RADIUS authentication response packet as the Exec-Privilege (26-29) attribute.

Devices translate RADIUS attributes in a sent or received packet based on the Type, Length, and Value fields of the RADIUS attributes.

* If translation between attributes A and B is configured in the transmit direction on the device and the device sends a packet containing attribute A, the Type field of the attribute is attribute B but the Value field is encapsulated based on the content and format of attribute A.
* If translation between attributes A and B is configured in the receive direction on the device and the device receives a packet containing attribute A, it parses the Value field of attribute A as that of attribute B. To be specific, it can be understood that the device receives a packet containing attribute B instead of attribute A after attribute translation is configured.

Huawei-supported and non-Huawei-supported RADIUS attributes can be translated into each other. [Table 1](#EN-US_CONCEPT_0000001563995897__t1) shows the methods for translating Huawei-supported and non-Huawei-supported RADIUS attributes into each other.

![](public_sys-resources/note_3.0-en-us.png) 

* The device can translate a RADIUS attribute of another vendor only if the length of the Type field in the attribute is 1 octet.
* The device can translate the RADIUS attribute only when the type of the source RADIUS attribute is the same as that of the destination RADIUS attribute. For example, the types of the NAS-Identifier and NAS-Port-Id attributes are string, and they can be translated into each other. The types of the NAS-Identifier and NAS-Port attributes are string and integer respectively, they cannot be translated into each other.

**Table 1** Methods for translating RADIUS attributes
| Whether Huawei Supports the Source RADIUS Attribute | Whether Huawei Supports the Destination RADIUS Attribute | Supported Translation Direction | Configuration Command (in the RADIUS Server Template View) |
| --- | --- | --- | --- |
| Supported | Supported | Transmit and receive directions | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) *src-attribute-name* *dest-attribute-name* { **receive** | **send** | **access-accept** | **access-request** | **account-request** | **account-response** } \*  NOTE:  If you specify multiple parameters in the command, all these parameters take effect. When both the RADIUS attribute translation direction and packet type are specified, both the translation direction and packet type take effect. |
| Supported | Not supported | Transmit direction | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** *src-attribute-name* **vendor-specific** *dest-vendor-id* *dest-sub-id* { **access-request** | **account-request** } \* |
| Not supported | Supported | Receive direction | [**radius-attribute translate**](cmdqueryname=radius-attribute+translate) **extend** **vendor-specific** *src-vendor-id* *src-sub-id* *dest-attribute-name* { **access-accept** | **account-response** } \* |