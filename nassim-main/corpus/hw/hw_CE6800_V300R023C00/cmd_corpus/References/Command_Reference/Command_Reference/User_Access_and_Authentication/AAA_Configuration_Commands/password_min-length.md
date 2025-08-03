password min-length
===================

password min-length

Function
--------

The **password min-length** command configures the minimum length of a password.

The **undo password min-length** command restores the minimum length of a password to the default value.

The default value is 8



Format
------

**password min-length** *password-min-length*

**undo password min-length**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *password-min-length* | Sets the minimum length of a password. | The value is an integer that ranges from 8 to 128. The default is 8. |




Views
-----

Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To prevent security risks such as account stealing, run this command to raise password strength requirements.

**Prerequisites**

Log in to the device as an administrator.

**Configuration Impact**

After the password min-length command is configured and if you create a local user or change the password of an existing local user, the length of the new user's password or the length of the existing user's new password must exceed the value specified by the password min-length command; otherwise, the user cannot be created or the password cannot be changed.



Example
-------

# Set the minimum length of administrator passwords to 10.
```
<HUAWEI> system-view
[HUAWEI] aaa
[HUAWEI-aaa] local-aaa-user password policy administrator
[HUAWEI-aaa-lupp-admin] password min-length 10

```