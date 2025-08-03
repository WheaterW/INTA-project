user-interface vty security-policy disable
==========================================

user-interface vty security-policy disable

Function
--------



The **user-interface vty security-policy disable** command disables the VTY user interface's security policy.

The **undo user-interface vty security-policy disable** command enables the VTY user interface's security policy.



By default, the VTY user interface's security policy is enabled.


Format
------

**user-interface vty security-policy disable**

**undo user-interface vty security-policy disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* The **undo user-interface vty security-policy disable** command clears a user authentication request that has been pending for a long time to access the VTY user interface. For example, if the number of existing user authentication requests has already reached the upper limit but a new authentication request is received, the system clears the authentication request of the user that fails to pass the authentication within 15 seconds and starts authenticating the new user.
* The **user-interface vty security-policy disable** command cannot clear any user authentication request that has been pending for a long time to access the VTY user interface.
* It is recommended that you enable the security policy to harden the VTY user interface's security.

Example
-------

# Disable the VTY user interface's security policy.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty security-policy disable

```