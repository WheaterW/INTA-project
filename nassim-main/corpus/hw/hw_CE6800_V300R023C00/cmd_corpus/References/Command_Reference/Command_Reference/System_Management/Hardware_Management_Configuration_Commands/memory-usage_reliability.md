memory-usage reliability
========================

memory-usage reliability

Function
--------



The **memory-usage reliability** command sets thresholds for memory usage reliability.

The **undo memory-usage reliability** command restores the default thresholds for memory usage reliability.



The default notice, overload, and exception thresholds for memory usage reliability are 70, 85, and 95, respectively.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**memory-usage reliability notice-threshold** *notice-threshold-value* **overload-threshold** *overload-threshold-value* **exception-threshold** *exception-threshold-value* [ **slot** *slotId* ]

**undo memory-usage reliability** [ **notice-threshold** *notice-threshold-value* **overload-threshold** *overload-threshold-value* **exception-threshold** *exception-threshold-value* ] [ **slot** *slotId* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **overload-threshold** *overload-threshold-value* | Memory reliability overload threshold. | The value is an integer ranging from (notice-threshold-value + 5) to 95. |
| **exception-threshold** *exception-threshold-value* | Specifies the exception threshold for memory overload reliability. | The value is an integer ranging from max(overload-threshold-value+5, 75) to 100. |
| **slot** *slotId* | Specifies the slot ID of a board. | The value depends on the device. You can enter a question mark (?) and select a value from the displayed value range. |
| **notice-threshold** *notice-threshold-value* | Specifies the notice threshold for memory overload reliability. | The value is an integer ranging from 5 to 90. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set proper thresholds for memory usage reliability based on service deployment on the device. In this way, when the memory usage of the device is too high, the device can detect the high memory usage in a timely manner and release the memory to prevent unexpected board resets.

* When the memory usage of a device is higher than the notice threshold, the system notifies all components of the information about the components (a maximum of 10 components with the highest memory usage) whose memory usage is higher than 5%. When the memory usage of the board falls below the notice threshold minus 5%, the system sends an alarm clearance message to all components.
* When the memory usage of a device is higher than the overload threshold, the system generates the hwSystemMemoryOverload alarm and notifies all components of the information about the components (a maximum of 10 components with the highest memory usage) whose memory usage is higher than 5%. When the memory usage of the board falls below the overload threshold minus 5%, the system generates the hwSystemMemoryOverloadResume alarm and sends an alarm clearance message to all components.

**Prerequisites**



Memory usage reliability has been enabled using the **memory-usage reliability switch on** command.



**Precautions**



If no board is specified, this command takes effect only on the main control board.




Example
-------

# Set the memory reliability notification threshold to 75, overload threshold to 88, and exception threshold to 96 for a specified slot.
```
<HUAWEI> system-view
[~HUAWEI] memory-usage reliability switch on
[~HUAWEI] memory-usage reliability notice-threshold 75 overload-threshold 88 exception-threshold 96 slot 1

```

# Set the default memory reliability notification threshold to 75, overload threshold to 88, and exception threshold to 96 for the main control board.
```
<HUAWEI> system-view
[~HUAWEI] memory-usage reliability switch on
[~HUAWEI] memory-usage reliability notice-threshold 75 overload-threshold 88 exception-threshold 96

```