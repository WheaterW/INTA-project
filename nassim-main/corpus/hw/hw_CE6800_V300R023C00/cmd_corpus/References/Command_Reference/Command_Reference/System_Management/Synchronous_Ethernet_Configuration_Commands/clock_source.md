clock source
============

clock source

Function
--------



The **clock source** command configures the clock source selection mode as manual or forcible clock source selection and specifies a clock source to be synchronized.



The default clock source selection mode is automatic clock source selection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock** { **manual** | **force** } **source** **ptp**

**clock** { **manual** | **force** } **source** **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **manual** | Specifies the clock source to be manually traced. | - |
| **force** | Specifies the clock source for system synchronization. | - |
| **ptp** | Specifies a PTP clock source as the master clock source. | - |
| **interface** *interface-name* | Specifies an interface clock source as the master clock source. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **interface** *interface-type* *interface-number* | Specifies an interface clock source as the master clock source. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to manually or forcibly specify a clock source to be traced.

**Configuration Impact**

After the **clock manual source** command is run, this command is not saved in the configuration file. To view the configuration results, run the **display clock config** command. If the reference clock source fails, the clock selection mode is automatically switched to automatic clock source selection. After a device is restarted, the **clock manual source** command is not restored, and the default automatic clock source selection mode takes effect.After a device is upgraded to the target version, the configured **clock manual source** command fails, and the default automatic clock source selection mode takes effect.

**Precautions**

* When you forcibly specify a clock source, ensure that clock synchronization has been enabled on the specified clock source. If clock synchronization has not been enabled, the **clock force source** command does not take effect.
* If the status of a specified clock source is not normal or its SSM level is dnu, the system clock works in the hold state or free state.
* If the status of a manually specified clock source is neither normal nor holdoff, or its SSM level is not the highest, the **clock manual source** command does not take effect.

Example
-------

# Configure manual clock source selection and specify a PTP clock source to be synchronized.
```
<HUAWEI> system-view
[~HUAWEI] clock manual source ptp

```