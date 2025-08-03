flow-aggregation enable
=======================

flow-aggregation enable

Function
--------



The **flow-aggregation enable** command enables the flow aggregation function.

The **undo flow-aggregation enable** command disables the flow aggregation function.



By default, the flow aggregation function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**flow-aggregation enable**

**undo flow-aggregation enable**


Parameters
----------

None

Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the AnyFlow function is enabled on a device, the device exports original flow statistics by default. That is, the device sends the statistics about each flow to the analyzer. Original flow statistics export occupies much network bandwidth. To reduce bandwidth consumption, you can configure aggregation flow statistics export. The device aggregates flows with a specified port number based on aggregation keywords including the source IP address, destination IP address, destination port number, and protocol type.

**Precautions**

After the flow aggregation function is enabled, only statistics about the flows aggregated based on the specified destination port number are exported, and original flow statistics will not be exported.


Example
-------

# Enable the flow aggregation function.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] flow-aggregation enable

```