display ftp server ip-block list
================================

display ftp server ip-block list

Function
--------



The **display ftp server ip-block list** command displays information about client IP addresses that are locked because of FTP authentication failures.




Format
------

**display ftp server ip-block list**


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

To check information about client IP addresses that are locked because of FTP authentication failures, run the **display ftp server ip-block list** command. The command output includes the names of VPN instances to which the locked client IP addresses belong and the remaining locking period.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about client IP addresses that are locked because of FTP authentication failures.
```
<HUAWEI> display ftp server ip-block list
----------------------------------------------------------------------------------------------------------
IP Address                                     VPN Name                         UnBlock Interval (Seconds)
----------------------------------------------------------------------------------------------------------
10.0.0.1                                       _public_                         294                       
----------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ftp server ip-block list** command output
| Item | Description |
| --- | --- |
| IP Address | Locked client IP address. |
| VPN Name | Name of a VPN instance to which a locked client IP address belongs. |
| UnBlock Interval (Seconds) | Remaining locking period, in seconds. |