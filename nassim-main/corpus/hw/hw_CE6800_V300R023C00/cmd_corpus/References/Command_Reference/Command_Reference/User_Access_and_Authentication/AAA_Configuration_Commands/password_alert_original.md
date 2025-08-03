password alert original
=======================

password alert original

Function
--------

The **password alert original** command enables the device to prompt users to change first configured passwords.

The **undo password alert original** command disables the device from prompting users to change first configured passwords.

By default, the device prompts users to change first configured passwords.



Format
------

**password alert original**

**undo password alert original**



Parameters
----------

None


Views
-----

Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

For security purposes, use this command to enable the device to prompt users to change first configured passwords. When a user logs in to the device:

* If the user enters the first configured password, the device displays a message to ask whether to change the first configured password. The user can select Y or N:
* If the user selects Y to change the password, the user needs to enter the old password, new password, and confirm password. The password can be successfully changed only when the old password is correct and the new password and confirm password are the same and meet requirements (password length and complexity). After the password is changed, the user can log in to the device successfully.
* If the user selects N or fails to change the password, the device does not allow the user to log in.
* If the entered password is not the first configured password, the device does not display any message and the user can successfully log in.After the **undo password alert original** command is executed, the device is disabled from prompting users to change first configured passwords, causing a security risk.

**Precautions**

This function takes effect only for MD-CLI, Telnet, HTTP, SSH, and terminal users.

Some clients do not support password change upon the first login. As a result, the login fails. In this case, you need to disable this function. To disable this function only for specific administrators, run the
**local-user password-force-change disable** command.

Example
-------

# Enable the device to prompt users to change first configured passwords.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator
[*HUAWEI-aaa-lupp-admin] password alert original

```