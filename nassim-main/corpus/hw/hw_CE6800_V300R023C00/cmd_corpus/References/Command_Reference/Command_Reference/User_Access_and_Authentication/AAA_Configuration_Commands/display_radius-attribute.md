display radius-attribute
========================

display radius-attribute

Function
--------



The **display radius-attribute** command displays the RADIUS attributes supported by the device.




Format
------

**display radius-attribute** [ **name** *attribute-name* | **type** { *attribute-number1* | **huawei** *attribute-number2* | **microsoft** *attribute-number3* | **dslforum** *attribute-number4* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *attribute-name* | Displays the RADIUS attribute with a specified name. | The value is a string of 1 to 64 characters. After the name is entered, the system automatically associates the RADIUS attribute with the name. |
| **type** | Displays the RADIUS attribute of a specified type. | - |
| *attribute-number1* | Indicates a standard attribute. | The value is an integer that ranges from 1 to 2048. |
| **huawei** *attribute-number2* | Indicates Huawei attribute. | The value is an integer that ranges from 1 to 2048. |
| **microsoft** *attribute-number3* | Indicates the Microsoft attribute. | The value is an integer that ranges from 1 to 2048. |
| **dslforum** *attribute-number4* | Indicates the Digital Subscriber Line Forum attribute. | The value is an integer that ranges from 1 to 2048. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before connecting the device to a RADIUS server, run the display radius-attribute command to view the RADIUS attributes supported by the device. If the device and RADIUS server support different RADIUS attributes according to the command output, run the radius-attribute disable command on the device to disable RADIUS attributes that are not supported by the RADIUS server or run the radius-attribute translate command to translate RADIUS attributes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the RADIUS attributes supported by the device.
```
<HUAWEI> display radius-attribute
  Codes: Auth(Authentication), Acct(Accounting)
         Req(Request), Accp(Accept), Rej(Reject)
         Resp(Response), COA(Change-of-Authorization)
         0(Can not exist in this packet)
         1(Can exist in this packet)
--------------------------------------------------------------------------------
Attribute                       Service    Auth Auth Auth Acct Acct COA COA
Name(Type)                       Type      Req  Accp Rej  Req  Resp Req Ack
--------------------------------------------------------------------------------
User-Name(1)                     All       1    0    0    1    0    1    1
User-Password(2)                 All       1    0    0    0    0    0    0
CHAP-Password(3)                 All       1    0    0    0    0    0    0
NAS-IP-Address(4)                All       1    0    0    1    0    1    1
NAS-Port(5)                      All       1    0    0    1    0    1    1
Service-Type(6)                  All       1    1    0    0    0    0    0
......

```

# Display the RADIUS attribute numbered 2.
```
<HUAWEI> display radius-attribute type 2
 Radius Attribute Type        : 2
 Radius Attribute Name        : User-Password
 Radius Attribute Description : This Attribute indicates the password of the user to be authenticated. Only valid for the PAP authentication.
 Supported Packets            : Auth Request

```

**Table 1** Description of the **display radius-attribute** command output
| Item | Description |
| --- | --- |
| 0(Can not exist in this packet) | The value 0 indicates that the attribute is not supported in packets. |
| 1(Can exist in this packet) | The value 1 indicates that the attribute is supported in packets. |
| Attribute Name(Type) | Attribute name and type. |
| Service Type | Protocol type of the attribute. |
| Auth Req | Authentication request packet. |
| Auth Accp | Authentication accept packet. |
| Auth Rej | Authentication reject packet. |
| Acct Req | Accounting request packet. |
| Acct Resp | Accounting response packet. |
| COA Req | Change of Authorization (COA) request packet. |
| COA Ack | COA acknowledgement packet. |
| Radius Attribute Type | Type of the RADIUS attribute. |
| Radius Attribute Name | Name of the RADIUS attribute. |
| Radius Attribute Description | Description of the RADIUS attribute. |
| Supported Packets | Packets that support the RADIUS attribute. |