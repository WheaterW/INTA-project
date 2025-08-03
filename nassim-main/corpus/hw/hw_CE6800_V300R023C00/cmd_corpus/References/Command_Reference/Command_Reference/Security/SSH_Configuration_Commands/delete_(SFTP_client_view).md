delete (SFTP client view)
=========================

delete (SFTP client view)

Function
--------



The **delete** command deletes the specified file from the SFTP server.




Format
------

**delete** *file*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file* | Specifies the file name. | It is a string data type. The absolute path of the file range is from 1 to 1060 characters. It contains the alphanumeric and special characters. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can delete a maximum of 10 files at a time.


Example
-------

# Delete the file test.cc on the server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.164.39.223
Trying 10.164.39.223 ...
Press CTRL+K to abort
Connected to 10.164.39.223 ...
Please input the username: client001
Enter password:   
sftp-client> delete test.cc
Are you sure to delete it?(Y/N): Y
Successfully deleted the file: /home/test.cc

```

# Delete the file test.cc on the server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.164.39.223
Trying 10.164.39.223 ...
Press CTRL+K to abort
Connected to 10.164.39.223 ...
Please input the username: client001
Enter password:   
sftp-client> delete ./test.cc
Warning: Are you sure to delete it? [Y/N]: Y
Info: Successfully deleted the file: /test.cc

```