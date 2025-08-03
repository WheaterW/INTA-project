authentication no-ip-check
==========================

authentication no-ip-check

Function
--------



The **authentication no-ip-check** command disables the device from creating an IP hash table for client IP addresses.

The **undo authentication no-ip-check** command allows the device to create an IP hash table for client IP addresses.



By default, the device creates an IP hash table for client IP addresses.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication no-ip-check**

**undo authentication no-ip-check**


Parameters
----------

None

Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After users obtain IP addresses, the device creates an IP hash table. If the hash value of a client IP address conflicts with a value in the IP hash table on the device, the client cannot be authenticated. When two branches are connected to the device, the address pools of the branches may overlap. As a result, two clients in different branches may have the same IP address. When the device detects conflicting IP addresses, the clients fail to go online. To address this problem, you can run the **authentication no-ip-check** command to disable the device from creating an IP hash table for client IP addresses.

**Precautions**

* You are not advised to configure this function. Otherwise, if two clients with the same IP address go online through the same interface, the rules (such as ACLs) configured based on the IP address may be incorrectly matched.
* After this function is enabled, user rights depend on ARP learning.
* After the **authentication no-ip-check** command is run, dynamic authorization cannot be performed based on IP addresses.


Example
-------

# Disable the device from creating an IP hash table for client IP addresses.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name test
[*HUAWEI-authen-profile-test] authentication no-ip-check

```