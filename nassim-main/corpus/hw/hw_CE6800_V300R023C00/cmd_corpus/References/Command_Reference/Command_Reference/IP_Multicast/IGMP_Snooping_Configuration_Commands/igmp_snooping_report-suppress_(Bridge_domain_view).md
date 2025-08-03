igmp snooping report-suppress (Bridge domain view)
==================================================

igmp snooping report-suppress (Bridge domain view)

Function
--------



The **igmp snooping report-suppress** command enables the suppression of IGMP Report messages.

The **undo igmp snooping report-suppress** command disables the suppression of IGMP Report messages.



By default, the suppression for IGMP Report messages is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping report-suppress**

**undo igmp snooping report-suppress**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the igmp snooping report-suppress command is run, the device is configured to work in host mode. Assume that the robustness variable is N, the device sends N Report messages and N Leave messages to an upstream router for the first time. When the device periodically responds to IGMP Query messages sent by the upstream router, the device needs to send only one IGMP Report message to the upstream router to reduce traffic on the network side, regardless of the number of interfaces in the multicast group. The default robustness variable is 2. You can run the igmp snooping robust command to change a robustness variable.

**Precautions**

It is recommended that the IGMP version configured on the upstream device be the same as that configured on the local device.


Example
-------

# Disable the suppression of IGMP Report messages in the view of BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] undo igmp snooping report-suppress

```