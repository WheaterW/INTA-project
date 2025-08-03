authentication event authen-server-down action close re-authen
==============================================================

authentication event authen-server-down action close re-authen

Function
--------



The **authentication event authen-server-down action close re-authen** command disables re-authentication when the authentication server is Down.

The **undo authentication event authen-server-down action close re-authen** command restores the default setting.



By default, the device does not re-authenticate users when the authentication server turns Up from Down.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication event authen-server-down action close re-authen**

**undo authentication event authen-server-down action close re-authen**


Parameters
----------

None

Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a re-authentication scenario, after the **authentication event action authorize keep** command is run, online users retain the original network access rights when the authentication server is Down. If re-authentication is performed on these users, the client frequently initiates re-authentication and may remain silent after multiple times. As a result, these users cannot access the network. To prevent this problem, you are advised to run the **authentication event authen-server-down action close re-authen** command to disable re-authentication when the authentication server is Down.


Example
-------

# Disable re-authentication when the authentication server is Down.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name authen1
[*HUAWEI-authen-profile-authen1] authentication event authen-server-down action close re-authen

```