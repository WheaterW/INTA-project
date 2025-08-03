mkdir
=====

mkdir

Function
--------



The **mkdir** command creates a new directory on the FTP server.




Format
------

**mkdir** *remote-directory*


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

By executing the mkdir command creates a subdirectory. The new remote directory name cannot have the same name as any other subdirectory or file in the specified directory.

**Prerequisites**

After logging in to the FTP server, you can run this command to create a directory. The created directory is stored on the FTP server.

**Configuration Impact**

After a subdirectory is created, either of the following situations may occur:

* If no path is specified, a subdirectory is created in the current directory.
* If a path is specified, a subdirectory is created in either an absolute path or a relative path.

Example
-------

# Create a new directory named new\_folder.
```
<HUAWEI> ftp 10.18.26.133
[ftp] mkdir new_folder

```