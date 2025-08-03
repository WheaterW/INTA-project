reset mld snooping group
========================

reset mld snooping group

Function
--------



The **reset mld snooping group** command clears dynamic outbound interface entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset mld snooping group** { **vlan** { *vlanid* | **all** } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlanid* | Clears dynamic outbound interface entries of a specified VLAN. | The value is an integer ranging from 1 to 4094. |
| **vlan** **all** | Clears dynamic outbound interface entries of all VLANs. | - |
| **all** | Clears all of dynamic outbound interface entries. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the reset mld snooping group command is run to clear dynamic outbound interface entries of a VLAN, hosts in the VLAN fail to receive multicast flows temporarily. The hosts can receive multicast flows again only after they send MLD Report messages and the router re-generates outbound interface entries.


Example
-------

# Clear dynamic outbound interface entries of all VLANs.
```
<HUAWEI> reset mld snooping group all

```

# Clear dynamic outbound interface entries of VLAN 2.
```
<HUAWEI> reset mld snooping group vlan 2

```