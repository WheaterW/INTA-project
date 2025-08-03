reset igmp snooping group
=========================

reset igmp snooping group

Function
--------



The **reset igmp snooping group** command clears the dynamic forwarding entries from a multicast forwarding table.




Format
------

**reset igmp snooping group** { **vlan** { *vlan-id* | **all** } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Clears the dynamic forwarding entries of a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **all** | Clears all of the dynamic forwarding entries from the multicast forwarding tables. | - |
| **all** | Clears the dynamic forwarding entries from the multicast forwarding tables in all VLANs. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the command is used to clear the dynamic forwarding entries in a certain VLAN, the multicast traffic received by hosts in the VLAN is interrupted until the hosts send IGMP Report messages again. After receiving the IGMP Report messages, the router regenerates the forwarding entries and the hosts start to receive the multicast traffic again.


Example
-------

# Clear all dynamic forwarding entries in VLAN 2.
```
<HUAWEI> reset igmp snooping group vlan 2

```

# Clear the dynamic forwarding entries in all VLANs.
```
<HUAWEI> reset igmp snooping group all

```