password expire
===============

password expire

Function
--------

The **password expire** command sets the password validity period.

The **undo password expire** command restores the default value of password validity period.

By default, the password validity period is 90 days.



Format
------

**password expire** *days*

**undo password expire**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *days* | Indicates the password validity period.  If the value is 0, the password is permanently valid. | The value is an integer that ranges from 0 to 999, in days. The default value is 90. |




Views
-----

Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To improve password security, you are advised to run this command to set the validity period of a local user password. After the validity period expires, the password becomes invalid. If a user uses this password to log in to the device, the device displays a message indicating that the password has expired and asking the user whether to change the password after the user successfully logs in. If the user enters Y, the user needs to enter the old password, new password, and confirm password. The password can only be successfully changed when the old password is correct, the new password and confirm password are the same, and the new password meets the password length and complexity requirements. Then, the user can log in to the device. If the user enters N or fails to change the password, the user cannot log in to the device.

**Precautions**

Changing the system time will affect the password validity status.After this command is executed, the device checks whether the password expires every minute; therefore, there may be a time difference within 1 minute.



Example
-------

# Set the password validity period to 120 days.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator
[*HUAWEI-aaa-lupp-admin] password expire 120

```