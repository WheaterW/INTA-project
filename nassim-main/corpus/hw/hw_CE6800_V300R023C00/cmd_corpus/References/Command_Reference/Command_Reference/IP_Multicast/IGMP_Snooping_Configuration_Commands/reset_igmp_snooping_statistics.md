reset igmp snooping statistics
==============================

reset igmp snooping statistics

Function
--------



The **reset igmp snooping statistics** command clears the statistics of IGMP snooping.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset igmp snooping statistics** { **vlan** { *vlan-id* | **all** } | **all** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset igmp snooping statistics bridge-domain** { *bd-id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Specifies the ID of a VLAN. | The value ranges from 1 to 4094. |
| **all** | Clears all the statistics information. | - |
| **all** | Clears IGMP snooping statistics in all BDs.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **all** | Clears IGMP snooping statistics in all VLANs. | - |
| **bridge-domain** *bd-id* | Clears the statistics information of specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To clear the statistics of IGMP snooping in all VLANs, use the **reset igmp snooping statistics all** command.To clear the statistics of IGMP snooping in a specified VLAN, use the **reset igmp snooping statistics vlan** command.To clear the statistics of IGMP snooping in all VLANs, use the reset igmp snooping statisticsvlan all command.


Example
-------

# Clear the IGMP snooping statistics of VLAN 2.
```
<HUAWEI> reset igmp snooping statistics vlan 2

```

# Clear the IGMP snooping statistics.
```
<HUAWEI> reset igmp snooping statistics all

```