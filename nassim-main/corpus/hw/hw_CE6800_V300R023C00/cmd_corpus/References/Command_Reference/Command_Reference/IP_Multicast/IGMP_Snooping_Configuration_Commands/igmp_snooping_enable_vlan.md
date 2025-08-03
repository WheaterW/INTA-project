igmp snooping enable vlan
=========================

igmp snooping enable vlan

Function
--------



The **igmp snooping enable vlan** command enables IGMP snooping on a specified VLAN.

The **undo igmp snooping enable vlan** command disables IGMP snooping on a specified VLAN.



By default, IGMP snooping is disabled on a VLAN.


Format
------

**igmp snooping enable vlan** { *vid1* [ **to** *vid2* ] } &<1-10>

**undo igmp snooping enable vlan** { **all** | { *vid1* [ **to** *vid2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vid1* | Specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. |
| **to** *vid2* | Specifies the ending VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. |
| **all** | Enables IGMP snooping on all VLANs. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IGMP snooping is used on a Layer 2 device running between a Layer 3 device and hosts, allowing the Layer 2 device to listen to the multicast protocol packets exchanged between the Layer 3 device and hosts. By listening to the multicast protocol packets, the Layer 2 device maintains a multicast forwarding table to manage and control multicast packet forwarding. You need to enable IGMP snooping before implementing Layer 2 multicast.

**Configuration Impact**

If the igmp snooping enable vlan command is run more than once, all configurations take effect.

**Precautions**

Theigmp snooping enable vlan command may fail to be configured in the following situations:

* The Dot1q sub-interface has been bound to the VLAN.

Example
-------

# Enable IGMP snooping on multiple VLANs in the system view.
```
<HUAWEI> system-view
[*HUAWEI] igmp snooping enable
[*HUAWEI] vlan batch 2 to 10
[*HUAWEI] igmp snooping enable vlan 2 to 10

```