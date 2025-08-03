tail
====

tail

Function
--------



The **tail** command displays information in the last lines of a specified file.




Format
------

**tail** *file-name* [ *line* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Displays information in a specified file. | The value is a string of 1 to 128 characters in the [ <drive> ][ path ][ <file-name> ] format. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported. |
| *line* | Displays information in the last lines of a specified file. | The value is an integer ranging from 0 to 2147483647. By default, if this parameter is not selected, information in the last 10 lines is displayed. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To display information in the last lines of a specified file, run the **tail** command.


Example
-------

# Display the last two lines of the rpm.log file.
```
<HUAWEI> tail rpm.log 2
[140808-07:52:26] [RPM][SIGN] RPM ReqAppDBRspHandle RequestType:2, RequestId:10001, RcvTransNo:655458744,SndTransNo:655458744,Session:655458744
[140808-07:52:27] [RPM][ERR] File:autoconfig.py does exist in the filelist in node /opt/svrp/router1/1-17/vrpv8/home/$_system for osnode:273 when add file [PID(25786): LinuxError(0)]

```