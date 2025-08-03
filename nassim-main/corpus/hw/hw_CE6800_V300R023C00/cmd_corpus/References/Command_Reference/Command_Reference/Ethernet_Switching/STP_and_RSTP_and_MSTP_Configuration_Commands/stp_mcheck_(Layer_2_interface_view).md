stp mcheck (Layer 2 interface view)
===================================

stp mcheck (Layer 2 interface view)

Function
--------



The **stp mcheck** command configures a port to automatically switch from the STP mode back to the Rapid Spanning Tree Protocol (RSTP)/MSTP mode.



By default, a port cannot switch from the STP mode back to the RSTP/MSTP mode.


Format
------

**stp mcheck**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a port of an RSTP/MSTP device is directly connected to an STP device, the port automatically switches to the STP mode and then sends configuration BPDUs to communicate with the remote device. If the STP device is powered off, removed, or is configured to run RSTP/MSTP, the port on the RSTP/MSTP device cannot switch back to the RSTP/MSTP mode. As a result, the RSTP/MSTP device cannot communicate with other RSTP/MSTP devices.To address this problem, run the **stp mcheck** command. After this command is run on a port, the port will automatically switch from the STP mode back to the RSTP/MSTP mode.



**Precautions**



Running the **stp mcheck** command in the interface view configures only the current port to automatically switch back to the RSTP/MSTP mode.




Example
-------

# Perform MCheck on the interface and switch it to the MSTP mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp mcheck

```