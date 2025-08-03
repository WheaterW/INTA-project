local-user change-password
==========================

local-user change-password

Function
--------

The **local-user change-password** command enables local users to change their passwords.



Format
------

**local-user change-password**



Parameters
----------

None


Views
-----

User view



Default Level
-------------

0: Visit level



Usage Guidelines
----------------

**Usage Scenario**

If you are a low-level administrator, to ensure security of the password, you can run the local-user change-password command in the user view to change your password after passing the authentication.

After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. To check these passwords, run the
**display security weak-password-dictionary** command.

**Precautions**

To modify the password, a local user must enter the old password. Only the user who passes local authentication can change the password using this command. After a local user successfully changes the password, the user needs to enter the new password for authentication upon the next login.

This command is used to change the password of a local user. It does not save the configuration, but the result of changing the password is saved through the
**local-user password** command. If the server does not receive the old password, new password, or confirmed password from the user within 30 seconds, it terminates the password change process. When the user presses Ctrl+C to cancel password change, the password change process is terminated.A simple password of a local user may bring security risks. When a local user changes the password, the new password must be a string of 8 to 128 characters and must contain at least two types of the following: uppercase letters, lowercase letters, digits, and special characters. In addition, the new password cannot repeat or reverse the user name. For device security purposes, change the password periodically.

Example
-------

# The local user changes the password.
```
<HUAWEI> local-user change-password
Please configure the login password (8-128)
It is recommended that the password consist of at least 2 types of characters, including lowercase letters, uppercase letters, numer
als and special characters. 
Please enter old password: 
Please enter new password: 
Please confirm new password: 
Info: The password is changed successfully.

```