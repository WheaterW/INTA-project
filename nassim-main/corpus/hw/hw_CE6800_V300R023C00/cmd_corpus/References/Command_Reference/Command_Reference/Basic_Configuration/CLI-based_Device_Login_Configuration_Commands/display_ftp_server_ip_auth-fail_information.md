display ftp server ip auth-fail information
===========================================

display ftp server ip auth-fail information

Function
--------



The **display ftp server ip auth-fail information** command displays the information of the FTP auth-failed IP addresses of a user.




Format
------

**display ftp server ip auth-fail information**


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

**Usage Scenario**

The **display ftp server ip auth-fail information** command displays the information of the FTP auth-failed IP addresses. The command output includes the names of VPN instances to which the IP addresses belong, IP address status, numbers of authentication failures, and the IP addresses that fail to pass FTP authentication will not be adopted to make invalid authentication.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about client IP addresses that are locked because of FTP authentication failures.
```
<HUAWEI> display ftp server ip auth-fail information
--------------------------------------------------------------------------------------------------------------------------------
IP Address                                     VPN Name                         First Time Auth-fail             Auth-fail Count
--------------------------------------------------------------------------------------------------------------------------------
10.0.0.1                                       _public_                         2016-09-05 11:19:28                            1
--------------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ftp server ip auth-fail information** command output
| Item | Description |
| --- | --- |
| IP Address | Locked client IP address. |
| VPN Name | Name of a VPN instance to which a locked client IP address belongs. |
| First Time Auth-fail | Time when the first authentication fails. |
| Auth-fail Count | Number of consecutive client authentication failures in the latest authentication period. |