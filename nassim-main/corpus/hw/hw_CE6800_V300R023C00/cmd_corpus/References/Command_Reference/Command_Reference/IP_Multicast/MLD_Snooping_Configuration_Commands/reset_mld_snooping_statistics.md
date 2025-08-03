reset mld snooping statistics
=============================

reset mld snooping statistics

Function
--------



The **reset mld snooping statistics** command clears MLD snooping statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset mld snooping statistics** { **vlan** { *vlan-id* | **all** } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Clears MLD snooping statistics of a specified VLAN. | The value is an integer ranging from 1 to 4094. |
| **vlan** **all** | Clears MLD snooping statistics of all VLANs. | - |
| **all** | Clears all of MLD snooping statistics. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To clear MLD snooping statistics of all VLANs, run the reset mld snooping statistics all command.To clear MLD snooping statistics of a specified VLAN, run the **reset mld snooping statistics vlan** command.To clear MLD snooping statistics of all VLANs, run the **reset mld snooping statistics vlan all** command.


Example
-------

# Delete MLD snooping statistics of VLAN 2.
```
<HUAWEI> reset mld snooping statistics vlan 2

```

# Clear MLD snooping statistics of all VLANs.
```
<HUAWEI> reset mld snooping statistics all

```