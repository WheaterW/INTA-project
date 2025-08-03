time-range
==========

time-range

Function
--------



The **time-range** command sets the access permission time range for a local access user.

The **undo time-range** command deletes the access permission time range for a local access user.



By default, a local access user can access the network anytime.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**time-range** *time-name*

**undo time-range**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-name* | Indicates the access permission time range of the local account. time-name specifies the name of the access permission time range. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

aaa-access-user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a local access user account is created, the account has no expiration date by default. To restrict the network access time of a local account, run the local-user **time-range** command. After the command is executed, the account can access network resources only in the specified time range.

**Prerequisites**

The time range has been created using the **time-range** command.

**Precautions**

If you run the **time-range** and **expire-date** commands in the local user view multiple times, only the latest configuration takes effect. After the access permission time range of an online local access user is changed, the access permission time range of the user will take effect only when the user goes online next time.


Example
-------

# Set the access permission time segment of local access account hello@163.net to 9:00-18:00 from Monday to Friday.
```
<HUAWEI> system-view
[~HUAWEI] time-range huawei 9:00 to 18:00 working-day
[*HUAWEI] aaa
[*HUAWEI-aaa] local-access-user hello@163.net
[*HUAWEI-aaa-access-user-hello@163.net] time-range huawei

```