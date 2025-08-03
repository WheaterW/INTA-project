reset ospfv3 counters
=====================

reset ospfv3 counters

Function
--------



The **reset ospfv3 counters** command resets OSPFv3 statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ospfv3** { *process-id* | **all** } **counters** [ **neighbor** [ *interface-name* | *interface-type* *interface-number* ] [ *router-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of an OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Resets all OSPFv3 processes. | - |
| **neighbor** | Resets neighbor statistics. | - |
| *interface-type* | Specifies the interface type. | - |
| *interface-number* | Specifies the interface number. | - |
| *router-id* | Specifies the router ID of a neighbor. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Clearing OSPFv3 counters does not affect OSPFv3 services.Statistics cannot be restored after being deleted. Therefore, exercise caution when running the command.


Example
-------

# Reset OSPFv3 statistics.
```
<HUAWEI> reset ospfv3 1 counters

```