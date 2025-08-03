display master-key version(All views)
=====================================

display master-key version(All views)

Function
--------



The **display master-key version** command displays KMC version information on the current device.




Format
------

**display master-key version**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

In KMC 3.0, the master key can be protected by hardware. In KMC 2.0, the master key can be protected by software. To check the master key protection mode of the current device, run this command to check the KMC version of the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the KMC version of the current device.
```
<HUAWEI> display master-key version
-----------------------------------------------------------
SlotID         KMCVersion      HardwareCapability
-----------------------------------------------------------
5               3.0                 Y
-----------------------------------------------------------

```

**Table 1** Description of the **display master-key version(All views)** command output
| Item | Description |
| --- | --- |
| SlotID | Slot ID. |
| KMCVersion | KMC version. |
| HardwareCapability | Hardware root key capability. |