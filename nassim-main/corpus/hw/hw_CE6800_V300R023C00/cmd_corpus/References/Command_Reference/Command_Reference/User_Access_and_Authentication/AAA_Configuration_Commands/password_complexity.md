password complexity
===================

password complexity

Function
--------

The **password complexity** command enables password complexity check.

The **undo password complexity** command restores the default setting.

By default, a device checks whether a password contains at least four types of characters.



Format
------

**password complexity** { **two-of-kinds** | **three-of-kinds** | **four-of-kinds** }

**undo password complexity** { **two-of-kinds** | **three-of-kinds** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **two-of-kinds** | Indicates that a password must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters. | - |
| **three-of-kinds** | Indicates that a password must contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters. | - |
| **four-of-kinds** | Indicates that a password must contain at least four types of the following characters: uppercase letters, lowercase letters, digits, and special characters. | - |




Views
-----

Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

If the password complexity is low, the device has security risks. You are advised to set the password according to highest password complexity. That is, the password contains four types of the following characters: uppercase letters, lowercase letters, digits, and special characters. In addition, you need to change the password periodically.



Example
-------

# Enable the device to check the password complexity in the mode of three out of four.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator
[~HUAWEI-aaa-lupp-admin] password complexity three-of-kinds

```