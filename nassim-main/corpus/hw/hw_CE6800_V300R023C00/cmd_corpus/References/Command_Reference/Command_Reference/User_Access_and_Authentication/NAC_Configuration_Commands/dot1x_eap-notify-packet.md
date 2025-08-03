dot1x eap-notify-packet
=======================

dot1x eap-notify-packet

Function
--------



The **dot1x eap-notify-packet** command configures the device to send EAP packets with a code number to 802.1X users.

The **undo dot1x eap-notify-packet** command restores the default configuration.



By default, the device does not send EAP packets with a code number to users.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x eap-notify-packet eap-code** *code-num* **data-type** *type-num*

**undo dot1x eap-notify-packet** [ **eap-code** *code-num* **data-type** *type-num* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **data-type** *type-num* | Specifies the data type in EAP packets sent by the device. | The value is an integer that ranges from 1 to 255. The default value is 255. |
| **eap-code** *code-num* | Specifies the code number in EAP packets sent by the device. | The value is an integer that ranges from 5 to 255, the default value is 255. |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a non-Huawei device used as the RADIUS server sends RADIUS packets with attribute 61, EAP packet code number 0xa (hexadecimal notation, 10 in decimal notation), and data type being 0x19 (hexadecimal notation, 25 in decimal notation) to the device, run the **dot1x eap-notify-packet** command on the device so that the device can send EAP packets with code number 0xa and data type 0x19 to users. If the **dot1x eap-notify-packet** command is not executed, the device does not process EAP packets of this type and users are disconnected.

**Precautions**

Currently, the device can only process EAP packets with code number 10 and data type 25.


Example
-------

# In the 802.1X access profile d1, configure the device to send EAP packets with code number 10 and data type 25 to users.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] dot1x eap-notify-packet eap-code 10 data-type 25

```