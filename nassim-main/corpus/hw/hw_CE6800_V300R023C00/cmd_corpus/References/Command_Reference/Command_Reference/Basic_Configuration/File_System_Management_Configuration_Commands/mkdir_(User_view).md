mkdir (User view)
=================

mkdir (User view)

Function
--------



The **mkdir** command creates a subdirectory in a specified directory of a storage device.




Format
------

**mkdir** *directory*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *directory* | Specifies the directory name. | The value is a character string in the format of [ drive ][ path ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of drive[ path ], and a relative path is in the format of path. That is, a relative path is the root path of the current working path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **mkdir** command to create a subdirectory.The created subdirectory cannot have the same name as any other subdirectory or file in the specified directory.

**Configuration Impact**

After a subdirectory is created, either of the following situations may occur:

* If no path is specified, a subdirectory is created in the current directory.
* If a path is specified, a subdirectory is created in either an absolute path or a relative path.

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
Info: Succeeded in creating a directory.

```

# Create a new directory named new\_folder.
```
<HUAWEI> ftp 10.18.26.133
[ftp] mkdir new_folder

```

# Create a subdirectory named dd in the current directory.
```
<HUAWEI> mkdir dd
Info: Create directory flash:/dd/...Done.

```