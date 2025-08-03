ipv6 nd pre-detect
==================

ipv6 nd pre-detect

Function
--------



The **ipv6 nd pre-detect** command enables the pre-detection of ND entries.

The **undo ipv6 nd pre-detect** command disables the pre-detection of ND entries.



By default, the pre-detection of ND entries is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd pre-detect**

**undo ipv6 nd pre-detect**


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

To enable a Router to send an NS message to detect the validity of ND entries before the ND entries change from the REACHABLE state to the STALE state, you can enable the pre-detection of ND entries. If the neighbor still exists, the ND entry status is REACHABLE; otherwise, the ND entry is deleted. In this manner, the forwarding plane no longer needs to frequently sense ND entry status changes. Instead, it considers all the existent entries as available to packet forwarding, thereby improving forwarding efficiency.

**Configuration Impact**

Enabling the pre-detection of ND entries does not affect the system compatibility.As defined in the ND protocol standard, if an ND entry is in the STALE state and a packet needs to use this entry, a Router must send an NS message to detect the availability of the entry. You are recommended to keep the pre-detection of ND entries disabled unless the entries are frequently in the STALE state and ND entry probes are repeatedly triggered during the lower-layer forwarding process, which affects the forwarding efficiency.

**Precautions**

By default, an ND entry changes from the REACHABLE state to the STALE state if it remains unused for 20 minutes.


Example
-------

# Enable pre-detection on ND entries in the system view.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd pre-detect

```