authentication event authen-server-up action re-authen
======================================================

authentication event authen-server-up action re-authen

Function
--------



The **authentication event authen-server-up action re-authen** command enables the device to re-authenticate users in the survival state when the authentication server changes from Down or forcible Up to Up.

The **undo authentication event authen-server-up action re-authen** command restores the default setting.



By default, the device does not re-authenticate users in the survival state when the authentication server changes from Down or forcible Up to UP.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication event authen-server-up action re-authen**

**undo authentication event authen-server-up action re-authen**


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

**Usage Scenario**

After network access rights are configured for users who fail to be authenticated because the authentication server is down, users who obtain the rights (users in the bypass state) can access only limited network resources. In this case, after the authentication server goes up, the device needs to re-authenticate users in the bypass state in a timely manner to meet normal network access requirements.The device sets the RADIUS server status to down. You can run the **radius-server dead-time** command to set the interval for the RADIUS server to return to the active state. After the dead-time expires, the device sets the RADIUS server status to up. This state is the forcible up state. If the server can successfully send and receive packets, the server is in the up state. When the server status changes from down or forcible up to up, the device re-authenticates users in the bypass state. When the server status changes from down to forcible up, re-authentication is not triggered.

**Prerequisites**

The **radius-server testuser** command has been configured in the RADIUS server template so that the device can detect that the authentication server changes from Down to Up.

**Precautions**

This function takes effect only for users who go online after this function is successfully configured.


Example
-------

# In the authentication profile authen1, enable the device to re-authenticate users when the authentication server turns Up from Down or forcible Up.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name authen1
[*HUAWEI-authen-profile-authen1] authentication event authen-server-up action re-authen

```