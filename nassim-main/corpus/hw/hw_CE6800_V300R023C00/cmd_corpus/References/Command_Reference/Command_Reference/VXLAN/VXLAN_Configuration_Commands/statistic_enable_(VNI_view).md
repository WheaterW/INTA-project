statistic enable (VNI view)
===========================

statistic enable (VNI view)

Function
--------



The **statistic enable** command enables VXLAN traffic statistics collection.

The **undo statistic enable** command disables VXLAN traffic statistics collection.



By default, VXLAN traffic statistics collection is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**statistic enable**

**undo statistic enable**


Parameters
----------

None

Views
-----

VNI view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, VXLAN packet statistics collection is disabled. To view VXLAN packet statistics of a specified VNI for fault locating, run this command in the VNI view to enable VXLAN packet statistics collection. Otherwise, you cannot view VXLAN packet statistics of the VNI.

**Configuration Impact**

If a large number of VXLAN packets exist, the device counts all these packets and subsequently stores large amounts of statistics, causing device operation performance to deteriorate. If VXLAN traffic statistics collection is not needed, run the undo statistic enable command to disable the function.

**Follow-up Procedure**

After running the **statistics enable** command, you can run the display vxlan statistics vni <vni-id> command to view VNI-specific statistics. The statistics can be used for fault diagnosis.


Example
-------

# Enable VXLAN traffic statistics collection.
```
<HUAWEI> system-view
[~HUAWEI] vni 10
[*HUAWEI-vni10] statistic enable

```