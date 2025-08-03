multicast layer-2 ipv6 source-lifetime
======================================

multicast layer-2 ipv6 source-lifetime

Function
--------



The **multicast layer-2 ipv6 source-lifetime** command sets the aging time for (S, G) entries of multicast traffic in a specified VLAN.

The **undo multicast layer-2 ipv6 source-lifetime** command restores the default setting.



By default, the aging time is 210s for an (S, G) or (\*, G) entry of multicast traffic in a specified VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast layer-2 ipv6 source-lifetime** *lifetime*

**undo multicast layer-2 ipv6 source-lifetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-lifetime** *lifetime* | Sets the aging time for (S, G) entries of multicast traffic in a specified VLAN. | The value is an integer ranging from 60 to 65535, in seconds. The default value is 210. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a multicast source no longer sends multicast data flows, the source needs to be deleted. This requires constant probes on whether the source sends multicast data flows, deteriorating system performance. To address this problem, run the multicast layer-2 ipv6 source-lifetime command to set the aging time for entries of multicast traffic in a specified VLAN.


Example
-------

# Set the aging time of entries triggered by multicast traffic in VLAN 100 to 100 seconds.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] multicast layer-2 ipv6 source-lifetime 100

```