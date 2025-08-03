display vty ip-block list
=========================

display vty ip-block list

Function
--------



The **display vty ip-block list** command displays the list of IP addresses that are locked due to authentication failures.




Format
------

**display vty ip-block list**


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

You can run this command to view the locked IP address and the remaining time before the IP address is unlocked.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the IP addresses that are locked due to authentication failures.
```
<HUAWEI> display vty ip-block list
-------------------------------------------------------------------------------------
 IP Address                 VPN Name                   UnBlock Interval(Seconds)     
-------------------------------------------------------------------------------------
 192.168.10.1               _public_                          36                     
-------------------------------------------------------------------------------------

```

**Table 1** Description of the **display vty ip-block list** command output
| Item | Description |
| --- | --- |
| IP Address | Locked IP address. |
| VPN Name | Name of the VPN to which the locked IP address belongs. |
| UnBlock Interval(Seconds) | Remaining time before the lock is removed. |