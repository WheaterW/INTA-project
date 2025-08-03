reset vlan statistics
=====================

reset vlan statistics

Function
--------



The **reset vlan statistics** command clears statistics about sent and received VLAN packets.




Format
------

**reset vlan** *vlan-id* **statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a VLAN in which packet statistics are cleared. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **slot** *slot-id* | Specifies a slot ID. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before collecting traffic statistics of an interface in a specified VLAN within a period, run the reset vlan statistics command to clear existing traffic statistics.

**Precautions**

Traffic statistics cannot be restored once being cleared. Therefore, exercise caution when running this reset vlan statistics command.


Example
-------

# Clear statistics about sent and received packets in VLAN 4.
```
<HUAWEI> reset vlan 4 statistics

```