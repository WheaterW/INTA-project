reset ptp statistics
====================

reset ptp statistics

Function
--------



The **reset ptp statistics** command clears statistics about 1588v2 messages received and sent by interfaces.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ptp statistics** { **all** | **interface** *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears statistics about 1588v2 messages received and sent by all interfaces. | - |
| **interface** *interface-type* *interface-number* | Clears statistics about 1588v2 messages received and sent by a specified interface. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During device debugging or maintenance, to check whether a 1588v2 device can implement time synchronization, run the reset ptp statistics command to clear statistics about 1588v2 messages received and sent by a specified interface or all interfaces and then run the **display ptp interface** command to check statistics about 1588v2 messages.

**Precautions**

1588v2 statistics cannot be restored after being cleared. Exercise caution when running the reset ptp statistics command.


Example
-------

# Clear statistics about 1588v2 messages received and sent by 100GE1/0/1.
```
<HUAWEI> reset ptp statistics interface 100GE 1/0/1

```