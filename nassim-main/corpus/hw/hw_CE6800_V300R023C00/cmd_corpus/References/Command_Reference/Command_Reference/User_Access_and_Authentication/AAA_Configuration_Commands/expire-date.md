expire-date
===========

expire-date

Function
--------



The **expire-date** command sets the expiration date of a local access account.

The **undo expire-date** command restores the default expiration date of a local access account.



By default, a local access account is permanently valid.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**expire-date** *expire-date*

**undo expire-date**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *expire-date* | Specifies the expiration date of the local access account. | The value is in the format of YYYY/MM/DD. YYYY/MM/DD indicates year/month/day. YYYY ranges from 2000 to 2099, MM ranges from 1 to 12, and DD ranges from 1 to 31. |



Views
-----

aaa-access-user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After a local access account is created, the account has no expiration date by default. You can run the local-user **expire-date** command to set the expiration date of a local access account. When the expiration date is reached, the account expires. This configuration enhances network security.


Example
-------

# Set the expiration date of local access account hello@163.net to 2021/10/1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-access-user hello@163.net
[*HUAWEI-aaa-access-user-hello@163.net] expire-date 2021/10/1

```