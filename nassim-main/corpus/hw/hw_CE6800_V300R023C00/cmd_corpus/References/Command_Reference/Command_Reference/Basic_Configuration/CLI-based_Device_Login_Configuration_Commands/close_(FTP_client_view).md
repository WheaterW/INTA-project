close (FTP client view)
=======================

close (FTP client view)

Function
--------



The **close** command terminates the FTP session from the remote server and remains in the FTP client view.




Format
------

**close**


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

This command terminates both control connection and data connection from the remote FTP server.

**Prerequisites**

Ensure no data transfer is in progress before using close command.

**Precautions**

If you run this command during file transfer, the command does not take effect immediately. The device is disconnected only after the file transfer is complete.


Example
-------

# Terminate the FTP session using close command.
```
<HUAWEI> ftp 1.1.1.1
[ftp] close

```