ipv6 intelligent-convergence enable
===================================

ipv6 intelligent-convergence enable

Function
--------



The **ipv6 intelligent-convergence enable** command configures IS-IS IPv6 intelligent convergence.

The **undo ipv6 intelligent-convergence enable** command disables IS-IS IPv6 intelligent convergence.



By default, IS-IS IPv6 intelligent convergence is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 intelligent-convergence enable**

**undo ipv6 intelligent-convergence enable**


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

In a scenario where a single route source fails, after the **ipv6 intelligent-convergence enable** command is run, IS-IS can perform fast convergence using a fast convergence algorithm, improving convergence performance.

**Precautions**



IS-IS IPv6 intelligent convergence is mutually exclusive with microloop avoidance and FRR. That is, this command is mutually exclusive with the ipv6 frr and **ipv6 avoid-microloop segment-routing** commands.




Example
-------

# Configure IS-IS IPv6 intelligent convergence.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 intelligent-convergence enable

```