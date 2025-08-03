tiebreaker preference (IS-IS FRR view)
======================================

tiebreaker preference (IS-IS FRR view)

Function
--------



The **tiebreaker preference** command sets the solution of selecting a backup path for IS-IS Auto FRR.

The **undo tiebreaker preference** command restores the default solution of selecting a backup path for IS-IS Auto FRR.



By default, the node-protection path first solution is used in IS-IS Auto FRR.


Format
------

**tiebreaker** { **node-protecting** | **lowest-cost** | **non-ecmp** | **srlg-disjoint** | **hold-max-cost** } **preference** *preference* [ **level-1** | **level-2** | **level-1-2** ]

**undo tiebreaker** { **node-protecting** | **lowest-cost** | **non-ecmp** | **srlg-disjoint** | **hold-max-cost** } [ **preference** *preference* ] [ **level-1** | **level-2** | **level-1-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **node-protecting** | Sets the solution of selecting a backup path for IS-IS Auto FRR to node-protection path first. | - |
| **lowest-cost** | Sets the solution of selecting a backup path for IS-IS Auto FRR to smallest-cost path first. | - |
| **non-ecmp** | Sets the solution of selecting a backup path for IS-IS Auto FRR to non-ECMP first. | - |
| **srlg-disjoint** | Sets the solution of selecting a backup path for IS-IS Auto FRR to shared risk link group (SRLG) disjoint first. | - |
| **hold-max-cost** | Sets the solution of selecting a backup path for IS-IS Auto FRR to the maximum cost path first. | - |
| **preference** *preference* | Specifies a priority for the solution. The larger the value, the higher the priority. | The value is an integer ranging from 1 to 255. |
| **level-1** | Sets the solution of selecting a backup path for Level-1 IS-IS Auto FRR. | - |
| **level-2** | Sets the solution of selecting a backup path for Level-2 IS-IS Auto FRR. | - |
| **level-1-2** | Sets the solution of selecting a backup path for both Level-1 and Level-2 IS-IS Auto FRR. | - |



Views
-----

IS-IS FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In IS-IS Auto FRR, the solution of protecting nodes is preferred for selecting a backup path. However, in an actual network, due to factors such as interface data capability or link cost, the solution of selecting a backup path may need to be adjusted to a path with the minimum cost or another optional path. In this case, you can run the **tiebreaker** command to adjust the value.

**Prerequisites**

IS-IS Auto FRR has been enabled using the **loop-free-alternate** command.

**Precautions**



By default, the preference value is 40 for the node-protection path first solution, 20 for the smallest-cost path first solution, and 15 for the maximum cost path first solution.




Example
-------

# Sets the solution of selecting a backup path for IS-IS Auto FRR to the maximum path first.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] frr
[*HUAWEI-isis-1-frr] loop-free-alternate
[*HUAWEI-isis-1-frr] tiebreaker hold-max-cost preference 255

```

# Set the solution of selecting a backup path for IS-IS Auto FRR to smallest-cost path first.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] frr
[*HUAWEI-isis-1-frr] loop-free-alternate
[*HUAWEI-isis-1-frr] tiebreaker lowest-cost preference 255

```