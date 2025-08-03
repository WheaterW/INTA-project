ipv6 route recursive-lookup default-route protocol
==================================================

ipv6 route recursive-lookup default-route protocol

Function
--------



The **ipv6 route recursive-lookup default-route protocol** command enables IPv6 static route recursion to the default route.

The **undo ipv6 route recursive-lookup default-route protocol** command disables IPv6 static route recursion to the default route.



By default, IPv6 static route recursion to the default route is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route recursive-lookup default-route protocol** { **static** | **msr** }

**undo ipv6 route recursive-lookup default-route protocol** { **static** | **msr** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **static** | Allows IPv6 static routes to recurse to the default route. | - |
| **msr** | Indicates the multicast static route. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The next hop of an IPv6 static route may not be directly reachable. In this case, route recursion is required. During route recursion, you can run the **ipv6 route recursive-lookup default-route protocol** command to control whether to allow IPv6 static routes to be recursed to the default route.

**Precautions**

After the **ipv6 route recursive-lookup default-route protocol** command is run, IPv6 static routes can be recursed to the default route. As a result, the actual forwarding path may change.


Example
-------

# Enable multicast static routes to be recursed to the default route.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route recursive-lookup default-route protocol msr

```

# Allow IPv6 static routes to recurse to the default route.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route recursive-lookup default-route protocol static

```