hwtacacs-user change-password hwtacacs-server
=============================================

hwtacacs-user change-password hwtacacs-server

Function
--------



The **hwtacacs-user change-password hwtacacs-server** command enables the device to change the passwords saved on the HWTACACS server.




Format
------

**hwtacacs-user change-password hwtacacs-server** *template-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of an HWTACACS server template. | The HWTACACS server template must already exist. |



Views
-----

User view


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

To change the password saved on the HWTACACS server, users can run the hwtacacs-user change-password hwtacacs-server command on the device. You do not need to change the configuration on the HWTACACS server. After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. You can run the **display security weak-password-dictionary** command to view the passwords.

**Precautions**

* Users logging in to the device must pass HWTACACS authentication, and the HWTACACS server template must exist.
* A user can run this command to change the password only when the user name and password saved on the HWTACACS server do not expire. When a user whose password has expired logs in to the device, the HWTACACS server returns a message indicating that the authentication fails and the user is not allowed to change the password.
* If the user does not enter the user name, new password, or confirm password within 30 seconds, the password change is interrupted.
* You can press Ctrl+C to cancel the password change.
* HWTACACS users who pass AAA authentication can use this command to change the passwords that have not expired. To change the passwords of other HWTACACS users, the users who use this command must have the administrator rights.

Example
-------

# Enable the user that passes HWTACACS authentication to change the password.
```
<HUAWEI> hwtacacs-user change-password hwtacacs-server huawei
Username:cj@huawei 
Old Password: 
New Password: 
Re-enter New password: 
Info: The password has been changed successfully.

```