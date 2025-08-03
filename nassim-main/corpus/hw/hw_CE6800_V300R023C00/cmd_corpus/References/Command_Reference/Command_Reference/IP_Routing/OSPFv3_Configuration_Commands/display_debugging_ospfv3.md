display debugging ospfv3
========================

display debugging ospfv3

Function
--------



The **display debugging ospfv3** command displays information about OSPFv3 debugging functions.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display debugging ospfv3**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When a large amount of information is output, the **display debugging ospfv3** command can be used to view information about the enabled OSPFv3 debugging functions. Based on the command output, you can disable some unnecessary debugging functions to minimize the debugging information output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPFv3 debugging functions.
```
<HUAWEI> display debugging ospfv3
OSPFv3 ROUTE-CALC debugging switch is on

```

**Table 1** Description of the **display debugging ospfv3** command output
| Item | Description |
| --- | --- |
| OSPFv3 ROUTE-CALC debugging switch is on | OSPFv3 ROUTE-CALC debugging is enabled. |