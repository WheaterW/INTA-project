ipv6 prefix-limit
=================

ipv6 prefix-limit

Function
--------



The **ipv6 prefix-limit** command configures a limit on the number of IPv6 public route prefixes.

The **undo ipv6 prefix-limit** command restores the default configuration.



By default, the maximum number of IPv6 public route prefixes is not limited.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 prefix-limit** *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** }

**undo ipv6 prefix-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of IPv6 public route prefixes. | The value is an integer ranging from 1 to 4294967295. |
| *alert-percent* | Specifies the percentage of the maximum number of IPv6 public route prefixes. If you specify alert-percent in the command, when the number of IPv6 public route prefixes exceeds the value calculated by number x alert-percent/100, an alarm is generated. Additional IPv4 public route prefixes can still be added to the routing table until the number of IPv6 public route prefixes reaches number. Subsequent route prefixes are discarded. | The value is an integer ranging from 1 to 100. |
| **route-unchanged** | Indicates that the routing table remains unchanged. If you decrease alert-percent after the number of IPv4 public route prefixes exceeds number, whether the routing table remains unchanged is determined by route-unchanged:   * If you specify route-unchanged in the command, the routing table remains unchanged. * If you do not specify route-unchanged in the command, the system deletes the routes from the routing table and re-adds routes.   By default, the system deletes the routes from the routing table and re-adds routes. | - |
| **simply-alert** | Indicates the following function: If you specify simply-alert in the command, new IPv6 public route prefixes can still be added to the routing table and only an alarm is generated after the number of IPv6 public route prefixes exceeds number. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the device imports a large number of routes, system performance may be affected when processing services because the routes consume excessive system resources. To improve system security and reliability, run the **ipv6 prefix-limit** command to configure a limit on the number of IPv6 public route prefixes. When the number of IPv6 public route prefixes exceeds the limit, an alarm is generated, prompting you to check whether unneeded IPv6 public route prefixes exist.

**Configuration Impact**

After the **ipv6 prefix-limit** command is run, the device may discard unneeded IPv6 public route prefixes.

* If the number of IPv6 public route prefixes exceeds the value calculated from number\* alert-percent/100, an alarm (RM\_1.3.6.1.4.1.2011.5.25.145.19.2.3 hwPublicIpv6PrefixThresholdExceed) is generated.
* If the number of IPv6 public route prefixes exceeds number, an alarm (RM\_1.3.6.1.4.1.2011.5.25.145.19.2.1 hwPublicIpv6PrefixExceed) is generated.
* If the number of IPv6 public route prefixes falls below the value calculated from number\* alert-percent/100, a clear alarm (RM\_1.3.6.1.4.1.2011.5.25.145.19.2.4 hwPublicIpv6PrefixThresholdExceedClear) is generated.
* If the number of IPv6 public route prefixes exceeds number, a clear alarm (RM\_1.3.6.1.4.1.2011.5.25.145.19.2.2 hwPublicIpv6PrefixExceedClear) is generated.

**Precautions**

If you run the **ipv6 prefix-limit** command multiple times, the latest configuration overrides the previous one.After the number of route prefixes exceeds the upper limit:

* If you run the **ipv6 prefix-limit** command to increase the maximum number of IPv6 public route prefixes or run the **undo ipv6 prefix-limit** command to cancel the limit, the device relearns IPv6 public route prefixes.
* IPv6 direct routes and IPv6 static routes can still be added to the IPv6 routing table.


Example
-------

# Configure simply-alert so that only an alarm is generated when the device imports more than 1000 IPv6 public route prefixes.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 prefix-limit 1000 simply-alert

```