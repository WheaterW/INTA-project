rename (SFTP client view)
=========================

rename (SFTP client view)

Function
--------



The **rename** command renames a file or directory on the SFTP server.




Format
------

**rename** *old-name* *new-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *old-name* | Specifies the name of the source file or directory on the SFTP server. | It is a string data type. The absolute path of the file or directory range is from 1 to 255 characters. |
| *new-name* | Specifies the name of the target file or directory on the SFTP server. | It is a string data type. The absolute path of the file or directory range is from 1 to 255 characters. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After renaming, the original file name becomes invalid. This command returns error, if a file exists with the new-name.


Example
-------

# Rename the file in the authorized directory on the SSH server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.3
Trying 10.1.1.3 ...
Press CTRL+K to abort
Connected to 10.1.1.3 ...
Please input the username: client001
Enter password:   
sftp-client> rename /test.txt /testnew.txt
Warning: Rename /test.txt to /testnew.txt?[Y/N]: y

```