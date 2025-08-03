multicast layer-2 source-lifetime
=================================

multicast layer-2 source-lifetime

Function
--------



The **multicast layer-2 source-lifetime** command sets the aging time for an (S, G) or (\*, G) entry triggered by multicast traffic.

The **undo multicast layer-2 source-lifetime** command restores the default configuration.



By default, the aging time of an (S, G) or (\*, G) entry triggered by multicast traffic 210s.


Format
------

**multicast layer-2 source-lifetime** *SrcLifetimeValue*

**undo multicast layer-2 source-lifetime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *SrcLifetimeValue* | Specifies the aging time of an (S, G) or (\*, G) entry triggered by multicast traffic. | The value is an integer that ranges from 60 to 65535, in seconds. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a multicast source no longer sends multicast data traffic, the source needs to be deleted. This requires constant probes on whether the source sends multicast data flows. To address this problem, the multicast layer-2 source-lifetime command can be used to set the aging time for entries triggered by multicast traffic based on system performance.


Example
-------

# Set the timer for deleting multicast forwarding entries triggered by multicast traffic to 100 seconds in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] multicast layer-2 source-lifetime 100

```