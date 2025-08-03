hwtacacs-server authentication user-name in-authentication-start
================================================================

hwtacacs-server authentication user-name in-authentication-start

Function
--------



The **hwtacacs-server authentication user-name in-authentication-start** command configures the device to carry a user name in the authentication start packets of administrators.

The **undo hwtacacs-server authentication user-name in-authentication-start** command configures the device not to carry a user name in the authentication start packets of administrators.



By default, the authentication start packets of administrators do not carry the user name.


Format
------

**hwtacacs-server authentication user-name in-authentication-start**

**undo hwtacacs-server authentication user-name in-authentication-start**


Parameters
----------

None

Views
-----

HWTACACS server template view,Vsys hwtacacs server template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the authentication start packets sent by the device to the HWTACACS server do not carry a user name. When the device is connected to a server, the server determines whether a user is an administrator based on the user name in the authentication start packet. You can run the **hwtacacs-server authentication user-name in-authentication-start** command to configure the device to carry the user name in the authentication start packets of administrators.

**Precautions**

This function takes effect only for the administrators.


Example
-------

# Configure the device to carry a user name in the authentication start packets of administrators.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server authentication user-name in-authentication-start

```