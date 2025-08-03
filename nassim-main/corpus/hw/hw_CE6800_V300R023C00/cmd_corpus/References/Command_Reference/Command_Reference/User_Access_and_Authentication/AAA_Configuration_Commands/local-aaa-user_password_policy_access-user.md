local-aaa-user password policy access-user
==========================================

local-aaa-user password policy access-user

Function
--------



The **local-aaa-user password policy access-user** command enables the password policy for local access users and enters the local access user password policy view.

The **undo local-aaa-user password policy access-user** command disables the password policy of local access users.



By default, the password policy of local access users is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**local-aaa-user password policy access-user**

**undo local-aaa-user password policy access-user**


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

When a local access user is created using the local-access-user command, the minimum length and complexity of the password are limited. If you want to improve password security, run this command to configure password policies. The new password cannot be the same as any previously used password stored on the device.


Example
-------

# Enable the local access user password policy and enter the local access user password policy view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy access-user
[*HUAWEI-aaa-lupp-acc]

```