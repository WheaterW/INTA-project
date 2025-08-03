clear device alarm hardware
===========================

clear device alarm hardware

Function
--------



The **clear device alarm hardware** command clears hardware alarms.

The **clear device alarm hardware history** command clears historical hardware alarms.




Format
------

**clear device alarm hardware all** { **send-trap** | **no-trap** }

**clear device alarm hardware slot** *slotid* { **send-trap** | **no-trap** }

**clear device alarm hardware index** *indexID* { **send-trap** | **no-trap** }

**clear device alarm hardware history** { **all** | **slot** *slotid* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **send-trap** | Indicates that alarms are sent to the NMS when hardware alarms are cleared. | - |
| **no-trap** | Indicates that no alarm is sent to the NMS when hardware alarms are cleared. | - |
| **slot** *slotid* | Specifies a slot ID. | The value is a string of 1 to 49 case-insensitive characters, spaces not supported. |
| **index** *indexID* | Specifies the index of an alarm. | The value is an integer ranging from 0 to 4294967295. |
| **all** | Clears all hardware alarms or historical hardware alarms. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To clear hardware alarms on a device, run the **display device alarm hardware** command to view all hardware alarms on the device, select the hardware alarms to be cleared, and run the **clear device alarm hardware** command. Index-specific, slot ID-specific, or all alarms can be cleared. You can also allow the device to send alarms to the NMS.
* To clear historical hardware alarms on a device, run the **display device alarm hardware history** command to view all historical hardware alarms on the device, select the historical hardware alarms to be cleared, and run the **clear device alarm hardware history** command. You can specify different parameters to clear historical hardware alarms of a specified board or all historical hardware alarms of the device in batches.

Example
-------

# Clear hardware alarms on the board in a specified slot.
```
<HUAWEI> clear device alarm hardware history slot 1
Warning: Confirm to delete. Continue? [Y/N]:y

```

# Clear the hardware alarm with index 1.
```
<HUAWEI> clear device alarm hardware index 1 no-trap
Info: The following alarm will be cleared:
"The power totally failed.(PowerID=POWER 1, Reason=The power module was not present.)"
Warning: Confirm to delete. Continue? [Y/N]:y

```

# Clear all hardware alarms and send clear alarms to the NMS.
```
<HUAWEI> clear device alarm hardware all send-trap
Warning: Confirm to delete. Continue? [Y/N]:Y

```

# Clear hardware alarms in a specified slot and send clear alarms to the NMS.
```
<HUAWEI> clear device alarm hardware slot 1 send-trap
Warning: Confirm to delete. Continue? [Y/N]:Y

```