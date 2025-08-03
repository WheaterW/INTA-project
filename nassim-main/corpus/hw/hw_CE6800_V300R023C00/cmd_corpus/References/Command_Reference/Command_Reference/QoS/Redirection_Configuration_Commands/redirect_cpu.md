redirect cpu
============

redirect cpu

Function
--------



The **redirect cpu** command configures an action of redirecting packets to the CPU in a traffic behavior.

The **undo redirect cpu** command deletes the redirection configuration.



By default, the action of redirecting packets to the CPU is not configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**redirect cpu**

**undo redirect** [ **cpu** ]


Parameters
----------

None

Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **redirect cpu** command to configure an action of redirecting packets to the CPU.

**Precautions**

After a traffic policy containing an action of redirecting packets to the CPU is applied, the system performance may be affected. Therefore, exercise caution when running this command.


Example
-------

# Configure a traffic behavior named b1 to redirect packets to the CPU.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] redirect cpu

```