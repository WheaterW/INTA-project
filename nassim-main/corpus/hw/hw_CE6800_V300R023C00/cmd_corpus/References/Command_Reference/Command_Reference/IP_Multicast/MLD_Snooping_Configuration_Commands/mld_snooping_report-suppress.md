mld snooping report-suppress
============================

mld snooping report-suppress

Function
--------



The **mld snooping report-suppress** command enables MLD Report message suppression.

The **undo mld snooping report-suppress** command disables MLD Report message suppression.



By default, MLD Report message suppression is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping report-suppress**

**undo mld snooping report-suppress**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The mld snooping report-suppress command allows a device to respond only one MLD Report message to an MLD Query message of a group sent by the upstream multicast router, regardless of the number of interfaces that have joined the same multicast group. This function reduces network-side traffic.

**Precautions**

It is recommended that the MLD version configured on the upstream device be the same as that configured on the local device.


Example
-------

# Enable MLD Report message suppression in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping report-suppress

```