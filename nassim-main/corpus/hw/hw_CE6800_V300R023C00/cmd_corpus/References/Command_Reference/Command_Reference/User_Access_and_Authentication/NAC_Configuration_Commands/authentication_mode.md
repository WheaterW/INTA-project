authentication mode
===================

authentication mode

Function
--------



The **authentication mode** command configures the user access mode.

The **undo authentication mode** command restores the default setting.



By default, the user access mode is multi-authen.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication mode** { **single-terminal** | **multi-share** | **multi-authen** [ **max-user** *max-user-number* [ **dot1x** | **none** ] \* ] }

**undo authentication mode** [ **multi-authen** **max-user** [ **dot1x** | **none** ] \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **single-terminal** | Indicates that an authentication profile allows only one user to go online. | - |
| **multi-share** | Indicates that an authentication profile allows multiple users to go online.  In this mode, the device authenticates only the first user. If the authentication succeeds, subsequent users share the network access rights of the first user. If the first user goes offline, other users also go offline. | - |
| **multi-authen** | Indicates that an authentication profile allows multiple users to go online.  In this mode, the device authenticates each user. If the authentication succeeds, the device grants independent network access rights to the user. After a user goes offline, other users are not affected. | - |
| **max-user** *max-user-number* | Specifies the maximum number of access users allowed in an authentication profile in multi-authen mode. | The value is an integer that ranges from 1 to 4096. The default value is 4096. |
| **dot1x** | Specifies the maximum number of 802.1X authentication users allowed in an authentication profile in multi-authen mode. | - |
| **none** | Specifies the maximum number of pre-connection users allowed in an authentication profile in multi-authen mode. | - |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After enabling NAC authentication, you can configure a user access mode based on the user access on the interface. The user access modes include:

* single-terminal: applies to the scenario in which only one data terminal is connected to the network through the interface.
* multi-share: applies to the scenario that does not require high security and in which multiple data terminals are connected to the network on the device interface.
* multi-authen: applies to the scenario that requires high security and in which multiple data terminals are connected to the network on the device interface. In this access mode, you can configure the maximum number of access users based on the actual user quantity on the interface. This prevents malicious users from occupying a large amount of device resources and ensures that the users on other device interfaces can normally go online.

**Precautions**

* VLANIF interfaces do not support this function.
* The **authentication mode multi-authen max-user max-user-number** command only indicates the maximum number of access users allowed on the interface in multi-authen mode, not the access mode of the specified interface. To set the access mode of the interface access to multi-authen, run the **authentication mode multi-authen** command.
* If the multi-share mode is configured on a physical interface and the first access user fails to be authenticated and a pre-connection is established, subsequent access users cannot be authenticated. Therefore, the following operations are recommended if the first access user may fail to be authenticated after the multi-share mode is configured on a physical interface.You are advised to disable the pre-connection function (using the **undo authentication pre-authen-access enable** command) when 802.1X or MAC address authentication is used.
* When the authentication mode is set to multi-share in the authentication profile, to authorize a VLAN, set the interface type to hybrid or trunk. If the authentication mode in the authentication profile is set to other modes and VLANs need to be authorized, set the interface type to hybrid.


Example
-------

# In the authentication profile p1, set the user access mode to multi-authen.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] authentication mode multi-authen

```