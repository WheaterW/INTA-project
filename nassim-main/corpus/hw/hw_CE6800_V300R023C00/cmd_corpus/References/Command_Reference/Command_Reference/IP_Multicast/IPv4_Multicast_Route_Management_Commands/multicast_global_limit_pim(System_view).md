multicast global limit pim(System view)
=======================================

multicast global limit pim(System view)

Function
--------



The **multicast global limit pim** command sets a limit on the number of global PIM entries.

The **undo multicast global limit pim** command disables a limit on the number of global PIM entries.



By default, no limit is set on the number of global IPv4 PIM entries.


Format
------

**multicast global limit pim** { **sm** | **dm** } { **star-group-number** | **source-group-number** } *limit-count* [ **threshold-alarm** **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]

**undo multicast global limit pim** { **sm** | **dm** } { **star-group-number** | **source-group-number** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sm** | Specifies PIM-SM/SSM mode. | - |
| **dm** | Specifies PIM-DM mode. | - |
| **star-group-number** | Configures the specified limit to take effect for (\*, G) multicast entries. | - |
| **source-group-number** | Configures the specified limit to take effect for (S, G) multicast entries. | - |
| *limit-count* | Sets a limit on the number of PIM entries. | The value is an integer ranging from 1 to 32000. |
| **threshold-alarm** | Sets an alarm trigger threshold. | - |
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

To set a limit on the number of PIM entries on the device, run the multicast global limit pim sm command.

**Configuration Impact**

After the specified limit is reached, new entries are not created, and the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.23 routeExceed alarm is generated.NOTE:After the specified limit is reached, new (\*, G) and (S, G) entries can be manually added, and ASM share-group entries for Rosen MVPN can be created.If threshold-alarm upper-limit-value is set, the PIM\_1.3.6.1.4.1.2011.5.25.149.4.0.21 routeThresholdExceed alarm is generated when the percentage ratio of created PIM entries to the specified limit reaches upper-limit-value.

**Precautions**

The number of PIM entries is limited by the PAF file. If the configured limit-count exceeds the PAF file limit, PIM entries can be generated, but traffic may fail to be forwarded.


Example
-------

# Set the limit to 1000 for PIM (S, G) entries.
```
<HUAWEI> system-view
[~HUAWEI] multicast global limit pim sm source-group-number 1000

```

# Set the limit to 2000 for PIM (\*, G) entries, alarm trigger threshold to 80%, and alarm clear threshold to 70%.
```
<HUAWEI> system-view
[~HUAWEI] multicast global limit pim sm star-group-number 2000 threshold-alarm upper-limit 80 lower-limit 70

```