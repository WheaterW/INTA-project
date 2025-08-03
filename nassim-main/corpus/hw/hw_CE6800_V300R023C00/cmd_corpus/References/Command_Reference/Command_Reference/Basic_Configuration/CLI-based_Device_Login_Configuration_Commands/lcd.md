lcd
===

lcd

Function
--------



The **lcd** command changes the local working directory of an FTP client.




Format
------

**lcd** [ *directory* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *directory* | Specifies the name of the destination directory. | The value is a string of 1 to 255 case-sensitive characters without a blank space. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By executing the **lcd** command displays the local working directory of FTP client. By executing the pwd command displays the remote working directory of FTP server, which is different from **lcd** command.


Example
-------

# Change the local working directory to /opt/vrpv8/home.
```
<HUAWEI> ftp 10.1.1.1
[ftp] lcd /opt/vrpv8/home

```