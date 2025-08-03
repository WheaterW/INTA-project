quit (SFTP client view)
=======================

quit (SFTP client view)

Function
--------



The **quit** command enables the system to disconnect from the remote SFTP server and return to the SFTP client view.




Format
------

**quit**


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

You can use this command to return to the system view from the SFTP client view.


Example
-------

# Disconnect from SFTP server using quit command.
```
<HUAWEI> system-view
[~HUAWEI] sftp 1.1.1.1
sftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL+K to abort
Connected to 1.1.1.1 ...
Please input the username: sftp
sftp-client> quit

```