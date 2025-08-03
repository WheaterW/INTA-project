reset ospf flush-source-trace
=============================

reset ospf flush-source-trace

Function
--------



The **reset ospf flush-source-trace** command resets OSPF flush LSA source tracing.




Format
------

**reset ospf** *process-id* **flush-source-trace**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If a large number of OSPF flush LSA source tracing statistics are stored on a device, you can run the **reset ospf flush-source-trace** command to reset the statistics. After the command is run, all OSPF flush LSA source tracing statistics are reset, and the device needs to re-negotiate the OSPF flush LSA source tracing capability with neighboring devices.




Example
-------

# Reset OSPF flush LSA source tracing.
```
<HUAWEI> reset ospf 1 flush-source-trace

```