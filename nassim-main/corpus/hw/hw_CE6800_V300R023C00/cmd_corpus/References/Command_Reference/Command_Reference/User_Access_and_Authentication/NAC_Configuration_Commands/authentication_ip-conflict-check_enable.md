authentication ip-conflict-check enable
=======================================

authentication ip-conflict-check enable

Function
--------



The **authentication ip-conflict-check enable** command enables the client IP address conflict detection function.

The **undo authentication ip-conflict-check enable** command disables the client IP address conflict detection function.



By default, the device detects whether client IP addresses conflict with each other.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication ip-conflict-check enable**

**undo authentication ip-conflict-check enable**


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

IP address conflict detection is performed based on an IP hash table. If the hash value of a client IP address conflicts with a value in the IP hash table on the device, the client cannot be authenticated. To prevent unauthorized users from accessing the network using forged IP addresses, you can enable the IP address conflict detection function. Some clients may use the same fixed source IP address to send ARP probe packets. If multiple such clients exist on the network, IP address conflict occurs. In this case, you can disable the IP address conflict detection function.


Example
-------

# Enable the client IP address conflict detection function.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name test
[*HUAWEI-authen-profile-test] authentication ip-conflict-check enable

```