ipv6 nd auto-detect disable
===========================

ipv6 nd auto-detect disable

Function
--------



The **ipv6 nd auto-detect disable** command disables the auto-detection of ND entries.

The **undo ipv6 nd auto-detect disable** command enables the auto-detection of ND entries.



By default, the auto-detection function is enabled for ND entries.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd auto-detect disable**

**undo ipv6 nd auto-detect disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve network reliability, you can run the **undo ipv6 nd auto-detect disable** command to enable the auto-detection of ND entries so that the system can send Neighbor Solicitation (NS) messages to probe whether its neighbors are reachable before aging ND entries.

**Configuration Impact**



If the system receives a Neighbor Advertisement (NA) message from a neighbor responding to the sent NS message, the system updates the aging time of the ND entries. If the system does not receive any NA message, the ND entries automatically age.You are recommended to keep the auto-detection of ND entries enabled.



**Precautions**

* After the **ipv6 nd auto-detect disable** command is run, the system does not send NS messages to detect ND entries after the aging time expires. Instead, the system directly ages and deletes ND entries. This may cause problems such as traffic interruption and route flapping.
* If the auto-detection of ND entries is not enabled, the system directly deletes ND entries when the aging time of ND entries expires or the system no longer probes the reachability of its neighbors after the aging time of the passively established ND entries expires.


Example
-------

# Enable the auto-detection of ND entries.
```
<HUAWEI> system-view
[~HUAWEI] undo ipv6 nd auto-detect disable

```