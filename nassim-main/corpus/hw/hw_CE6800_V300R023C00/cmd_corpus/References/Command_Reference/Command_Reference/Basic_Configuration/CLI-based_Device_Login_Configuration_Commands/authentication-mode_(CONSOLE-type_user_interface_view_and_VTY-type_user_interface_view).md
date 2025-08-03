authentication-mode (CONSOLE-type user interface view/VTY-type user interface view)
===================================================================================

authentication-mode (CONSOLE-type user interface view/VTY-type user interface view)

Function
--------



The **authentication-mode** command sets the authentication mode for the login to the user interface view.

The **undo authentication-mode** command restores the default authentication mode.



By default, no authentication mode is set.


Format
------

**authentication-mode aaa**

**authentication-mode password**

**undo authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **password** | Specifies the password authentication mode for the login to the user interface view. | - |
| **aaa** | Specifies the AAA authentication mode for the login to the user interface view. | - |



Views
-----

CONSOLE-type user interface view,VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* Authentication modes of user interfaces must be set for logging in to the device.
* When AAA authentication is applied to a local user, the commands that the local user can use after logging in to the device depends on the level of the local user specified in the AAA configuration.
* If password authentication is configured, the level of the command that a user can access is determined by the priority of the user interface after the user logs in to the system.

**Precautions**

* When the authentication mode of the user interface is set to password, you can run the **set authentication password** command to change the authentication password of the user interface.
* When the authentication mode of a user interface is set to aaa, the system clears the password configured for the user interface.
* When the authentication mode of the user interface is changed from password to aaa, the system prompts you to enter the old password first.
* If AAA authentication is used, you must run the local-user <username> password irreversible-cipher [ <passwdStr> ] command to configure a local user name and password. Otherwise, the user cannot log in to the device.
* When you run the **undo authentication-mode** command to delete the authentication mode of a user interface, the system prompts you to confirm the deletion before deleting the password of the user interface.
* The password authentication mode is insecure. You are advised to use the AAA authentication mode.
* When you log in to the device through SSH, you must configure the AAA authentication mode.


Example
-------

# In the console user interface view, set the authentication mode to aaa.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] authentication-mode aaa

```

# In the vty user interface view, set the authentication mode to aaa.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] authentication-mode aaa

```