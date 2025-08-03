password alert before-expire
============================

password alert before-expire

Function
--------

The **password alert before-expire** command to set the password expiration prompt days.

The **undo password alert before-expire** command restores the default number of password expiration prompt days.

By default, the number of password expiration prompt days is 30 days.



Format
------

**password alert before-expire** *days*

**undo password alert before-expire**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *days* | Indicates how long the system displays a prompt before the password expires.  If the value is set to 0, the device does not prompt users that the passwords will expire. | The value is an integer that ranges from 0 to 999, in days. The default value is 30. |




Views
-----

Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

When a user logs in to the device, the device checks how many more days the password is valid for. If the number of days is less than the prompt days set in this command, the device notifies the user in how many days the password will expire and asks the user whether they want to change the password.If the user changes the password, the device records the new password and modification time.If the user does not change the password or fails to change the password, the user can still log in as long as the password has not expired.



Example
-------

# Set the number of password expiration prompt days to 90.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator
[*HUAWEI-aaa-lupp-admin] password alert before-expire 90

```