ip prefix-limit system threshold-alarm
======================================

ip prefix-limit system threshold-alarm

Function
--------



The **ip prefix-limit system threshold-alarm** command configures thresholds (one alarm threshold and one clear alarm threshold) for the number of IPv4 route prefixes on a device.

The **undo ip prefix-limit system threshold-alarm** command restores the default configuration.



By default, the alarm threshold for IPv4 route prefixes is 80%, and the clear alarm threshold for IPv4 route prefixes is 70%.


Format
------

**ip prefix-limit system threshold-alarm upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value*

**undo ip prefix-limit system threshold-alarm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lower-limit** *lower-limit-value* | Specifies the clear alarm threshold for the number of IPv4 route prefixes. | The value is a percent integer ranging from 1 to 100.  lowerlimit-percent must be less than upperlimit-percent. Set lowerlimit-percent to a value at least 10 less than upperlimit-percent to prevent alarms from being frequently generated and cleared due to route flapping. |
| **upper-limit** *upper-limit-value* | Specifies the alarm threshold for the number of IPv4 route prefixes. | The value is a percent integer ranging from 1 to 100.  Set a value less than or equal to 95 for upperlimit-percent. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The number of IPv4 route prefixes that can be added to a routing table is limited. If the number exceeds the limit, new prefixes cannot be added to the routing table, which may interrupt services. To address this problem, configure an alarm threshold for the number of IPv4 route prefixes.You can run the **ip prefix-limit system threshold-alarm** command to configure the two thresholds based on service requirements.

* When the number of IPv4 route prefixes reaches the maximum number of route prefixes (configured using the **ip prefix-limit** command) multiplied by upperlimit-percent, an alarm (RM\_1.3.6.1.4.1.2011.5.25.145.10.3 hwIpv4PrefixThresholdExceed) is generated.
* When the number of IPv4 route prefixes falls below the maximum number of route prefixes multiplied by lowerlimit-percent, a clear alarm (RM\_1.3.6.1.4.1.2011.5.25.145.10.4 hwIpv4PrefixThresholdExceedClear) is generated.
* When the number of IPv4 route prefixes reaches the maximum number of route prefixes (configured using the **ip prefix-limit** command) multiplied by upperlimit-percent, an alarm (RM\_1.3.6.1.4.1.2011.5.25.145.10.3 hwIpv4PrefixThresholdExceed) is generated.
* When the number of IPv4 route prefixes falls below the maximum number of route prefixes multiplied by lowerlimit-percent, a clear alarm (RM\_1.3.6.1.4.1.2011.5.25.145.10.4 hwIpv4PrefixThresholdExceedClear) is generated.

**Precautions**

The **ip prefix-limit system threshold-alarm** command can configure only two thresholds. An alarm is generated only when the following two conditions are met:

* The alarm function is enabled for the RM module using the **snmp-agent trap enable feature-name rm** command.
* The number of IPv4 route prefixes on the device exceeds the alarm threshold.


Example
-------

# Configure the alarm threshold for IPv4 route prefixes as 85% and the clear alarm threshold as 65%.
```
<HUAWEI> system-view
[~HUAWEI] ip prefix-limit system threshold-alarm upper-limit 85 lower-limit 65

```