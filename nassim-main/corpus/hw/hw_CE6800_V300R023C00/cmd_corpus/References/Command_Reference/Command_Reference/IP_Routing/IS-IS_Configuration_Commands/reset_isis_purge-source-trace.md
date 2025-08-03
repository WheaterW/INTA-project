reset isis purge-source-trace
=============================

reset isis purge-source-trace

Function
--------



The **reset isis purge-source-trace** command resets IS-IS purge LSP source tracing.




Format
------

**reset isis** [ *process-id* ] **purge-source-trace**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If a large number of IS-IS purge LSP source tracing statistics are stored on a device, you can run the **reset isis purge-source-trace** command to reset the statistics. After the command is run, all IS-IS purge LSP source tracing statistics are reset, and the device needs to re-negotiate the IS-IS purge LSP source tracing capability with neighboring devices.




Example
-------

# Reset IS-IS purge LSP source tracing.
```
<HUAWEI> reset isis purge-source-trace

```