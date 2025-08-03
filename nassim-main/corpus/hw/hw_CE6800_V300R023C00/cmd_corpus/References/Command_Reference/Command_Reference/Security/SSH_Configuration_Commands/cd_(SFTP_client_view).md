cd (SFTP client view)
=====================

cd (SFTP client view)

Function
--------



The **cd** command changes the current working path or directory on the remote SFTP server.




Format
------

**cd** [ *path* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *path* | Specifies the name of the target path or directory on the SFTP server. | The value is a string. The absolute path of the directory ranges from 1 to 255 case-insensitive characters without a blank space. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the cd command to change the current working directory. The root directory is the default working directory.

**Prerequisites**

To execute this command, you must enter into the SFTP client view after log in to the SFTP server.

**Precautions**

The path specified in this command must exist on the server. If the path is not specified, then the current working directory for the SSH user is displayed.


Example
-------

# Switch the current working path or directory of SSH users to directory-test.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL+K to abort
Connected to 10.1.1.1 ...
Please input the username: sftp
sftp-client> cd /directory-test

```