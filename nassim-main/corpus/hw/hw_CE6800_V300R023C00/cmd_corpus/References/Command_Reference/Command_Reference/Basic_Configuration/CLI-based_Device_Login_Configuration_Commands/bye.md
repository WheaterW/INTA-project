bye
===

bye

Function
--------



The **bye** command terminates the FTP session from the remote server and exit from FTP view.




Format
------

**bye**


Parameters
----------

None

Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After running the **bye** command, you can terminate the connection with the remote FTP server and return from the FTP client view to the user view.

**Prerequisites**

Ensure no data transfer is in progress before using close command.

**Precautions**

If you run this command during file transfer, the command does not take effect immediately. The device disconnects from the network and returns to the user view only after the file transfer is complete.


Example
-------

# Disconnect from the remote FTP server and return to the user view using bye command.
```
<HUAWEI> ftp 1.1.1.1
[ftp] bye

```