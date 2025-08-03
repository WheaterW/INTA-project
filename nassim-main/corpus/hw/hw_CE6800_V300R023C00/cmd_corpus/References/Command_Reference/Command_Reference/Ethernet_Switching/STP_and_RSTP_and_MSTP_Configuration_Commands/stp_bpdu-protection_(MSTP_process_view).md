stp bpdu-protection (MSTP process view)
=======================================

stp bpdu-protection (MSTP process view)

Function
--------



The **stp bpdu-protection** command enables bridge protocol data unit (BPDU) protection in MSTP process.

The **undo stp bpdu-protection** command disables BPDU protection in MSTP process.



By default, BPDU protection is disabled.


Format
------

**stp bpdu-protection**

**undo stp bpdu-protection**


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



On a Layer 2 network running STP, ports connected to terminals do not need to participate in spanning tree calculation. You can run the **stp edged-port enable** command to configure a port connecting to a terminal as an edge port, because an edge port does not participate in spanning tree calculation. This speeds up network convergence and improves network stability.An edge port will no longer be an edge port after receiving BPDUs. To prevent an edge port from receiving bogus BPDUs from attackers, run the **stp bpdu-protection** command to configure BPDU protection.



**Configuration Impact**



After BPDU protection is enabled on an edge port, the port will be shut down after receiving a BPDU, but it remains an edge port.



**Precautions**



BPDU protection takes effect only on the edge ports configured using the stp edged-port default command in the system view or on a specific edge port configured using the **stp edged-port enable** command in the interface view. BPDU protection does not take effect on edge ports generated through automatic detection.




Example
-------

# Enable BPDU protection in MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp bpdu-protection

```