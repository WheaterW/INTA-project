dot1x timer
===========

dot1x timer

Function
--------



The **dot1x timer** command configures 802.1X timer parameters.

The **undo dot1x timer** command restores the default settings.



For the default 802.1X timer parameter settings, see the parameter description.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x timer** { **client-timeout** *client-timeout-value* | **reauthenticate-period** *reauthenticate-period-value* }

**undo dot1x timer** { **client-timeout** | **reauthenticate-period** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **client-timeout** *client-timeout-value* | Sets the client authentication timeout period.  If there are some terminals on the network, the terminals wait for a long time to respond to the EAP-Request/MD5 Challenge packets sent by the device. In this case, you can increase the value of client-timeout client-timeout-value to prevent user login failures caused by slow response of terminals. The adjustment principle is as follows: 3 x client-timeout-value > Response delay of terminals. | The value is an integer that ranges from 1 to 120, in seconds.  By default, the client authentication timeout period is 5 seconds. |
| **reauthenticate-period** *reauthenticate-period-value* | Specifies the periodic re-authentication period for online 802.1X users. | The value is an integer that ranges from 1 to 65535, in seconds.  By default, the periodic re-authentication period is 3600 seconds for online 802.1X users. |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During 802.1X authentication, multiple timers are started to implement proper and orderly interactions between access users, access devices, and the authentication server. You can change the values of some timers by running this command to adjust the interaction process. (The values of some timers cannot be changed.) This command is necessary in special network environments. Generally, the default settings of the timers are recommended.This command only sets the values of the timers. To enable the timers, perform corresponding configurations or use default settings.

* The client authentication timeout timer and the timer for the interval for sending authentication requests are enabled by default. You can run the **dot1x retry** command to configure the number of retransmissions of authentication request packets when the client authentication times out.
* By default, the re-authentication timer for online 802.1X users is disabled. You can run the **dot1x reauthenticate** command to enable the timer.

**Precautions**

The timeout period of EAP-Request/MD5 Challenge packets must be less than 100 seconds. The timeout period is calculated using the following formula: Timeout = (*max-retry-value*+1) \* *client-timeout-value*(*max-retry-value*is configured using the **dot1x retry** *max-retry-value*command, and *client-timeout-value*is configured using the **dot1x timer client-timeout** *client-timeout*command).In most cases, the default re-authentication period is recommended. If many ACL rules need to be delivered during user authorization, to improve the device processing performance, you are advised to disable re-authentication or increase the re-authentication period. When remote authentication and authorization are used, a short re-authentication period may lead to high CPU usage.When many users need to be re-authenticated, to reduce the impact of re-authentication on device performance, the actual re-authentication period may be longer than the configured re-authentication period.

A smaller value of the re-authentication period requires higher device performance. If there are more than 1000 users, you are advised to set the re-authentication period to a large value. The following lists the recommended minimum re-authentication period based on the number of users.

* If the number of users ranges from 1 to 99, it is recommended that the re-authentication period be greater than or equal to 1 second.
* If the number of users ranges from 100 to 499, it is recommended that the re-authentication period be greater than or equal to 5 seconds.
* If the number of users ranges from 500 to 999, it is recommended that the re-authentication period be greater than or equal to 10 seconds.
* If the number of users ranges from 1000 to 1999, it is recommended that the re-authentication period be greater than or equal to 20 seconds.
* If the number of users is greater than 2000, it is recommended that the re-authentication period be greater than or equal to 60 seconds.

Example
-------

# In the 802.1X access profile d1, set the client authentication timeout period to 90 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[~HUAWEI-dot1x-access-profile-d1] dot1x timer client-timeout 90

```