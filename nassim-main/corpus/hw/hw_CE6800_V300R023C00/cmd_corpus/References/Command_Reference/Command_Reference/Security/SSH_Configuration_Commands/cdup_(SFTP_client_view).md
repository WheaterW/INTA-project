cdup (SFTP client view)
=======================

cdup (SFTP client view)

Function
--------



The **cdup** command switches the users from the current directory to one level upper directory of the SFTP server.




Format
------

**cdup**


Parameters
----------

None

Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to access another authorized directory on the SFTP server.

**Prerequisites**

To execute this command, you must enter into the SFTP client view after log in to the SFTP server.

**Configuration Impact**

If the current directory is the upper most directory, the current directory is displayed. For example, the authorized directory of the SFTP service for the SSH user.

**Precautions**

To use this command, one session must be established between the SFTP client and SFTP server. You can switch the users from the current directory to one level upper directory of the SFTP server.


Example
-------

# Switch the current directory of users to the upper-level directory.
```
<HUAWEI> system-view
[~HUAWEI] sftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL+K to abort
Connected to 1.1.1.1 ...
Please input the username: sftp
sftp-client> cdup
Current directory is:
/

```