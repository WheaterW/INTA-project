tiebreaker preference (OSPF FRR view)
=====================================

tiebreaker preference (OSPF FRR view)

Function
--------



The **tiebreaker preference** command sets the solution of selecting a backup path for OSPF IP FRR.

The **undo tiebreaker preference** command restores the default solution of selecting a backup path for OSPF IP FRR.



By default, the solution of selecting a backup path for OSPF IP FRR is node-protection path first.


Format
------

**tiebreaker** { **node-protecting** | **lowest-cost** } **preference** *value*

**undo tiebreaker** { **node-protecting** | **lowest-cost** } [ **preference** *value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **node-protecting** | Sets the solution of selecting a backup path for OSPF IP FRR to node-protection path first. | - |
| **lowest-cost** | Sets the solution of selecting a backup path for OSPF IP FRR to smallest-cost path first. | - |
| **preference** *value* | Specifies a priority for the solution. The larger the value, the higher the priority. | The value is an integer ranging from 1 to 255.  By default, the priority of the node-protection path first solution is 40, and the priority of the smallest-cost path first solution is 20. |



Views
-----

OSPF FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the solution of selecting a backup path for OSPF IP FRR is node-protection path first. In some cases, the solution needs to be changed to smallest-cost path first because of data forwarding capacity or link cost consideration. To change the solution of selecting a backup path for OSPF IP FRR to smallest-cost path first, run the **tiebreaker** command.

**Prerequisites**

The OSPF FRR view has been displayed using the **frr** command, and OSPF IP FRR has been enabled using the **loop-free-alternate** command.


Example
-------

# Set the solution of selecting a backup path for OSPF IP FRR to smallest-cost path first.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] frr
[*HUAWEI-ospf-1-frr] loop-free-alternate
[*HUAWEI-ospf-1-frr] tiebreaker lowest-cost preference 255

```