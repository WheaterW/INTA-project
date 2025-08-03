reset qos car statistics
========================

reset qos car statistics

Function
--------



The **reset qos car statistics** command clears packet statistics on an interface to which a QoS CAR profile is applied.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset qos car statistics interface** { *interface-name* | *interface-type* *interface-number* } **inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **inbound** | Inbound configuration. | - |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before recollecting statistics on forwarded and discarded packets on an interface to which a QoS CAR profile is applied, run the **reset qos car statistics** command to clear existing statistics. Then run the **display qos car statistics** command to view the packet statistics.

**Precautions**

The cleared statistics on forwarded and discarded packets on an interface cannot be restored. Exercise caution when you use this command.


Example
-------

# Clear statistics in the inbound direction on the 100GE1/0/1.
```
<HUAWEI> reset qos car statistics interface 100GE 1/0/1 inbound

```