reset ifit flow-cache
=====================

reset ifit flow-cache

Function
--------



The **reset ifit flow-cache** command clears IFIT flow table information on a device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ifit** [ **forward** ] **flow-cache** **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **forward** | Specifies the forwarding action. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to clear IFIT flow table information on a device.

**Precautions**

Hardware flow table information can be cleared only when IFIT is disabled.


Example
-------

# Clear cached IFIT flow table information on a device.
```
<HUAWEI> reset ifit flow-cache slot 1

```

# Clear information about the IFIT hardware flow table on the device.
```
<HUAWEI> reset ifit forward flow-cache slot 1

```