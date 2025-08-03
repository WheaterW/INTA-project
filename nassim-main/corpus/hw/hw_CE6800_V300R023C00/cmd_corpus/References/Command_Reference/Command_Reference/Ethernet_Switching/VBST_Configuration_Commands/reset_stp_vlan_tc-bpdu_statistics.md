reset stp vlan tc-bpdu statistics
=================================

reset stp vlan tc-bpdu statistics

Function
--------



The **reset stp vlan tc-bpdu statistics** command clears statistics on sent and received TC/TCN packets on the VBST-enabled interface in a VLAN.




Format
------

**reset stp vlan** { *vlan-id* | **all** } **tc-bpdu** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Clears spanning tree information about a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **all** | Clears spanning tree information about all VLANs. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before collecting statistics on sent and received VBST TC/TCN packets about a VLAN or all VLANs on the VBST-enabled interface, run the **reset stp vlan tc-bpdu statistics** command to clear existing statistics on VBST TC/TCN packets to ensure the correctness of statistics.

**Configuration Impact**

After the **reset stp vlan tc-bpdu statistics** command is executed, statistics on sent and received VBST TC/TCN packets about a VLAN or all VLANs are cleared. The cleared statistics cannot be restored. Exercise caution when you run the **reset stp vlan tc-bpdu statistics** command.


Example
-------

# Clear VBST TC/TCN packets in VLAN 5.
```
<HUAWEI> reset stp vlan 5 tc-bpdu statistics
Warning: Tc-bpdu statistics of this vlan will be cleared. Continue? [Y/N]:Y

```