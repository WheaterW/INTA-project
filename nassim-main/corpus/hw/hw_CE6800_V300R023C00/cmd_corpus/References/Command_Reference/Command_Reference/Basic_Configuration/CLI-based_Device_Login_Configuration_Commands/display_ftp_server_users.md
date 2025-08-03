display ftp server users
========================

display ftp server users

Function
--------



The **display ftp server users** command displays the information of FTP users log in to the FTP server.




Format
------

**display ftp server users**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can view the list of FTP users. It contains FTP user name, IP address of the client, port number, idle timeout of FTP client, and FTP root directory.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the current logged in users.
```
<HUAWEI> display ftp server users
User Name        : client001
Host Address     : 10.1.1.1
Control Port     : 4142
Idle Time (mins) : 0
Root Directory   : 17#flash:

```

**Table 1** Description of the **display ftp server users** command output
| Item | Description |
| --- | --- |
| User Name | FTP user name. |
| Host Address | IP address of the client. |
| Control Port | Control port number. |
| Idle Time (mins) | Idle time of FTP client. |
| Root Directory | FTP root directory. |