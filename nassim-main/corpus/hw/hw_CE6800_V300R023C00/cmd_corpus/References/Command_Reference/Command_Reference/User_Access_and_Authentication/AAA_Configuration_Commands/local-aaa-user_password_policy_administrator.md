local-aaa-user password policy administrator
============================================

local-aaa-user password policy administrator

Function
--------

The **local-aaa-user password policy administrator** command enables the password policy for local administrators and enters the local administrator password policy view.

By default, the password policy of local administrators is enabled.



Format
------

**local-aaa-user password policy administrator**



Parameters
----------

None


Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

After a local user is created using the local-user command, the minimum length and complexity of the password are limited. If you want to improve password security, you can run the following commands to configure the password policy for the local administrators:

* Run the **password expire** command to set the password validity period.
* Run the **password alert before-expire** command to set the password expiration prompt days.
* Run the **password alert original** command to enable the device to prompt users to change first configured passwords.
* Run the **password history record number** command to set the maximum number of previously used passwords recorded for each user.
* Run the **password min-length length** command to set the minimum length of a password.


Example
-------

# Enable the local administrator password policy and enter the local administrator password policy view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator

```