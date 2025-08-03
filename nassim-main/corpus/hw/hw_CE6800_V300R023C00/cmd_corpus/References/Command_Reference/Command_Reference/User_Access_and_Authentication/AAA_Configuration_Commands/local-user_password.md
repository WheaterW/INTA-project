local-user password
===================

local-user password

Function
--------

The **local-user password** command configures a password for a local account.

By default, the password of a local account is empty.



Format
------

**local-user** *user-name* **password**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies the local user name. | The value is a string of 1 to 253 characters. It cannot contain spaces, asterisk, double quotation mark and question mark.  During local authentication or authorization, run the authentication-mode { local | local-case } or authorization-mode { local | local-case } command to configure case sensitivity for user names. If the parameter is set to local, user names are case-insensitive. If the parameter is set to local-case, user names are case-sensitive. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

If no password is configured when a local user is created, the password is empty, and the local user cannot log in to the device.

**Precautions**

A simple local user password may bring security risks. The user password must consist of two types of characters, including uppercase letters, lowercase letters, numerals, and special characters. In addition, the password cannot be the same as the user name or user name in a reverse order.



Example
-------

# Set the password to abc@#123456 for the local account hello@163.net.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-user hello@163.net password
Please configure the login password (8-128)
It is recommended that the password consist of at least 2 types of characters, i
ncluding lowercase letters, uppercase letters, numerals and special characters. 
Please enter password:                                      
Please confirm password:                               
Info: Add a new user.

```