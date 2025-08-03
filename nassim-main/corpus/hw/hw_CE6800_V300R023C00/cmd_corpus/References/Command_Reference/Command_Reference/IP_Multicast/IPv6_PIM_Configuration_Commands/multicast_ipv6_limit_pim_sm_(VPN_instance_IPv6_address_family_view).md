multicast ipv6 limit pim sm (VPN instance IPv6 address family view)
===================================================================

multicast ipv6 limit pim sm (VPN instance IPv6 address family view)

Function
--------



The **multicast ipv6 limit pim sm** command configures a limit on the number of PIM-SM entries and alarm thresholds for them in the IPv6 address family of a VPN instance.

The **undo multicast ipv6 limit pim sm** command restores the default configuration.



By default, no limit is configured on the number of PIM-SM entries and no alarm thresholds are configured in the IPv6 address family of a VPN instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 limit pim sm** { **star-group-number** | **source-group-number** } *limit-count* [ **threshold-alarm** **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]

**undo multicast ipv6 limit pim sm** { **star-group-number** | **source-group-number** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **star-group-number** | Configures the specified limit to take effect for (\*, G) multicast entries. | - |
| **source-group-number** | Configures the specified limit to take effect for (S, G) multicast entries. | - |
| *limit-count* | Specifies a limit on the number of PIM entries. | The value is an integer ranging from 1 to 16384. |
| **threshold-alarm** | threshold-alarm. | - |
| **upper-limit** *upper-limit-value* | Sets an alarm trigger threshold, in percentage. An alarm is generated when the percentage ratio of created PIM entries to limit-count reaches upper-limit-value. Setting upper-limit-value to a value greater than 95% is not recommended. | The value is an integer ranging from 1 to 100. The default value is 80. |
| **lower-limit** *lower-limit-value* | Sets an alarm clear threshold, in percentage. An alarm is cleared when the percentage ratio of created PIM entries to limit-count falls below lower-limit-value.   * lower-limit-value must be less than upper-limit-value. * To prevent alarms from being frequently generated and cleared due to route flapping, setting lower-limit-value to a value at least 10 less than upper-limit-value is recommended. | The value is an integer ranging from 1 to 100. The default value is 70. |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure a proper limit on the number of PIM-SM entries in the IPv6 address family of a VPN instance, run the **multicast ipv6 limit pim sm** command. This prevents multicast services from being affected by an improper limit on the number of PIM-SM entries

**Prerequisites**

The **multicast ipv6 routing-enable** command has been run in the IPv6 address family of a VPN instance.

**Configuration Impact**

If the number of PIM-SM entries in the IPv6 address family of a VPN instance reaches a configured limit, new entries fail to be created and the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.32 hwPimVrfTypeSGExceed is triggered.If upper-limit upper-limit-value is specified and the number of PIM-SM entries in the IPv6 address family of a VPN instance reaches the configured alarm trigger threshold, the alarm PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.30 hwPimVrfTypeSGThresholdExceed is triggered.Statically created (\*, G) and (S, G) entries are not affected by a limit on the number of PIM-SM entries in the IPv6 address family of a VPN instance. The limit takes effect only on dynamic entries.


Example
-------

# Set a limit on the number of PIM (S, G) entries in the IPv6 address family of a VPN instance named abc to 1000.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] ipv6-family
[*HUAWEI-vpn-instance-abc-af-ipv6] route-distinguisher 1:1
[*HUAWEI-vpn-instance-abc-af-ipv6] multicast ipv6 routing-enable
[*HUAWEI-vpn-instance-abc-af-ipv6] multicast ipv6 limit pim sm source-group-number 1000

```

# Set a limit on the number of PIM (\*, G) entries, alarm trigger threshold, and alarm clear threshold to 2000, 80%, and 70% in the IPv6 address family of a VPN instance named abc, respectively.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] ipv6-family
[*HUAWEI-vpn-instance-abc-af-ipv6] route-distinguisher 1:1
[*HUAWEI-vpn-instance-abc-af-ipv6] multicast ipv6 routing-enable
[*HUAWEI-vpn-instance-abc-af-ipv6] multicast ipv6 limit pim sm star-group-number 2000 threshold-alarm upper-limit 80 lower-limit 70

```