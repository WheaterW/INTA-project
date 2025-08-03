local-aaa-user wrong-password
=============================

local-aaa-user wrong-password

Function
--------

The **local-aaa-user wrong-password** command enables local account locking function and sets the retry interval, consecutive incorrect password attempts, and lockout duration.

The **undo local-aaa-user wrong-password** command disables local account locking function.

By default, the local account locking function is enabled, retry interval is 5 minutes, maximum number of consecutive incorrect password attempts is 3, and account lockout duration is 5 minutes.



Format
------

**local-aaa-user wrong-password retry-interval** *retry-interval* **retry-time** *retry-time* **block-time** *block-time*

**undo local-aaa-user wrong-password**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **retry-interval** *retry-interval* | Specifies the retry interval of a local account. | The value is an integer ranging from 5 to 65535. |
| **retry-time** *retry-time* | Specifies the consecutive incorrect password attempts. | The value is an integer ranging from 3 to 65535. |
| **block-time** *block-time* | Specifies the local account lockout duration.  In actual applications, there is one minute difference in the lockout duration, and the actual lockout duration is less than the configured one. | The value is an integer ranging from 5 to 65535. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to the following scenarios:

* The command locks a local account to improve password security of the local user. If the password is entered incorrectly more than a certain number of times within the given retry period, the account is locked. The device does not authenticate the user when the account is locked.
* The command locks a local account to ensure that the password will not be cracked by a brute force from a malicious user. When attempting to change the password, if the original password is entered incorrectly more than a certain number of times within the given retry period, the account is locked. The user cannot modify the password when the account is locked.

**Follow-up Procedure**

If the number of failed login attempts reaches the upper limit within the retry interval, the user is locked. You can run the local-user user-name **state active** command to unlock the user.

**Precautions**

1. The number of authentication failures is counted only when the password is incorrect. Other local authentication errors are not counted. If a local user fails to log in to the system or the number of password change failures does not reach the upper limit configured using the **local-aaa-user wrong-password** command, the user is not locked. If you run the **local-aaa-user wrong-password** command to change the maximum number of login attempts to a value smaller than the number of login failures or the number of password change failures, the user still has one chance to log in or change the password.
2. The local-aaa-user?wrong-password command takes effect for both password change locking and user locking.


Example
-------

# Enable local account locking, and set the authentication retry interval to 5 minutes, maximum number of consecutive incorrect password attempts to 3, and account lockout duration to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user wrong-password retry-interval 5 retry-time 3 block-time 5

```