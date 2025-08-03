local-user password-force-change disable
========================================

local-user password-force-change disable

Function
--------

The **local-user password-force-change disable** command disables the function of forcibly changing the password (configured when the user is created) when an administrator logs in to the system for the first time.

The **undo local-user password-force-change disable** command enables the function of forcibly changing the password (configured when the user is created) when an administrator logs in to the system for the first time.

By default, the administrator must change the password (configured when the user is created) upon the first login.



Format
------

**local-user** *user-name* **password-force-change** **disable**

**undo local-user** *user-name* **password-force-change** **disable**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | User name, for example, username@domainname or username. The user name cannot contain the following characters: @@ \* ? ". The value cannot start with @. | The value is a string of 1 to 253 case-sensitive characters, spaces not supported. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

When an administrator logs in to the system for the first time, by default, the administrator must change the password configured when the administrator is created. To disable this function, run the **local-user password-force-change disable** command.



Example
-------

# Configure the local user hello\_123 not to change the password upon the first login (the password is configured when the user is created).
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-user hello_123 password irreversible-cipher YsHsjx_202206
[*HUAWEI-aaa] local-user hello_123 password-force-change disable

```