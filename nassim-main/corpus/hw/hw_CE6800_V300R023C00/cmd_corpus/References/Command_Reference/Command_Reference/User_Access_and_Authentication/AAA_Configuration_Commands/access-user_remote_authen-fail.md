access-user remote authen-fail
==============================

access-user remote authen-fail

Function
--------



The **access-user remote authen-fail** command enables the account locking function for access users who fail remote authentication.

The **undo access-user remote authen-fail** command disables the account locking function for access users who fail remote authentication.



By default, the account locking function is disabled for access users who fail remote authentication.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**access-user remote authen-fail retry-interval** *retry-interval* **retry-time** *retry-time* **block-time** *block-time*

**undo access-user remote authen-fail**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **retry-interval** *retry-interval* | Specifies the authentication retry interval after a remote AAA authentication failure. | The value is an integer that ranges from 5 to 65535. |
| **retry-time** *retry-time* | Specifies the maximum number of consecutive authentication failures. | The value is an integer that ranges from 3 to 65535. |
| **block-time** *block-time* | Specifies the account lockout duration. | The value is an integer that ranges from 5 to 65535. |



Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To ensure account and password security for access users, you are advised to enable the account locking function for access users who fail remote authentication. If the number of consecutive incorrect account or password attempts reaches the upper limit within the retry interval, the account is locked and will be automatically unlocked after a specified period.

**Precautions**

* This command takes effect only for remote authentication access users.
* In active/standby scenarios, after an active/standby switchover, the locked account is automatically unlocked.
* After you run the **undo access-user remote authen-fail** command to disable the account locking function for access users who fail remote authentication, the locked accounts are automatically unlocked.
* If the number of consecutive authentication attempts of a remote authentication user does not reach the limit configured using the **access-user remote authen-fail** command, the user is not locked. If you run the **access-user remote authen-fail** command to change the maximum number of authentication attempts and the new maximum number is smaller than the number of consecutive authentication failures, the user has one chance to attempt authentication.

Example
-------

# Enable the account locking function for access users who fail remote authentication. Set the authentication retry interval to 5 minutes, maximum number of consecutive authentication failures to 3, and account lockout duration to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] access-user remote authen-fail retry-interval 5 retry-time 3 block-time 5

```