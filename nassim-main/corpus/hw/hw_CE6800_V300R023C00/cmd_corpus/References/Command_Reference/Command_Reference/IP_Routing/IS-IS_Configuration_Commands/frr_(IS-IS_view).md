frr (IS-IS view)
================

frr (IS-IS view)

Function
--------



The **frr** command enables fast reroute (FRR) for IS-IS or displays the IS-IS FRR view if FRR has been enabled.

The **undo frr** command disables IS-IS FRR.

The **ipv6 frr** command enables IPv6 FRR and displays an IPv6 FRR view.

The **undo ipv6 frr** command enables the system to exit from an IPv6 FRR view.



By default, FRR and IPv6 FRR are disabled.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**frr**

**undo frr**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 frr**

**undo ipv6 frr**


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

To enable FRR for IS-IS or display the IS-IS FRR view if FRR has been enabled, run the **frr** command. Before using the **frr** command, you need to enable an IS-IS process.Running the **undo frr** command will also delete all configurations from the FRR view. Therefore, exercise caution when running this command.On a network with redundant links, a backup link can be pre-computed through IP FRR, and then the backup link is added to the forwarding table. In this manner, if the primary link fails, traffic can be protected in time and the traffic interruption time is reduced to within 50 ms. This meets the requirement for real-time services.The **ipv6 frr** command is applicable to IPv6 base topologies.The **ipv6 frr** command is used to enable IPv6 FRR and enter the IPv6 FRR view.After configuring the **ipv6 frr** command, run the **loop-free-alternate** command to compute a loop-free backup route.

**Prerequisites**

Before configuring the **frr** command, enable an IS-IS process.Before configuring the **ipv6 frr** command, enable IPv6 IS-IS.

**Precautions**

Running the **undo frr** command will delete all configurations in the FRR view. Therefore, exercise caution when running this command.FRR and IS-IS intelligent convergence are mutually exclusive. That is, in the IS-IS view, the **frr** command and the **intelligent-convergence enable** command are mutually exclusive, and the **ipv6 frr** command and the **ipv6 intelligent-convergence enable** command are mutually exclusive.


Example
-------

# Display the FRR view for IS-IS process 1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] frr

```

# Enable IPv6 FRR in IS-IS process 1 and display the IPv6 FRR view.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 frr

```