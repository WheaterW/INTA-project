reset adaptive-routing notification statistics
==============================================

reset adaptive-routing notification statistics

Function
--------



The **reset adaptive-routing notification statistics** command clears the statistics on ARN messages for congestion and congestion relief notification sent and received on an interface where adaptive routing is enabled.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**reset adaptive-routing notification statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the adaptive routing function is enabled on a device, you can run this command to clear statistics on ARN messages about congestion and congestion relief sent and received on a specified interface.


Example
-------

# Clear statistics on ARN messages about congestion and congestion relief sent and received on a specified interface.
```
<HUAWEI> reset adaptive-routing notification statistics interface 100GE1/0/2

```