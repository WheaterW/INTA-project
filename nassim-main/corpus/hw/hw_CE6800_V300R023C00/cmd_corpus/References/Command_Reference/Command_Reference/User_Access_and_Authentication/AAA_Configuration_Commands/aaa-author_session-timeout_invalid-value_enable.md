aaa-author session-timeout invalid-value enable
===============================================

aaa-author session-timeout invalid-value enable

Function
--------



The **aaa-author session-timeout invalid-value enable** command prevents a device from disconnecting or reauthenticating users when the RADIUS server delivers session-timeout with value 0.

The **undo aaa-author session-timeout invalid-value enable** command restores the default setting.



By default, when the RADIUS server delivers session-timeout with value 0, this attribute does not take effect.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**aaa-author session-timeout invalid-value enable**

**undo aaa-author session-timeout invalid-value enable**


Parameters
----------

None

Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When the RADIUS server delivers session-timeout with value 0:If the **aaa-author session-timeout invalid-value enable** command is not configured, the session-timeout attribute delivered by the server does not take effect and the period for disconnecting or reauthenticating users depends on the device configuration.If the **aaa-author session-timeout invalid-value enable** command is configured, the session-timeout attribute delivered by the server takes effect and the device does not disconnect or reauthenticate users.You can run the dot1x timer reauthenticate-period reauthenticate-period-value or **mac-authen timer reauthenticate-period reauthenticate-period-value** command to configure the period for disconnecting or reauthenticating users on the device.


Example
-------

# Prevent the device from disconnecting or reauthenticating users when the RADIUS server delivers session-timeout with value 0.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] aaa-author session-timeout invalid-value enable

```