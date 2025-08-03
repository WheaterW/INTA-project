multicast ipv6 global limit pim sm
==================================

multicast ipv6 global limit pim sm

Function
--------



The **multicast ipv6 global limit pim sm** command sets a limit on the number of global IPv6 PIM entries.

The **undo multicast ipv6 global limit pim sm** command restores the default configuration.



By default, no limit is set on the number of global IPv6 PIM entries.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 global limit pim sm** { **star-group-number** | **source-group-number** } *limit-count6* [ **threshold-alarm** **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]

**undo multicast ipv6 global limit pim sm** { **star-group-number** | **source-group-number** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **star-group-number** | Configures the specified limit to take effect for (\*, G) multicast entries. | - |
| **source-group-number** | Configures the specified limit to take effect for (S, G) multicast entries. | - |
| *limit-count6* | Specifies a limit on the number of PIM entries. | The value is an integer ranging from 1 to 16384. |
| **threshold-alarm** | threshold-alarm. | - |
| **upper-limit** *upper-limit-value* | Sets an alarm trigger threshold, in percentage. An alarm is generated when the percentage ratio of created PIM entries to limit-count reaches upper-limit-value. Setting upper-limit-value to a value greater than 95% is not recommended. | The value is an integer ranging from 1 to 100. The default value is 80. |
| **lower-limit** *lower-limit-value* | Sets an alarm clear threshold, in percentage. An alarm is cleared when the percentage ratio of created PIM entries to limit-count falls below lower-limit-value.   * lower-limit-value must be less than upper-limit-value. * To prevent alarms from being frequently generated and cleared due to route flapping, setting lower-limit-value to a value at least 10 less than upper-limit-value is recommended. | The value is an integer ranging from 1 to 100. The default value is 70. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set a limit on the number of PIM entries on the device, run the **multicast ipv6 global limit pim sm** command.

**Configuration Impact**

* After the specified limit is reached, new entries cannot be created, and the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.23 routeExceed alarm is generated. After the specified limit is reached, new (\*, G) and (S, G) entries can be manually added, and ASM share-group entries for Rosen MVPN can be created.
* If upper-limit upper-limit-value is set, the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.21 routeThresholdExceed alarm is generated when the percentage ratio of created PIM entries to the specified limit reaches upper-limit-value.

Example
-------

# Set the limit to 2000 for PIM (\*, G) entries, alarm trigger threshold to 80%, and alarm clear threshold to 70%.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 global limit pim sm star-group-number 2000 threshold-alarm upper-limit 80 lower-limit 70

```

# Set the limit to 1000 for PIM (S, G) entries.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 global limit pim sm source-group-number 1000

```