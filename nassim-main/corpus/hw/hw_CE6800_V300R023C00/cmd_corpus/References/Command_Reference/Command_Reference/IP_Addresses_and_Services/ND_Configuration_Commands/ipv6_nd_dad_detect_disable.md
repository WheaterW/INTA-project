ipv6 nd dad detect disable
==========================

ipv6 nd dad detect disable

Function
--------



The **ipv6 nd dad detect disable** command disables DAD from continuing detection in the case of an IPv6 address conflict.

The **undo ipv6 nd dad detect disable** command restores the default configuration.



By default, DAD continues detection in the case of an IPv6 address conflict.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd dad detect disable**

**undo ipv6 nd dad detect disable**


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

Before using an IPv6 unicast address for an interface, a device performs DAD. If DAD detects an address conflict, the detection ends. To remove the address conflict, you need to reconfigure an IPv6 address or change the interface status for the device to perform DAD again. This causes a long service interruption. To resolve this issue, enable DAD to continue detection in an address conflict scenario. In this case, after detecting an address conflict, DAD will continue detection until any of the following occurs:

* The loopback is released.
* No more NS messages are received from a neighbor.
* No more NA messages are received from a neighbor.

If the network is stable and no new IPv6 address needs to be configured, you can run the **ipv6 nd dad detect disable** command to disable DAD from continuing detection in an address conflict scenario.


Example
-------

# Disable DAD from continuing detection in the system view.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd dad detect disable

```