put (SFTP client view)
======================

put (SFTP client view)

Function
--------



The **put** command uploads the files to a remote SFTP server.




Format
------

**put** *local-filename* [ *remote-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-filename* | Specifies the name of the local source file on the SFTP client. | It is a string data type. The absolute path of the file range is from 1 to 255 characters. It contains the alphanumeric and special characters. |
| *remote-filename* | Specifies the name of the destination file on the SFTP server. | It is a string data type. The absolute path of the file range is from 1 to 255 characters. It contains the alphanumeric and special characters. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the remote-filename is not specified, the name of the source file is considered as the uploaded destination file name on the SFTP server.


Example
-------

# Upload files to the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL+K to abort
Connected to 10.1.1.1 ...
Please input the username: client001
Enter password:
sftp-client> put XXX.cc

```