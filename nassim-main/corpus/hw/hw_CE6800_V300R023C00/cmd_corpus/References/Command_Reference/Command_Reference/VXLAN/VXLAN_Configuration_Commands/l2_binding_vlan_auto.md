l2 binding vlan auto
====================

l2 binding vlan auto

Function
--------



The **l2 binding vlan auto** command configures automatic VLAN binding to a BD in a BD profile. When the BD profile is bound to a BD, the BD is automatically bound to a VLAN.

The **undo l2 binding vlan auto** command disables automatic binding between a BD and a VLAN in a BD profile.



By default, a BD is not automatically bound to a VLAN in a BD profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**l2 binding vlan auto**

**undo l2 binding vlan auto**


Parameters
----------

None

Views
-----

bd-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a VXLAN network, you need to configure VXLAN service access points on a VXLAN network edge node. After a VLAN is bound to a BD using the **l2 binding vlan** command, interfaces added to the VLAN become VXLAN service access points. The l2 binding vlan auto command is used to automatically bind a BD to a VLAN in a BD profile. After a BD is bound to a BD profile, if the l2 binding vlan auto command is run in the BD profile, the BD is automatically bound to a VLAN, and the bound VLAN ID is the same as the BD ID.


Example
-------

# Enable the function of automatically binding a BD to a VLAN in profile 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain profile 10
[*HUAWEI-bd-profile10] l2 binding vlan auto

```