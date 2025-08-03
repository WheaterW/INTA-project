authentication event action authorize keep
==========================================

authentication event action authorize keep

Function
--------



The **authentication event action authorize keep** command configures authentication event authorization information.

The **undo authentication event action authorize** command restores the default setting.



By default, authentication event authorization information is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication event authen-server-down action authorize keep** [ **no-response** | **response-fail** ]

**authentication event authen-server-noreply action authorize keep** [ **no-response** | **response-fail** ]

**undo authentication event authen-server-down action authorize**

**undo authentication event authen-server-noreply action authorize**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **no-response** | Indicates that the device does not respond to users after network access rights are assigned to the users.  If this parameter is not specified, the device sends an authentication success packet to an online user by default after the user initiates an authentication request. | - |
| **response-fail** | Configures the device to send authentication failure packets to users after assigning network access rights to the users.  If this parameter is not specified, the device sends an authentication success packet to an online user by default when the user initiates an authentication request. As a result, the user is unaware of the authentication failure. To solve this problem, specify this parameter so that the device will send authentication failure packets for the users to know their authentication results. | - |
| **authen-server-noreply** | Configures the device to assign network access rights to users when the authentication server does not respond. | - |
| **keep** | Indicates that online users retain their original network access rights.  If an online user is re-authenticated and the re-authentication mode is different from the original authentication mode, the online user cannot retain the original network access rights. | - |
| **authen-server-down** | Configures the device to assign network access rights to users when the authentication server is Down or the server is in the forcible Up state. | - |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the authentication server is down or does not respond, the device allows online users to continue accessing the network.

**Precautions**

You can run the **authentication timer authorize-keep-aging** command to adjust the aging time of online user entries.Run the **authentication event authen-server-down action close re-authen** command to disable re-authentication when the authentication server is down.The **authentication event authen-server-down action authorize keep no-response** command takes effect for both new users and online users.


Example
-------

# In the authentication profile authen1, configure the device to assign network access rights to users when the authentication server does not respond.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name authen1
[*HUAWEI-authen-profile-authen1] authentication event authen-server-noreply action authorize keep

```