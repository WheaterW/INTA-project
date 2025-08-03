reset qos ecn statistics
========================

reset qos ecn statistics

Function
--------



The **reset qos ecn statistics** command clears statistics on packets with the ECN flag on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset qos ecn statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before re-collecting statistics about packets with the ECN flag on an interface, run the reset qos ecn statistics command to clear existing statistics.

**Precautions**

The cleared statistics cannot be restored. Exercise caution when you run the command.


Example
-------

# Clear statistics on packets with the ECN flag on a specified interface.
```
<HUAWEI> reset qos ecn statistics interface 100GE 1/0/1

```