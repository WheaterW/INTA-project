set htm password
================

set htm password

Function
--------



The **set htm password** command sets the HTM password.




Format
------

**set htm password** { **slot** *slotId* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotId* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **all** | Specifies all cards. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve security, run the **set htm password** command to change the HTM password.

**Prerequisites**

Before running this command, run the **trustem** command.

**Precautions**

The new password specified in the **set htm password** command is a string of 8 to 32 characters and must contain at least two types of the following characters: lowercase letters, uppercase letters, digits, and special characters. Only HTM profiles support this command.


Example
-------

# Set a password for the HTM module.
```
<HUAWEI> set htm password slot 1
Please configure the authentication password of slot 1 first.
Enter authentication password:
Set the new password of slot 1.
Please configure the password (8-32)
Enter Password:
Confirm Password:
Info: set the htm password of slot 1 successfully.

```