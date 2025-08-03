intelligent-convergence enable
==============================

intelligent-convergence enable

Function
--------



The **intelligent-convergence enable** command enables IS-IS intelligent convergence.

The **undo intelligent-convergence enable** command disables IS-IS intelligent convergence.



By default, IS-IS intelligent convergence is disabled.


Format
------

**intelligent-convergence enable**

**undo intelligent-convergence enable**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a fault-triggered switching scenario where the local device receives a route from a single node, to enable IS-IS intelligent convergence, run the **intelligent-convergence enable** command. After this command is run, IS-IS can perform fast route convergence by using the fast convergence algorithm, thereby improving convergence performance.

**Precautions**



In the same networking scenario, if you run this command on one or more devices, the convergence speed of these devices is greatly different from that of other devices. As a result, routing loops occur. Therefore, exercise caution when running this command.IS-IS intelligent convergence is mutually exclusive with microloop avoidance and FRR. That is, IS-IS intelligent convergence is mutually exclusive with the avoid-microloop segment-routing and **frr** commands in the IS-IS view.




Example
-------

# Enable IS-IS intelligent convergence.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] intelligent-convergence enable

```