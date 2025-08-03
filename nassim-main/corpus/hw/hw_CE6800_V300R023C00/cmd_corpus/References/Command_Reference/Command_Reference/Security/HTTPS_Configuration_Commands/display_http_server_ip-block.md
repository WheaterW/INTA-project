display http server ip-block
============================

display http server ip-block

Function
--------



The **display http server ip-block all** command displays the IP addresses of all the clients that fail to be authenticated.

The **display http server ip-block list** command displays information about client IP addresses that are locked due to authentication failures.




Format
------

**display http server ip-block list**

**display http server ip-block all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays information about the IP addresses of all clients that fail to be authenticated. | - |
| **list** | Displays the list of locked client IP addresses. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* You can run the **display http server ip-block all** command to view the IP addresses of all the clients that fail to be authenticated, including the names of the VPN instances to which the IP addresses belong, IP address status, and number of authentication failures. This prevents invalid authentication using the IP addresses that fail to be authenticated. For example, in an HTTP connection, if a user enters incorrect passwords for six consecutive times within 5 minutes, the IP address will be locked for 5 minutes. In this case, the IP address status in the **display http server ip-block all** command output changes from AUTH FAILED to BLOCKED.
* You can run the **display http server ip-block list** command to view information about client IP addresses that are locked due to authentication failures, including the name of the VPN instance to which the locked client IP addresses belong and the remaining locking time.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about client IP addresses that are locked because of authentication failures.
```
<HUAWEI> display http server ip-block list
-------------------------------------------------------------------------------------
 IP Address                 VPN Name                   UnBlock Interval(Seconds)     
-------------------------------------------------------------------------------------
 192.168.10.1               _public_                          36                     
-------------------------------------------------------------------------------------

```

# Display the IP addresses of all the clients that fail to be authenticated.
```
<HUAWEI> display http server ip-block all
-------------------------------------------------------------------------------------
 IP Address                 VPN Name                   State           Auth-fail Count
--------------------------------------------------------------------------------------
 192.168.10.1               _public_                   BLOCKED             6          
--------------------------------------------------------------------------------------

```

**Table 1** Description of the **display http server ip-block** command output
| Item | Description |
| --- | --- |
| IP Address | Locked client IP address. |
| VPN Name | Name of a VPN instance to which a locked client IP address belongs. |
| UnBlock Interval(Seconds) | Remaining locking period, in seconds. |
| State | Status of the blocked client IP address:   * BLOCKED: The IP address is locked. * AUTH FAILED: IP address authentication failed. |
| Auth-fail Count | Number of consecutive client authentication failures within the check period. |