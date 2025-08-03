set cpu-reliability
===================

set cpu-reliability

Function
--------



The **set cpu-reliability** command specifies the level-1 alarm threshold, level-1 clear alarm threshold, level-2 alarm threshold, level-2 clear alarm threshold, and detection period of CPU overload.

The **undo set cpu-reliability** command restores the default configuration.



By default, the level-1 alarm threshold, level-1 clear alarm threshold, level-2 alarm threshold, level-2 clear alarm threshold, and detection period of CPU overload are 60, 50, 80, 70, and 60, respectively.


Format
------

**set cpu-reliability first-recover** *first-recover-value* **first-alarm** *first-alarm-value* **second-recover** *second-recover-value* **second-alarm** *second-alarm-value* **period** *period-value* [ **slot** *slot-id* ]

**undo set cpu-reliability** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **first-alarm** *first-alarm-value* | Specifies a level-1 alarm threshold. | The value is an integer ranging from (first-recover-value + 1) to 97. The default value is 60. |
| **second-recover** *second-recover-value* | Specifies a level-2 clear alarm threshold. | The value is an integer ranging from (first-alarm-value + 1) to 98. The default value is 70. |
| **second-alarm** *second-alarm-value* | Specifies a level-2 alarm threshold. | The value is an integer ranging from (second-recover-value + 1) to 99. The default value is 80. |
| **period** *period-value* | Specifies a detection period. | The value is an integer ranging from 30 to 3600, in seconds. The default value is 60. |
| **slot** *slot-id* | Specifies the level-1 and level-2 alarm thresholds of CPU overload on the slave control board. | - |
| **first-recover** *first-recover-value* | Specifies a level-1 clear alarm threshold. | The value is an integer ranging from 1 to 96. The default value is 50. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure the level-1 alarm threshold, level-1 clear alarm threshold, level-2 alarm threshold, level-2 clear alarm threshold, and detection period of CPU overload, run the set cpu-reliability command based on deployed services.


Example
-------

# Configure the level-1 alarm threshold, level-1 clear alarm threshold, level-2 alarm threshold, level-2 clear alarm threshold, and detection period of CPU overload on the interface board in the specified slot as 30, 10, 60, 50, and 1000, respectively.
```
<HUAWEI> system-view
[~HUAWEI] set cpu-reliability first-recover 10 first-alarm 30 second-recover 50 second-alarm 60 period 1000 slot 1

```

# Configure the default level-1 alarm threshold, level-1 clear alarm threshold, level-2 alarm threshold, level-2 clear alarm threshold, and detection period of CPU overload on the main control board as 30, 10, 60, 50, and 1000, respectively.
```
<HUAWEI> system-view
[~HUAWEI] set cpu-reliability first-recover 10 first-alarm 30 second-recover 50 second-alarm 60 period 1000

```