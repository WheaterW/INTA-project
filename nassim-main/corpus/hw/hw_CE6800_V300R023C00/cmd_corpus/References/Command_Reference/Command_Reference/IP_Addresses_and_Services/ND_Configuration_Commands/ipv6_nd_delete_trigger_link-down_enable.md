ipv6 nd delete trigger link-down enable
=======================================

ipv6 nd delete trigger link-down enable

Function
--------



The **ipv6 nd delete trigger link-down enable** command enables the function to trigger fast deletion of ND entries upon link down.

The **undo ipv6 nd delete trigger link-down enable** command disables the function to trigger fast deletion of ND entries upon link down.



By default, link down does not trigger fast deletion of ND entries.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd delete trigger link-down enable**

**undo ipv6 nd delete trigger link-down enable**


Parameters
----------

None

Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Layer 2 link down causes ND neighbor entries to be in the Delay state. After 5 seconds, this event triggers ND neighbor detection. If ND neighbor detection is unreachable, ND entries are automatically deleted. If there are many ND entries, the deletion is slow and some entries may remain residual for too long. To address this problem, run the **ipv6 nd delete trigger link-down enable** command to trigger fast deletion of ND entries upon link down. This may lead to intermittent interruption of flows.

**Precautions**



This command causes instant intermittent interruption of flows. Exercise caution while running this command.




Example
-------

# Enable the function to trigger fast deletion of ND entries upon link down.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] quit
[*HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] ipv6 nd delete trigger link-down enable

```