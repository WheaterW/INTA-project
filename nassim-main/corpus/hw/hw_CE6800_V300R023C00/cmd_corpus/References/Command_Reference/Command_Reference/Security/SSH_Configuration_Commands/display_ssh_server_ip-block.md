display ssh server ip-block
===========================

display ssh server ip-block

Function
--------



The **display ssh server ip-block all** command displays information about the IP addresses of all the clients that fail to pass authentication.

The **display ssh server ip-block list** command displays information about client IP addresses that are locked because of authentication failures.




Format
------

**display ssh server ip-block list**

**display ssh server ip-block all**


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

To check information about the IP addresses of all the clients that fail to pass authentication, run the **display ssh server ip-block all** command. The command output includes the names of VPN instances to which the IP addresses belong, IP address status, numbers of authentication failures, and the IP addresses that fail to pass authentication will not be adopted to make invalid authentication.If a user logs in using SSH, the user's IP address will be locked for 5 minutes upon 6 incorrect password attempts within 5 minutes. After the IP address is locked, the IP address status displayed in the **display ssh server ip-block all** command output changes from AUTH FAILED to BLOCKED.To check information about client IP addresses that are locked because of authentication failures, run the **display ssh server ip-block list** command. The command output includes the names of VPN instances to which the locked client IP addresses belong and the remaining locking period.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about client IP addresses that are locked because of authentication failures.
```
<HUAWEI> display ssh server ip-block list
-------------------------------------------------------------------------------------
 IP Address                 VPN Name                   UnBlock Interval(Seconds)     
-------------------------------------------------------------------------------------
 192.168.10.1               _public_                          36                     
-------------------------------------------------------------------------------------

```

# Display information about the IP addresses of all the clients that fail to pass authentication.
```
<HUAWEI> display ssh server ip-block all
-------------------------------------------------------------------------------------
 IP Address                 VPN Name                   State           Auth-fail Count
--------------------------------------------------------------------------------------
 192.168.10.1               _public_                   BLOCKED             6          
--------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ssh server ip-block** command output
| Item | Description |
| --- | --- |
| IP Address | Locked client IP address. |
| VPN Name | Name of a VPN instance to which a locked client IP address belongs. |
| UnBlock Interval(Seconds) | Remaining locking period, in seconds. |
| State | Status of a locked client IP address:   * BLOCKED: The IP address is locked. * AUTH FAILED: The IP address fails to pass authentication. |
| Auth-fail Count | Number of consecutive authentication failures within 5 minutes. |