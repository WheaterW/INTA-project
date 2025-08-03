stp process
===========

stp process

Function
--------



The **stp process** command creates and enters the MSTP process view.

The **undo stp process** command deletes a specified MSTP process.



By default, all MSTP configurations on a device belong to MSTP process 0.


Format
------

**stp process** *process-id*

**undo stp process** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Indicates the ID of an MSTP process. | The value is an integer ranging from 1 to 256. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running MSTP, if devices on the public link belong to multiple access rings that are isolated from each other and these access rings do not need communication, MSTP cannot calculate one spanning tree for all these access rings. To resolve this problem, run the stp process command to configure a process for each ring.Each device on these access rings can be configured with multiple MSTP processes. After ports of each device are bound to different MSTP processes, they participate in the MSTP calculations of different MSTP processes. MSTP calculations in different MSTP processes are independent of each other.



**Follow-up Procedure**



After an MSTP process is created, run the **stp binding process** command to bind interfaces to the MSTP process.



**Precautions**



After a device that runs MSTP starts correctly, MSTP process 0 exists by default. MSTP configurations in the system view and interface view belong to this process.If you run the **undo stp process** command, all configurations of the MSTP process with a specified ID will be deleted.




Example
-------

# Create MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1

```