mkdir (SFTP client view)
========================

mkdir (SFTP client view)

Function
--------



The **mkdir** command creates a directory on the remote SSH server.




Format
------

**mkdir** *path*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *path* | Specifies the directory path or name on the SFTP server. | It is a string data type. The value ranges from 1 to 255 characters. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After creating the directory by using the **mkdir** command, you can run the dir or **ls** command to view the information. The **mkdir** command returns error, if the file or directory with the same name already exists.To use the **mkdir** command, you must be an authorized user with a permission on the SFTP server.


Example
-------

# Create a directory on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.164.39.222
Trying 10.164.39.222 ...
Press CTRL+K to abort
Connected to 10.164.39.222 ...
Please input the username: client001
Enter password:   
sftp-client> mkdir ssh

```