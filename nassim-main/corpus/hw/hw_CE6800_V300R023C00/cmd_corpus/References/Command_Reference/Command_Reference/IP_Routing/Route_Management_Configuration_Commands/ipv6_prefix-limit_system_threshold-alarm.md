ipv6 prefix-limit system threshold-alarm
========================================

ipv6 prefix-limit system threshold-alarm

Function
--------



The **ipv6 prefix-limit system threshold-alarm** command configures thresholds (one alarm threshold and one clear alarm threshold) for the number of IPv6 route prefixes on a device.

The **undo ipv6 prefix-limit system threshold-alarm** command restores the default configuration.



By default, the alarm threshold for IPv6 route prefixes is 80%, and the clear alarm threshold for IPv6 route prefixes is 70%.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 prefix-limit system threshold-alarm upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*

**undo ipv6 prefix-limit system threshold-alarm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lower-limit** *lower-limit-value* | Specifies the clear alarm threshold for the number of IPv6 route prefixes. | The value is a percent integer ranging from 1 to 100.  lowerlimit-percent must be less than upperlimit-percent. Set lowerlimit-percent to a value at least 10 less than upperlimit-percent to prevent alarms from being frequently generated and cleared due to route flapping. |
| **upper-limit** *upper-limit-value* | Specifies the alarm threshold for the number of IPv6 route prefixes. | The value is a percent integer ranging from 1 to 100.  Set a value less than or equal to 95 for upperlimit-percent. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The number of IPv6 route prefixes that can be added to a routing table is limited. If the number exceeds the limit, new prefixes cannot be added to the routing table, which may interrupt services. To address this problem, configure an alarm threshold for the number of IPv6 route prefixes.You can run the **ipv6 prefix-limit system threshold-alarm** command to configure the two thresholds based on the requirements of services.

* When the number of IPv6 route prefixes reaches the maximum number of route prefixes (configured using the **ipv6 prefix-limit** command) multiplied by upperlimit-percent, an alarm (RM\_1.3.6.1.4.1.2011.5.25.145.11.3 hwIpv6PrefixThresholdExceed) is generated.
* When the number of IPv6 route prefixes falls below the maximum number of route prefixes multiplied by lowerlimit-percent, a clear alarm (RM\_1.3.6.1.4.1.2011.5.25.145.11.4 hwIpv6PrefixThresholdExceedClear) is generated.

**Precautions**

The **ipv6 prefix-limit system threshold-alarm** command can configure only two thresholds. An alarm is generated only when the following two conditions are met:

* The alarm function is enabled for the RM module using the **snmp-agent trap enable feature-name rm** command.
* The number of IPv6 route prefixes on the device exceeds the alarm threshold.

Example
-------

# Configure the alarm threshold for IPv6 route prefixes as 85% and the clear alarm threshold as 65%.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 prefix-limit system threshold-alarm upper-limit 85 lower-limit 65

```