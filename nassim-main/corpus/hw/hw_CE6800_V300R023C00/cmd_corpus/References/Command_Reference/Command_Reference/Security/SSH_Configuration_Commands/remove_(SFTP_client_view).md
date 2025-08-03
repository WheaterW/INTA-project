remove (SFTP client view)
=========================

remove (SFTP client view)

Function
--------



The **remove** command deletes the specified file from the SFTP server.




Format
------

**remove** *path*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *path* | Specifies the file name. | It is a string data type. The absolute path of the file range is from 1 to 1060 characters. It contains the alphanumeric and special characters. |



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

# Remove the file testnew.txt on the server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.3
Trying 10.1.1.3 ...
Press CTRL+K to abort
Connected to 10.1.1.3 ...
Please input the username: client001
Enter password:   
sftp-client> remove /testnew.txt
Are you sure to remove it?(Y/N): Y
Successfully removed the file: /testnew.txt

```