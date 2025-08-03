dot1x authentication-method
===========================

dot1x authentication-method

Function
--------



The **dot1x authentication-method** command configures an 802.1X authentication mode.

The **undo dot1x authentication-method** command restores the default configuration.



The default 802.1X authentication mode is eap, which indicates Extensible Authentication Protocol (EAP) relay authentication.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x authentication-method** { **chap** | **eap** | **pap** }

**undo dot1x authentication-method**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **chap** | Specifies EAP termination authentication using the Challenge Handshake Authentication Protocol (CHAP). | - |
| **eap** | Specifies Extensible Authentication Protocol (EAP) relay authentication. | - |
| **pap** | Specifies EAP termination authentication using the Password Authentication Protocol (PAP). | - |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During 802.1X authentication, users exchange authentication information with the device using EAP packets. The device uses two modes to exchange authentication information with the RADIUS server.EAP termination: The device directly parses EAP packets, encapsulates user authentication information into a RADIUS packet, and sends the packet to the RADIUS server for authentication. EAP termination is classified into PAP or CHAP authentication.PAP is a two-way handshake authentication protocol. It transmits passwords in plain text format in RADIUS packets.CHAP is a three-way handshake authentication protocol. It transmits only user names but not passwords in RADIUS packets. CHAP is more secure and reliable than PAP. If higher security is required, CHAP is recommended.EAP relay (specified by eap): The device encapsulates EAP packets into RADIUS packets and sends the RADIUS packets to the RADIUS server. The device does not parse the received EAP packets but encapsulates them into RADIUS packets. This mechanism is called EAP over Radius (EAPoR).The processing capability of the RADIUS server determines whether EAP termination or EAP relay is used. If the RADIUS server has a higher processing capability and can parse a large number of EAP packets before authentication, the EAP relay mode is recommended. If the RADIUS server has a processing capability not good enough to parse a large number of EAP packets and complete authentication, the EAP termination mode is recommended and the device parses EAP packets for the RADIUS server. When the authentication packet processing method is configured, ensure that the client and server both support this method; otherwise, the users cannot pass authentication.

**Precautions**

* In PAP authentication mode, user passwords are transmitted in plain text. In CHAP authentication mode, user passwords are transmitted in cipher text using MD5, which is not secure enough. You are advised to use EAP authentication, which ensures more secure transmission of user passwords.
* The authentication mode for 802.1X users can be set to EAP relay only when RADIUS authentication is used.
* When AAA local authentication is used, the authentication mode for 802.1X users can only be set to EAP termination.
* If the 802.1X client uses MD5 encryption, the authentication mode on the device can be set to EAP or CHAP. If the 802.1X client uses PEAP authentication, the authentication mode on the device can be set to EAP.
* When an 802.1X user is online on an interface and the user authentication mode is changed in the 802.1X access profile bound to the interface, if the user authentication mode is switched between EAP termination and EAP relay, the online user is logged out. If the user authentication mode is switched between CHAP and PAP of EAP termination, the user remains online.

Example
-------

# In the 802.1X access profile d1, configure the device to use PAP authentication for 802.1X users.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] dot1x authentication-method pap
Info: PAP/CHAP is not a secure protocol, and EAP is recommended.                                                                    
Warning: Changing the configuration will cause online users to go offline. Continue? [Y/N]:y

```