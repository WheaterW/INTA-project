mld snooping learning disable vlan
==================================

mld snooping learning disable vlan

Function
--------



The **mld snooping learning disable vlan** command disables an interface in VLANs to dynamically learn forwarding entries.

The **undo mld snooping learning disable vlan** command enables the function.



By default, interfaces in VLANs are enabled to dynamically learn forwarding entries.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping learning disable vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }

**undo mld snooping learning disable vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies a start VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **to** *vlan-id2* | Specifies an end VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **all** | Disables an interface in all VLANs to learn forwarding entries. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,VLAN range view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable an interface to dynamically learn forwarding entries in MLD Report messages received, run the mld snooping learning command. After this command is run for an interface, the interface can be added to a multicast group manually. However, after the undo mld snooping learning command is run for an interface, the interface cannot dynamically learn forwarding entries, but can still be added to a multicast group manually.If the undo mld snooping learning command is run more than once, all configurations take effect.


Example
-------

# Disable 100GE 1/0/1 in VLAN 3 and VLAN 4 from dynamically learning forwarding entries.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 3
[*HUAWEI-vlan3] mld snooping enable
[*HUAWEI-vlan3] quit
[*HUAWEI] vlan 4
[*HUAWEI-vlan4] mld snooping enable
[*HUAWEI-vlan4] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 3 to 4
[*HUAWEI-100GE1/0/1] mld snooping learning disable vlan 3 to 4

```