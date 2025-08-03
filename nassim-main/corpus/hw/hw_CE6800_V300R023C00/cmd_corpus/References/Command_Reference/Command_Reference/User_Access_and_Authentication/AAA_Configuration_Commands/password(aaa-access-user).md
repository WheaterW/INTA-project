password(aaa-access-user)
=========================

password(aaa-access-user)

Function
--------



The **password** command configures a password for a local access user.



By default, the password of a local access user is empty.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**password cipher** *password*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cipher** *password* | Specifies the password of a local access user. | The value is a string of 8 to 128 case-sensitive characters in plaintext or a string of 128 to 268 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |



Views
-----

aaa-access-user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If no password is configured when a local access user is created, the password is empty, and the local access user cannot log in to the device.

**Precautions**



A simple local access user password may bring security risks. The user password must consist of two types of the following characters, including uppercase letters, lowercase letters, digits, and special characters. In addition, the password cannot repeat or reverse the user name.




Example
-------

# Set the login password of the local access user abc to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-access-user abc
[*HUAWEI-aaa-access-user-abc] password cipher YsHsjx_202206

```