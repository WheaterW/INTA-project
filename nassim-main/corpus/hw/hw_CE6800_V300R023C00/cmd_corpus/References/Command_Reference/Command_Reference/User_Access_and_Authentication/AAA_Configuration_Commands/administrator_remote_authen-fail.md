administrator remote authen-fail
================================

administrator remote authen-fail

Function
--------

The **administrator remote authen-fail** command enables the account locking function for administrators who fail remote authentication.

The **undo administrator remote authen-fail** command disables the account locking function for administrators who fail remote authentication.

By default, the account locking function is enabled for administrators who fail remote authentication. The authentication retry interval is 5 minutes, the maximum number of consecutive authentication failures is 30, and the account lockout duration is 5 minutes.



Format
------

**administrator remote authen-fail retry-interval** *retry-interval* **retry-time** *retry-time* **block-time** *block-time*

**undo administrator remote authen-fail**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **retry-interval** *retry-interval* | Specifies the authentication retry interval after a remote AAA authentication failure. | The value is an integer that ranges from 5 to 65535, in minutes. The default value is 5. |
| **retry-time** *retry-time* | Specifies the maximum number of consecutive authentication failures. | The value is an integer ranging from 3 to 65535. The default value is 30. |
| **block-time** *block-time* | Specifies the account lockout duration. | The value is an integer that ranges from 5 to 65535, in minutes. The default value is 5. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To ensure account and password security of administrators, you are advised to enable the account locking function for administrators who fail remote authentication. If an administrator enters the incorrect account and password more than the maximum number of consecutive authentication failures within the authentication retry interval, the account is locked. After a certain period, the account is automatically unlocked.

**Precautions**

* This command takes effect only for remote authentication administrators.
* In active/standby scenarios, the locked account is automatically unlocked after an active/standby switchover.
* After the account locking function is disabled for administrators who fail remote authentication using the **undo administrator remote authen-fail** command, the locked account is automatically unlocked.
* If the number of consecutive authentication attempts of a remote authentication user does not reach the upper limit configured using the **administrator remote authen-fail** command, the user is not locked. If you run the **administrator remote authen-fail** command to change the maximum number of consecutive authentication failures to a value smaller than the number of consecutive authentication failures, the user has one more chance to be authenticated.


Example
-------

# Enable the account locking function for administrators who fail remote authentication, and set the authentication retry interval to 5 minutes, maximum number of consecutive authentication failures to 3, and account lockout period to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] administrator remote authen-fail retry-interval 5 retry-time 3 block-time 5

```