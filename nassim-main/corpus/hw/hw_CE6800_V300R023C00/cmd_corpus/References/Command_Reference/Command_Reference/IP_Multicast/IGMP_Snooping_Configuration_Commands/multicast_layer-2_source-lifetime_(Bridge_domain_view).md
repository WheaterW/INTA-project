multicast layer-2 source-lifetime (Bridge domain view)
======================================================

multicast layer-2 source-lifetime (Bridge domain view)

Function
--------



The **multicast layer-2 source-lifetime** command sets the aging time for an (S, G) or (\*, G) entry triggered by multicast traffic.

The **undo multicast layer-2 source-lifetime** command restores the default configuration.



By default, the aging time of an (S, G) or (\*, G) entry triggered by multicast traffic 210s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast layer-2 source-lifetime** *SrcLifetimeValue*

**undo multicast layer-2 source-lifetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *SrcLifetimeValue* | Specifies the aging time of an (S, G) or (\*, G) entry triggered by multicast traffic. | The value is an integer ranging from 60 to 65535. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a multicast source no longer sends multicast data traffic, the source needs to be deleted. This requires constant probes on whether the source sends multicast data flows. To address this problem, the multicast layer-2 source-lifetime command can be used to set the aging time for entries triggered by multicast traffic based on system performance.


Example
-------

# Set the timer for deleting multicast forwarding entries triggered by multicast traffic to 100 seconds in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] multicast layer-2 source-lifetime 100

```