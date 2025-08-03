authentication event action authorize
=====================================

authentication event action authorize

Function
--------



The **authentication event action authorize** command configures authentication event authorization information.

The **undo authentication event action authorize** command restores the default setting.



By default, authentication event authorization information is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication event authen-fail action authorize** { **vlan** *vlan-id* | **service-scheme** *scheme-name* } [ **response-fail** ]

**authentication event pre-authen action authorize** { **vlan** *vlan-id* | **service-scheme** *scheme-name* }

**authentication event authen-server-down action authorize** { **vlan** *vlan-id* | **service-scheme** *scheme-name* } [ **response-fail** ]

**undo authentication event authen-fail action authorize**

**undo authentication event pre-authen action authorize**

**undo authentication event authen-server-down action authorize**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Specifies a VLAN ID. When this parameter is specified, users can access only the resources in the VLAN. | The VLAN must exist on the device. Otherwise, the configuration does not take effect. The value is an integer that ranges from 1 to 4094. |
| **service-scheme** *scheme-name* | Specifies the name of the service scheme based on which network access rights are assigned to users. | The value must be an existing service scheme name on the device. The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **response-fail** | Configures the device to send authentication failure packets to users after network access rights are assigned to the users. If this parameter is specified, the client does not send a logoff packet to log out the user. This prevents the client from automatically sending a logoff packet to log out the user.  If this parameter is not specified, the device sends an authentication success packet to the user by default. As a result, the user is unaware of the authentication failure. In this case, if a user who fails to be authenticated needs to know its authentication status after obtaining network access rights, you can configure the device to send an authentication failure packet to the user. | - |
| **pre-authen** | Configures the device to assign network access rights to users when the users establish pre-connections with the device. | - |
| **authen-server-down** | Configures the device to assign network access rights to users when the authentication server is Down or the server is in the forcible Up state. | - |
| **authen-fail** | Configures the device to assign network access rights to users when the authentication server sends authentication failure packets to the device. | - |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If users establish pre-connections with the device or fail to be authenticated, they have no network access rights.To meet these users' basic network access requirements such as updating the antivirus database and downloading the client, configure authentication event authorization information. The device will assign network access rights to these users based on the authentication phase.

**Precautions**

* This command takes effect only for new access users.
* If no network access rights are configured for users who fail authentication or when the authentication server is Down, the users remain in the pre-connection state and have the network access rights of pre-connection users after authentication fails.
* VLAN-based authorization does not apply to the authentication users who access the network through VLANIF interfaces.
* When the RADIUS server is Down during 802.1X authentication for wired users, some new online clients cannot have bypass rights. For example, new online Windows clients do not receive authentication packets from the RADIUS server after receiving Success packets from the device. As a result, the authentication fails and the clients cannot go online. Currently, the following clients have bypass rights when they go online after the user bypass function is configured: H3C iNode clients using Extensible Authentication Protocol (EAP)-message digest algorithm 5 (MD5) and Protected Extensible Authentication Protocol (PEAP), and Cisco AnyConnect clients using EAP-FAST and PEAP. For a Windows client, for example, Windows 7, choose Local Area Connection > Properties > Authentication > Rollback to Unauthorized Network.


Example
-------

# In the authentication profile authen1, configure the device to assign network access rights specified in VLAN 10 to pre-connection users.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 10
[*HUAWEI] authentication-profile name authen1
[*HUAWEI-authen-profile-authen1] authentication event pre-authen action authorize vlan 10

```