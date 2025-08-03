rmdir (User view)
=================

rmdir (User view)

Function
--------



The **rmdir** command deletes a directory.




Format
------

**rmdir** *directory*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *directory* | Specifies the remote directory name. | The value is a string of case-sensitive characters in the format of [ <drive> ][ path ][ <file-name> ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of <drive> [ path ][ <file-name> ], and a relative path is in the format of [ path ][ <file-name> ]. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By executing the rmdir command deletes an unused or deserted directory.Before executing the rmdir command, ensure that the directory is an empty directory, else the system throws an error message.

**Configuration Impact**

A directory to be deleted must be empty; otherwise, it cannot be deleted.


Example
-------

# Delete the directory named test.
```
<HUAWEI> rmdir test/
Info: Are you sure to remove directory flash:/test/? [Y/N]:y
Info: Removing directory flash:/test/.......Done.

```

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