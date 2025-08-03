ipv6 nd mac-check enable
========================

ipv6 nd mac-check enable

Function
--------



The **ipv6 nd mac-check enable** command enables MAC address check for ND.

The **undo ipv6 nd mac-check enable** command disables MAC address check for ND.



By default, MAC address check for ND is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd mac-check enable**

**undo ipv6 nd mac-check enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To allow the system to proactively check the source MAC address consistency to improve network reliability, run the **ipv6 nd mac-check enable** command to enable MAC address check for ND so that MAC address consistency is checked on four different types of ICMPv6 packets.

* NS: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the NS message is discarded.
* NA: The system checks whether the source MAC address is the same as the MAC address in the TLLA. If not, the NA message is discarded.
* RS: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the RS message is discarded.
* RA: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the RA message is discarded.

Example
-------

# Enable MAC address check for ND.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd mac-check enable

```