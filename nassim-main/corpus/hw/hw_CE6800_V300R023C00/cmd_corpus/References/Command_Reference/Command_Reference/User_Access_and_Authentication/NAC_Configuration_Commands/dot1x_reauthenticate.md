dot1x reauthenticate
====================

dot1x reauthenticate

Function
--------



The **dot1x reauthenticate** command configures re-authentication for online 802.1X authentication users.

The **undo dot1x reauthenticate** command restores the default configuration.



By default, re-authentication is not configured for online 802.1X authentication users.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x reauthenticate**

**undo dot1x reauthenticate**


Parameters
----------

None

Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After modifying the authentication parameters of a user on the authentication server, the administrator must re-authenticate the user in real time to ensure user validity if the user has been online.After the user goes online, the device saves authentication parameters of the user. After re-authentication is configured for online 802.1X authentication users using the **dot1x reauthenticate** command in the 802.1X access profile, the device automatically sends the user authentication parameters in the 802.1X access profile to the authentication server at an interval (specified using the **dot1x timer reauthenticate-period reauthenticate-period-value** command) for re-authentication. If the user authentication information on the authentication server remains unchanged, the users are kept online. If the information has been changed, the users are disconnected and need to be re-authenticated based on the changed authentication parameters.


Example
-------

# In the 802.1X access profile d1, configure re-authentication for online 802.1X authentication users.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[*HUAWEI-dot1x-access-profile-d1] dot1x reauthenticate

```