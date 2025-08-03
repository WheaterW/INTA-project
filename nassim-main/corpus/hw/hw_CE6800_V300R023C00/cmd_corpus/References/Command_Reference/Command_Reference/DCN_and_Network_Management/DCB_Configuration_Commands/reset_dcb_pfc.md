reset dcb pfc
=============

reset dcb pfc

Function
--------



The **reset dcb pfc** command clears PFC statistics on an interface to which a PFC profile is applied.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset dcb pfc** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Clears PFC statistics on a specified interface.   * interface-type specifies the type of an interface. * interface-number specifies the number of an interface.   If this parameter is not specified, PFC statistics on all the interfaces to which PFC profiles are applied are cleared. | - |
| **interface** *interface-name* | Clears PFC statistics on a specified interface.   * interface-name specifies the name of an interface.   If this parameter is not specified, PFC statistics on all the interfaces to which PFC profiles are applied are cleared. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When diagnosing and locating PFC faults, you need to collect PFC statistics in a period of time.Before re-collecting PFC statistics, run the **reset dcb pfc** command to clear existing PFC statistics. You can then run the **display dcb pfc** command to view PFC statistics.

**Precautions**

After the **reset dcb pfc** command is run, PFC statistics are cleared and cannot be restored. Exercise caution when you run this command.


Example
-------

# Clear PFC statistics on 100GE1/0/1.
```
<HUAWEI> reset dcb pfc interface 100GE 1/0/1

```