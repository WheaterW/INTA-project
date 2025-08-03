display ftp server
==================

display ftp server

Function
--------



The **display ftp server** command displays the current status of FTP server.




Format
------

**display ftp server**


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

You can display the result after configuring the FTP server parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the current state of the FTP server.
```
<HUAWEI> display ftp server
Server state             : Disabled
IPv6 server state        : Disabled
Timeout value (mins)     : 30
IPv6 Timeout value (mins): 30
Listen port              : 21
IPv6 listen port         : 21
ACL name                 :
IPv6 ACL name            : 
ACL number               :
IPv6 ACL number          : 
Current user count       : 0
Max user number          : 15

```

**Table 1** Description of the **display ftp server** command output
| Item | Description |
| --- | --- |
| Server state | Status of the FTP server.   * Enabled: The FTP service is enabled. * Disabled: The FTP service is disabled.   By default, the FTP service is disabled. |
| IPv6 server state | Status of the IPv6 FTP server:   * Enabled: The IPv6 FTP service is enabled. * Disabled: The IPv6 FTP service is disabled.   By default, the IPv6 FTP service is disabled. |
| IPv6 Timeout value (mins) | IPv6 Timeout value. |
| IPv6 listen port | FTP IPv6 server listening port.  By default, the server listening port value is 21. |
| IPv6 ACL name | IPv6 access control list names. |
| IPv6 ACL number | IPv6 access control list number. |
| Timeout value (mins) | Timeout value. |
| Listen port | FTP server listening port.  By default, the server listening port value is 21. |
| ACL name | IPv4 access control list names. |
| ACL number | IPv4 access control list number. |
| Current user count | Number of users currently connected to FTP server. |
| Max user number | Maximum number of users.  By default, the maximum number of users is 15. |