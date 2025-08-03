delete (FTP client view)
========================

delete (FTP client view)

Function
--------



The **delete** command deletes the corresponding file from the FTP server.




Format
------

**delete** *remote-filename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-filename* | Specifies the file that needs to be deleted from FTP server. | The value is a string of 1 to 128 case-insensitive characters without a blank space. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Whether files can be deleted depends on whether the FTP user has the delete permission. To view the list of directories and files in the specified directory, run the **dir** command.A file deleted in the FTP client view cannot be restored.


Example
-------

# Delete the remote file name as temp.txt
```
<HUAWEI> ftp 1.1.1.1
[ftp] delete temp.txt
Warning: File temp.txt will be deleted. Continue? [Y/N]:y

```