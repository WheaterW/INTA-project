local-user time-range
=====================

local-user time-range

Function
--------

The **local-user time-range** command sets the access permission time range for a local user.

The **undo local-user time-range** command deletes the access permission time range for a local user.

By default, a local account can access the network anytime.



Format
------

**local-user** *user-name* **time-range** *time-name*

**undo local-user** *user-name* **time-range**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Indicates the local account. | The value is a string of 1 to 253 case-sensitive characters. It cannot contain spaces. |
| *time-name* | Indicates the access permission time range of the local account. time-name specifies the name of the access permission time range. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, must start with a letter. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After a local account is created, the account has no expiration date by default. To restrict the network access time of a local account, run the **local-user time-range** command. After the command is executed, the account can access network resources only in the specified time range.

**Prerequisites**

The time range has been created using the **time-range** command.

**Precautions**

If you run the **local-user time-range** and **local-user expire-date** commands in the AAA view multiple times, only the latest configuration takes effect.After the access permission time range of an online local user is changed, the access permission time range of the user will take effect only when the user goes online next time.

Note the following when configuring case sensitivity for user names:

* Only the user name is case-sensitive and the domain name is case-insensitive.
* For user security purposes, you cannot configure multiple local users with the user names that differ only in uppercase or lowercase. For example, after configuring ABC, you cannot configure Abc or abc as the user name.


Example
-------

# Set the access permission time segment of local account hello@163.net to 9:00-18:00 from Monday to Friday.
```
<HUAWEI> system-view
[~HUAWEI] time-range huawei 9:00 to 18:00 working-day
[*HUAWEI] aaa
[*HUAWEI-aaa] local-user hello@163.net time-range huawei

```