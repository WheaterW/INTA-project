get (SFTP client view)
======================

get (SFTP client view)

Function
--------



The **get** command downloads the files from a remote SFTP server to the local device.




Format
------

**get** *remote-filename* [ *local-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-filename* | Specifies the name of the source file on the SFTP server. | It is a string data type. The absolute path of the file range is from 1 to 255 case-sensitive characters without a blank space. |
| *local-filename* | Specifies the name of the local file on the SFTP client. | It is a string data type. The absolute path of the file range is from 1 to 255 case-sensitive characters without a blank space. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the local file name is not specified, the default name of the file downloaded to the local device is the same as that of the file on the SFTP server.


Example
-------

# Download files from the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.3
Trying 10.1.1.3 ...
Press CTRL+K to abort
Connected to 10.1.1.3 ...
Please input the username: client001
Enter password:
sftp-client> get XXX.cc
Remote file: flash:/ XXX.cc --->  Local file: XXX.cc
Downloading file successfully ended.
File download is completed in 1 seconds.

```