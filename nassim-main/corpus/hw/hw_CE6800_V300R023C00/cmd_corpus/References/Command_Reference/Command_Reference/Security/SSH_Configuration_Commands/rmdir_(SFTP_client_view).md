rmdir (SFTP client view)
========================

rmdir (SFTP client view)

Function
--------



The **rmdir** command deletes the specified directory on the SFTP server.




Format
------

**rmdir** *directory-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *directory-name* | Specifies the directory on the SFTP server. | It is a string data type. The string length range is from 1 to 1060 characters. It contains alphanumeric and special characters. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before executing the rmdir command, ensure that the directory is an empty directory, else the system throws an error message.You can delete a maximum of 10 directories at a time.


Example
-------

# Delete the directory on the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.164.39.222
Trying 10.164.39.222 ...
Press CTRL+K to abort
Connected to 10.164.39.222 ...
Enter User Name: client001
Enter password:   
sftp-client> rmdir ssh
Are you sure to remove it?(Y/N):Y
Successfully removed the directory: flash:/ssh

```