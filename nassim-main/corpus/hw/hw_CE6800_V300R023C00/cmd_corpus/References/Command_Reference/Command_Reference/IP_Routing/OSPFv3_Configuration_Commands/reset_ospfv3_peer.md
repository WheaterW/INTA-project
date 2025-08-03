reset ospfv3 peer
=================

reset ospfv3 peer

Function
--------



The **reset ospfv3 peer** command resets OSPFv3 neighbors.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ospfv3** { *process-id* | **all** } **peer** [ *interface-name* | *interface-type* *interface-number* ] *router-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Resets all OSPFv3 processes. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the interface number. | - |
| *router-id* | The router ID of a neighbor. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Running the **reset ospfv3 peer** command resets OSPFv3 neighbors. Once cleared, the statistics information cannot be restored. Therefore, exercise caution when running this command.


Example
-------

# Reset OSPFv3 peer.
```
<HUAWEI> reset ospfv3 1 peer 1.1.1.1

```