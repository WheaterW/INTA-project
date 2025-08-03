radius-attribute translate
==========================

radius-attribute translate

Function
--------

The **radius-attribute translate** command configures a RADIUS attribute to be translated.

The **undo radius-attribute translate** command cancels the configuration.

By default, no RADIUS attribute is translated.



Format
------

**radius-attribute translate** *src-attribute-name* *dest-attribute-name* { **receive** | **send** | **access-accept** | **access-request** | **account-request** | **account-response** } \*

**radius-attribute translate extend** *src-attribute-name* **vendor-specific** *dest-vendor-id* *dest-sub-id* { **access-request** | **account-request** } \*

**radius-attribute translate extend vendor-specific** *src-vendor-id* *src-sub-id* *dest-attribute-name* { **access-accept** | **account-response** } \*

**undo radius-attribute translate** [ *src-attribute-name* ]

**undo radius-attribute translate extend** *src-attribute-name*

**undo radius-attribute translate extend vendor-specific** *src-vendor-id* *src-sub-id*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *src-attribute-name* | Specifies the name of the source attribute. | The value is a string of 1 to 64 characters. After the name is entered, the system automatically associates the RADIUS attribute with the name. |
| *dest-attribute-name* | Specifies the name of the destination attribute. | The value is a string of 1 to 64 characters. After the name is entered, the system automatically associates the RADIUS attribute with the name. |
| **receive** | Translates RADIUS attributes for received packets. | - |
| **send** | Translates RADIUS attributes for sent packets. | - |
| **access-accept** | Translates RADIUS attributes for Authentication Accept packets. | - |
| **access-request** | Translates RADIUS attributes for Authentication Request packets. | - |
| **account-request** | Translates RADIUS attributes for Accounting Request packets. | - |
| **account-response** | Translates RADIUS attributes for Accounting Response packets. | - |
| **extend** | Translates extended RADIUS attributes. | - |
| **vendor-specific** | Specifies the source extended attribute to be translated. | - |
| *dest-vendor-id* | The vendor ID in the extended RADIUS attributes needs to be translated. | The value is an integer ranging from 1 to 4294967295. |
| *dest-sub-id* | The sub ID in the extended RADIUS attributes needs to be translated. | The value is an integer ranging from 1 to 255. |
| *src-vendor-id* | The vendor ID in the extended RADIUS attributes needs to be translated. | The value is an integer ranging from 1 to 4294967295. |
| *src-sub-id* | The sub ID in the RADIUS attributes needs to be translated. | The value is an integer ranging from 1 to 255. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Currently, RADIUS servers of different vendors may support different RADIUS attributes and have vendor-specific RADIUS attributes. To communicate with different RADIUS servers, the device provides the RADIUS attribute translation function. After RADIUS attribute translation is enabled, the device can translate RADIUS attributes when sending or receiving packets.

RADIUS attribute translation is used in the following modes:

* Format translation for the same attributeThis mode is widely applied. It solves the problem of compatibility because different users have different requirements for the format of a RADIUS attribute.
* Translation between different attributesThis mode is used because different vendors have different implementations of RADIUS attributes.For example, the device delivers the priority of the administrator by using the Huawei proprietary attribute HW-Exec-Privilege (26-29), whereas another vendor's device delivers it by using the Login-service (15) attribute. When the device and the vendor's device use the same RADIUS server on a network, the user hopes that the device can deliver the priority of the administrator by using the Login-service (15) attribute. After the **radius-attribute translate** command is configured, the device automatically processes the Login-service attribute in the received RADIUS authentication response packet as the HW-Exec-Privilege attribute.

**Prerequisites**

RADIUS attribute translation has been enabled by using the **radius-server attribute translate** command.

Before configuring RADIUS attribute translation, run the display radius-attribute command to view the RADIUS attributes supported by the device.

**Precautions**

* When the device sends packets, if attribute A is to be translated to attribute B, the type of the encapsulated attribute is the same as that of attribute B but the attribute content and format are the same as those of attribute A.
* When the device receives packets, if attribute A is to be translated to attribute B, the device parses the received attribute A as attribute B.
* Three commands are available to translate RADIUS attributes:
* To translate the attributes supported by the device to other attributes also supported by the device, run the **radius-attribute translate** command.
* To translate the non-Huawei attributes not supported by the device to the attributes supported by the device, run the **radius-attribute translate extend vendor-specific** command.
* To translate the attributes supported by the device to the non-Huawei attributes not supported by the device, run the **radius-attribute translate extend** command.
* The RADIUS attribute consists of Type, Length, and Value fields. A device can translate a non-Huawei RADIUS attribute (specified using the src-sub-id and dest-sub-id parameters) only when the length of the Type field in the RADIUS attribute is 1 byte.
* The device can translate the RADIUS attribute only when the type of the source RADIUS attribute is the same as that of the destination RADIUS attribute. For example, the types of NAS-Identifier and NAS-Port-Id attributes are string, and they can be translated into each other. The types of NAS-Identifier and Vendor-Specific attributes are string and integer respectively, they cannot be translated into each other.
* When both the packet direction and packet type are configured, they both take effect.


Example
-------

# Configure the device to translate NAS-Identifier into Vendor-Specific when sending RADIUS packets.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template temp1
[*HUAWEI-radius-temp1] radius-server attribute translate
[*HUAWEI-radius-temp1] radius-attribute translate NAS-Identifier Vendor-Specific send

```

# Translate the Cisco No. 2 attribute (vendor ID 9) in Authentication Accept and Accounting Response packets to Huawei No. 255 extended attribute HW-Product-ID.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template temp1
[*HUAWEI-radius-temp1] radius-server attribute translate
[*HUAWEI-radius-temp1] radius-attribute translate extend Vendor-Specific 9 2 HW-Product-ID access-accept account-response

```

# Translate the Huawei No. 153 extended attribute HW-Access-Type in Authentication Request and Accounting Request packets to Cisco No. 11 attribute.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template temp1
[*HUAWEI-radius-temp1] radius-server attribute translate
[*HUAWEI-radius-temp1] radius-attribute translate extend HW-Access-Type vendor-specific 9 11 access-request account-request

```