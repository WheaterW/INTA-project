set boot password
=================

set boot password

Function
--------



The **set boot password** command sets the Boot menu password.




Format
------

**set boot password slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Indicates the slot number. | The value is a string of 1 to 47 case-insensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the Boot menu password.

* The password can contain 8 to 255 characters.
* The password must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
* The password cannot contain question marks (?) or spaces.

**Precautions**

* If you enter an incorrect password for three consecutive times when changing the Boot menu password, you need to wait for 600s before changing the password again.
* When you log in to a new device for the first time through the console port, you need to immediately set the BootLoader password to prevent the console port password from being cleared without authorization. If the BootLoader password is not set, unauthorized users may attempt to log in to a device through the BootLoader and clear the console port password, which will cause security risks.

Example
-------

# Change the Boot menu password of a specified slot.
```
<HUAWEI> system-view
[~HUAWEI] set boot password slot 1
Please set a login password (8~255)
Enter old password:**********
Enter new password:***********
Confirm new password:***********
Info: The password was changed successfully.

```

# Set the Boot menu password for a specified slot.
```
<HUAWEI> system-view
[~HUAWEI] set boot password slot 1
Please set a login password (8~255)
Enter new password:**********
Confirm new password:**********
Info: Setting the boot password is successful.

```