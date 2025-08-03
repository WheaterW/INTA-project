reset ospfv3 frr
================

reset ospfv3 frr

Function
--------



The **reset ospfv3 frr** command resets OSPFv3 IP FRR.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ospfv3** { *process-id* | **all** } **frr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of an OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Resets FRR for all OSPFv3 processes running on router. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



This command is a maintenance command. It can be used to forcibly reset FRR without deleting the FRR configuration.



**Prerequisites**



FRR has been configured in an OSPFv3 process.EffectOSPFv3 IP FRR calculation does not affect the normal running of OSPFv3.



**Configuration Impact**



OSPFv3 IP FRR calculation does not affect the normal running of OSPFv3.




Example
-------

# Reset FRR in OSPFv3 process 1.
```
<HUAWEI> reset ospfv3 1 frr

```