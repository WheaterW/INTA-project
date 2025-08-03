rmdir
=====

rmdir

Function
--------



The **rmdir** command deletes a specified directory from the FTP server.




Format
------

**rmdir** *remote-directory*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-directory* | Specifies the name of the destination directory. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By executing the rmdir command deletes an unused or deserted directory.

**Precautions**

A directory to be deleted must be empty, otherwise, it cannot be deleted.You can use this command to delete the specified directory from FTP server and not from FTP client.


Example
-------

# Delete the new\_folder directory on the FTP server.
```
<HUAWEI> ftp 10.1.1.2
[ftp] rmdir new_folder

```