igmp snooping learning disable vlan
===================================

igmp snooping learning disable vlan

Function
--------



The **igmp snooping learning disable vlan** command disables an interface from dynamically learning forwarding entries of VLAN.

The **undo igmp snooping learning disable vlan** command enables an interface to dynamically learn forwarding entries of VLAN.



By default, an interface is enabled to dynamically learn forwarding entries.


Format
------

**igmp snooping learning disable vlan** { { *vid1* [ **to** *vid2* ] } &<1-10> | **all** }

**undo igmp snooping learning disable vlan** { { *vid1* [ **to** *vid2* ] } &<1-10> | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vid1* | Specifies a start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The vlan-id or vlan-id2 value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vid2* | Specifies an end VLAN ID. If you do not specify to vlan-id2 interfaces are added only to the VLAN specified by vlan-id1. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The vlan-id or vlan-id2 value is an integer ranging from 1 to 4094.  vlan-id2 must be greater than or equal to vlan-id1. vlan-id2 and vlan-id1 specify a VLAN ID range.  For the CE6885-LL (low latency mode): The value is an integer that ranges from 1 to 1023.  vlan-id2 must be greater than vlan-id1. vlan-id1 and vlan-id2 specify a VLAN range. |
| **all** | Indicates that dynamic forwarding entry learning is enabled in all the VLANs to which a specific interface belongs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the undo igmp snooping learning disable command to enable an interface dynamically to learn forwarding entries, the interface can both be added to a multicast group statically and learn forwarding entries dynamically based on received IGMP Report messages. After the interface is disabled from dynamically learning forwarding entries, you can only add the interface to a multicast group statically.If the igmp snooping learning disable command is run more than once, all configurations take effect.


Example
-------

# Disable 100GE 1/0/1 that belongs to VLANs 3 and 4 from dynamically learning forwarding entries.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 3
[*HUAWEI-vlan3] igmp snooping enable
[*HUAWEI-vlan3] quit
[*HUAWEI] vlan 4
[*HUAWEI-vlan4] igmp snooping enable
[*HUAWEI-vlan4] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 3 to 4
[*HUAWEI-100GE1/0/1] igmp snooping learning disable vlan 3 to 4

```