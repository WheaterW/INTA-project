dot1x-access-profile (authentication profile view)
==================================================

dot1x-access-profile (authentication profile view)

Function
--------



The **dot1x-access-profile** command binds an authentication profile to an 802.1X access profile.

The **undo dot1x-access-profile** command unbinds an authentication profile from an 802.1X access profile.



By default, an authentication profile is not bound to an 802.1X access profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x-access-profile** *access-profile-name*

**undo dot1x-access-profile**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *access-profile-name* | Specifies the name of an 802.1X access profile. | The value must be the name of an existing 802.1X access profile. |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The authentication type used by an authentication profile is determined by the access profile bound to the authentication profile. After being bound to an 802.1X access profile, the authentication profile is enabled with 802.1X authentication. After the authentication profile is applied to the interface, 802.1X authentication can be performed on online users.

**Prerequisites**

An 802.1X access profile has been created using the dot1x-access-profile (system view) command.

**Follow-up Procedure**

Run the authentication-profile (interface view) command to apply the authentication profile to an interface.

**Precautions**

An authentication profile can be bound to only one 802.1X access profile.


Example
-------

# Bind the authentication profile dot1x\_authen\_profile1 to the 802.1X access profile d1.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] quit
[*HUAWEI] authentication-profile name dot1x_authen_profile1
[*HUAWEI-authen-profile-dot1x_authen_profile1] dot1x-access-profile d1

```