user (FTP client view)
======================

user (FTP client view)

Function
--------



The **user** command specifies the user name and password for remote login.




Format
------

**user** *username*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *username* | Specifies the login user name. | The value is a string of 1 to 255 case-insensitive characters, spaces not supported. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The device allows you to log in to the FTP server by using another user name without exiting from the FTP client view. This command also establishes the FTP connection same as **ftp** command.This feature is completely dependent on the FTP server's behaviour.


Example
-------

# Log in to the FTP server with the user name user1.
```
<HUAWEI> ftp 10.1.1.1
[ftp] user user1
331 Password required for root.
Enter password:

```