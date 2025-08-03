lsdb limit
==========

lsdb limit

Function
--------



The **lsdb limit** command configures alarm and clear alarm thresholds for the number of LSPs in the LSDB. When the proportion of the number of LSPs to the maximum number of LSPs in the LSDB exceeds the alarm threshold, an alarm is generated; when the proportion of the number of LSPs to the maximum number of LSPs in the LSDB falls below the clear alarm threshold, a clear alarm is generated.

The **undo lsdb limit** command deletes the configured thresholds.



By default, no such thresholds are configured.


Format
------

**lsdb limit** *limit-number* [ **threshold-alarm** **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* ]

**undo lsdb limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit-number* | Specifies the maximum number of LSPs in the LSDB. | The value is an integer ranging from 1 to 100000. |
| **threshold-alarm** | Indicates the threshold of the number of LSPs in the LSDB. | - |
| **upper-limit** *upper-limit-value* | Specifies the alarm threshold that triggers an alarm. If the proportion of the number of LSPs to the maximum number of LSPs in the LSDB exceeds upper-limit-value, an alarm is generated. | The value is an integer ranging from 1 to 100. The default value is 80. |
| **lower-limit** *lower-limit-value* | Specifies the clear alarm threshold that triggers a clear alarm. If the proportion of the number of LSPs to the maximum number of LSPs in the LSDB falls below lower-limit-value, a clear alarm is generated. | The value is an integer ranging from 1 to 100. The default value is 70. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An IS-IS-capable device may advertise a large number of LSPs due to an excessive number of external routes received because of incorrect configurations or attack packets. In this situation, you can run the **lsdb limit** command to configure alarm and clear alarm thresholds for the number of LSPs in the LSDB. When the proportion of the number of LSPs to the maximum number of LSPs in the LSDB exceeds the alarm threshold, an alarm is generated, which facilitates troubleshooting of network administrators.



**Prerequisites**



An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.



**Precautions**



upper-limit-value must be greater than or equal to lower-limit-value.




Example
-------

# Set the maximum number of LSPs in the LSDB to 1000, alarm threshold to 85, and clear alarm threshold to 75.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] lsdb limit 1000 threshold-alarm upper-limit 85 lower-limit 75

```