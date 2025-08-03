reset ospfv3 flush-source-trace
===============================

reset ospfv3 flush-source-trace

Function
--------



The **reset ospfv3 flush-source-trace** command resets OSPFv3 flush LSA source tracing.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ospfv3** *process-id* **flush-source-trace**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If a large number of OSPFv3 flush LSA source tracing statistics are stored on a device, you can run the **reset ospfv3 flush-source-trace** command to reset the statistics. After the command is run, all OSPFv3 flush LSA source tracing statistics are reset, and the device needs to re-negotiate the OSPFv3 flush LSA source tracing capability with neighboring devices.


Example
-------

# Reset OSPFv3 flush LSA source tracing.
```
<HUAWEI> reset ospfv3 1 flush-source-trace

```