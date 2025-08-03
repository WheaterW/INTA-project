set memory threshold
====================

set memory threshold

Function
--------



The **set memory threshold** command sets the board memory overload threshold and recovery threshold.

The **undo set memory threshold** command resets the board-level memory overload threshold and recovery threshold.



By default:

* For a device whose total physical memory is greater than 4 GB, the memory usage alarm threshold is 95% and the alarm clearance threshold is 75%.
* For a device whose total physical memory is less than or equal to 4 GB, the memory usage alarm threshold is 92% and the alarm clearance threshold is 75%.


Format
------

**set memory threshold** *thresholdValue* [ **restore** *restoreValue* ] [ **slot** *slotId* [ **cpu** *cpuid* ] ]

**undo set memory threshold** [ **slot** *slotId* [ **cpu** *cpuid* ] ]

**undo set memory threshold** *thresholdValue* **restore** *restoreValue* **slot** *slotId* **cpu** *cpuid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *thresholdValue* | Specify the memory overload threshold. | The value is an integer ranging from 50 to 100.   * For a device whose total physical memory is greater than 4 GB, the default value is 95. * For a device whose total physical memory is less than or equal to 4 GB, the default value is 92.   To check the total physical memory size, run the display memory command in any view and check the Total Physical Available Memory field. |
| **restore** *restoreValue* | Specifies the memory restore overload threshold. | The value is an integer ranging from 1 to threshold-value - 3. The default value is 75. |
| **slot** *slotId* | Specifies an available slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **cpu** *cpuid* | Specifies an available CPU ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can use the **set memory threshold** command to set the memory usage threshold. When memory usage exceeds the alarm threshold, the system logs the event and generates an alarm. By viewing log information, you can learn about memory usage. When memory usage falls within the recovery threshold, the system generates a clear alarm.

**Configuration Impact**

When the memory usage reaches the monitoring alarm threshold, the system will trigger monitoring alarms and logs.

**Precautions**

The default values are recommended for monitoring the alarm threshold and the restore threshold. Otherwise, if the setting is too low, the system will frequently report alarms and logs; if the setting is too high, the user will not be able to know the usage of the memory usage in time. The configuration item value supports product capability set customization, and the default value is not displayed in the device prompt information.


Example
-------

# Set the memory usage alarm threshold to 90% and the alarm clearance threshold to 70%.
```
<HUAWEI> system-view
[~HUAWEI] set memory threshold 90 restore 70

```

# Set the memory usage threshold of the specified board to 80%.
```
<HUAWEI> system-view
[~HUAWEI] set memory threshold 80 slot 1 cpu 0

```