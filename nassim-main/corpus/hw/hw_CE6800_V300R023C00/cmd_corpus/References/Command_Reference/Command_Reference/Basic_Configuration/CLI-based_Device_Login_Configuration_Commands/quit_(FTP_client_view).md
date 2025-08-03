quit (FTP client view)
======================

quit (FTP client view)

Function
--------



The **quit** command terminates the FTP session from the remote server and exit from FTP view.




Format
------

**quit**


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

After running the **quit** command, you can return to the user view from the FTP client view.For example, you can run the **quit** command in the user view to exit the system.


Example
-------

# Disconnect from the remote FTP server and return to the user view using quit command.
```
<HUAWEI> ftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 VRPV8 FTP service ready.
User(1.1.1.1:(none)):ftp
331 Password required for ftp.
Enter password:
230 Logged on
[ftp] quit

```