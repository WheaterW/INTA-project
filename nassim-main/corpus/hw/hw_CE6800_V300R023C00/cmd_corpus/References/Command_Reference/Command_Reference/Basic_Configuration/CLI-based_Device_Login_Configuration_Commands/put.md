put
===

put

Function
--------



The **put** command uploads a local file to the remote FTP server.




Format
------

**put** *local-filename* [ *remote-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-filename* | Specifies the local file name. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |
| *remote-filename* | Specifies the file name on the remote FTP server. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you do not specify the file name on the remote server, the uploaded file uses the same name as that of the local file.


Example
-------

# Upload the local file to the remote FTP server and save the file as a.txt.
```
<HUAWEI> ftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 (vsFTPd 2.2.1)
Username:root
331 Please specify the password.
Password:
230 Login successful.
[ftp] put a.txt
200 EPRT command successful. Consider using EPSV.
150 Ok to send data.
226 File receive OK.
\     100% [***********]
FTP: 12386115 byte(s) send in 2.649768000 second(s) 4566.181Kbyte(s)/sec.

```