cd
==

cd

Function
--------



The **cd** command changes the current remote working directory.




Format
------

**cd** *pathname*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pathname* | Specifies the remote directory name. | The value is a string of 1 to 255 case-sensitive characters without a blank space. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the cd command to change the current working directory. The root directory is the default working directory.

**Precautions**

To successfully run this command, FTP users must have the permission to switch directories on the remote server.


Example
-------

# Change the remote directory name to new\_folder.
```
<HUAWEI> ftp 1.1.1.1
[ftp] cd new_folder

```