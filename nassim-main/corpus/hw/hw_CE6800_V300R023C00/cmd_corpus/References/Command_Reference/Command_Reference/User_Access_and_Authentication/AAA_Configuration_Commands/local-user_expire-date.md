local-user expire-date
======================

local-user expire-date

Function
--------

The **local-user expire-date** command sets the expiration date of a local account.

The **undo local-user expire-date** command restores the default expiration date of a local account.

By default, a local account is permanently valid.



Format
------

**local-user** *user-name* **expire-date** *expire-date*

**undo local-user** *user-name* **expire-date**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies a local account. | The value is a string of 1 to 253 case-sensitive characters, spaces not supported. |
| *expire-date* | Specifies the expiration date of the local account. | The value is expressed in the format of YYYY/MM/DD. The value is a date ranging from 2000/01/01 to 2099/12/31. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

After a local account is created, the account has no expiration date by default. You can run the **local-user expire-date** command to set the expiration date of a local account. When the expiration date is reached, the account expires. This configuration enhances network security.



Example
-------

# Set the expiration date of local account hello@163.net to 2013/10/1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-user hello@163.net expire-date 2013/10/1

```