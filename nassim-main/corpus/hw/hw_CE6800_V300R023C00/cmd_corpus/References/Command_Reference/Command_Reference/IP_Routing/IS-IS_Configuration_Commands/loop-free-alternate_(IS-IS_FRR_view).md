loop-free-alternate (IS-IS FRR view)
====================================

loop-free-alternate (IS-IS FRR view)

Function
--------



The **loop-free-alternate** command enables IS-IS Auto FRR to calculate loop-free backup routes based on the LFA algorithm.

The **undo loop-free-alternate** command disables IS-IS Auto FRR.



By default, IS-IS Auto FRR is disabled.


Format
------

**loop-free-alternate** [ **level-1** | **level-2** | **level-1-2** ]

**undo loop-free-alternate** [ **level-1** | **level-2** | **level-1-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Indicates that Level-1 Auto FRR is enabled to generate loop-free backup routes. | - |
| **level-2** | Indicates that Level-2 Auto FRR is enabled to generate loop-free backup routes. | - |
| **level-1-2** | Indicates that Level-1 Auto FRR and Level 2 Auto FRR are enabled to generate loop-free backup routes. | - |



Views
-----

IS-IS FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To provide real-time transmission for network services, traffic must be fast switched if IS-IS faults occur. Configuring IS-IS Auto FRR can fast switch traffic to the backup link before route convergence on the control plane. This ensures uninterrupted traffic transmission. The backup link is calculated based on the LFA algorithm. With the neighbor that can provide the backup link as the root, the shortest path to the destination node is calculated based on the SPF algorithm. Then, the loop-free backup link with the smallest cost is calculated according to the inequality defined in standard protocols.

**Prerequisites**

An IS-IS process has been created, and the IS-IS FRR view or IS-IS IPv6 FRR view has been displayed.

**Configuration Impact**



After LFA is enabled, backup outbound interfaces and next hops are calculated according to the current topology.



**Precautions**



IS-IS can generate loop-free backup routes only when the IS-IS Auto FRR traffic protection inequality is met.If no level is specified, IS-IS Auto FRR is enabled at both Level-1 and Level-2 to generate backup routes.This command can be based on IPv4 and IPv6 IS-IS Auto FRR.This command takes effect regardless of whether the same route is advertised by multiple nodes.




Example
-------

# Enable Level-2 IS-IS Auto FRR to generate loop-free backup routes.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] frr
[*HUAWEI-isis-1-frr] loop-free-alternate level-2

```