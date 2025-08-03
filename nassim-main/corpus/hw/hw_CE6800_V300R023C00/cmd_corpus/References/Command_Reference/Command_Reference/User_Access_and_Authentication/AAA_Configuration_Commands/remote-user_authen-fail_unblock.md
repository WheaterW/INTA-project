remote-user authen-fail unblock
===============================

remote-user authen-fail unblock

Function
--------

The **remote-user authen-fail unblock** command unlocks remote AAA authentication accounts.



Format
------

**remote-user authen-fail unblock** { **username** *username* | **all** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **username** *username* | Unlocks a specified account that fails the remote AAA authentication. | The value is a string of 1 to 253 case-insensitive characters without spaces. |
| **all** | Unlocks all accounts that fail the remote AAA authentication. | - |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

You may need to unlock remote AAA authentication accounts in the following situations:

* When a user enters an incorrect user name or password fewer times than the maximum permitted, run the **remote-user authen-fail unblock** command to unlock the user and delete the incorrect record of the user from the device.
* When a user is incorrectly locked or needs to be unlocked due to special reasons, run the **remote-user authen-fail unblock** command to unlock the user.


Example
-------

# Unlock the remote AAA authentication account test.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] remote-user authen-fail unblock username test

```