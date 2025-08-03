radius-attribute set
====================

radius-attribute set

Function
--------

The **radius-attribute set** command modifies the RADIUS attributes.

The **undo radius-attribute set** command restores the default RADIUS attributes.

By default, values of the RADIUS attributes are not modified.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**radius-attribute set** *attribute-name* *attribute-value*

**undo radius-attribute set** *attribute-name*

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**radius-attribute set** *attribute-name* *attribute-value* **auth-type** **dot1x**

**undo radius-attribute set** *attribute-name* **auth-type** **dot1x**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *attribute-name* | Specifies the name of the attribute to be modified. | The value is a string of 1 to 64 characters. After the name is entered, the system automatically associates the RADIUS attribute with the name. |
| *attribute-value* | Indicates the value of the attribute to be modified. | The value is an integer that ranges from 0 to 4294967295. |
| **auth-type** | Specifies the authentication type.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **dot1x** | Specifies the 802.1X authentication type.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The RADIUS attribute values of different vendors are different. To ensure that Huawei device can successfully communicate with the devices of other vendors, run the **radius-attribute set** command to modify the RADIUS attribute values.

For example, the Huawei device uses Service-Type value 2 to indicate an authentication request from a common user by default, while a non-Huawei RADIUS server uses Service-Type value 1 to indicate an authentication request from a common user; you can run the radius-attribute set service-type 1 command to change the Service-Type value on the device so that the device can communicate with the RADIUS server.

**Precautions**

* The **radius-attribute set** command can modify only the RADIUS attributes in the authentication or accounting request packets sent from a device to the RADIUS server, and cannot modify the RADIUS attributes in the packets sent from the RADIUS server to a device.
* If you run the **display radius-attribute** command to check the RADIUS attributes supported by a device and the **Auth Req** or **Acct Req** field in the command output displays 1, the RADIUS attributes in the authentication or accounting request packets sent from the device to the RADIUS server are supported.
* Among the attributes that can be sent from the device to the RADIUS server, the User-Password, Agent-Circuit-Id, Agent-Remote-Id, NAS-IP-Address, NAS-IPv6-Address, CHAP-Password, CHAP-Challenge, EAP-Message, Framed-Interface-Id, Framed-IPv6-Prefix, and Message-Authenticator attributes cannot be configured using this command.
* The type of the attribute value set using the **radius-attribute set** command must be the same as that of the original attribute value.
* When the value of the HW-Output-Committed-Information-Rate attribute is changed to 0, the attribute is not carried in packets to be sent.



Example
-------

# Create the template temp1 and set the Service-Type attribute value to 1.
```
<HUAWEI> system-view
[HUAWEI] radius-server template temp1
[HUAWEI-radius-temp1] radius-attribute set service-type 1

```