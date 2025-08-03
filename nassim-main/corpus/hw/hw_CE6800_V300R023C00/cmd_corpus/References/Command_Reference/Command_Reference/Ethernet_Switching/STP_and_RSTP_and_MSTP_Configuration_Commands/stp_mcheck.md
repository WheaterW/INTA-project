stp mcheck
==========

stp mcheck

Function
--------



The **stp mcheck** command configures a system to automatically switch from the STP mode back to the RSTP/MSTP mode.



By default, a system cannot switch from the STP mode back to the RSTP/MSTP mode.


Format
------

**stp mcheck**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a port of an RSTP/MSTP device is directly connected to an STP device, the port automatically switches to the STP mode and then sends configuration BPDUs to communicate with the remote device. If the STP device is powered off, removed, or is configured to run RSTP/MSTP, the port on the RSTP/MSTP device cannot switch back to the RSTP/MSTP mode. As a result, the RSTP/MSTP device cannot communicate with other RSTP/MSTP devices.To address this problem, run the **stp mcheck** command. After this command is run on a port, the port will automatically switch from the STP mode back to the RSTP/MSTP mode.



**Precautions**



Running the **stp mcheck** command in the system view configures all ports on a device to automatically switch back to the RSTP/MSTP mode.




Example
-------

# Perform MCheck on the system and switch it to the MSTP mode.
```
<HUAWEI> system-view
[~HUAWEI] stp mcheck

```