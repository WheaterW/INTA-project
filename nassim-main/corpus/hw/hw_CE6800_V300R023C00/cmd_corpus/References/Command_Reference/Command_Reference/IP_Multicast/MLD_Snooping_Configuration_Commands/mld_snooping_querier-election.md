mld snooping querier-election
=============================

mld snooping querier-election

Function
--------



The **mld snooping querier-election** command enables the querier election function.

The **undo mld snooping querier-election** command disables the querier election function.



By default, querier election is disabled for a VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping querier-election**

**undo mld snooping querier-election**


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

If queriers are enabled on multiple devices in the same VLAN, run the **mld snooping querier-election** command to elect a device that sends MLD Query messages with the minimum source IP address as the querier, thus freeing the upstream device from sending Query messages to users. To set source IP addresses for MLD Query messages, run the **mld snooping send-query source-address** command. By default, the source IP addresses of MLD Query messages are FF80::.


Example
-------

# Enable the querier election function for VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping querier-election

```