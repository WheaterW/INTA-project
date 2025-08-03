aaa-authen-bypass
=================

aaa-authen-bypass

Function
--------

The **aaa-authen-bypass** command sets the bypass authentication timeout interval.

The **undo aaa-authen-bypass** command cancels the bypass authentication timeout interval.

By default, no bypass authentication timeout interval is set.



Format
------

**aaa-authen-bypass enable time** *time-value*

**undo aaa-authen-bypass enable**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables remote bypass authentication. | - |
| **time** *time-value* | Specifies the bypass authentication timeout interval. | The value is an integer that ranges from 1 to 1440, in minutes. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to the scenarios that require fast authentication response. When a user in a user domain where multiple authentication modes (for example, RADIUS authentication and local authentication) are configured, bypass authentication is enabled, and the bypass authentication timeout interval is configured, the user will be authenticated using the local authentication mode and the bypass authentication timer is enabled simultaneously if the RADIUS server does not respond to the authentication request. When other users in the same domain are authenticated during the configured bypass authentication timeout interval, the users are directly authenticated using the local authentication mode, so that the users can be authenticated without waiting until the RADIUS server responds to their authentication requests, accelerating the authentication response.

**Precautions**

If only one authentication mode is configured in a user domain, the bypass authentication timer does not take effect after being configured.



Example
-------

# Set the bypass authentication timeout interval to 3 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa-authen-bypass enable time 3

```