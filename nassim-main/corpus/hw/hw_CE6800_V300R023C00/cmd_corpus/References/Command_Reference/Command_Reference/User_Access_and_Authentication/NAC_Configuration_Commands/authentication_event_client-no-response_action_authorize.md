authentication event client-no-response action authorize
========================================================

authentication event client-no-response action authorize

Function
--------



The **authentication event client-no-response action authorize** command configures network access rights for users when the 802.1X client does not respond.

The **undo authentication event client-no-response action authorize** command restores the default setting.



By default, no network access right is configured for users when the 802.1X client does not respond.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication event client-no-response action authorize service-scheme** *service-scheme-name*

**authentication event client-no-response action authorize vlan** *vlan-id*

**undo authentication event client-no-response action authorize**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **service-scheme** *service-scheme-name* | Specifies the name of a service scheme based on which network access rights are assigned. | The value must be the name of an existing service scheme name on the device.  The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlan-id* | Specifies a VLAN ID. When this parameter is specified, users can access only the resources in the VLAN. | The value is an integer ranging from 1 to 4094. |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the 802.1X client does not respond, users cannot pass authentication and thereby have no network access right. Before being successfully authenticated, some users may need certain basic network access rights to download client software and update the antivirus database. The network access rights can be configured for the users when the 802.1X client does not respond, so that the users can access specified network resources.

**Precautions**

This function takes effect only for users who go online after the configuration is successful.When bypass authentication is configured, the no-response authorization event cannot be added, and bypass authentication takes effect preferentially.In 802.1X authentication or multi-mode authentication, if the client does not respond, the timer is started based on the pre-connection re-authentication interval (configured using the authentication timer re-authen pre-authen command) so that the user can pass the authentication in time.


Example
-------

# In the 802.1X access profile d1, configure the device to assign the network access rights specified in VLAN 10 for users when the 802.1X client does not respond.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 10
[*HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] authentication event client-no-response action authorize vlan 10

```