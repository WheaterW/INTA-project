set cpu-usage threshold(System view)
====================================

set cpu-usage threshold(System view)

Function
--------



The **set cpu-usage threshold** command is used to set the overload threshold, recovery threshold, and overload detection period for board-level CPU usage.

The **undo set cpu-usage threshold** command is used to reset the overload threshold, recovery threshold, and overload detection period of the board-level CPU usage.



By default, the CPU usage monitoring alarm overload threshold is 90%, the monitoring alarm recovery threshold is 75%, and the overload detection cycle is 1 minute.


Format
------

**set cpu-usage threshold** *thresholdValue* [ **restore** *restoreValue* ] [ **interval** *interval-time* ] [ **slot** *slotId* [ **cpu** *cpuid* ] ]

**undo set cpu-usage threshold** [ **slot** *slotId* [ **cpu** *cpuid* ] ]

**undo set cpu-usage threshold** *thresholdValue* **restore** *restoreValue* **interval** *interval-time* **slot** *slotId* **cpu** *cpuid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *thresholdValue* | Specify the CPU overload threshold. | The value is an integer ranging from 4 to 100, default value is 90. |
| **restore** *restoreValue* | Specifies the CPU restore overload threshold. | The value is an integer ranging from 1 to threshold-value - 3, default value is 75. |
| **interval** *interval-time* | Specifies a CPU overload detection period. | The value is an integer ranging from 1 to 60, in minutes, default value is 1. |
| **slot** *slotId* | Specifies an available slot ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **cpu** *cpuid* | Specifies an available CPU ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can use the **set cpu-usage threshold** command to set the CPU usage alarm threshold and CPU usage alarm recovery threshold. When CPU usage exceeds the alarm threshold, the system logs the event and generates an alarm. By viewing log information, you can learn about CPU usage. When CPU usage falls within the recovery threshold, the system generates a clear alarm.

**Configuration Impact**

When the CPU usage reaches the threshold for monitoring alarms, the system triggers monitoring alarms and logs.

**Precautions**

The default values are recommended for monitoring the alarm threshold and the restore threshold. Otherwise, if the setting is too low, the system will frequently report alarms and logs; if the setting is too high, users will not be able to know the CPU usage in time. Configuration item values support product capability set customization, and default values are not displayed in device prompts.


Example
-------

# Set the CPU usage overload threshold for all boards to 60%, the de-overload threshold to 50%, and the detection period to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] set cpu-usage threshold 60 restore 50 interval 5

```

# Set the CPU usage threshold of the specified board to 80%.
```
<HUAWEI> system-view
[~HUAWEI] set cpu-usage threshold 80 slot 1 cpu 0

```