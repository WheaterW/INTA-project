stp flush disable
=================

stp flush disable

Function
--------



The **stp flush disable** command disables a device or MSTP process from updating MAC address entries when the device or MSTP process receives TC BPDUs.

The **undo stp flush disable** command enables a device or MSTP process to update MAC address entries when the device or MSTP process receives TC BPDUs.



By default, a device or MSTP process updates MAC address entries when the device or MSTP process receives TC BPDUs.


Format
------

**stp flush disable**

**undo stp flush disable**


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



On loop-free networks, STP is still configured to prevent potential loops caused by incorrect connections. However, STP will send TC BPDUs to instruct devices to update MAC address entries when the network topology encounters any changes. For example, the local device's interface goes Up from Down. This change does not require MAC address updates. If MAC addresses are updated in a large scale, unknown unicast or broadcast may occur.

To resolve this problem, run the **stp flush disable** command to disable a device or MSTP process from updating MAC address entries when it receives TC BPDUs.



**Precautions**



If you run the **stp flush disable** command in the system view, process 0 does not update MAC address entries after receiving TC BPDUs. If you run this command in an MSTP process view, the MSTP process does not update MAC address entries after receiving TC BPDUs.After you run the **stp flush disable** command, the device or MSTP process does not update MAC address entries after receiving TC BPDUs. Services may be interrupted for a long time if the MAC address entries are incorrect. Therefore, exercise caution when running this command.




Example
-------

# Disable MSTP process 0 from updating MAC address entries after receiving TC BPDUs.
```
<HUAWEI> system-view
[~HUAWEI] stp flush disable

```