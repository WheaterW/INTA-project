reset mac-address flapping record
=================================

reset mac-address flapping record

Function
--------



The **reset mac-address flapping record** command clears aged MAC address flapping records.




Format
------

**reset mac-address flapping record** [ **all** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears all the MAC address flapping records, including historical and active records. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To re-collect MAC address flapping records during the rectification of a MAC address flapping fault, run the **reset mac-address flapping record** command to clear existing MAC address flapping records.



**Precautions**



Using the **reset mac-address flapping record** command, you can clear only the records about MAC address flapping entries that do not flap. To clear all flapping MAC addresses, specify all.To clear historical MAC address flapping records, run the **display mac-address flapping** command o view the existing ones.MAC address flapping records cannot be restored after being cleared. Exercise caution when clearing them.




Example
-------

# Clear historical MAC address flapping records from a device.
```
<HUAWEI> reset mac-address flapping record

```