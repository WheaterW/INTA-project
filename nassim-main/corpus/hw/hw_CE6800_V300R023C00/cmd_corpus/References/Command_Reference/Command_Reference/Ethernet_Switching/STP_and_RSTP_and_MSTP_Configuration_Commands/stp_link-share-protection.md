stp link-share-protection
=========================

stp link-share-protection

Function
--------



The **stp link-share-protection** command enables shared-link protection for a Multiple Spanning Tree Protocol (MSTP) process.

The **undo stp link-share-protection** command disables shared-link protection of an MSTP process.



By default, shared-link protection of an MSTP process is disabled.


Format
------

**stp link-share-protection**

**undo stp link-share-protection**


Parameters
----------

None

Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a public link becomes faulty on a dual-homing networking, rings that the public link accesses may unblock their blocked ports, causing a permanent network loop.To resolve this problem, run the stp link-share-protection command to enable shared-link protection. When a public link becomes faulty, the working mode of each device on the public link will be forcibly switched to RSTP. After shared-link protection and root protection are deployed, a port will remain in the blocked state after receiving packets of a higher priority from a downstream device. This prevents network loops.



**Precautions**



Shared-link protection is valid only in processes. Before running the stp link-share-protection command, ports have been correctly bound to the corresponding process using the **stp binding process** command.




Example
-------

# Enable shared-link protection for MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp link-share-protection

```