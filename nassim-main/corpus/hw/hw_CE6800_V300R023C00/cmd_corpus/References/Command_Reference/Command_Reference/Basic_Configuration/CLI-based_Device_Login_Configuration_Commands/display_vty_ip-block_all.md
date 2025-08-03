display vty ip-block all
========================

display vty ip-block all

Function
--------



The **display vty ip-block all** command displays all IP addresses that fail to be authenticated.




Format
------

**display vty ip-block all**


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

To check IP addresses that fail to be authenticated, run the display vty ip-block all command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all IP addresses that fail to be authenticated.
```
<HUAWEI> display vty ip-block all
-------------------------------------------------------------------------------------
 IP Address                 VPN Name                   State           Auth-fail Count
--------------------------------------------------------------------------------------
 192.168.10.1               _public_                   BLOCKED             6           
--------------------------------------------------------------------------------------

```

**Table 1** Description of the **display vty ip-block all** command output
| Item | Description |
| --- | --- |
| IP Address | Blocked IP address. |
| VPN Name | Name of the VPN to which the blocked IP address belongs. |
| State | State of an IP address.   * BLOCKED: The IP address is blocked. * AUTH FAILED: The IP address fails to be authenticated. |
| Auth-fail Count | Number of IP address authentication failures in the latest 5 minutes. |