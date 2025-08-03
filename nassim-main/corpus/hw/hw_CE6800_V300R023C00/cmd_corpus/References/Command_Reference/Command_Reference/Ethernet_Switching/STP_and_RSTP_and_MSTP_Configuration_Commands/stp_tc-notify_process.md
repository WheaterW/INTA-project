stp tc-notify process
=====================

stp tc-notify process

Function
--------



The **stp tc-notify process** command enables TC notification function on a Multiple Spanning Tree Protocol (MSTP) process.

The **undo stp tc-notify process** command disables the TC notification function.



By default, TC notification function is disabled on MSTP processes.


Format
------

**stp tc-notify process 0**

**undo stp tc-notify process 0**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **0** | Specifies the ID of an MSTP process. | The value can only be 0. |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the **stp tc-notify process** command is run on an MSTP process, if the MSTP process receives a TC message, the process instructs the MSTIs in MSTP process 0 to update MAC entries and ARP entries. This prevents user services from being interrupted.




Example
-------

# Configure MSTP process 1 to notify MSTP process 0 that MSTP process 1 receives a TC BPDU.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp tc-notify process 0

```