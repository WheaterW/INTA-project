mld snooping proxy
==================

mld snooping proxy

Function
--------



The **mld snooping proxy** command enables MLD snooping proxy in a VLAN.

The **undo mld snooping proxy** command disables MLD snooping proxy in a VLAN.



By default, MLD snooping proxy is disabled in a VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping proxy**

**undo mld snooping proxy**


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

Forwarding entries are set up based on MLD messages exchanged between a Layer 3 device and user hosts. If there are many user hosts, redundant MLD messages increase the workload of the Layer 3 device.MLD snooping proxy can address this problem. MLD snooping proxy provides two functions: querier and unified message transmission, which should be both implemented on the Layer 3 device without MLD snooping proxy. With the querier function, a Layer 2 device can send MLD Query messages. With the unified message transmission function, a Layer 2 device can receive and terminate MLD Query messages sent from users, and then send them in a unified manner. To enable MLD snooping proxy, run the mld snooping proxy command, which helps reduce the burden of the Layer 3 device and saves bandwidth resources on the Layer 2 and Layer 3 devices.


Example
-------

# Enable MLD snooping proxy in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping proxy

```