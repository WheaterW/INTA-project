local-access-user
=================

local-access-user

Function
--------



The **local-access-user** command creates an access user view. You can set parameters for the access user in the access user view.

The **undo local-access-user** command deletes an access user view.



By default, no access user is created in the system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**local-access-user** *user-name*

**undo local-access-user** *user-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | User account. | The value is a string of 1 to 64 case-insensitive characters, spaces not supported. The administrator name and access user name can be the same.  If the user name contains a delimiter @, the character before @ is the user name and the character after @ is the domain name. If the value does not contain @, the entire character string represents the user name and the domain name is the default one. ------It is determined by the domain name resolution direction.  In the AAA view, a user name cannot contain @@, \*, ? ". |



Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To facilitate device maintenance, create an access user view on the device and configure the password, the access permission time range, and account expiration date.

**Precautions**



The user specifications include the specifications for administrators and access users.




Example
-------

# Create an access user view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-access-user huawei

```