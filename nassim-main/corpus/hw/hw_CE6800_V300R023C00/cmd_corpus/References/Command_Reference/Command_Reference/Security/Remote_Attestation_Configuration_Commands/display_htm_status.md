display htm status
==================

display htm status

Function
--------



The **display htm status** command displays the status of the HTM module.




Format
------

**display htm status** { **slot** *slotId* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotId* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **all** | Specifies all slots. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to query whether the HTM module is activated.

**Prerequisites**

Run the **trustem** command in the system view to deploy the trustem component.

**Precautions**

If the **trustem** command is not configured, this command fails to be executed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the HTM module status.
```
<HUAWEI> display htm status slot 1
------------------------------------------------------
SlotID   HTM version  HTM manufacturer  HTM status
------------------------------------------------------
1 2.0.7.62   IFX             active
------------------------------------------------------
<HUAWEI>

```

**Table 1** Description of the **display htm status** command output
| Item | Description |
| --- | --- |
| SlotID | Slot ID. |
| HTM version | HTM version number. |
| HTM manufacturer | HTM manufacturer. |
| HTM status | HTM status. |