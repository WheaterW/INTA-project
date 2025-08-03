pwd
===

pwd

Function
--------



The **pwd** command displays the working directory on the FTP server.




Format
------

**pwd**


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

You can run this command to view the current working directory of the FTP server. By executing this command displays either the root directory or a subdirectory.

**Prerequisites**

You must establish the connection between FTP client and FTP server before executing this command.


Example
-------

# Display the working directory on the remote FTP server.
```
<HUAWEI> ftp 10.1.1.2
[ftp] pwd

```