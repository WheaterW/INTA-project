authentication timer re-authen
==============================

authentication timer re-authen

Function
--------



The **authentication timer re-authen** command configures the interval for re-authenticating pre-connection users or users who fail the authentication.

The **undo authentication timer re-authen** command restores the default setting.



By default, pre-connection users and users who fail the authentication are re-authenticated at an interval of 60 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication timer re-authen** { **pre-authen** *pre-authen-time* | **authen-fail** *authen-fail-time* }

**undo authentication timer re-authen** { **pre-authen** | **authen-fail** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pre-authen** *pre-authen-time* | Specifies the interval for re-authenticating pre-connection users. | The value is 0 or an integer ranging from 30 to 7200, in seconds. The default value is 60s.  The value 0 indicates that the re-authentication function is disabled for pre-connection users. |
| **authen-fail** *authen-fail-time* | Specifies the interval for re-authenticating users who fail the authentication. | The value is 0 or an integer ranging from 30 to 7200, in seconds. The default value is 60s.  The value 0 indicates that the re-authentication function is disabled for users who fail to be authenticated. |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device creates the mapping user entries when network access policies are assigned to users who are in the pre-connection phase or fail the authentication. To enable users to pass authentication in real time, the device periodically re-authenticates the users who are in the pre-connection phase or fail the authentication according to the user entries. The administrator can adjust the re-authentication interval based on the actual network requirements.

**Precautions**

* This function takes effect only for users who go online after the configuration is successful.
* When there are a large number of users, the re-authentication interval may be longer than the configured re-authentication interval to reduce the impact on device performance.
* If a static user configured with 802.1X authentication fails to be authenticated and enters the pre-connection state, 802.1X authentication is performed first. During 802.1X authentication, the pre-authen re-authen-time timer does not take effect. If 802.1X authentication fails, the pre-authen re-authen-time timer takes effect and re-authentication is triggered for the static user based on the re-authentication interval configured on the timer.


Example
-------

# In the authentication profile authen1, set the interval for re-authenticating users who fail the authentication to 300 seconds.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name authen1
[*HUAWEI-authen-profile-authen1] authentication timer re-authen authen-fail 300

```