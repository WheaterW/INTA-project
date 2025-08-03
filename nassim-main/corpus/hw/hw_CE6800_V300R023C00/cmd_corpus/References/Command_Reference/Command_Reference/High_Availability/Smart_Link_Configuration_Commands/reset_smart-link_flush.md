reset smart-link flush
======================

reset smart-link flush

Function
--------



The **reset smart-link flush** command clears statistics about normal Flush packets and received error packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset smart-link flush**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To collect Flush packet statistics within a specified period of time, run the reset smart-link flush command to clear existing Flush packet statistics. For example, a large number of Flush packets are sent after a link switchover is performed in a Smart Link group. If a device is faulty, you can check information about received Flush packets to help locate the fault. If existing Flush packet statistics are of no use, run the reset smart-link flush command to clear the statistics to avoid the impact of excessive Flush packet statistics on the next fault locating.

**Precautions**

Flush packet statistics cannot be restored after being cleared, therefore, exercise caution when running the reset smart-link flush command, run the **display smart-link flush** command.


Example
-------

# Clear Flush packet statistics.
```
<HUAWEI> reset smart-link flush

```