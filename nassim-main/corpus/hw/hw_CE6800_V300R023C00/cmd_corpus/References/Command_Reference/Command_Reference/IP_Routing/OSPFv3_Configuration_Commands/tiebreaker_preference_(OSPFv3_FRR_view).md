tiebreaker preference (OSPFv3 FRR view)
=======================================

tiebreaker preference (OSPFv3 FRR view)

Function
--------



The **tiebreaker preference** command sets the solution of selecting a backup path for OSPFv3 IP FRR.

The **undo tiebreaker preference** command restores the default solution of selecting a backup path for OSPFv3 IP FRR.



By default, the solution of selecting a backup path for OSPFv3 IP FRR is node-protection path first.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tiebreaker** { **node-protecting** | **lowest-cost** } **preference** *value*

**undo tiebreaker** { **node-protecting** | **lowest-cost** } [ **preference** *value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **node-protecting** | Sets the solution of selecting a backup path for IP FRR to node-protection path first. | - |
| **lowest-cost** | Sets the solution of selecting a backup path for IP FRR to smallest-cost path first. | - |
| **preference** *value* | Specifies a priority for the solution. The larger the value, the higher the priority. | The value is an integer ranging from 1 to 255.  By default, the priority of the node-protection path first solution is 40, and the priority of the smallest-cost path first solution is 20. |



Views
-----

OSPFv3 FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the solution of selecting a backup path for OSPFv3 IP FRR is node-protection path first. In some cases, the solution needs to be changed to smallest-cost path first because of data forwarding capacity or link cost consideration. To change the solution of selecting a backup path for OSPFv3 IP FRR to smallest-cost path first, run the **tiebreaker** command.

**Prerequisites**

The OSPFv3 FRR view has been displayed using the **frr** command, and OSPFv3 IP FRR has been enabled using the **loop-free-alternate** command.


Example
-------

# Set the solution of selecting a backup path for OSPFv3 IP FRR to smallest-cost path first.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] frr
[*HUAWEI-ospfv3-1-frr] loop-free-alternate
[*HUAWEI-ospfv3-1-frr] tiebreaker lowest-cost preference 255

```